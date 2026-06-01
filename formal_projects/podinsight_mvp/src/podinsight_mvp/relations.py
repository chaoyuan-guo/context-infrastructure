from __future__ import annotations

from math import sqrt

from podinsight_mvp.types import EmbeddingProvider, ExtractedCard, RelationClassifier, RelationEdge


MIN_RELATION_CONFIDENCE = {
    "support": 0.85,
    "conflict": 0.85,
    "prerequisite": 0.85,
}


def _cosine_similarity(left: list[float], right: list[float]) -> float:
    numerator = sum(a * b for a, b in zip(left, right))
    left_norm = sqrt(sum(a * a for a in left))
    right_norm = sqrt(sum(b * b for b in right))
    if left_norm == 0 or right_norm == 0:
        return 0.0
    return numerator / (left_norm * right_norm)


def build_relations(
    cards: list[ExtractedCard],
    embedding_client: EmbeddingProvider,
    classifier: RelationClassifier,
    top_k: int = 5,
) -> list[RelationEdge]:
    embeddings = {card.claim: embedding_client.embed(card.claim)["embedding"] for card in cards}
    relations: list[RelationEdge] = []

    for card in cards:
        scored = []
        for candidate in cards:
            if candidate.claim == card.claim:
                continue
            similarity = _cosine_similarity(embeddings[card.claim], embeddings[candidate.claim])
            scored.append((similarity, candidate))
        scored.sort(key=lambda item: item[0], reverse=True)

        for _, candidate in scored[:top_k]:
            result = classifier.classify(card.claim, candidate.claim)
            if result["label"] == "unrelated":
                continue
            min_confidence = MIN_RELATION_CONFIDENCE.get(result["label"], 1.0)
            if result["confidence"] < min_confidence:
                continue
            relations.append(
                RelationEdge(
                    left_claim=card.claim,
                    right_claim=candidate.claim,
                    label=result["label"],
                    confidence=result["confidence"],
                )
            )

    deduped: dict[tuple[str, str, str], RelationEdge] = {}
    for relation in relations:
        left_claim, right_claim = sorted([relation.left_claim, relation.right_claim])
        key = (left_claim, right_claim, relation.label)
        stored = deduped.get(key)
        if stored is None or relation.confidence > stored.confidence:
            deduped[key] = relation
    return list(deduped.values())
