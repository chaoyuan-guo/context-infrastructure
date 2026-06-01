import json

from podinsight_mvp.extract import merge_view_candidates


def test_merge_view_candidates_dedupes_overlap_and_preserves_provenance(project_root) -> None:
    fixtures = project_root / "tests" / "fixtures"
    judgment = json.loads((fixtures / "extract_judgment_response.json").read_text(encoding="utf-8"))
    controversy = json.loads((fixtures / "extract_controversy_response.json").read_text(encoding="utf-8"))
    practice = json.loads((fixtures / "extract_practice_response.json").read_text(encoding="utf-8"))

    merged = merge_view_candidates(
        episode_id="4597222",
        view_payloads={
            "judgment": judgment,
            "controversy": controversy,
            "practice": practice,
        },
    )

    assert len(merged) == 3
    first = next(card for card in merged if card.claim.startswith("Claude Code becomes more valuable"))
    assert sorted(first.source_views) == ["controversy", "judgment"]
    assert first.episode_id == "4597222"
    assert "context engineering" in first.topics
