import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import TypedDict, cast

import pytest

from podinsight_mvp.ingest import parse_transcript


RUN_PIPELINE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "run_pipeline.py"
RUN_PIPELINE_SPEC = importlib.util.spec_from_file_location("podinsight_run_pipeline", RUN_PIPELINE_PATH)
assert RUN_PIPELINE_SPEC is not None
assert RUN_PIPELINE_SPEC.loader is not None
run_pipeline = importlib.util.module_from_spec(RUN_PIPELINE_SPEC)
RUN_PIPELINE_SPEC.loader.exec_module(run_pipeline)


class CliPayload(TypedDict):
    output_dir: str
    card_count: int
    mode: str


TITLE_TEMPLATE_FRAGMENTS = (
    "frames coding agents as highest-leverage",
    "also shows cost or reliability tradeoffs",
    "suggests that agent workflows improve",
)

WEAK_DEMO_FRAGMENTS = (
    "ABCN",
    "understimulated body and overstimulated mind",
    "我举个具体的例子讲",
    "什么时候能够实现这个机会",
)

WEAK_DEMO_CLAIMS = (
    "我觉得模型机产品这个东西我没法说，但我觉得模型机能力这个可以吗。",
    "我们前几年聊了很多你的 AI Talker，你的 Prompt 工程师，或者是 Agent 的创业。",
    "前两天写了个朋友圈，我就说美国有很多这种 AI 创业让人感觉是中产创业。",
    "抽象出来的一个 AI 的思维链或者 AI 的 Prompt。",
    "包括我们产品的一些具体问题。",
    "这个问题第一时间就想到了刚打完扣的一个创业者吧。",
    "在大量的被 AI agent 替换掉。",
    "第四次是用了 MCP，然后第五次是用 Cursor。",
    "它是基于 MCP 还是 API 还是一些别的东西。",
    "这样的一个 prompt 其实丢给豆包也好。",
    "思考这个问题的价值在于思考模型下一步能进化到什么程度。",
    "会觉得说 MCP 是一个很好玩的一个新的方向。",
    "我们用 20 个问题一起搞懂 AI Agent。",
    "亚哥很快做了那个就是 Cursor to Devon，然后我们又出了 AgenticAI 的课，那是 1 月份出的。",
    "而且是一句非常简单的 prompt 所带来的这很漂亮的一整套的结果。",
)

FIXED_BOUNDARY_TEMPLATES = (
    "This works when the team can scope the task and still verify the output against real work.",
    "This matters when cost, reliability, or replacement risk directly shapes adoption decisions.",
    "This holds when the operator can turn goals into explicit prompts, tools, or workflow steps.",
)

FIXED_ACTION_TEMPLATES = (
    "Benchmark the workflow on one bounded task before scaling it.",
    "Track cost and operational risk before scaling usage.",
    "Write the workflow down before delegating it to an agent.",
)

GENERIC_HELPER_WRAPPERS = (
    "the business case",
    "the human role",
    "the workflow design",
    "the context setup",
    "the business model",
    "the coding workflow",
)

IMPLAUSIBLE_RELATION_TRIPLES = (
    (
        "所以， 目前看起来 AI 应用最确定的应该就是写代码了。",
        "还有技术报告，我全让 Claude Code 去看，看这啥意思，然后我就可以问他问题。",
        "conflict",
    ),
    (
        "那 Cursor 的话大家都知道了，它就是你可以通过 prompt 然后让它去写代码。",
        "第二个好用的功能是 sub-agent，就是 Claude Code 他自己是一个大 agent。",
        "prerequisite",
    ),
    (
        "它是基于 MCP 还是 API 还是一些别的东西。",
        "那这种情况下，创业公司最大的机会就是说我能探索新的交互方式。",
        "support",
    ),
    (
        "还有技术报告，我全让 Claude Code 去看，看这啥意思，然后我就可以问他问题。",
        "然后我会让 Claude Code 把市面上知名的大概十几个开源的 3D 模型自己去部署上去。",
        "conflict",
    ),
    (
        "所以说我不觉得 AI 所谓的取代了这些程序员的工作。",
        "但是这一年以来的话，我发现大量的这种 Busy work 都已经被 AI 取代了。",
        "support",
    ),
)


def _assert_non_boilerplate_metadata(cards: list[dict[str, object]]) -> None:
    boundaries = {cast(str, card["boundary"]) for card in cards}
    actions = {cast(str, card["action"]) for card in cards if card.get("action")}

    assert not boundaries.intersection(FIXED_BOUNDARY_TEMPLATES)
    assert not actions.intersection(FIXED_ACTION_TEMPLATES)
    assert len(boundaries) > 1
    assert len(actions) > 1
    metadata = boundaries | actions
    assert not any(fragment in text for text in metadata for fragment in GENERIC_HELPER_WRAPPERS)
    assert not any("human judgment still depends on human judgment" in text for text in metadata)


def _assert_no_implausible_relations(relations: list[dict[str, object]]) -> None:
    relation_triples = {
        (cast(str, relation["left_claim"]), cast(str, relation["right_claim"]), cast(str, relation["label"]))
        for relation in relations
    }
    for triple in IMPLAUSIBLE_RELATION_TRIPLES:
        assert triple not in relation_triples


def test_run_pipeline_cli_writes_output(project_root: Path, tmp_path: Path) -> None:
    env = os.environ.copy()
    env["PODINSIGHT_OUTPUT_DIR"] = str(tmp_path / "derived")
    env["PODINSIGHT_CHAT_API_KEY"] = ""
    _ = env.pop("PODINSIGHT_CHAT_BASE_URL", None)
    _ = env.pop("PODINSIGHT_HEAVY_MODEL", None)
    _ = env.pop("PODINSIGHT_LIGHT_MODEL", None)
    _ = env.pop("PODINSIGHT_EMBEDDING_BASE_URL", None)
    _ = env.pop("PODINSIGHT_EMBEDDING_MODEL", None)
    _ = env.pop("PODINSIGHT_CACHE_DIR", None)

    result = subprocess.run(
        [sys.executable, "scripts/run_pipeline.py"],
        cwd=project_root,
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0, result.stderr
    payload = cast(CliPayload, json.loads(result.stdout.strip()))
    assert payload["mode"] == "demo"
    assert payload["card_count"] > 0
    assert (tmp_path / "derived" / "cards.json").exists()

    cards = cast(list[dict[str, object]], json.loads((tmp_path / "derived" / "cards.json").read_text(encoding="utf-8")))
    relations = cast(list[dict[str, object]], json.loads((tmp_path / "derived" / "relations.json").read_text(encoding="utf-8")))
    assert cards
    assert not any(fragment in cast(str, card["claim"]) for card in cards for fragment in TITLE_TEMPLATE_FRAGMENTS)
    assert any(
        "Claude Code" in cast(str, card["claim"]) or "Cursor" in cast(str, card["claim"]) or "外脑" in cast(str, card["claim"])
        for card in cards
    )
    assert all(cast(list[dict[str, str]], card["evidence"])[0]["quote"] != "Hello，大家好，这里是 AsyncTalk。" for card in cards)
    _assert_non_boilerplate_metadata(cards)
    assert not any(fragment in cast(str, card["claim"]) for card in cards for fragment in WEAK_DEMO_FRAGMENTS)
    assert not any(cast(str, card["claim"]) in WEAK_DEMO_CLAIMS for card in cards)
    _assert_no_implausible_relations(relations)


def test_demo_extractor_builds_transcript_grounded_candidates(workspace_root: Path) -> None:
    transcript = parse_transcript(workspace_root / "contexts" / "podcast_read" / "4597222" / "Transcript.md")

    view_payloads = run_pipeline.DemoExtractor().build_candidates(transcript)
    cards = [card for cards in view_payloads.values() for card in cards]

    assert len(cards) == 3
    assert not any(fragment in card["claim"] for card in cards for fragment in TITLE_TEMPLATE_FRAGMENTS)
    assert any("Claude Code" in card["claim"] or "最确定" in card["claim"] or "Cursor" in card["claim"] for card in cards)
    assert any(card["evidence"][0]["quote"] == card["claim"] for card in cards)
    assert all(card["evidence"][0]["quote"] != "Hello，大家好，这里是 AsyncTalk。" for card in cards)
    _assert_non_boilerplate_metadata(cast(list[dict[str, object]], cards))


def test_demo_extractor_skips_low_signal_customer_support_fragment(workspace_root: Path) -> None:
    transcript = parse_transcript(workspace_root / "contexts" / "podcast_read" / "4822400" / "Transcript.md")

    view_payloads = run_pipeline.DemoExtractor().build_candidates(transcript)
    cards = [card for cards in view_payloads.values() for card in cards]

    assert not any("ABCN" in card["claim"] for card in cards)


def test_demo_extractor_prefers_ai_product_claims_over_lifestyle_quotes(workspace_root: Path) -> None:
    transcript = parse_transcript(workspace_root / "contexts" / "podcast_read" / "4886157" / "Transcript.md")

    view_payloads = run_pipeline.DemoExtractor().build_candidates(transcript)
    cards = [card for cards in view_payloads.values() for card in cards]

    assert not any("understimulated body and overstimulated mind" in card["claim"] for card in cards)
    assert any(
        "有什么问题" in card["claim"]
        or "context,window management" in card["claim"]
        or "documentation" in card["claim"]
        or "创业机会" in card["claim"]
        for card in cards
    )


def test_demo_extractor_skips_prompt_startup_metacommentary(workspace_root: Path) -> None:
    transcript = parse_transcript(workspace_root / "contexts" / "podcast_read" / "5006605" / "Transcript.md")

    view_payloads = run_pipeline.DemoExtractor().build_candidates(transcript)
    cards = [card for cards in view_payloads.values() for card in cards]

    assert not any("我们前几年聊了很多" in card["claim"] for card in cards)


def test_demo_extractor_skips_personal朋友圈_metacommentary(workspace_root: Path) -> None:
    transcript = parse_transcript(workspace_root / "contexts" / "podcast_read" / "4822400" / "Transcript.md")

    view_payloads = run_pipeline.DemoExtractor().build_candidates(transcript)
    cards = [card for cards in view_payloads.values() for card in cards]

    assert not any("前两天写了个朋友圈" in card["claim"] for card in cards)


def test_demo_extractor_skips_prompt_fragment_metacommentary(workspace_root: Path) -> None:
    transcript = parse_transcript(workspace_root / "contexts" / "podcast_read" / "5006605" / "Transcript.md")

    view_payloads = run_pipeline.DemoExtractor().build_candidates(transcript)
    cards = [card for cards in view_payloads.values() for card in cards]

    assert not any("抽象出来的一个 AI 的思维链或者 AI 的 Prompt" in card["claim"] for card in cards)


def test_demo_extractor_skips_product_issue_fragment(workspace_root: Path) -> None:
    transcript = parse_transcript(workspace_root / "contexts" / "podcast_read" / "4822400" / "Transcript.md")

    view_payloads = run_pipeline.DemoExtractor().build_candidates(transcript)
    cards = [card for cards in view_payloads.values() for card in cards]

    assert not any("包括我们产品的一些具体问题" in card["claim"] for card in cards)


@pytest.mark.parametrize(
    ("left_claim", "right_claim"),
    [
        (
            "那 Cursor 的话大家都知道了，它就是你可以通过 prompt 然后让它去写代码。",
            "第二个好用的功能是 sub-agent，就是 Claude Code 他自己是一个大 agent。",
        ),
        (
            "所以， 目前看起来 AI 应用最确定的应该就是写代码了。",
            "还有技术报告，我全让 Claude Code 去看，看这啥意思，然后我就可以问他问题。",
        ),
        (
            "它是基于 MCP 还是 API 还是一些别的东西。",
            "那这种情况下，创业公司最大的机会就是说我能探索新的交互方式。",
        ),
        (
            "所以说我不觉得 AI 所谓的取代了这些程序员的工作。",
            "但是这一年以来的话，我发现大量的这种 Busy work 都已经被 AI 取代了。",
        ),
    ],
)
def test_demo_relation_classifier_rejects_implausible_edges(left_claim: str, right_claim: str) -> None:
    classifier = run_pipeline.DemoRelationClassifier()

    result = classifier.classify(left_claim, right_claim)

    assert result["label"] == "unrelated"
    assert result["confidence"] == 0.0


def test_demo_relation_classifier_keeps_explicit_cost_support() -> None:
    classifier = run_pipeline.DemoRelationClassifier()

    result = classifier.classify(
        "然后最近也出了 API，但这个东西它有个问题就是它的成本实在是过高。",
        "一个新的科技出现，成本还没有下降到足够普惠到可以做一个大规模的 To C 的应用。",
    )

    assert result["label"] == "support"
    assert result["confidence"] >= 0.85


def test_should_use_live_clients_requires_real_key() -> None:
    assert run_pipeline._should_use_live_clients("") is False
    assert run_pipeline._should_use_live_clients("   ") is False
    assert run_pipeline._should_use_live_clients("replace-me") is False
    assert run_pipeline._should_use_live_clients("RePlAcE-Me") is False
    assert run_pipeline._should_use_live_clients("real-token") is True


def test_build_runtime_clients_returns_live_stack(project_root: Path, monkeypatch) -> None:
    settings = run_pipeline.load_settings(project_root)
    monkeypatch.setattr(
        run_pipeline,
        "load_settings",
        lambda _project_root: settings.__class__(
            chat_base_url="http://example.com/v1",
            chat_api_key="real-token",
            heavy_model="deepseek-v4-pro",
            light_model="deepseek-v4-flash",
            embedding_base_url="http://embed.example.com/v1",
            embedding_model="Qwen3-Embedding-0.6B",
            cache_dir=project_root / "data" / "cache-test",
        ),
    )

    mode, extractor, embedding_client, relation_classifier, answer_client = run_pipeline._build_runtime_clients(project_root)

    assert mode == "live"
    assert isinstance(extractor, run_pipeline.LLMExtractor)
    assert isinstance(embedding_client, run_pipeline.EmbeddingClient)
    assert isinstance(relation_classifier, run_pipeline.LLMRelationClassifier)
    assert isinstance(answer_client, run_pipeline.LLMClient)
    assert answer_client.config.model == "deepseek-v4-flash"
    assert embedding_client.config.model == "Qwen3-Embedding-0.6B"


def test_main_reports_live_mode_without_network(project_root: Path, tmp_path: Path, monkeypatch, capsys) -> None:
    monkeypatch.chdir(project_root)
    monkeypatch.setenv("PODINSIGHT_OUTPUT_DIR", str(tmp_path / "derived"))

    class StubExtractor:
        def build_candidates(self, transcript) -> dict[str, list[dict[str, object]]]:
            _ = transcript
            return {"judgment": [], "controversy": [], "practice": []}

    class StubEmbeddingClient:
        def embed(self, text: str) -> dict[str, list[float]]:
            _ = text
            return {"embedding": [1.0, 0.0]}

    class StubRelationClassifier:
        def classify(self, left_claim: str, right_claim: str) -> dict[str, float | str]:
            _ = (left_claim, right_claim)
            return {"label": "unrelated", "confidence": 0.0}

    class StubAnswerClient:
        def complete(self, messages: list[dict[str, str]]) -> dict[str, str]:
            _ = messages
            return {"content": "stub"}

    monkeypatch.setattr(
        run_pipeline,
        "_build_runtime_clients",
        lambda _project_root: (
            "live",
            StubExtractor(),
            StubEmbeddingClient(),
            StubRelationClassifier(),
            StubAnswerClient(),
        ),
    )
    monkeypatch.setattr(
        run_pipeline,
        "build_demo_artifacts",
        lambda **kwargs: {"cards": [{"claim": "stub claim"}], "episodes": [], "relations": [], "themes": {}, "answers_preview": []},
    )

    run_pipeline.main()

    payload = cast(CliPayload, json.loads(capsys.readouterr().out.strip()))
    assert payload["mode"] == "live"
    assert payload["card_count"] == 1
    assert payload["output_dir"] == str(tmp_path / "derived")


def test_main_does_not_fallback_when_live_path_fails(project_root: Path, tmp_path: Path, monkeypatch) -> None:
    monkeypatch.chdir(project_root)
    monkeypatch.setenv("PODINSIGHT_OUTPUT_DIR", str(tmp_path / "derived"))

    class ExpectedLiveError(RuntimeError):
        pass

    class FailingExtractor:
        def build_candidates(self, transcript) -> dict[str, list[dict[str, object]]]:
            _ = transcript
            raise ExpectedLiveError("401 auth from live extractor")

    class StubEmbeddingClient:
        def embed(self, text: str) -> dict[str, list[float]]:
            _ = text
            return {"embedding": [1.0, 0.0]}

    class StubRelationClassifier:
        def classify(self, left_claim: str, right_claim: str) -> dict[str, float | str]:
            _ = (left_claim, right_claim)
            return {"label": "unrelated", "confidence": 0.0}

    class StubAnswerClient:
        def complete(self, messages: list[dict[str, str]]) -> dict[str, str]:
            _ = messages
            return {"content": "stub"}

    monkeypatch.setattr(
        run_pipeline,
        "_build_runtime_clients",
        lambda _project_root: (
            "live",
            FailingExtractor(),
            StubEmbeddingClient(),
            StubRelationClassifier(),
            StubAnswerClient(),
        ),
    )

    with pytest.raises(ExpectedLiveError, match="401 auth from live extractor"):
        run_pipeline.main()
