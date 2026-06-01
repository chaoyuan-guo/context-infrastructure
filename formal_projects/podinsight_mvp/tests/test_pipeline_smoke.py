import json

from podinsight_mvp.pipeline import build_demo_artifacts
from podinsight_mvp.types import CardCandidatePayload, ChatCompletionPayload, EmbeddingPayload, RelationClassification, TranscriptDocument


class StubExtractor:
    def build_candidates(self, transcript: TranscriptDocument) -> dict[str, list[CardCandidatePayload]]:
        return {
            "judgment": [
                {
                    "claim": "Scoped context makes coding agents reliable in real delivery work.",
                    "evidence": [
                        {
                            "speaker": transcript.segments[0].speaker,
                            "timestamp": transcript.segments[0].timestamp,
                            "quote": transcript.segments[0].text,
                        }
                    ],
                    "boundary": "This works when the task is scoped and the repository context is available.",
                    "action": "Start with a bounded task.",
                    "topics": ["ai coding", "agent workflow"],
                    "source_view": "judgment",
                }
            ],
            "controversy": [
                {
                    "claim": "API costs still block broad rollout when usage volume compounds.",
                    "evidence": [
                        {
                            "speaker": transcript.segments[1].speaker,
                            "timestamp": transcript.segments[1].timestamp,
                            "quote": transcript.segments[1].text,
                        }
                    ],
                    "boundary": "This matters when the team is deciding whether the API is worth the extra cost and operating risk.",
                    "action": "Compare the API path against the current baseline before rolling it out further.",
                    "topics": ["ai product strategy"],
                    "source_view": "controversy",
                }
            ],
            "practice": [
                {
                    "claim": "Prompt workflows need explicit handoffs so another operator can reproduce them.",
                    "evidence": [
                        {
                            "speaker": transcript.segments[2].speaker,
                            "timestamp": transcript.segments[2].timestamp,
                            "quote": transcript.segments[2].text,
                        }
                    ],
                    "boundary": "This holds when the prompt workflow can be written down and verified by another operator.",
                    "action": "Turn the workflow into a short checklist another operator can follow.",
                    "topics": ["agent workflow", "context engineering"],
                    "source_view": "practice",
                }
            ],
        }


class StubEmbeddingClient:
    def embed(self, text: str) -> EmbeddingPayload:
        base = float(len(text) % 7 + 1)
        return {"embedding": [base, 1.0]}


class StubRelationClassifier:
    def classify(self, left_claim: str, right_claim: str) -> RelationClassification:
        if left_claim == right_claim:
            return {"label": "unrelated", "confidence": 0.0}
        return {"label": "support", "confidence": 0.9}


class StubAnswerClient:
    def complete(self, messages: list[dict[str, str]]) -> ChatCompletionPayload:
        _ = messages
        return {"content": "Scoped context makes coding agents more reliable across the demo set."}


def test_pipeline_writes_demo_assets(project_root, workspace_root, tmp_path) -> None:
    derived_dir = tmp_path / "derived"
    build_demo_artifacts(
        project_root=project_root,
        workspace_root=workspace_root,
        output_dir=derived_dir,
        extractor=StubExtractor(),
        embedding_client=StubEmbeddingClient(),
        relation_classifier=StubRelationClassifier(),
        answer_client=StubAnswerClient(),
    )

    cards = json.loads((derived_dir / "cards.json").read_text(encoding="utf-8"))
    relations = json.loads((derived_dir / "relations.json").read_text(encoding="utf-8"))
    themes = json.loads((derived_dir / "themes.json").read_text(encoding="utf-8"))
    answers = json.loads((derived_dir / "answers_preview.json").read_text(encoding="utf-8"))

    assert cards, "cards artifact should not be empty"
    assert relations, "relations artifact should not be empty"
    assert "ai coding" in themes
    assert answers[0]["summary"].startswith("Scoped context")
    assert {card["boundary"] for card in cards} == {
        "This works when the task is scoped and the repository context is available.",
        "This matters when the team is deciding whether the API is worth the extra cost and operating risk.",
        "This holds when the prompt workflow can be written down and verified by another operator.",
    }
    assert {card["action"] for card in cards} == {
        "Start with a bounded task.",
        "Compare the API path against the current baseline before rolling it out further.",
        "Turn the workflow into a short checklist another operator can follow.",
    }
