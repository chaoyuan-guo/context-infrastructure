from __future__ import annotations

import json
import os
import sqlite3
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import pytest


sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ai_session_export.cli import DEFAULT_OPENCODE_DB, run_export
from ai_session_export.markdown import render_markdown
from ai_session_export.models import MessageTurn, SessionRecord
from ai_session_export.sources.claude_code import export_claude_code, parse_claude_session_file
from ai_session_export.sources.codex import (
    DEFAULT_CODEX_SESSION_DIRS,
    DEFAULT_CODEX_SESSION_INDEX,
    export_codex,
    parse_codex_session_file,
)
from ai_session_export.sources.opencode import export_opencode
from ai_session_export.state import DEFAULT_STATE, load_state, save_state
from ai_session_export.utils import sanitize_filename, should_skip_session, unique_output_path, yaml_string


# --------------------------------------------------------------------------- #
# 1. Unit tests (always run, no external deps)
# --------------------------------------------------------------------------- #


def test_sanitize_filename() -> None:
    assert sanitize_filename("应对新老板推翻路线与文档埋坑") == "应对新老板推翻路线与文档埋坑"
    assert sanitize_filename(" AI  @@@  Session !!! ") == "AI_Session"
    assert sanitize_filename("a__b---c") == "a_b_c"
    assert sanitize_filename("") == "untitled"
    assert len(sanitize_filename("x" * 200)) == 80


def test_should_skip_session() -> None:
    assert should_skip_session("@explore subagent: run task")
    assert should_skip_session("Search anything subagent")
    assert should_skip_session("Find details with subagent now")
    assert not should_skip_session("My normal user session")


def test_render_markdown_opencode_shape() -> None:
    record = SessionRecord(
        source="opencode",
        session_id="ses_377f8237dffe",
        title="AI Era Scaling and Organizational Knowledge Transfer",
        date="2026-02-22",
        project_directory="/home/user/project",
        models_used=["claude-opus-4-6", "claude-haiku-4-5"],
        messages=[
            MessageTurn(role="user", content="Question", model="claude-opus-4-6"),
            MessageTurn(role="assistant", content="Answer", model="claude-opus-4-6"),
        ],
    )
    output = render_markdown(record)
    assert output.startswith("---\nsource: opencode\n")
    assert 'session_id: "ses_377f8237dffe"' in output
    assert 'project_directory: "/home/user/project"' in output
    assert 'models_used: ["claude-opus-4-6", "claude-haiku-4-5"]' in output
    assert 'turn_models: ["claude-opus-4-6", "claude-opus-4-6"]' in output
    assert "\n## User\n\nQuestion\n" in output
    assert "\n## Assistant\n\nAnswer\n" in output


def test_render_markdown_turn_models_preserves_null_alignment() -> None:
    record = SessionRecord(
        source="opencode",
        session_id="ses_mixed_models",
        title="Mixed model fixture",
        date="2026-02-22",
        messages=[
            MessageTurn(role="user", content="Question", model="gpt-example"),
            MessageTurn(role="assistant", content="Answer"),
        ],
    )

    output = render_markdown(record)

    assert 'turn_models: ["gpt-example", null]' in output


def test_render_markdown_with_timestamps() -> None:
    # 09:30 and 09:31 local time on a fixed date, expressed as ms epoch.
    t_user = int(datetime(2026, 2, 22, 9, 30).timestamp() * 1000)
    t_assistant = int(datetime(2026, 2, 22, 9, 31).timestamp() * 1000)
    record = SessionRecord(
        source="opencode",
        session_id="ses_ts",
        title="Timestamped session",
        date="2026-02-22",
        messages=[
            MessageTurn(role="user", content="Question", time_created=t_user),
            MessageTurn(role="assistant", content="Answer", time_created=t_assistant),
        ],
    )
    output = render_markdown(record)
    assert "\n## User [09:30]\n\nQuestion\n" in output
    assert "\n## Assistant [09:31]\n\nAnswer\n" in output
    # Frontmatter date is independent of per-turn headers.
    assert 'date: "2026-02-22"' in output


def test_state_load_save_roundtrip(tmp_path: Path) -> None:
    state_file = tmp_path / ".export_state.json"
    assert not state_file.exists()

    loaded = load_state(state_file)
    assert loaded == DEFAULT_STATE

    loaded["opencode"]["last_session_time"] = 123456
    loaded["custom_key"] = "value"
    save_state(loaded, state_file)
    assert state_file.exists()

    reloaded = load_state(state_file)
    assert reloaded["opencode"]["last_session_time"] == 123456
    assert reloaded["custom_key"] == "value"
    # Defaults for other sources are preserved on reload.
    assert reloaded["claude_code"]["last_timestamp"] == 0


def test_state_defaults() -> None:
    state = load_state(Path("/nonexistent/ai-session-export-state.json"))
    assert state["opencode"] == {"last_session_time": 0}
    assert state["claude_code"] == {"last_timestamp": 0}
    assert state["codex"] == {"sessions": {}}


def test_unique_output_path(tmp_path: Path) -> None:
    first = unique_output_path(tmp_path, "2026-06-29", "My session title")
    assert first.name == "20260629_My_session_title.md"
    first.write_text("v1", encoding="utf-8")

    second = unique_output_path(tmp_path, "2026-06-29", "My session title")
    assert second.name == "20260629_My_session_title_2.md"
    second.write_text("v2", encoding="utf-8")

    third = unique_output_path(tmp_path, "2026-06-29", "My session title")
    assert third.name == "20260629_My_session_title_3.md"


def test_yaml_string() -> None:
    assert yaml_string("simple") == '"simple"'
    assert yaml_string('with "quotes"') == '"with \\"quotes\\""'
    assert yaml_string("中文标题") == '"中文标题"'
    # Embedded YAML-significant chars are JSON-quoted, so they stay safe.
    assert yaml_string("a: b") == '"a: b"'


# --------------------------------------------------------------------------- #
# Fixture builders (synthetic, public-safe data)
# --------------------------------------------------------------------------- #


def _seed_opencode_db(db_path: Path) -> None:
    conn = sqlite3.connect(str(db_path))
    conn.executescript(
        """
        CREATE TABLE session (
            id TEXT PRIMARY KEY, title TEXT, directory TEXT, time_created INTEGER
        );
        CREATE TABLE message (
            id TEXT PRIMARY KEY, session_id TEXT, time_created INTEGER, data TEXT
        );
        CREATE TABLE part (
            id TEXT PRIMARY KEY, message_id TEXT, session_id TEXT,
            time_created INTEGER, data TEXT
        );
        """
    )
    session_time = int(datetime(2026, 6, 29, 9, 0).timestamp() * 1000)
    conn.execute(
        "INSERT INTO session (id, title, directory, time_created) VALUES (?,?,?,?)",
        ("ses_fixture", "Fixture OpenCode Session", "/home/user/project", session_time),
    )
    turns = [
        ("user", "Tell me about pytest", "fixture/model", int(datetime(2026, 6, 29, 9, 15).timestamp() * 1000)),
        ("assistant", "pytest is a testing framework", "fixture/model", int(datetime(2026, 6, 29, 9, 16).timestamp() * 1000)),
    ]
    for i, (role, text, model_id, msg_ts) in enumerate(turns):
        msg_id = f"ses_fixture_m{i}"
        data: dict = {"role": role}
        if model_id:
            data["model"] = {"providerID": "fixture", "modelID": model_id} if role == "user" else None
            if role == "assistant":
                data["modelID"] = model_id
        conn.execute(
            "INSERT INTO message (id, session_id, time_created, data) VALUES (?,?,?,?)",
            (msg_id, "ses_fixture", msg_ts, json.dumps(data)),
        )
        conn.execute(
            "INSERT INTO part (id, message_id, session_id, time_created, data) VALUES (?,?,?,?,?)",
            (f"{msg_id}_p0", msg_id, "ses_fixture", msg_ts, json.dumps({"type": "text", "text": text})),
        )
    conn.commit()
    conn.close()


def _write_claude_session(projects_root: Path, history_file: Path) -> None:
    project_dir = projects_root / "-home-user-project"
    project_dir.mkdir(parents=True, exist_ok=True)
    history_file.write_text(
        json.dumps(
            {
                "display": "Fixture Claude Task",
                "timestamp": 1711260000000,
                "project": "/home/user/project",
                "sessionId": "claude-fixture-1",
            },
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    (project_dir / "claude-fixture-1.jsonl").write_text(
        "\n".join(
            [
                json.dumps(
                    {
                        "type": "user",
                        "timestamp": "2026-06-29T09:00:00Z",
                        "sessionId": "claude-fixture-1",
                        "cwd": "/home/user/project",
                        "message": {"role": "user", "content": "Review the fixture code"},
                        "isSidechain": False,
                    }
                ),
                json.dumps(
                    {
                        "type": "assistant",
                        "timestamp": "2026-06-29T09:05:00Z",
                        "sessionId": "claude-fixture-1",
                        "cwd": "/home/user/project",
                        "message": {
                            "role": "assistant",
                            "model": "claude-opus-4-6",
                            "content": [
                                {"type": "tool_use", "name": "Glob"},
                                {"type": "text", "text": "The fixture looks good."},
                            ],
                        },
                        "isSidechain": False,
                    }
                ),
                json.dumps(
                    {
                        "type": "user",
                        "timestamp": "2026-06-29T09:06:00Z",
                        "sessionId": "claude-fixture-1",
                        "cwd": "/home/user/project",
                        "message": {
                            "role": "user",
                            "content": [{"type": "tool_result", "content": "tool noise"}],
                        },
                        "isSidechain": False,
                    }
                ),
                json.dumps(
                    {
                        "type": "user",
                        "timestamp": "2026-06-29T09:07:00Z",
                        "sessionId": "claude-fixture-1",
                        "cwd": "/home/user/project",
                        "message": {"role": "user", "content": "Check one more fixture"},
                        "isSidechain": False,
                    }
                ),
                json.dumps(
                    {
                        "type": "assistant",
                        "timestamp": "2026-06-29T09:08:00Z",
                        "sessionId": "claude-fixture-1",
                        "cwd": "/home/user/project",
                        "message": {
                            "role": "assistant",
                            "model": "claude-sonnet-4-6",
                            "content": "The second fixture also looks good.",
                        },
                        "isSidechain": False,
                    }
                ),
            ]
        )
        + "\n",
        encoding="utf-8",
    )


def _write_codex_session(session_dir: Path, index_file: Path, *, include_followup: bool = False) -> Path:
    session_dir.mkdir(parents=True, exist_ok=True)
    index_file.write_text(
        json.dumps(
            {
                "id": "codex-fixture-1",
                "thread_name": "Fixture Codex Task",
                "updated_at": "2026-06-29T09:05:00Z",
            }
        )
        + "\n",
        encoding="utf-8",
    )
    events = [
        {
            "timestamp": "2026-06-29T09:00:00Z",
            "type": "session_meta",
            "payload": {
                "id": "codex-fixture-1",
                "cwd": "/home/user/project",
                "base_instructions": "private system instructions",
            },
        },
        {
            "timestamp": "2026-06-29T09:00:01Z",
            "type": "turn_context",
            "payload": {"cwd": "/home/user/project", "model": "fixture-codex-model"},
        },
        {
            "timestamp": "2026-06-29T09:00:02Z",
            "type": "event_msg",
            "payload": {"type": "user_message", "message": "Review the fixture project"},
        },
        {
            "timestamp": "2026-06-29T09:00:03Z",
            "type": "event_msg",
            "payload": {"type": "agent_reasoning", "text": "private reasoning"},
        },
        {
            "timestamp": "2026-06-29T09:00:04Z",
            "type": "response_item",
            "payload": {"type": "function_call_output", "output": "private tool output"},
        },
        {
            "timestamp": "2026-06-29T09:00:05Z",
            "type": "event_msg",
            "payload": {"type": "agent_message", "phase": "final_answer", "message": "The fixture looks good."},
        },
    ]
    if include_followup:
        events.extend(
            [
                {
                    "timestamp": "2026-06-29T09:04:59Z",
                    "type": "turn_context",
                    "payload": {"model": "fixture-codex-model-2"},
                },
                {
                    "timestamp": "2026-06-29T09:05:00Z",
                    "type": "event_msg",
                    "payload": {"type": "user_message", "message": "Anything else?"},
                },
                {
                    "timestamp": "2026-06-29T09:05:01Z",
                    "type": "event_msg",
                    "payload": {"type": "agent_message", "phase": "final_answer", "message": "No further issues."},
                },
            ]
        )
    session_file = session_dir / "rollout-2026-06-29T09-00-00-codex-fixture-1.jsonl"
    session_file.write_text("\n".join(json.dumps(event) for event in events) + "\n", encoding="utf-8")
    return session_file


# --------------------------------------------------------------------------- #
# 2. Source adapter unit tests (tmp_path + synthetic fixtures)
# --------------------------------------------------------------------------- #


def test_opencode_export_with_fixture(tmp_path: Path) -> None:
    db_path = tmp_path / "opencode.db"
    _seed_opencode_db(db_path)

    state = {"opencode": {"last_session_time": 0}}
    result = export_opencode(
        tmp_path / "out", state, db_path=db_path, full=True, dry_run=False, since_date=None
    )
    assert result["exported"] == 1

    files = list((tmp_path / "out").glob("*.md"))
    assert len(files) == 1
    text = files[0].read_text(encoding="utf-8")
    assert "source: opencode" in text
    assert "## User [09:15]" in text
    assert "## Assistant [09:16]" in text
    assert "Tell me about pytest" in text
    assert 'project_directory: "/home/user/project"' in text
    assert "fixture/model" in text  # surfaced in models_used
    assert 'turn_models: ["fixture/model", "fixture/model"]' in text


def test_claude_code_export_with_fixture(tmp_path: Path) -> None:
    projects_root = tmp_path / "projects"
    history_file = tmp_path / "history.jsonl"
    _write_claude_session(projects_root, history_file)

    state = {"claude_code": {"last_timestamp": 0}}
    result = export_claude_code(
        tmp_path / "claude_code",
        state,
        full=False,
        dry_run=False,
        since_date=None,
        project_dirs=(projects_root,),
        history_files=(history_file,),
    )
    assert result["exported"] == 1

    files = list((tmp_path / "claude_code").glob("*.md"))
    assert len(files) == 1
    content = files[0].read_text(encoding="utf-8")
    assert "source: claude_code" in content
    assert "Fixture Claude Task" in content
    assert 'project_directory: "/home/user/project"' in content
    # tool_result user message has no text content and is dropped.
    assert "tool noise" not in content
    # Assistant text survives even though a tool_use item sat next to it.
    assert "The fixture looks good." in content
    parsed = parse_claude_session_file(
        projects_root / "-home-user-project" / "claude-fixture-1.jsonl",
        {"claude-fixture-1": [(1711260000000, "Fixture Claude Task")]},
    )
    assert parsed is not None
    assert [m.role for m in parsed.record.messages] == ["user", "assistant", "user", "assistant"]
    assert [m.model for m in parsed.record.messages] == [
        "claude-opus-4-6",
        "claude-opus-4-6",
        "claude-sonnet-4-6",
        "claude-sonnet-4-6",
    ]
    assert (
        'turn_models: ["claude-opus-4-6", "claude-opus-4-6", "claude-sonnet-4-6", '
        '"claude-sonnet-4-6"]' in content
    )


def test_claude_missing_assistant_model_does_not_leak_later_model(tmp_path: Path) -> None:
    session_file = tmp_path / "claude-missing-model.jsonl"
    events = [
        {
            "type": "user",
            "timestamp": "2026-06-29T09:00:00Z",
            "sessionId": "claude-missing-model",
            "message": {"role": "user", "content": "First fixture question"},
        },
        {
            "type": "assistant",
            "timestamp": "2026-06-29T09:01:00Z",
            "sessionId": "claude-missing-model",
            "message": {"role": "assistant", "content": "First fixture answer"},
        },
        {
            "type": "user",
            "timestamp": "2026-06-29T09:02:00Z",
            "sessionId": "claude-missing-model",
            "message": {"role": "user", "content": "Second fixture question"},
        },
        {
            "type": "assistant",
            "timestamp": "2026-06-29T09:03:00Z",
            "sessionId": "claude-missing-model",
            "message": {
                "role": "assistant",
                "model": "claude-fixture-later",
                "content": "Second fixture answer",
            },
        },
    ]
    session_file.write_text("\n".join(json.dumps(event) for event in events) + "\n", encoding="utf-8")

    parsed = parse_claude_session_file(session_file, {})

    assert parsed is not None
    assert [message.model for message in parsed.record.messages] == [
        None,
        None,
        "claude-fixture-later",
        "claude-fixture-later",
    ]


def test_codex_export_with_fixture_and_incremental_update(tmp_path: Path) -> None:
    session_dir = tmp_path / "sessions"
    index_file = tmp_path / "session_index.jsonl"
    session_file = _write_codex_session(session_dir, index_file)
    state = {"codex": {"sessions": {}}}
    output_dir = tmp_path / "codex"

    first = export_codex(
        output_dir,
        state,
        full=False,
        dry_run=False,
        since_date=None,
        session_dirs=(session_dir,),
        session_index=index_file,
    )
    assert first == {"source": "codex", "scanned": 1, "exported": 1}
    files = list(output_dir.glob("*.md"))
    assert len(files) == 1
    text = files[0].read_text(encoding="utf-8")
    assert "source: codex" in text
    assert "Fixture Codex Task" in text
    assert "Review the fixture project" in text
    assert "The fixture looks good." in text
    assert "private reasoning" not in text
    assert "private tool output" not in text
    assert "private system instructions" not in text
    assert "fixture-codex-model" in text
    parsed = parse_codex_session_file(session_file, {"codex-fixture-1": "Fixture Codex Task"})
    assert parsed is not None
    assert [message.role for message in parsed.record.messages] == ["user", "assistant"]
    assert [message.model for message in parsed.record.messages] == [
        "fixture-codex-model",
        "fixture-codex-model",
    ]
    assert 'turn_models: ["fixture-codex-model", "fixture-codex-model"]' in text

    unchanged = export_codex(
        output_dir,
        state,
        full=False,
        dry_run=False,
        since_date=None,
        session_dirs=(session_dir,),
        session_index=index_file,
    )
    assert unchanged["exported"] == 0

    _write_codex_session(session_dir, index_file, include_followup=True)
    updated = export_codex(
        output_dir,
        state,
        full=False,
        dry_run=False,
        since_date=None,
        session_dirs=(session_dir,),
        session_index=index_file,
    )
    assert updated["exported"] == 1
    assert len(list(output_dir.glob("*.md"))) == 1
    updated_text = files[0].read_text(encoding="utf-8")
    assert "No further issues." in updated_text
    assert (
        'turn_models: ["fixture-codex-model", "fixture-codex-model", '
        '"fixture-codex-model-2", "fixture-codex-model-2"]' in updated_text
    )


def test_codex_model_context_after_user_backfills_turn(tmp_path: Path) -> None:
    session_file = tmp_path / "rollout-2026-06-29T09-00-00-codex-delayed.jsonl"
    events = [
        {
            "timestamp": "2026-06-29T09:00:00Z",
            "type": "session_meta",
            "payload": {"id": "codex-delayed", "cwd": "/home/user/project"},
        },
        {
            "timestamp": "2026-06-29T09:00:01Z",
            "type": "event_msg",
            "payload": {"type": "user_message", "message": "Review the delayed fixture"},
        },
        {
            "timestamp": "2026-06-29T09:00:02Z",
            "type": "turn_context",
            "payload": {"model": "fixture-delayed-model"},
        },
        {
            "timestamp": "2026-06-29T09:00:03Z",
            "type": "event_msg",
            "payload": {"type": "agent_message", "message": "Reviewed."},
        },
    ]
    session_file.write_text("\n".join(json.dumps(event) for event in events) + "\n", encoding="utf-8")

    parsed = parse_codex_session_file(session_file, {})

    assert parsed is not None
    assert [message.model for message in parsed.record.messages] == [
        "fixture-delayed-model",
        "fixture-delayed-model",
    ]


# --------------------------------------------------------------------------- #
# 3. Integration test (self-contained; also runnable via `pytest -m integration`)
# --------------------------------------------------------------------------- #


@pytest.mark.integration
def test_cli_run_export_all_sources(tmp_path: Path) -> None:
    opencode_db = tmp_path / "opencode.db"
    _seed_opencode_db(opencode_db)

    projects_root = tmp_path / "projects"
    history_file = tmp_path / "history.jsonl"
    _write_claude_session(projects_root, history_file)

    codex_dir = tmp_path / "codex_sessions"
    codex_index = tmp_path / "codex_session_index.jsonl"
    _write_codex_session(codex_dir, codex_index)

    state_file = tmp_path / ".export_state.json"
    results = run_export(
        "all",
        full=True,
        dry_run=False,
        base_dir=tmp_path,
        state_file=state_file,
        opencode_db=opencode_db,
        claude_project_dirs=(projects_root,),
        claude_history_files=(history_file,),
        codex_session_dirs=(codex_dir,),
        codex_session_index=codex_index,
    )

    assert {r["source"] for r in results} == {
        "opencode",
        "claude_code",
        "codex",
    }

    # Each source produced at least one markdown file under base_dir.
    for sub in ("opencode", "claude_code", "codex"):
        assert list((tmp_path / sub).glob("*.md")), f"no markdown emitted for {sub}"

    # State file was persisted with refreshed counters.
    persisted = load_state(state_file)
    assert persisted["opencode"]["last_session_time"] > 0
    assert persisted["claude_code"]["last_timestamp"] > 0
    assert persisted["codex"]["sessions"]["codex-fixture-1"]["latest_timestamp"] > 0


# --------------------------------------------------------------------------- #
# 4. Live end-to-end tests (real data; skipped unless AI_SESSION_EXPORT_LIVE=1)
# --------------------------------------------------------------------------- #


@pytest.mark.live_e2e
class TestLiveExport:
    @pytest.fixture(autouse=True)
    def _check_live(self) -> None:
        if not os.environ.get("AI_SESSION_EXPORT_LIVE"):
            pytest.skip("Set AI_SESSION_EXPORT_LIVE=1 to run live tests")

    def test_live_opencode_export(self, tmp_path: Path) -> None:
        """Export recent OpenCode sessions."""
        if not DEFAULT_OPENCODE_DB.exists():
            pytest.skip(f"OpenCode DB not found: {DEFAULT_OPENCODE_DB}")

        since = date.today() - timedelta(days=7)

        # Dry-run first.
        export_opencode(
            tmp_path / "dry",
            {},
            db_path=DEFAULT_OPENCODE_DB,
            full=True,
            dry_run=True,
            since_date=since,
        )

        # Real export.
        result = export_opencode(
            tmp_path / "opencode",
            {},
            db_path=DEFAULT_OPENCODE_DB,
            full=True,
            dry_run=False,
            since_date=since,
        )
        files = list((tmp_path / "opencode").glob("*.md"))
        if result["exported"] == 0:
            pytest.skip("No recent OpenCode sessions to export")
        assert len(files) == result["exported"]
        sample = files[0].read_text(encoding="utf-8")
        assert "source: opencode" in sample

    def test_live_codex_export(self, tmp_path: Path) -> None:
        """Export recent Codex sessions without exposing transcript content."""
        if not any(path.is_dir() for path in DEFAULT_CODEX_SESSION_DIRS):
            pytest.skip("No Codex session directories found")

        since = date.today() - timedelta(days=7)
        result = export_codex(
            tmp_path / "codex",
            {},
            full=True,
            dry_run=False,
            since_date=since,
            session_dirs=DEFAULT_CODEX_SESSION_DIRS,
            session_index=DEFAULT_CODEX_SESSION_INDEX,
        )
        files = list((tmp_path / "codex").glob("*.md"))
        if result["exported"] == 0:
            pytest.skip("No recent Codex sessions to export")
        assert len(files) == result["exported"]
        assert "source: codex" in files[0].read_text(encoding="utf-8")
