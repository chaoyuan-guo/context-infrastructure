from podinsight_mvp.query import answer_query
from podinsight_mvp.types import ChatCompletionPayload, EvidenceAnchor, ExtractedCard


class DummyAnswerClient:
    def complete(self, messages: list[dict[str, str]]) -> ChatCompletionPayload:
        _ = messages
        return {"content": "Scoped tasks make agents reliable. Evidence: card-1, card-2. Boundary: unfamiliar repos reduce gains."}


def test_answer_query_returns_supporting_cards_and_boundaries() -> None:
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
            episode_id="2",
            claim="Claude Code becomes more valuable when it can reason across multiple files and tools.",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:02", quote="q")],
            boundary="This only holds when the engineer can keep the task scoped.",
            topics=["ai coding"],
            source_views=["judgment"],
        ),
    ]

    answer = answer_query("What do these episodes suggest about coding agents?", cards, DummyAnswerClient())

    assert "Scoped tasks make agents reliable" in answer.summary
    assert len(answer.supporting_cards) == 2
    assert answer.supporting_cards[0].boundary


def test_answer_query_builds_deterministic_summary_without_client() -> None:
    cards = [
        ExtractedCard(
            episode_id="1",
            claim="Claude Code becomes more valuable when it can reason across multiple files and tools.",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:01", quote="q")],
            boundary="This works when the task is scoped.",
            topics=["ai coding", "agent workflow"],
            source_views=["judgment"],
        ),
        ExtractedCard(
            episode_id="2",
            claim="Prompt workflows become more reliable when the operator writes down explicit handoffs.",
            evidence=[EvidenceAnchor(speaker="s", timestamp="00:00:02", quote="q")],
            boundary="This holds when the workflow is documented.",
            topics=["agent workflow", "context engineering"],
            source_views=["practice"],
        ),
    ]

    answer = answer_query("What do these episodes suggest about coding agents?", cards, None)

    assert "AI coding tools are framed as real leverage" in answer.summary
    assert "Claude Code becomes more valuable" in answer.summary
    assert len(answer.supporting_cards) == 2
