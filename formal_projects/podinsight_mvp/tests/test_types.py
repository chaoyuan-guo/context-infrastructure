from podinsight_mvp.types import CardCandidate, EvidenceAnchor


def test_card_candidate_requires_core_fields() -> None:
    candidate = CardCandidate(
        claim="Context engineering matters more than prompt tricks once workflows become multi-step.",
        evidence=[EvidenceAnchor(speaker="Annatar", timestamp="00:01:00", quote="Context is what keeps the tool coherent.")],
        boundary="This applies when the workflow spans multiple files or tools.",
        action=None,
        topics=["context engineering"],
        source_view="judgment",
    )

    assert candidate.claim.startswith("Context engineering")
    assert candidate.evidence[0].speaker == "Annatar"
