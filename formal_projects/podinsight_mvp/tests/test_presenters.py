from podinsight_mvp.presenters import build_demo_summary


def test_demo_repository_summary() -> None:
    summary = build_demo_summary(
        episodes=[{"episode_id": "1"}, {"episode_id": "2"}],
        cards=[{"claim": "a"}, {"claim": "b"}, {"claim": "c"}],
        relations=[{"label": "support"}, {"label": "conflict"}],
        themes={"ai coding": [{"claim": "a"}], "agent workflow": [{"claim": "b"}]},
    )

    assert summary["episode_count"] == 2
    assert summary["card_count"] == 3
    assert summary["relation_count"] == 2
    assert summary["theme_count"] == 2
