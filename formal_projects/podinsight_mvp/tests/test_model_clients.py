import json

from podinsight_mvp.model_clients import LLMExtractor, LLMRelationClassifier
from podinsight_mvp.types import ChatCompletionPayload, TranscriptDocument, TranscriptSegment


class StubChatClient:
    def __init__(self, payload: ChatCompletionPayload) -> None:
        self.payload: ChatCompletionPayload = payload
        self.payload = payload
        self.calls: list[list[dict[str, str]]] = []

    def complete(self, messages: list[dict[str, str]]) -> ChatCompletionPayload:
        self.calls.append(messages)
        return self.payload


def test_llm_extractor_parses_json_content() -> None:
    transcript = TranscriptDocument(
        episode_id="episode-1",
        show="Demo Show",
        title="Why bounded work helps agents",
        date="2026-05-31",
        segments=[
            TranscriptSegment(timestamp="00:00:10", speaker="Host", text="Scoped tasks make agent output easier to verify."),
            TranscriptSegment(timestamp="00:03:00", speaker="Guest", text="Teams still need to watch for reliability drift at scale."),
        ],
    )
    client = StubChatClient(
        {
            "content": json.dumps(
                {
                    "judgment": [
                        {
                            "claim": "Scoped tasks make coding agents easier to trust.",
                            "evidence": [
                                {
                                    "speaker": "Host",
                                    "timestamp": "00:00:10",
                                    "quote": "Scoped tasks make agent output easier to verify.",
                                }
                            ],
                            "boundary": "This works when the engineer can review the repository context and verify the output.",
                            "action": "Start with bounded tasks.",
                            "topics": ["ai coding", "agent workflow"],
                            "source_view": "wrong-view",
                        }
                    ],
                    "controversy": [],
                    "practice": [],
                }
            )
        }
    )

    extractor = LLMExtractor(client)
    payload = extractor.build_candidates(transcript)

    assert payload["judgment"][0]["source_view"] == "judgment"
    assert payload["judgment"][0]["topics"] == ["ai coding", "agent workflow"]
    assert client.calls, "extractor should call the chat client"


def test_llm_relation_classifier_reads_choice_content() -> None:
    client = StubChatClient(
        {
            "choices": [
                {
                    "message": {
                        "content": '{"label": "support", "confidence": 0.91}',
                    }
                }
            ]
        }
    )

    classifier = LLMRelationClassifier(client)
    result = classifier.classify("Scoped tasks improve reliability.", "Repository context makes agent output more trustworthy.")

    assert result == {"label": "support", "confidence": 0.91}


def test_llm_extractor_skips_invalid_candidates_without_evidence() -> None:
    transcript = TranscriptDocument(
        episode_id="episode-2",
        show="Demo Show",
        title="Why evidence matters",
        date="2026-05-31",
        segments=[
            TranscriptSegment(timestamp="00:00:10", speaker="Host", text="Good evidence is what keeps the demo honest."),
            TranscriptSegment(timestamp="00:02:00", speaker="Guest", text="Scoped claims are easier to trust when the quote is exact."),
        ],
    )
    client = StubChatClient(
        {
            "content": json.dumps(
                {
                    "judgment": [
                        {
                            "claim": "Claims should always keep a supporting quote.",
                            "evidence": [{"speaker": "Host", "timestamp": "", "quote": "A quote that is not present in the transcript."}],
                            "boundary": "This works when a verifier can inspect the transcript and check the anchor directly.",
                            "action": "Keep the quote.",
                            "topics": ["verification"],
                            "source_view": "wrong-view",
                        },
                        {
                            "claim": "Scoped claims are easier to trust when the quote is exact.",
                            "evidence": [
                                {
                                    "speaker": "Guest",
                                    "timestamp": "00:02:00",
                                    "quote": "Scoped claims are easier to trust when the quote is exact.",
                                }
                            ],
                            "boundary": "This works when the reviewer can compare the claim against a precise transcript excerpt.",
                            "action": "Keep exact anchors.",
                            "topics": ["verification"],
                            "source_view": "wrong-view",
                        },
                    ],
                    "controversy": [],
                    "practice": [],
                }
            )
        }
    )

    extractor = LLMExtractor(client)
    payload = extractor.build_candidates(transcript)

    assert len(payload["judgment"]) == 1
    assert payload["judgment"][0]["claim"] == "Scoped claims are easier to trust when the quote is exact."
    assert payload["judgment"][0]["source_view"] == "judgment"


def test_llm_extractor_normalizes_object_view_and_string_evidence() -> None:
    transcript = TranscriptDocument(
        episode_id="episode-3",
        show="Demo Show",
        title="Claude Code ROI",
        date="2026-05-31",
        segments=[
            TranscriptSegment(timestamp="00:05:55", speaker="Guest", text="我发现它一天就能消耗 300 美元，我就一天回本。"),
            TranscriptSegment(timestamp="00:08:12", speaker="Host", text="这说明高成本工具也可能有很强的投资回报。"),
        ],
    )
    client = StubChatClient(
        {
            "content": json.dumps(
                {
                    "judgment": {
                        "claim": "使用 Claude Code 即使每天消耗 300 美元也能很快回本。",
                        "evidence": "我发现它一天就能消耗 300 美元，我就一天回本。",
                        "boundary": "This holds when the generated output creates enough immediate value to cover the daily spend.",
                        "action": "Compare the daily spend against the value returned in the same workflow.",
                        "topics": ["claude code", "roi"],
                        "source_view": "刘小排",
                    },
                    "controversy": [],
                    "practice": [],
                }
            )
        }
    )

    extractor = LLMExtractor(client)
    payload = extractor.build_candidates(transcript)

    assert len(payload["judgment"]) == 1
    assert payload["judgment"][0]["source_view"] == "judgment"
    assert payload["judgment"][0]["evidence"] == [
        {
            "speaker": "Guest",
            "timestamp": "00:05:55",
            "quote": "我发现它一天就能消耗 300 美元，我就一天回本。",
        }
    ]


def test_llm_extractor_skips_fabricated_full_evidence_anchor() -> None:
    transcript = TranscriptDocument(
        episode_id="episode-4",
        show="Demo Show",
        title="Evidence integrity",
        date="2026-05-31",
        segments=[
            TranscriptSegment(timestamp="00:01:00", speaker="Host", text="真实 transcript 里只有这一句。"),
        ],
    )
    client = StubChatClient(
        {
            "content": json.dumps(
                {
                    "judgment": [
                        {
                            "claim": "Fabricated anchors should not survive validation.",
                            "evidence": [
                                {
                                    "speaker": "Guest",
                                    "timestamp": "00:09:99",
                                    "quote": "这句并不在 transcript 里。",
                                }
                            ],
                            "boundary": "This works when every shipped card can be checked against the source transcript.",
                            "action": "Drop anchors that do not map back to the transcript.",
                            "topics": ["verification"],
                            "source_view": "wrong-view",
                        }
                    ],
                    "controversy": [],
                    "practice": [],
                }
            )
        }
    )

    extractor = LLMExtractor(client)
    payload = extractor.build_candidates(transcript)

    assert payload["judgment"] == []
