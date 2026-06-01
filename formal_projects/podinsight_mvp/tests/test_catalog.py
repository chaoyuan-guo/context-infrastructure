import json
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[3]
PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_demo_episode_catalog_is_curated_and_available() -> None:
    demo_ids_path = PROJECT_ROOT / "data" / "demo_episode_ids.json"
    prep_index_path = WORKSPACE_ROOT / "contexts" / "podcast_read" / "prep_index.json"

    demo_ids = json.loads(demo_ids_path.read_text(encoding="utf-8"))
    prep_index = json.loads(prep_index_path.read_text(encoding="utf-8"))
    indexed = {item["episode_id"]: item for item in prep_index}

    assert 6 <= len(demo_ids) <= 8, f"expected 6-8 curated episodes, got {len(demo_ids)}"
    assert len(set(demo_ids)) == len(demo_ids), "demo episode ids must be unique"

    for episode_id in demo_ids:
        assert episode_id in indexed, f"episode {episode_id} missing from prep index"
        transcript_path = WORKSPACE_ROOT / "contexts" / "podcast_read" / indexed[episode_id]["path_transcript"]
        qc_path = WORKSPACE_ROOT / "contexts" / "podcast_read" / indexed[episode_id]["path_qc_report"]
        assert transcript_path.exists(), f"missing transcript for {episode_id}"
        assert qc_path.exists(), f"missing qc report for {episode_id}"

        qc = json.loads(qc_path.read_text(encoding="utf-8"))
        assert qc.get("parse_success_rate") == 1.0, f"episode {episode_id} failed parse_success_rate gate"
        assert qc.get("dup_ratio", 1.0) <= 0.05, f"episode {episode_id} dup_ratio too high"
