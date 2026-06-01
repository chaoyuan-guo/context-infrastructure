from __future__ import annotations

from collections.abc import Mapping, Sequence


def build_demo_summary(
    *,
    episodes: Sequence[object],
    cards: Sequence[object],
    relations: Sequence[object],
    themes: Mapping[str, Sequence[object]],
) -> dict[str, int]:
    return {
        "episode_count": len(episodes),
        "card_count": len(cards),
        "relation_count": len(relations),
        "theme_count": len(themes),
    }
