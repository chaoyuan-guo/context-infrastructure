from podinsight_mvp.aggregate import group_cards_by_topic
from podinsight_mvp.types import EvidenceAnchor, ExtractedCard


def test_group_cards_by_topic_normalizes_aliases() -> None:
    cards = [
        ExtractedCard(
            episode_id="1",
            claim="A",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:01", quote="q")],
            boundary="This works when the task is scoped.",
            topics=["claude code", "agent workflow"],
            source_views=["judgment"],
        )
    ]
    aliases = {"ai coding": ["claude code"], "agent workflow": ["agent workflow"]}

    grouped = group_cards_by_topic(cards, aliases)

    assert set(grouped) == {"ai coding", "agent workflow"}
    assert grouped["ai coding"][0].claim == "A"
