from __future__ import annotations

from pathlib import Path
from typing import Protocol, TypedDict

from pydantic import BaseModel, ConfigDict, Field


class EvidenceAnchor(BaseModel):
    speaker: str
    timestamp: str
    quote: str


class CardCandidate(BaseModel):
    claim: str
    evidence: list[EvidenceAnchor]
    boundary: str
    action: str | None = None
    topics: list[str] = Field(min_length=1)
    source_view: str


class ExtractedCard(BaseModel):
    episode_id: str
    claim: str
    evidence: list[EvidenceAnchor]
    boundary: str
    action: str | None = None
    topics: list[str] = Field(min_length=1)
    source_views: list[str] = Field(min_length=1)


class RelationEdge(BaseModel):
    left_claim: str
    right_claim: str
    label: str
    confidence: float


class QueryAnswer(BaseModel):
    summary: str
    supporting_cards: list[ExtractedCard]


class QCReport(BaseModel):
    parse_success_rate: float
    dup_ratio: float = 0.0


class TranscriptSegment(BaseModel):
    timestamp: str
    speaker: str
    text: str


class TranscriptDocument(BaseModel):
    episode_id: str
    show: str
    title: str
    date: str
    source_url: str | None = None
    segments: list[TranscriptSegment]


class EpisodeRecord(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    episode_id: str
    show_id: str = "Unknown Show"
    title: str
    updated_at: str
    source_url: str
    transcript_path: str = Field(alias="path_transcript")
    qc_report_path: str = Field(alias="path_qc_report")


class DemoEpisode(BaseModel):
    episode_id: str
    show_id: str
    title: str
    updated_at: str
    source_url: str
    transcript_path: Path
    qc_path: Path
    qc: QCReport


class CardCandidatePayload(TypedDict):
    claim: str
    evidence: list[dict[str, str]]
    boundary: str
    action: str | None
    topics: list[str]
    source_view: str


class RelationClassification(TypedDict):
    label: str
    confidence: float


class ChatCompletionPayload(TypedDict, total=False):
    id: str
    content: str
    choices: list[dict[str, dict[str, str]]]


class EmbeddingPayload(TypedDict):
    embedding: list[float]


class CandidateExtractor(Protocol):
    def build_candidates(self, transcript: TranscriptDocument) -> dict[str, list[CardCandidatePayload]]: ...


class EmbeddingProvider(Protocol):
    def embed(self, text: str) -> EmbeddingPayload: ...


class RelationClassifier(Protocol):
    def classify(self, left_claim: str, right_claim: str) -> RelationClassification: ...


class AnswerProvider(Protocol):
    def complete(self, messages: list[dict[str, str]]) -> ChatCompletionPayload: ...
