import pytest

from podinsight_mvp.types import CardCandidate, EvidenceAnchor
from podinsight_mvp.validate import validate_card_candidate


def _build_candidate(claim: str) -> CardCandidate:
    return CardCandidate(
        claim=claim,
        evidence=[EvidenceAnchor(speaker="Guest", timestamp="00:02:00", quote=claim)],
        boundary="This works when the workflow stays scoped and another operator can still verify the result.",
        action="Pilot the workflow on one bounded task.",
        topics=["agent workflow"],
        source_view="practice",
    )


def test_validate_card_candidate_accepts_specific_boundary() -> None:
    candidate = CardCandidate(
        claim="Coding agents amplify output when the engineer can keep the task scoped.",
        evidence=[EvidenceAnchor(speaker="Guest", timestamp="00:02:00", quote="It works when the task stays scoped.")],
        boundary="It breaks down when the codebase is unfamiliar and the task has no clear boundary.",
        action="Break the work into smaller tasks first.",
        topics=["agent workflow"],
        source_view="practice",
    )

    validated = validate_card_candidate(candidate)
    assert validated.boundary.startswith("It breaks down")


def test_validate_card_candidate_rejects_generic_boundary() -> None:
    candidate = CardCandidate(
        claim="Agents are useful.",
        evidence=[EvidenceAnchor(speaker="Guest", timestamp="00:02:00", quote="Agents are useful.")],
        boundary="This may not apply in some cases.",
        action=None,
        topics=["agent workflow"],
        source_view="judgment",
    )

    with pytest.raises(ValueError, match="boundary"):
        validate_card_candidate(candidate)


@pytest.mark.parametrize(
    "claim",
    [
        "在大量的被 AI agent 替换掉。",
        "它是基于 MCP 还是 API 还是一些别的东西。",
        "我觉得模型机产品这个东西我没法说，但我觉得模型机能力这个可以吗。",
        "我们前几年聊了很多你的 AI Talker，你的 Prompt 工程师，或者是 Agent 的创业。",
        "前两天写了个朋友圈，我就说美国有很多这种 AI 创业让人感觉是中产创业。",
        "抽象出来的一个 AI 的思维链或者 AI 的 Prompt。",
        "包括我们产品的一些具体问题。",
        "这个问题第一时间就想到了刚打完扣的一个创业者吧。",
        "第四次是用了 MCP，然后第五次是用 Cursor。",
        "这样的一个 prompt 其实丢给豆包也好。",
        "思考这个问题的价值在于思考模型下一步能进化到什么程度。",
        "会觉得说 MCP 是一个很好玩的一个新的方向。",
        "我们用 20 个问题一起搞懂 AI Agent。",
        "亚哥很快做了那个就是 Cursor to Devon，然后我们又出了 AgenticAI 的课，那是 1 月份出的。",
        "而且是一句非常简单的 prompt 所带来的这很漂亮的一整套的结果。",
    ],
)
def test_validate_card_candidate_rejects_weak_or_fragmentary_claims(claim: str) -> None:
    with pytest.raises(ValueError, match="claim"):
        validate_card_candidate(_build_candidate(claim))


def test_validate_card_candidate_accepts_short_but_specific_claim() -> None:
    candidate = _build_candidate("MCP 很有价值，确实大家 adoption 包括生态支持非常好。")

    validated = validate_card_candidate(candidate)

    assert validated.claim.startswith("MCP 很有价值")
