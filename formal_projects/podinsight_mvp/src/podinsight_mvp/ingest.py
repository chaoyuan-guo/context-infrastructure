from __future__ import annotations

import json
import re
from pathlib import Path
from typing import cast

from podinsight_mvp.types import DemoEpisode, EpisodeRecord, QCReport, TranscriptDocument, TranscriptSegment


SEGMENT_RE = re.compile(r"^- \[(?P<timestamp>\d{2}:\d{2}:\d{2})\] (?P<speaker>[^:]+): (?P<text>.+)$")


def parse_transcript(transcript_path: Path) -> TranscriptDocument:
    lines = transcript_path.read_text(encoding="utf-8").splitlines()
    show = ""
    title = ""
    date = ""
    source_url = None
    segments: list[TranscriptSegment] = []

    for line in lines:
        if line.startswith("# 播客频道："):
            show = line.split("：", 1)[1].strip()
            continue
        if line.startswith("# title:"):
            title = line.split(":", 1)[1].strip()
            continue
        if line.startswith("# date:"):
            date = line.split(":", 1)[1].strip()
            continue
        if line.startswith("# url:"):
            source_url = line.split(":", 1)[1].strip()
            continue

        match = SEGMENT_RE.match(line)
        if not match:
            continue
        segments.append(
            TranscriptSegment(
                timestamp=match.group("timestamp"),
                speaker=match.group("speaker").strip(),
                text=match.group("text").strip(),
            )
        )

    return TranscriptDocument(
        episode_id=transcript_path.parent.name,
        show=show,
        title=title,
        date=date,
        source_url=source_url,
        segments=segments,
    )


def load_demo_catalog(project_root: Path, workspace_root: Path) -> list[DemoEpisode]:
    demo_ids = cast(list[str], json.loads((project_root / "data" / "demo_episode_ids.json").read_text(encoding="utf-8")))
    prep_index_raw = cast(list[dict[str, str]], json.loads((workspace_root / "contexts" / "podcast_read" / "prep_index.json").read_text(encoding="utf-8")))
    prep_index = [EpisodeRecord.model_validate(item) for item in prep_index_raw]
    indexed = {item.episode_id: item for item in prep_index}
    episodes: list[DemoEpisode] = []

    for episode_id in demo_ids:
        item = indexed[episode_id]
        qc_path = workspace_root / "contexts" / "podcast_read" / item.qc_report_path
        qc = QCReport.model_validate(json.loads(qc_path.read_text(encoding="utf-8")))
        episodes.append(
            DemoEpisode(
                episode_id=episode_id,
                show_id=item.show_id,
                title=item.title,
                updated_at=item.updated_at,
                source_url=item.source_url,
                transcript_path=workspace_root / "contexts" / "podcast_read" / item.transcript_path,
                qc_path=qc_path,
                qc=qc,
            )
        )

    return episodes
