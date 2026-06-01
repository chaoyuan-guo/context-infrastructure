from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import TypedDict, cast

from podinsight_mvp.aggregate import group_cards_by_topic
from podinsight_mvp.extract import merge_view_candidates
from podinsight_mvp.ingest import load_demo_catalog, parse_transcript
from podinsight_mvp.query import answer_query
from podinsight_mvp.relations import build_relations
from podinsight_mvp.types import AnswerProvider, CandidateExtractor, EmbeddingProvider, ExtractedCard, RelationClassifier, RelationEdge


class EpisodePreview(TypedDict):
    episode_id: str
    title: str
    show_id: str
    updated_at: str


class DemoArtifacts(TypedDict):
    episodes: list[EpisodePreview]
    cards: list[dict[str, object]]
    relations: list[dict[str, object]]
    themes: dict[str, list[dict[str, object]]]
    answers_preview: list[dict[str, object]]


def build_demo_artifacts(
    *,
    project_root: Path,
    workspace_root: Path,
    output_dir: Path,
    extractor: CandidateExtractor,
    embedding_client: EmbeddingProvider,
    relation_classifier: RelationClassifier,
    answer_client: AnswerProvider,
) -> DemoArtifacts:
    catalog = load_demo_catalog(project_root, workspace_root)
    output_dir.mkdir(parents=True, exist_ok=True)
    aliases = cast(dict[str, list[str]], json.loads((project_root / "data" / "topic_aliases.json").read_text(encoding="utf-8")))

    all_cards: list[ExtractedCard] = []
    episodes_payload: list[EpisodePreview] = []
    for episode in catalog:
        transcript = parse_transcript(episode.transcript_path)
        episodes_payload.append(
            {
                "episode_id": episode.episode_id,
                "title": episode.title,
                "show_id": episode.show_id,
                "updated_at": episode.updated_at,
            }
        )
        view_payloads = extractor.build_candidates(transcript)
        all_cards.extend(merge_view_candidates(episode.episode_id, view_payloads))

    grouped = group_cards_by_topic(all_cards, aliases)
    relations = build_relations(all_cards, embedding_client, relation_classifier, top_k=3)
    preview = answer_query(
        "What do these episodes suggest about AI agents in real work?",
        all_cards,
        answer_client,
    )

    cards_payload = [cast(dict[str, object], card.model_dump(mode="json")) for card in all_cards]
    relations_payload = [cast(dict[str, object], relation.model_dump(mode="json")) for relation in relations]
    themes_payload = {topic: [cast(dict[str, object], card.model_dump(mode="json")) for card in cards] for topic, cards in grouped.items()}
    answers_payload = [cast(dict[str, object], preview.model_dump(mode="json"))]

    _ = (output_dir / "episodes.json").write_text(json.dumps(episodes_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    _ = (output_dir / "cards.json").write_text(json.dumps(cards_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    _ = (output_dir / "relations.json").write_text(json.dumps(relations_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    _ = (output_dir / "themes.json").write_text(json.dumps(themes_payload, ensure_ascii=False, indent=2), encoding="utf-8")
    _ = (output_dir / "answers_preview.json").write_text(json.dumps(answers_payload, ensure_ascii=False, indent=2), encoding="utf-8")

    return {
        "episodes": episodes_payload,
        "cards": cards_payload,
        "relations": relations_payload,
        "themes": themes_payload,
        "answers_preview": answers_payload,
    }
