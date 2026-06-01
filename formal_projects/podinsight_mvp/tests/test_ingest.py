from podinsight_mvp.ingest import parse_transcript, load_demo_catalog


def test_parse_transcript_extracts_segments(workspace_root, project_root) -> None:
    transcript_path = workspace_root / "contexts" / "podcast_read" / "4597222" / "Transcript.md"

    transcript = parse_transcript(transcript_path)

    assert transcript.episode_id == "4597222"
    assert transcript.show == "AsyncTalk"
    assert transcript.title == "EP47 Claude Code 它不一样"
    assert transcript.date == "2025-07-03"
    assert len(transcript.segments) > 100
    first = transcript.segments[0]
    assert first.timestamp == "00:00:00"
    assert first.speaker == "Annatar"
    assert first.text.startswith("Hello")


def test_parse_transcript_skips_non_dialogue_lines(tmp_path) -> None:
    transcript_path = tmp_path / "Transcript.md"
    transcript_path.write_text(
        "# Transcript\n# 播客频道：Demo\n# title: Test\n# date: 2025-01-01\n\nnot a segment\n- [00:00:00] Host: hello\n",
        encoding="utf-8",
    )

    transcript = parse_transcript(transcript_path)

    assert len(transcript.segments) == 1
    assert transcript.segments[0].speaker == "Host"


def test_load_demo_catalog_resolves_curated_episodes(workspace_root, project_root) -> None:
    catalog = load_demo_catalog(project_root, workspace_root)

    assert len(catalog) == 8
    assert catalog[0].episode_id == "4597222"
    assert catalog[0].transcript_path.name == "Transcript.md"
    assert catalog[0].qc.parse_success_rate == 1.0
