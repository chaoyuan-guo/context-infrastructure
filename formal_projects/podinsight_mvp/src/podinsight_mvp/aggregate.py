from __future__ import annotations

from collections import defaultdict

from podinsight_mvp.types import ExtractedCard


def group_cards_by_topic(cards: list[ExtractedCard], aliases: dict[str, list[str]]) -> dict[str, list[ExtractedCard]]:
    alias_to_canonical = {
        alias.strip().lower(): canonical
        for canonical, values in aliases.items()
        for alias in values
    }
    grouped: dict[str, list[ExtractedCard]] = defaultdict(list)

    for card in cards:
        for topic in card.topics:
            canonical = alias_to_canonical.get(topic.strip().lower(), topic.strip().lower())
            grouped[canonical].append(card)

    return dict(grouped)
