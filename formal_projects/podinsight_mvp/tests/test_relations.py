import json
from typing import cast

from podinsight_mvp.relations import build_relations
from podinsight_mvp.types import EmbeddingPayload, EvidenceAnchor, ExtractedCard, RelationClassification


class DummyEmbeddingClient:
    def __init__(self, mapping: dict[str, list[float]]) -> None:
        self.mapping = mapping

    def embed(self, text: str) -> EmbeddingPayload:
        return {"embedding": self.mapping[text]}


class DummyRelationClassifier:
    def __init__(self, mapping: dict[tuple[str, str], RelationClassification]) -> None:
        self.mapping = mapping

    def classify(self, left_claim: str, right_claim: str) -> RelationClassification:
        return self.mapping.get((left_claim, right_claim), {"label": "unrelated", "confidence": 0.0})


def test_build_relations_uses_embedding_recall_and_confidence_gate(project_root) -> None:
    fixtures = project_root / "tests" / "fixtures"
    relation_pairs = cast(list[dict[str, object]], json.loads((fixtures / "relation_pairs.json").read_text(encoding="utf-8")))
    mapping: dict[tuple[str, str], RelationClassification] = {
        (cast(str, item["left_claim"]), cast(str, item["right_claim"])): {
            "label": cast(str, item["label"]),
            "confidence": cast(float, item["confidence"]),
        }
        for item in relation_pairs
    }

    cards = [
        ExtractedCard(
            episode_id="1",
            claim="Coding agents amplify output when the user decomposes work into bounded steps.",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:01", quote="q")],
            boundary="This works when the task is scoped.",
            topics=["agent workflow"],
            source_views=["practice"],
        ),
        ExtractedCard(
            episode_id="1",
            claim="Claude Code becomes more valuable when it can reason across multiple files and tools.",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:02", quote="q")],
            boundary="This only holds when the engineer can keep the task scoped.",
            topics=["ai coding"],
            source_views=["judgment"],
        ),
        ExtractedCard(
            episode_id="1",
            claim="API-priced coding agents are too expensive for sustained heavy use.",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:03", quote="q")],
            boundary="This matters when usage is frequent enough that token spend compounds.",
            topics=["ai product strategy"],
            source_views=["controversy"],
        ),
    ]

    embeddings = DummyEmbeddingClient(
        {
            cards[0].claim: [1.0, 0.0],
            cards[1].claim: [0.9, 0.1],
            cards[2].claim: [0.8, 0.2],
        }
    )
    classifier = DummyRelationClassifier(mapping)

    relations = build_relations(cards, embeddings, classifier, top_k=2)

    assert len(relations) == 2
    assert {relation.label for relation in relations} == {"support", "conflict"}


def test_build_relations_drops_low_confidence_support_edges() -> None:
    cards = [
        ExtractedCard(
            episode_id="1",
            claim="Prompt workflows become more reliable when they are written down as repeatable steps.",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:01", quote="q")],
            boundary="This works when another operator can verify the workflow.",
            topics=["agent workflow"],
            source_views=["practice"],
        ),
        ExtractedCard(
            episode_id="1",
            claim="Documentation keeps prompt workflows reproducible across operators.",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:02", quote="q")],
            boundary="This holds when the workflow is shared with the team.",
            topics=["context engineering"],
            source_views=["practice"],
        ),
    ]

    embeddings = DummyEmbeddingClient(
        {
            cards[0].claim: [1.0, 0.0],
            cards[1].claim: [0.95, 0.05],
        }
    )
    classifier = DummyRelationClassifier(
        {
            (cards[0].claim, cards[1].claim): {"label": "support", "confidence": 0.84},
            (cards[1].claim, cards[0].claim): {"label": "support", "confidence": 0.84},
        }
    )

    relations = build_relations(cards, embeddings, classifier, top_k=1)

    assert relations == []
