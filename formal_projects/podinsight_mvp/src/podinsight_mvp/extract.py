from __future__ import annotations

from collections import OrderedDict

from podinsight_mvp.types import CardCandidate, CardCandidatePayload, ExtractedCard
from podinsight_mvp.validate import validate_card_candidate


def _normalize_claim(claim: str) -> str:
    return " ".join(claim.lower().split())


def merge_view_candidates(episode_id: str, view_payloads: dict[str, list[CardCandidatePayload]]) -> list[ExtractedCard]:
    merged: OrderedDict[str, ExtractedCard] = OrderedDict()

    for view_name, payload in view_payloads.items():
        for item in payload:
            candidate = validate_card_candidate(CardCandidate.model_validate(item))
            key = _normalize_claim(candidate.claim)

            if key not in merged:
                merged[key] = ExtractedCard(
                    episode_id=episode_id,
                    claim=candidate.claim,
                    evidence=candidate.evidence,
                    boundary=candidate.boundary,
                    action=candidate.action,
                    topics=list(candidate.topics),
                    source_views=[view_name],
                )
                continue

            current = merged[key]
            topic_union = list(dict.fromkeys([*current.topics, *candidate.topics]))
            source_views = list(dict.fromkeys([*current.source_views, view_name]))
            action = current.action or candidate.action
            merged[key] = current.model_copy(
                update={
                    "topics": topic_union,
                    "source_views": source_views,
                    "action": action,
                }
            )

    return list(merged.values())
