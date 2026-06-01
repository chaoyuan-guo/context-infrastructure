from __future__ import annotations

import json
import re
from typing import cast

from podinsight_mvp.types import AnswerProvider, CardCandidate, CardCandidatePayload, ChatCompletionPayload, RelationClassification, TranscriptDocument
from podinsight_mvp.validate import validate_card_candidate


VIEW_NAMES = ("judgment", "controversy", "practice")
ALLOWED_RELATION_LABELS = {"support", "conflict", "prerequisite", "unrelated"}
EVIDENCE_SPLIT_RE = re.compile(r"[;；\n]+")


def _as_object_dict(value: object) -> dict[str, object] | None:
    if not isinstance(value, dict):
        return None
    return cast(dict[str, object], value)


def _response_text(response: ChatCompletionPayload) -> str:
    content = response.get("content")
    if isinstance(content, str) and content.strip():
        return content

    choices = response.get("choices", [])
    if not choices:
        raise ValueError("Model response is missing content")

    first_choice = choices[0]
    message = first_choice.get("message", {})
    choice_content = message.get("content")
    if not isinstance(choice_content, str) or not choice_content.strip():
        raise ValueError("Model response choice is missing content")
    return choice_content


def _strip_code_fence(text: str) -> str:
    stripped = text.strip()
    if not stripped.startswith("```"):
        return stripped

    lines = stripped.splitlines()
    if len(lines) >= 2 and lines[-1].startswith("```"):
        return "\n".join(lines[1:-1]).strip()
    return stripped


def _load_json_object(response: ChatCompletionPayload) -> dict[str, object]:
    raw_payload = cast(object, json.loads(_strip_code_fence(_response_text(response))))
    payload = _as_object_dict(raw_payload)
    if payload is None:
        raise ValueError("Model response must be a JSON object")
    return payload


def _normalize_text(text: str) -> str:
    return " ".join(text.strip().split()).lower()


def _match_transcript_anchor(transcript: TranscriptDocument, quote_text: str) -> dict[str, str] | None:
    normalized_quote = _normalize_text(quote_text)
    if not normalized_quote:
        return None

    for segment in transcript.segments:
        segment_text = segment.text.strip()
        normalized_segment = _normalize_text(segment_text)
        if normalized_quote == normalized_segment:
            quote = segment_text
        elif normalized_quote in normalized_segment:
            quote = quote_text.strip()
        elif normalized_segment in normalized_quote:
            quote = segment_text
        else:
            continue

        return {
            "speaker": segment.speaker,
            "timestamp": segment.timestamp,
            "quote": quote,
        }

    return None


def _coerce_evidence_payload(transcript: TranscriptDocument, evidence_payload: object) -> list[dict[str, str]]:
    evidence: list[dict[str, str]] = []

    def append_anchor(anchor_payload: object) -> None:
        anchor_dict = _as_object_dict(anchor_payload)
        if anchor_dict is not None:
            quote = str(anchor_dict.get("quote", "")).strip()
            if quote:
                matched_anchor = _match_transcript_anchor(transcript, quote)
                if matched_anchor is not None:
                    evidence.append(matched_anchor)
                return

        if isinstance(anchor_payload, str):
            chunks = [chunk.strip() for chunk in EVIDENCE_SPLIT_RE.split(anchor_payload) if chunk.strip()]
            if not chunks:
                chunks = [anchor_payload.strip()]
            for chunk in chunks:
                matched_anchor = _match_transcript_anchor(transcript, chunk)
                if matched_anchor is not None:
                    evidence.append(matched_anchor)

    if isinstance(evidence_payload, list):
        for anchor in evidence_payload:
            append_anchor(anchor)
    else:
        append_anchor(evidence_payload)

    deduped: list[dict[str, str]] = []
    seen = set()
    for anchor in evidence:
        key = (anchor["speaker"], anchor["timestamp"], anchor["quote"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(anchor)

    return deduped


def _coerce_card_payload(item: dict[str, object], view_name: str, transcript: TranscriptDocument) -> CardCandidatePayload:
    evidence = _coerce_evidence_payload(transcript, item.get("evidence", []))

    topics_payload = item.get("topics", [])
    topics: list[str] = []
    if isinstance(topics_payload, list):
        for topic in topics_payload:
            topic_text = str(topic).strip()
            if topic_text:
                topics.append(topic_text)

    action_payload = item.get("action")
    action = str(action_payload).strip() if isinstance(action_payload, str) and action_payload.strip() else None

    return {
        "claim": str(item.get("claim", "")).strip(),
        "evidence": evidence,
        "boundary": str(item.get("boundary", "")).strip(),
        "action": action,
        "topics": topics,
        "source_view": view_name,
    }


def _view_items(view_payload: object) -> list[object]:
    if isinstance(view_payload, list):
        return view_payload
    if isinstance(view_payload, dict):
        return [view_payload]
    return []


def _coerce_view_payloads(payload: dict[str, object], transcript: TranscriptDocument) -> dict[str, list[CardCandidatePayload]]:
    normalized: dict[str, list[CardCandidatePayload]] = {}
    for view_name in VIEW_NAMES:
        view_payload = payload.get(view_name, [])
        items = _view_items(view_payload)
        normalized_items: list[CardCandidatePayload] = []
        for item in items[:2]:
            item_dict = _as_object_dict(item)
            if item_dict is None:
                continue
            candidate_payload = _coerce_card_payload(item_dict, view_name, transcript)
            try:
                validate_card_candidate(CardCandidate.model_validate(candidate_payload))
            except ValueError:
                continue
            normalized_items.append(candidate_payload)
        normalized[view_name] = normalized_items
    return normalized


def _render_transcript_excerpt(transcript: TranscriptDocument, max_segments: int = 60) -> str:
    if not transcript.segments:
        return ""

    if len(transcript.segments) <= max_segments:
        sampled_segments = transcript.segments
    else:
        last_index = len(transcript.segments) - 1
        sampled_indices = sorted({round(index * last_index / (max_segments - 1)) for index in range(max_segments)})
        sampled_segments = [transcript.segments[index] for index in sampled_indices]

    return "\n".join(
        f"[{segment.timestamp}] {segment.speaker}: {segment.text}"
        for segment in sampled_segments
    )


class LLMExtractor:
    def __init__(self, client: AnswerProvider) -> None:
        self.client: AnswerProvider = client
        self.client = client

    def build_candidates(self, transcript: TranscriptDocument) -> dict[str, list[CardCandidatePayload]]:
        response = self.client.complete(
            messages=[
                {
                    "role": "system",
                    "content": "You extract structured opinion cards from podcast transcripts. Return raw JSON only.",
                },
                {
                    "role": "user",
                    "content": (
                        "Extract up to one card for each view: judgment, controversy, and practice.\n"
                        "Return a JSON object with exactly these keys: judgment, controversy, practice.\n"
                        "Each item must have: claim, evidence, boundary, action, topics, source_view.\n"
                        "Rules:\n"
                        "- Use only evidence anchors that appear verbatim in the transcript excerpt.\n"
                        "- boundary must express a concrete condition and should start with phrases like 'This works when', 'This matters when', or 'This holds when'.\n"
                        "- topics should be 1-3 short lowercase phrases.\n"
                        "- If the excerpt does not support a view, return an empty list for that view.\n"
                        "- Return raw JSON only, with no markdown fence.\n\n"
                        f"Episode ID: {transcript.episode_id}\n"
                        f"Show: {transcript.show}\n"
                        f"Title: {transcript.title}\n"
                        f"Date: {transcript.date}\n\n"
                        "Transcript excerpt:\n"
                        f"{_render_transcript_excerpt(transcript)}"
                    ),
                },
            ]
        )
        return _coerce_view_payloads(_load_json_object(response), transcript)


class LLMRelationClassifier:
    def __init__(self, client: AnswerProvider) -> None:
        self.client: AnswerProvider = client
        self.client = client

    def classify(self, left_claim: str, right_claim: str) -> RelationClassification:
        response = self.client.complete(
            messages=[
                {
                    "role": "system",
                    "content": "You classify the relationship between two claims. Return raw JSON only.",
                },
                {
                    "role": "user",
                    "content": (
                        "Return JSON in the form {\"label\": \"support|conflict|prerequisite|unrelated\", \"confidence\": 0.0}.\n"
                        "Use prerequisite only when the right claim is an enabling condition or prior step for the left claim.\n"
                        "Use unrelated when the claims do not materially reinforce, conflict, or depend on each other.\n\n"
                        f"Left claim: {left_claim}\n"
                        f"Right claim: {right_claim}"
                    ),
                },
            ]
        )

        payload = _load_json_object(response)
        label = str(payload.get("label", "unrelated")).strip().lower()
        if label not in ALLOWED_RELATION_LABELS:
            return {"label": "unrelated", "confidence": 0.0}

        confidence_value = payload.get("confidence", 0.0)
        if isinstance(confidence_value, (int, float)):
            confidence = float(confidence_value)
        elif isinstance(confidence_value, str):
            try:
                confidence = float(confidence_value)
            except ValueError:
                confidence = 0.0
        else:
            confidence = 0.0

        return {"label": label, "confidence": max(0.0, min(1.0, confidence))}
