import importlib.util
from pathlib import Path


STREAMLIT_APP_PATH = Path(__file__).resolve().parents[1] / "streamlit_app.py"
STREAMLIT_APP_SPEC = importlib.util.spec_from_file_location("podinsight_streamlit_app", STREAMLIT_APP_PATH)
assert STREAMLIT_APP_SPEC is not None
assert STREAMLIT_APP_SPEC.loader is not None
streamlit_app = importlib.util.module_from_spec(STREAMLIT_APP_SPEC)
STREAMLIT_APP_SPEC.loader.exec_module(streamlit_app)


def test_build_query_answer_payload_uses_user_question_not_static_preview() -> None:
    cards_payload = [
        {
            "episode_id": "1",
            "claim": "Claude Code becomes more valuable when it can reason across multiple files and tools.",
            "evidence": [{"speaker": "s", "timestamp": "00:00:01", "quote": "q"}],
            "boundary": "This works when the task is scoped.",
            "action": "Start with a bounded task.",
            "topics": ["ai coding", "agent workflow"],
            "source_views": ["judgment"],
        },
        {
            "episode_id": "2",
            "claim": "Human taste becomes more important after AI adoption.",
            "evidence": [{"speaker": "s", "timestamp": "00:00:02", "quote": "q"}],
            "boundary": "This works when humans still verify the output.",
            "action": "Keep a human in the loop.",
            "topics": ["human leverage"],
            "source_views": ["judgment"],
        },
    ]
    preview_answers = [{"summary": "stale preview", "supporting_cards": []}]

    payload = streamlit_app.build_query_answer_payload(
        "What do these episodes suggest about coding agents?",
        cards_payload,
        preview_answers,
    )

    assert payload is not None
    assert payload["summary"] != "stale preview"
    supporting_claims = [card["claim"] for card in payload["supporting_cards"]]
    assert "Claude Code becomes more valuable when it can reason across multiple files and tools." in supporting_claims


def test_build_query_answer_payload_falls_back_to_preview_for_blank_question() -> None:
    preview_answers = [{"summary": "stale preview", "supporting_cards": []}]

    payload = streamlit_app.build_query_answer_payload("   ", [], preview_answers)

    assert payload == preview_answers[0]
