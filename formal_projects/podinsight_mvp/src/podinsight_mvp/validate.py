from __future__ import annotations

import re

from podinsight_mvp.types import CardCandidate


GENERIC_BOUNDARY_PHRASES = {
    "this may not apply in some cases",
    "this may not apply",
    "in some cases",
    "某些情况",
    "有些情况下",
}

CONDITION_MARKERS = ("when ", "if ", "unless", "except", "only when", "当", "如果", "除非", "只有在")
QUESTION_MARKERS = ("?", "？")
LOW_SIGNAL_CLAIM_MARKERS = (
    "这个问题第一时间",
    "刚打完扣",
    "一些别的东西",
    "一些具体问题",
    "在大量的被",
    "没法说",
    "写了个朋友圈",
    "聊了很多你的",
    "抽象出来的一个 ai 的思维链",
    "这样的一个 prompt",
    "思考这个问题的价值",
    "会觉得说",
    "回答这个问题",
    "我们用 20 个问题",
    "亚哥很快做了那个",
    "而且是一句非常简单的 prompt",
)
SEQUENCE_CLAIM_RE = re.compile(r"^第[一二三四五六七八九十0-9]+次是用了")


def _strip_claim_punctuation(claim: str) -> str:
    return claim.strip().rstrip("。！？!?，,；;：:")


def _claim_is_question_style(claim: str) -> bool:
    text = _strip_claim_punctuation(claim)
    return any(marker in text for marker in QUESTION_MARKERS) or text.endswith(("吗", "呢")) or (
        "还是" in text and any(marker in text for marker in ("什么", "吗", "呢", "一些别的东西"))
    )


def _claim_is_fragmentary_or_low_signal(claim: str) -> bool:
    text = _strip_claim_punctuation(claim)
    lowered = text.lower()
    if len(text) < 10:
        return True
    if any(marker in lowered for marker in LOW_SIGNAL_CLAIM_MARKERS):
        return True
    if text.endswith("也好"):
        return True
    if SEQUENCE_CLAIM_RE.match(text):
        return True
    if text.endswith("吧") and text.startswith("这个问题"):
        return True
    return False


def validate_card_candidate(candidate: CardCandidate) -> CardCandidate:
    boundary = candidate.boundary.strip()
    if len(boundary) < 20:
        raise ValueError("boundary is too short")

    lowered = boundary.lower()
    if lowered in GENERIC_BOUNDARY_PHRASES or any(phrase in lowered for phrase in GENERIC_BOUNDARY_PHRASES):
        raise ValueError("boundary is too generic")

    if not any(marker in lowered for marker in CONDITION_MARKERS):
        raise ValueError("boundary must express a specific condition")

    if not candidate.evidence:
        raise ValueError("evidence is required")

    if not candidate.claim.strip():
        raise ValueError("claim is required")

    if _claim_is_question_style(candidate.claim):
        raise ValueError("claim must be declarative")

    if _claim_is_fragmentary_or_low_signal(candidate.claim):
        raise ValueError("claim is too weak")

    return candidate
