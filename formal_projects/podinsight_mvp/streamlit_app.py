from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from pathlib import Path
import sys
from typing import Any, cast

import streamlit as st

SRC_ROOT = Path(__file__).resolve().parent / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from podinsight_mvp.presenters import build_demo_summary
from podinsight_mvp.query import answer_query
from podinsight_mvp.types import EvidenceAnchor, ExtractedCard


PROJECT_ROOT = Path(__file__).resolve().parent
DERIVED_DIR = PROJECT_ROOT / "data" / "derived"


def load_json(name: str) -> object | None:
    path = DERIVED_DIR / name
    if not path.exists():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _deserialize_cards(cards_payload: list[dict[str, object]]) -> list[ExtractedCard]:
    cards: list[ExtractedCard] = []
    for payload in cards_payload:
        evidence_items = cast(list[dict[str, str]], payload.get("evidence", []))
        evidence = [
            EvidenceAnchor(
                speaker=item["speaker"],
                timestamp=item["timestamp"],
                quote=item["quote"],
            )
            for item in evidence_items
        ]
        cards.append(
            ExtractedCard(
                episode_id=cast(str, payload["episode_id"]),
                claim=cast(str, payload["claim"]),
                evidence=evidence,
                boundary=cast(str, payload["boundary"]),
                action=cast(str | None, payload.get("action")),
                topics=cast(list[str], payload["topics"]),
                source_views=cast(list[str], payload["source_views"]),
            )
        )
    return cards


def build_query_answer_payload(
    question: str,
    cards_payload: list[dict[str, object]],
    preview_answers: list[dict[str, object]],
) -> dict[str, object] | None:
    normalized_question = question.strip()
    if normalized_question and cards_payload:
        answer = answer_query(normalized_question, _deserialize_cards(cards_payload), None)
        return cast(dict[str, object], answer.model_dump(mode="json"))
    if preview_answers:
        return preview_answers[0]
    return None


def main() -> None:
    st.set_page_config(page_title="PodInsight MVP", layout="wide")
    st.title("PodInsight MVP")
    st.caption("Interview-demo view over curated podcast transcripts")

    episodes = cast(list[dict[str, object]], load_json("episodes.json") or [])
    cards = cast(list[dict[str, object]], load_json("cards.json") or [])
    relations = cast(list[dict[str, object]], load_json("relations.json") or [])
    themes = cast(dict[str, list[dict[str, object]]], load_json("themes.json") or {})
    answers = cast(list[dict[str, object]], load_json("answers_preview.json") or [])

    summary = build_demo_summary(episodes=episodes, cards=cards, relations=relations, themes=themes)
    cols = st.columns(4)
    cols[0].metric("Episodes", summary["episode_count"])
    cols[1].metric("Cards", summary["card_count"])
    cols[2].metric("Relations", summary["relation_count"])
    cols[3].metric("Themes", summary["theme_count"])

    st.subheader("Curated episodes")
    st.dataframe(episodes, width="stretch")

    st.subheader("Theme aggregation")
    theme_names = sorted(themes.keys())
    selected_theme = st.selectbox("Theme", theme_names) if theme_names else None
    if selected_theme:
        for card in themes[selected_theme]:
            claim = cast(str, card["claim"])
            boundary = cast(str, card["boundary"])
            topics = cast(list[str], card["topics"])
            source_views = cast(list[str], card["source_views"])
            evidence_items = cast(list[dict[str, str]], card["evidence"])
            with st.expander(claim):
                st.write(f"**Boundary**: {boundary}")
                st.write(f"**Topics**: {', '.join(topics)}")
                st.write(f"**Source views**: {', '.join(source_views)}")
                evidence = evidence_items[0]
                st.write(f"**Evidence**: [{evidence['timestamp']}] {evidence['speaker']}: {evidence['quote']}")
                if card.get("action"):
                    st.write(f"**Action**: {cast(str, card['action'])}")

    st.subheader("Evidence-backed query")
    query_question = st.text_input(
        "Ask a question about the demo corpus",
        value="What do these episodes suggest about AI agents in real work?",
    )
    query_payload = build_query_answer_payload(query_question, cards, answers)
    if query_payload:
        st.write(cast(str, query_payload["summary"]))
        supporting_cards = cast(list[dict[str, object]], query_payload["supporting_cards"])
        for card in supporting_cards:
            st.markdown(f"- **{cast(str, card['claim'])}** — {cast(str, card['boundary'])}")
    else:
        st.info("Run the pipeline first to generate cards and query output.")


if __name__ == "__main__":
    main()
