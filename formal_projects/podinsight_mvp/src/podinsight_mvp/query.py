from __future__ import annotations

from podinsight_mvp.types import AnswerProvider, ExtractedCard, QueryAnswer


def _question_hints(question: str) -> set[str]:
    lowered = question.lower()
    hints: set[str] = set()
    if "agent" in lowered or "workflow" in lowered or "tool" in lowered or "work" in lowered:
        hints.add("agent workflow")
    if "coding" in lowered or "code" in lowered or "developer" in lowered:
        hints.add("ai coding")
    if "context" in lowered or "memory" in lowered or "repo" in lowered:
        hints.add("context engineering")
    if "cost" in lowered or "startup" in lowered or "product" in lowered or "business" in lowered:
        hints.add("ai product strategy")
    if "human" in lowered or "career" in lowered or "agency" in lowered or "taste" in lowered:
        hints.add("human leverage")
    return hints


def _select_supporting_cards(question: str, cards: list[ExtractedCard]) -> list[ExtractedCard]:
    hints = _question_hints(question)
    scored_cards: list[tuple[int, int, ExtractedCard]] = []
    question_lower = question.lower()

    for index, card in enumerate(cards):
        score = 0
        for topic in card.topics:
            if topic.lower() in hints:
                score += 4
        searchable = f"{card.claim} {card.boundary}".lower()
        for token in question_lower.split():
            if len(token) > 3 and token in searchable:
                score += 1
        scored_cards.append((score, -index, card))

    scored_cards.sort(reverse=True)
    if scored_cards and scored_cards[0][0] > 0:
        return [card for _, _, card in scored_cards[: min(3, len(scored_cards))]]
    return cards[: min(3, len(cards))]


def _deterministic_summary(question: str, supporting_cards: list[ExtractedCard]) -> str:
    hints = _question_hints(question)
    lowered = question.lower()

    if "ai coding" in hints or "claude code" in lowered or "cursor" in lowered or "coding" in lowered:
        lead = "Across the selected cards, AI coding tools are framed as real leverage for small teams and individual builders."
    elif "human leverage" in hints or "agency" in lowered or "taste" in lowered:
        lead = "Across the selected cards, speakers treat agency and taste as the human advantages that become more important after AI adoption."
    else:
        lead = "Across the selected cards, speakers repeatedly describe AI as useful when it is tied to concrete work rather than abstract hype."

    if any("ai product strategy" in card.topics for card in supporting_cards):
        caveat = "The main caveat is that cost, replacement risk, and rollout discipline still shape where adoption makes sense."
    else:
        caveat = "The main caveat is that teams still need clear workflows and explicit operator judgment around the tool."

    evidence = " ".join(card.claim for card in supporting_cards[:2])
    summary = f"{lead} {caveat}"
    if evidence:
        summary += f" Evidence in the selected cards includes: {evidence}"
    return summary


def answer_query(
    question: str,
    cards: list[ExtractedCard],
    answer_client: AnswerProvider | None,
) -> QueryAnswer:
    supporting_cards = _select_supporting_cards(question, cards)

    if answer_client is None:
        summary = _deterministic_summary(question, supporting_cards)
    else:
        context_lines = []
        for card in supporting_cards:
            evidence_quote = card.evidence[0].quote if card.evidence else ""
            context_lines.append(
                f"Claim: {card.claim}\nBoundary: {card.boundary}\nTopics: {', '.join(card.topics)}\nEvidence: {evidence_quote}"
            )

        response = answer_client.complete(
            messages=[
                {
                    "role": "user",
                    "content": f"Question: {question}\n\nContext:\n" + "\n\n".join(context_lines),
                }
            ]
        )

        summary = response.get("content")
        if summary is None:
            choices = response.get("choices", [])
            if choices:
                summary = choices[0]["message"]["content"]
            else:
                summary = ""

    return QueryAnswer(summary=summary, supporting_cards=supporting_cards)
