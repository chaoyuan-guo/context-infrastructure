#!/usr/bin/env python3

import argparse
import json
import re
import sqlite3
from collections import defaultdict
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from pathlib import Path
from typing import Iterable

try:
    from zoneinfo import ZoneInfo
except ImportError:  # pragma: no cover
    ZoneInfo = None


DEFAULT_TIMEZONE = "Asia/Shanghai"
DEFAULT_USER_LABEL = "chaoyuan"
EXPORT_FORMAT_VERSION = 10
SESSION_ID_PATTERN = re.compile(r"^session_id:\s*'([^']+)'", re.M)
EXPORT_FORMAT_VERSION_PATTERN = re.compile(r"^export_format_version:\s*(\d+)\s*$", re.M)
INTERNAL_INITIATOR_COMMENT_PATTERN = re.compile(
    r"(?m)^\s*<!--\s*OMO_INTERNAL_INITIATOR\s*-->\s*$"
)
LEADING_MODE_PREAMBLE_PATTERN = re.compile(
    r"^\s*(?:"
    r"\[(?:search|analyze)-mode\]\s*.*?"
    r"(?:\n\s*\[(?:search|analyze)-mode\]\s*.*?)*"
    r"\n\s*---\s*"
    r"(?:\n\s*MANDATORY delegate_task params:.*?(?:\n\s*Example: delegate_task\(.*?\))?)?"
    r"\n\s*---\s*\n*"
    r")",
    re.S | re.I,
)
LOW_SIGNAL_TITLE_QUERY_PREFIXES = {
    "增量同步 agent_traces 会话记录": [
        "<auto-slash-command>\n# /sync-agent-traces Command",
    ],
    "查看未提交的变更": [
        "查看未提交的变更",
        "现在有哪些未提交的变更",
    ],
}
LOW_SIGNAL_FIRST_QUERIES = {
    "查看未提交的变更",
    "现在有哪些未提交的变更",
}
LEADING_INTERNAL_XML_TAGS = (
    "system-reminder",
    "auto-slash-command",
    "ultrawork-mode",
)
CONTROL_ONLY_QUERY_PREFIXES = (
    "ultrawork [system directive:",
)
PROMISE_ONLY_LINE_PATTERN = re.compile(r"(?m)^\s*<promise>(DONE|VERIFIED)</promise>\s*$")
ULTRAWORK_LINE_PATTERN = re.compile(r"(?m)^\s*ULTRAWORK MODE ENABLED!\s*$")
WAIT_STATE_ACTION_MARKERS = (
    "wait",
    "waiting",
    "still running",
    "still-running",
    "completion reminder",
    "completion notification",
    "actively poll",
    "轮询",
    "完成通知",
    "等系统",
    "等后台",
    "结果回来",
    "收口",
)
WAIT_STATE_SUBJECT_MARKERS = (
    "reviewer",
    "review-work",
    "oracle",
    "background task",
    "security / context",
    "skeptical oracle",
    "后台",
)


@dataclass
class SessionRecord:
    session_id: str
    title: str
    slug: str
    parent_id: str | None
    time_created: int
    time_updated: int
    directory: str


@dataclass
class ConversationPair:
    query_text: str
    answer_text: str
    model_id: str | None
    provider_id: str | None
    user_time_created: int
    assistant_time_created: int | None


@dataclass
class ExportSession:
    session: SessionRecord
    pairs: list[ConversationPair]
    display_title: str
    stem: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export yesterday's OpenCode session queries and final answers to Markdown."
    )
    parser.add_argument(
        "--workspace",
        type=Path,
        default=Path.cwd(),
        help="Workspace path used to resolve .git/opencode (default: current directory).",
    )
    parser.add_argument(
        "--date",
        help="Target date in YYMMDD or YYYY-MM-DD. Default: yesterday in Asia/Shanghai. Use --all to export all sessions.",
    )
    parser.add_argument(
        "--timezone",
        default=DEFAULT_TIMEZONE,
        help=f"Timezone used to interpret dates (default: {DEFAULT_TIMEZONE}).",
    )
    parser.add_argument(
        "--db",
        type=Path,
        default=Path.home() / ".local/share/opencode/opencode.db",
        help="Path to OpenCode sqlite database.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory. Default: <workspace>/contexts/agent_traces.",
    )
    parser.add_argument(
        "--user-label",
        default=DEFAULT_USER_LABEL,
        help=f"Label used for the user speaker block (default: {DEFAULT_USER_LABEL}).",
    )
    parser.add_argument(
        "--include-subagents",
        action="store_true",
        help="Include child sessions whose parent_id is not null.",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Export all matching sessions for this workspace, ignoring --date.",
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="Incrementally export new or updated sessions across the whole workspace.",
    )
    parser.add_argument(
        "--include-probes",
        action="store_true",
        help="Include telemetry/probe sessions like exact-reply checks.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing markdown files with the same name.",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        help="Path to incremental export manifest. Default: <output-dir>/.export_manifest.json",
    )
    return parser.parse_args()


def resolve_timezone(name: str):
    if ZoneInfo is None:
        raise RuntimeError("zoneinfo is unavailable in this Python runtime")
    return ZoneInfo(name)


def parse_target_date(raw: str | None, tz) -> date:
    if not raw:
        return datetime.now(tz).date() - timedelta(days=1)
    raw = raw.strip()
    if re.fullmatch(r"\d{6}", raw):
        return datetime.strptime(raw, "%y%m%d").date()
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return datetime.strptime(raw, "%Y-%m-%d").date()
    raise ValueError("--date must be YYMMDD or YYYY-MM-DD")


def find_workspace_root(start: Path) -> Path:
    start = start.resolve()
    for candidate in [start, *start.parents]:
        if (candidate / ".git" / "opencode").exists():
            return candidate
    raise FileNotFoundError(f"Could not find .git/opencode from {start}")


def read_project_id(workspace_root: Path) -> str:
    project_id = (workspace_root / ".git" / "opencode").read_text(encoding="utf-8").strip()
    if not project_id:
        raise ValueError(f"Empty project id in {workspace_root / '.git/opencode'}")
    return project_id


def normalize_session_name(title: str, fallback: str) -> str:
    name = title.strip() or fallback
    if name.lower().startswith("new session"):
        name = fallback
    name = name.lower()
    name = re.sub(r"\s+", "-", name)
    name = re.sub(r"[^0-9a-z_\-\u4e00-\u9fff]+", "-", name)
    name = re.sub(r"-+", "-", name).strip("-_")
    return name or "session"


def is_suspicious_session_title(title: str) -> bool:
    normalized = title.strip().lower()
    return (
        normalized.startswith("new session")
        or normalized.startswith("<system-reminder>")
        or normalized.startswith("<auto-slash-command>")
        or normalized == "..."
        or "[pasted ~" in normalized
    )


def is_probe_query(text: str) -> bool:
    normalized = " ".join(text.strip().lower().split())
    if not normalized:
        return False
    probe_patterns = [
        '"reply with exactly:',
        "reply with exactly:",
        "telemetry-check",
        "telemetry-clean-check",
    ]
    return any(pattern in normalized for pattern in probe_patterns)


def normalize_text(text: str) -> str:
    return " ".join(text.strip().split())


CONTROL_ONLY_QUERY_EXACT = {
    normalize_text(
        "Continue if you have next steps, or stop and ask for clarification if you are unsure how to proceed."
    ).lower(),
    normalize_text("[restore checkpointed session agent configuration after compaction]").lower(),
    normalize_text("继续").lower(),
    normalize_text("继续啊").lower(),
    normalize_text("继续吧").lower(),
    normalize_text("继续处理").lower(),
    normalize_text("卡住了吗").lower(),
    normalize_text("卡住了吗？").lower(),
}


def remove_internal_initiator_comments(text: str) -> str:
    return INTERNAL_INITIATOR_COMMENT_PATTERN.sub("", text)


def strip_leading_xml_block(text: str, tag: str) -> str:
    pattern = rf"^\s*<{tag}>.*?</{tag}>\s*"
    return re.sub(pattern, "", text, count=1, flags=re.S)


def strip_leading_internal_blocks(text: str) -> str:
    cleaned = remove_internal_initiator_comments(text).strip()
    while True:
        previous = cleaned
        for tag in LEADING_INTERNAL_XML_TAGS:
            cleaned = strip_leading_xml_block(cleaned, tag).strip()
        cleaned = LEADING_MODE_PREAMBLE_PATTERN.sub("", cleaned, count=1).strip()
        cleaned = remove_internal_initiator_comments(cleaned).strip()
        if cleaned == previous:
            return cleaned


def clean_query_text(text: str) -> str:
    cleaned = strip_leading_internal_blocks(text)
    cleaned = re.sub(r"^(?:\s*---\s*)+", "", cleaned)
    return cleaned.strip()


def is_control_only_query(text: str) -> bool:
    normalized = normalize_text(text).lower()
    if not normalized:
        return True
    if normalized in CONTROL_ONLY_QUERY_EXACT:
        return True
    if any(normalized.startswith(prefix) for prefix in CONTROL_ONLY_QUERY_PREFIXES):
        return True
    if len(normalized) <= 8 and any(token in normalized for token in ("继续", "卡住", "好了", "ok", "好的")):
        return True
    return False


def clean_final_assistant_text(text: str) -> str:
    cleaned = remove_internal_initiator_comments(text).strip()
    cleaned = ULTRAWORK_LINE_PATTERN.sub("", cleaned)
    cleaned = PROMISE_ONLY_LINE_PATTERN.sub("", cleaned)
    paragraphs = [paragraph.strip() for paragraph in re.split(r"\n\s*\n", cleaned) if paragraph.strip()]
    kept = [strip_wait_state_sentences(paragraph) for paragraph in paragraphs if not is_wait_state_paragraph(paragraph)]
    kept = [paragraph for paragraph in kept if paragraph]
    return "\n\n".join(kept).strip()


def has_exportable_assistant_output(text: str) -> bool:
    normalized = normalize_text(clean_final_assistant_text(text)).lower()
    return bool(normalized and normalized != "_no final assistant output found._")


def is_wait_state_paragraph(paragraph: str) -> bool:
    normalized = normalize_text(paragraph).lower()
    if not normalized:
        return True
    return any(action in normalized for action in WAIT_STATE_ACTION_MARKERS) and any(
        subject in normalized for subject in WAIT_STATE_SUBJECT_MARKERS
    )


def strip_wait_state_sentences(paragraph: str) -> str:
    lines = [line.strip() for line in paragraph.splitlines() if line.strip()]
    kept_lines = [line for line in lines if not is_wait_state_line(line)]
    return "\n".join(kept_lines).strip()


def is_wait_state_line(line: str) -> bool:
    normalized = normalize_text(line).lower()
    if not normalized:
        return False
    if is_wait_state_paragraph(line):
        return True
    sentence_fragments = re.split(r"(?<=[。！？!?;；.])\s+", line)
    if len(sentence_fragments) <= 1:
        return False
    return all(is_wait_state_fragment(fragment) for fragment in sentence_fragments if normalize_text(fragment))


def is_wait_state_fragment(fragment: str) -> bool:
    normalized = normalize_text(fragment).lower()
    if not normalized:
        return False
    return any(action in normalized for action in WAIT_STATE_ACTION_MARKERS) and any(
        subject in normalized for subject in WAIT_STATE_SUBJECT_MARKERS
    )


def clean_query_for_title(text: str) -> str:
    cleaned = clean_query_text(text)

    candidates: list[str] = []
    for raw_line in cleaned.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        line = re.sub(r"^[A-Za-z0-9_./-]+\.md\s+", "", line)
        line = re.sub(r"^/[A-Za-z0-9_./-]+\.md\s+", "", line)
        if line.startswith("[Pasted ~"):
            break
        if line.startswith("/"):
            continue
        if re.match(r"^[A-Za-z0-9_./-]+$", line) and ("/" in line or line.endswith(".md")):
            continue
        if line.startswith("# "):
            continue
        if line.startswith("**") and line.endswith("**"):
            continue
        if line in {"---", "## Command Instructions"}:
            continue
        if re.match(r"^(def |class |from |import |return |if |for |while |with )", line):
            break
        if re.match(r"^[A-Za-z_][A-Za-z0-9_]*\s*=", line):
            break
        if candidates:
            if re.match(r"^[A-Za-z0-9_./-]+$", line) and ("/" in line or line.endswith(".md")):
                break
            if re.match(r"^(def |class |from |import |return |if |for |while |with )", line):
                break
            if re.match(r"^[A-Za-z_][A-Za-z0-9_]*\s*=", line):
                break
        candidates.append(line)
        break

    return " ".join(candidates).strip()


def truncate_title(text: str, limit: int) -> str:
    normalized = normalize_text(text)
    if len(normalized) <= limit:
        return normalized

    boundary_chars = "，。；：:,.!?！？()（）"
    cutoff = max(limit - 12, int(limit * 0.6))
    for index in range(min(limit, len(normalized)) - 1, cutoff - 1, -1):
        if normalized[index] in boundary_chars:
            return normalized[:index].rstrip(boundary_chars + " ")

    return normalized[:limit].rstrip()


def is_low_signal_session(session: SessionRecord, pairs: list[ConversationPair]) -> bool:
    if not pairs:
        return True

    first_pair = pairs[0]
    first_query = normalize_text(first_pair.query_text)
    title = normalize_text(session.title)
    has_assistant_output = any(pair.answer_text.strip() for pair in pairs)

    if not has_assistant_output:
        if "<auto-slash-command>" in first_pair.query_text:
            return True
        if len(pairs) == 1:
            return True

    title_prefixes = LOW_SIGNAL_TITLE_QUERY_PREFIXES.get(title, [])
    if any(first_pair.query_text.startswith(prefix) for prefix in title_prefixes):
        return True
    if first_query in LOW_SIGNAL_FIRST_QUERIES:
        return True

    return False


def summarize_query_as_name(text: str, limit: int = 48) -> str:
    normalized = clean_query_for_title(text) or " ".join(text.strip().split())
    normalized = normalized.strip('"\'')
    normalized = re.sub(r"\s*\[Pasted ~\d+.*$", "", normalized).rstrip("：: ([")
    normalized = truncate_title(normalized, limit)
    return normalized or "session"


def millis_range_for_date(target: date, tz) -> tuple[int, int]:
    start = datetime.combine(target, time.min, tzinfo=tz)
    end = start + timedelta(days=1)
    return int(start.timestamp() * 1000), int(end.timestamp() * 1000)


def fetch_sessions(
    conn: sqlite3.Connection,
    project_id: str,
    start_ms: int | None,
    end_ms: int | None,
    include_subagents: bool,
) -> list[SessionRecord]:
    query = """
        SELECT id, title, slug, parent_id, time_created, time_updated, directory
        FROM session
        WHERE project_id = ?
    """
    params: list[object] = [project_id]
    if start_ms is not None and end_ms is not None:
        query += " AND time_created >= ? AND time_created < ?"
        params.extend([start_ms, end_ms])
    if not include_subagents:
        query += " AND parent_id IS NULL"
    query += " ORDER BY time_created, id"

    rows = conn.execute(query, params).fetchall()
    return [
        SessionRecord(
            session_id=row["id"],
            title=row["title"],
            slug=row["slug"],
            parent_id=row["parent_id"],
            time_created=row["time_created"],
            time_updated=row["time_updated"],
            directory=row["directory"],
        )
        for row in rows
    ]


def load_session_payloads(
    conn: sqlite3.Connection, session_id: str
) -> tuple[list[sqlite3.Row], dict[str, list[dict]]]:
    messages = conn.execute(
        """
        SELECT id, time_created, data
        FROM message
        WHERE session_id = ?
        ORDER BY time_created, id
        """,
        (session_id,),
    ).fetchall()
    parts = conn.execute(
        """
        SELECT id, message_id, time_created, data
        FROM part
        WHERE session_id = ?
        ORDER BY time_created, id
        """,
        (session_id,),
    ).fetchall()

    parts_by_message: dict[str, list[dict]] = defaultdict(list)
    for row in parts:
        payload = json.loads(row["data"])
        payload["_id"] = row["id"]
        payload["_time_created"] = row["time_created"]
        parts_by_message[row["message_id"]].append(payload)
    return messages, parts_by_message


def extract_text_parts(parts: Iterable[dict]) -> str:
    texts: list[str] = []
    for part in parts:
        part_type = part.get("type")
        if part_type != "text":
            continue
        text_value = (part.get("text") or "").strip()
        if text_value:
            texts.append(text_value)
    return "\n\n".join(texts).strip()


def choose_final_assistant_message(
    candidates: Iterable[dict], parts_by_message: dict[str, list[dict]]
) -> dict | None:
    stop_candidates = [candidate for candidate in candidates if candidate["finish"] == "stop"]
    for candidate in reversed(stop_candidates):
        final_output = extract_text_parts(parts_by_message.get(candidate["id"], []))
        if has_exportable_assistant_output(final_output):
            candidate["_final_output"] = clean_final_assistant_text(final_output)
            return candidate
    return None


def build_conversation_pairs(conn: sqlite3.Connection, session_id: str) -> list[tuple[str, str]]:
    messages, parts_by_message = load_session_payloads(conn, session_id)

    parsed_messages: list[dict] = []
    children_by_parent: dict[str, list[dict]] = defaultdict(list)
    for row in messages:
        payload = json.loads(row["data"])
        item = {
            "id": row["id"],
            "time_created": row["time_created"],
            "role": payload.get("role"),
            "finish": payload.get("finish"),
            "parent_id": payload.get("parentID"),
            "model_id": payload.get("modelID"),
            "provider_id": payload.get("providerID"),
        }
        parsed_messages.append(item)
        if item["parent_id"]:
            children_by_parent[item["parent_id"]].append(item)

    pairs: list[ConversationPair] = []
    for message in parsed_messages:
        if message["role"] != "user":
            continue

        query_text = clean_query_text(extract_text_parts(parts_by_message.get(message["id"], [])))
        if not query_text:
            continue
        if is_control_only_query(query_text):
            continue

        assistant_candidates = [
            child for child in children_by_parent.get(message["id"], []) if child["role"] == "assistant"
        ]
        final_message = choose_final_assistant_message(assistant_candidates, parts_by_message)
        if final_message is None:
            continue

        pairs.append(
            ConversationPair(
                query_text=query_text,
                answer_text=final_message["_final_output"],
                model_id=final_message["model_id"],
                provider_id=final_message["provider_id"],
                user_time_created=message["time_created"],
                assistant_time_created=final_message["time_created"],
            )
        )

    return pairs


def format_assistant_label(model_id: str | None, provider_id: str | None) -> str:
    if model_id and provider_id:
        return f"OpenCode-{model_id}-{provider_id}"
    if model_id:
        return f"OpenCode-{model_id}"
    return "OpenCode"


def yaml_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def format_timestamp(timestamp_ms: int | None, tz_name: str) -> str | None:
    if timestamp_ms is None:
        return None
    tz = resolve_timezone(tz_name)
    return datetime.fromtimestamp(timestamp_ms / 1000, tz=tz).strftime("%Y-%m-%d %H:%M:%S")


def format_timestamp_iso(timestamp_ms: int | None, tz_name: str) -> str | None:
    if timestamp_ms is None:
        return None
    tz = resolve_timezone(tz_name)
    return datetime.fromtimestamp(timestamp_ms / 1000, tz=tz).strftime("%Y-%m-%dT%H:%M:%S")


def compute_session_time_bounds(
    session: SessionRecord, pairs: list[ConversationPair], tz_name: str
) -> tuple[str | None, str | None, int | None]:
    timestamps: list[int] = []
    for pair in pairs:
        timestamps.append(pair.user_time_created)
        if pair.assistant_time_created is not None:
            timestamps.append(pair.assistant_time_created)

    if not timestamps:
        created_iso = format_timestamp_iso(session.time_created, tz_name)
        return created_iso, created_iso, 0

    first_ms = min(timestamps)
    last_ms = max(timestamps)
    duration_seconds = max(0, int((last_ms - first_ms) / 1000))
    return (
        format_timestamp_iso(first_ms, tz_name),
        format_timestamp_iso(last_ms, tz_name),
        duration_seconds,
    )


def shift_markdown_headings(text: str, min_level: int = 3, increment: int = 1) -> str:
    lines = text.splitlines()
    adjusted: list[str] = []
    fence_marker: str | None = None

    for line in lines:
        stripped = line.lstrip()
        indent = line[: len(line) - len(stripped)]

        if stripped.startswith("```") or stripped.startswith("~~~"):
            marker = stripped[:3]
            if fence_marker is None:
                fence_marker = marker
            elif fence_marker == marker:
                fence_marker = None
            adjusted.append(line)
            continue

        if fence_marker is None:
            match = re.match(r"^(#{1,6})(\s+.*)$", stripped)
            if match:
                old_level = len(match.group(1))
                new_level = min(6, max(old_level + increment, min_level))
                adjusted.append(f"{indent}{'#' * new_level}{match.group(2)}")
                continue

        adjusted.append(line)

    return "\n".join(adjusted).strip()


def make_output_path(
    output_dir: Path,
    stem: str,
    session_id: str,
    existing_names: set[str],
) -> Path:
    suffix = 1
    while True:
        candidate_name = f"{stem}.md" if suffix == 1 else f"{stem}_{suffix:02d}.md"
        candidate_path = output_dir / candidate_name
        if candidate_name in existing_names:
            suffix += 1
            continue
        if not candidate_path.exists():
            existing_names.add(candidate_name)
            return candidate_path

        existing_session_id = read_session_id_from_file(candidate_path)
        if existing_session_id == session_id:
            existing_names.add(candidate_name)
            return candidate_path

        suffix += 1


def read_session_id_from_file(path: Path) -> str | None:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return None
    match = SESSION_ID_PATTERN.search(content)
    return match.group(1) if match else None


def read_export_format_version_from_file(path: Path) -> int | None:
    try:
        content = path.read_text(encoding="utf-8")
    except Exception:
        return None
    match = EXPORT_FORMAT_VERSION_PATTERN.search(content)
    return int(match.group(1)) if match else None


def find_existing_session_paths(output_dir: Path, session_id: str) -> list[Path]:
    matches: list[Path] = []
    for path in output_dir.glob("*.md"):
        if read_session_id_from_file(path) == session_id:
            matches.append(path)
    return matches


def build_existing_session_index(output_dir: Path) -> dict[str, str]:
    index: dict[str, str] = {}
    for path in output_dir.rglob("*.md"):
        session_id = read_session_id_from_file(path)
        if session_id:
            index[session_id] = relative_to_output_dir(path, output_dir)
    return index


def build_existing_session_multimap(output_dir: Path) -> dict[str, list[Path]]:
    index: dict[str, list[Path]] = defaultdict(list)
    for path in output_dir.rglob("*.md"):
        session_id = read_session_id_from_file(path)
        if session_id:
            index[session_id].append(path)
    return index


def relative_to_output_dir(path: Path, output_dir: Path) -> str:
    return str(path.resolve().relative_to(output_dir.resolve()))


def load_manifest(manifest_path: Path) -> dict:
    if not manifest_path.exists():
        return {"version": 1, "sessions": {}}
    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception:
        return {"version": 1, "sessions": {}}
    if not isinstance(payload, dict):
        return {"version": 1, "sessions": {}}
    if not isinstance(payload.get("sessions"), dict):
        payload["sessions"] = {}
    payload.setdefault("version", 1)
    return payload


def save_manifest(manifest_path: Path, manifest: dict) -> None:
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")


def render_markdown(
    session: SessionRecord,
    pairs: list[ConversationPair],
    tz_name: str,
    user_label: str,
    project_id: str,
    display_title: str,
) -> str:
    created_at = format_timestamp_iso(session.time_created, tz_name)
    first_message_at, last_message_at, duration_seconds = compute_session_time_bounds(
        session, pairs, tz_name
    )
    assistant_labels: list[str] = []
    seen_labels: set[str] = set()
    for pair in pairs:
        label = format_assistant_label(pair.model_id, pair.provider_id)
        if label not in seen_labels:
            seen_labels.add(label)
            assistant_labels.append(label)

    lines = [
        "---",
        "trace_type: opencode_session",
        f"export_format_version: {EXPORT_FORMAT_VERSION}",
        f"session_id: {yaml_quote(session.session_id)}",
        f"session_title: {yaml_quote(display_title)}",
        f"created_at: {yaml_quote(created_at) if created_at else 'null'}",
        f"user_label: {yaml_quote(user_label)}",
        f"round_count: {len(pairs)}",
        f"first_message_at: {yaml_quote(first_message_at) if first_message_at else 'null'}",
        f"last_message_at: {yaml_quote(last_message_at) if last_message_at else 'null'}",
        f"duration_seconds: {duration_seconds if duration_seconds is not None else 'null'}",
        "assistant_labels:",
    ]
    if session.title != display_title:
        lines.insert(5, f"source_session_title: {yaml_quote(session.title)}")
    if assistant_labels:
        lines.extend([f"  - {yaml_quote(label)}" for label in assistant_labels])
    else:
        lines.append("  - 'OpenCode'")

    lines = [
        *lines,
        "---",
        "",
    ]

    if not pairs:
        lines.extend(["_No user/final-assistant pairs found in this session._", ""])
        return "\n".join(lines)

    for index, pair in enumerate(pairs, start=1):
        assistant_label = format_assistant_label(pair.model_id, pair.provider_id)
        assistant_text = pair.answer_text or "_No final assistant output found._"
        assistant_text = shift_markdown_headings(assistant_text)
        user_heading = user_label
        assistant_heading = assistant_label
        user_timestamp = format_timestamp(pair.user_time_created, tz_name)
        assistant_timestamp = format_timestamp(pair.assistant_time_created, tz_name)
        if user_timestamp:
            user_heading = f"{user_heading} ({user_timestamp})"
        if assistant_timestamp:
            assistant_heading = f"{assistant_heading} ({assistant_timestamp})"
        lines.extend(
            [
                "---",
                "",
                f"# Round {index:02d}",
                "",
                f"## {user_heading}",
                "",
                pair.query_text,
                "",
                f"## {assistant_heading}",
                "",
                assistant_text,
                "",
            ]
        )

    return "\n".join(lines).rstrip() + "\n"


def export_sessions(args: argparse.Namespace) -> list[Path]:
    tz = resolve_timezone(args.timezone)
    if args.all and args.sync:
        raise ValueError("--all and --sync cannot be used together")
    if args.date and args.sync:
        raise ValueError("--date and --sync cannot be used together")

    target_date = None if (args.all or args.sync) else parse_target_date(args.date, tz)
    workspace_root = find_workspace_root(args.workspace)
    project_id = read_project_id(workspace_root)
    output_dir = (args.output_dir or workspace_root / "contexts" / "agent_traces").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    manifest_path = (args.manifest or output_dir / ".export_manifest.json").resolve()
    manifest = load_manifest(manifest_path)
    existing_session_index = build_existing_session_index(output_dir)
    existing_session_multimap = build_existing_session_multimap(output_dir)

    if target_date is None:
        start_ms, end_ms = None, None
    else:
        start_ms, end_ms = millis_range_for_date(target_date, tz)

    conn = sqlite3.connect(args.db)
    conn.row_factory = sqlite3.Row
    try:
        sessions = fetch_sessions(conn, project_id, start_ms, end_ms, args.include_subagents)
        exported_paths: list[Path] = []
        used_names_by_dir: dict[Path, set[str]] = defaultdict(set)
        export_items: list[ExportSession] = []
        filtered_probe_sessions: list[SessionRecord] = []
        filtered_low_signal_sessions: list[SessionRecord] = []
        session_records_by_id = {session.session_id: session for session in sessions}

        for session in sessions:
            pairs = build_conversation_pairs(conn, session.session_id)
            if not args.include_probes and len(pairs) == 1 and is_probe_query(pairs[0].query_text):
                filtered_probe_sessions.append(session)
                continue
            if is_low_signal_session(session, pairs):
                filtered_low_signal_sessions.append(session)
                continue
            if is_suspicious_session_title(session.title) and pairs:
                display_title = summarize_query_as_name(pairs[0].query_text)
            else:
                display_title = session.title

            stem = normalize_session_name(display_title, session.slug or session.session_id[-8:])
            export_items.append(
                ExportSession(
                    session=session,
                    pairs=pairs,
                    display_title=display_title,
                    stem=stem,
                )
            )

        for session in filtered_probe_sessions:
            session_date = datetime.fromtimestamp(session.time_created / 1000, tz=tz).date()
            month_prefix = session_date.strftime("%y%m")
            date_prefix = session_date.strftime("%y%m%d")
            day_dir = output_dir / month_prefix / date_prefix
            stale_paths = find_existing_session_paths(day_dir, session.session_id)
            for stale_path in stale_paths:
                stale_path.unlink(missing_ok=True)
            manifest.get("sessions", {}).pop(session.session_id, None)

        for session in filtered_low_signal_sessions:
            session_date = datetime.fromtimestamp(session.time_created / 1000, tz=tz).date()
            month_prefix = session_date.strftime("%y%m")
            date_prefix = session_date.strftime("%y%m%d")
            day_dir = output_dir / month_prefix / date_prefix
            stale_paths = find_existing_session_paths(day_dir, session.session_id)
            for stale_path in stale_paths:
                stale_path.unlink(missing_ok=True)
            manifest.get("sessions", {}).pop(session.session_id, None)

        if args.sync:
            valid_session_ids = {item.session.session_id for item in export_items}
            probe_session_ids = {session.session_id for session in filtered_probe_sessions}
            low_signal_session_ids = {session.session_id for session in filtered_low_signal_sessions}

            for session_id, paths in existing_session_multimap.items():
                if session_id in valid_session_ids:
                    continue
                if (
                    session_id in probe_session_ids
                    or session_id in low_signal_session_ids
                    or session_id not in session_records_by_id
                ):
                    for path in paths:
                        path.unlink(missing_ok=True)
                    manifest.get("sessions", {}).pop(session_id, None)

            for session_id in list(manifest.get("sessions", {}).keys()):
                if session_id in valid_session_ids:
                    continue
                if (
                    session_id in probe_session_ids
                    or session_id in low_signal_session_ids
                    or session_id not in session_records_by_id
                ):
                    manifest["sessions"].pop(session_id, None)

        if args.sync:
            sessions_to_export: list[ExportSession] = []
            for item in export_items:
                session = item.session
                session_date = datetime.fromtimestamp(session.time_created / 1000, tz=tz).date()
                month_prefix = session_date.strftime("%y%m")
                date_prefix = session_date.strftime("%y%m%d")
                relative_path = f"{month_prefix}/{date_prefix}/{item.stem}.md"
                entry = manifest.get("sessions", {}).get(session.session_id)
                expected_exists = (output_dir / relative_path).exists()
                existing_path = existing_session_index.get(session.session_id)
                if not entry:
                    if existing_path:
                        existing_version = read_export_format_version_from_file(
                            output_dir / existing_path
                        )
                        if existing_version == EXPORT_FORMAT_VERSION:
                            manifest.setdefault("sessions", {})[session.session_id] = {
                                "path": existing_path,
                                "time_updated": session.time_updated,
                                "created_at": session.time_created,
                                "display_title": item.display_title,
                                "export_format_version": EXPORT_FORMAT_VERSION,
                            }
                            continue
                    sessions_to_export.append(item)
                    continue
                if entry.get("time_updated") != session.time_updated:
                    sessions_to_export.append(item)
                    continue
                if entry.get("display_title") != item.display_title:
                    sessions_to_export.append(item)
                    continue
                if entry.get("path") != relative_path:
                    sessions_to_export.append(item)
                    continue
                if entry.get("export_format_version") != EXPORT_FORMAT_VERSION:
                    sessions_to_export.append(item)
                    continue
                if not expected_exists:
                    if existing_path and existing_path == relative_path:
                        entry["path"] = existing_path
                        entry["time_updated"] = session.time_updated
                        entry["created_at"] = session.time_created
                        entry["display_title"] = item.display_title
                        entry["export_format_version"] = EXPORT_FORMAT_VERSION
                        continue
                    sessions_to_export.append(item)
                    continue
                existing_file_version = read_export_format_version_from_file(output_dir / relative_path)
                if existing_file_version != EXPORT_FORMAT_VERSION:
                    sessions_to_export.append(item)
                    continue
            export_items = sessions_to_export

        for item in export_items:
            session = item.session
            pairs = item.pairs
            session_date = datetime.fromtimestamp(session.time_created / 1000, tz=tz).date()
            month_prefix = session_date.strftime("%y%m")
            date_prefix = session_date.strftime("%y%m%d")
            day_dir = output_dir / month_prefix / date_prefix
            day_dir.mkdir(parents=True, exist_ok=True)

            if args.overwrite or args.sync:
                stale_paths = find_existing_session_paths(day_dir, session.session_id)
                for stale_path in stale_paths:
                    if stale_path.name in used_names_by_dir[day_dir]:
                        used_names_by_dir[day_dir].discard(stale_path.name)
                    stale_path.unlink(missing_ok=True)

            output_path = make_output_path(
                day_dir,
                item.stem,
                session.session_id,
                used_names_by_dir[day_dir],
            )

            if output_path.exists() and not args.overwrite:
                raise FileExistsError(
                    f"Output already exists: {output_path}. Use --overwrite to replace it."
                )

            markdown = render_markdown(
                session,
                pairs,
                args.timezone,
                args.user_label,
                project_id,
                item.display_title,
            )
            output_path.write_text(markdown, encoding="utf-8")
            exported_paths.append(output_path)
            manifest.setdefault("sessions", {})[session.session_id] = {
                "path": relative_to_output_dir(output_path, output_dir),
                "time_updated": session.time_updated,
                "created_at": session.time_created,
                "display_title": item.display_title,
                "export_format_version": EXPORT_FORMAT_VERSION,
            }

        manifest["last_exported_at"] = format_timestamp_iso(int(datetime.now(tz).timestamp() * 1000), args.timezone)
        save_manifest(manifest_path, manifest)

        return exported_paths
    finally:
        conn.close()


def main() -> int:
    args = parse_args()
    exported_paths = export_sessions(args)
    if not exported_paths:
        print("No matching sessions found.")
        return 0
    for path in exported_paths:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
