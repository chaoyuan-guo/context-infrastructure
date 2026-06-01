import json
import os
from pathlib import Path
import re
import sys
from typing import cast


SRC_ROOT = Path(__file__).resolve().parents[1] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from podinsight_mvp.pipeline import build_demo_artifacts
from podinsight_mvp.cache import FileCache
from podinsight_mvp.model_clients import LLMExtractor, LLMRelationClassifier
from podinsight_mvp.openai_client import EmbeddingClient, LLMClient
from podinsight_mvp.settings import ModelEndpointConfig, load_settings
from podinsight_mvp.types import AnswerProvider, CandidateExtractor, CardCandidate, CardCandidatePayload, ChatCompletionPayload, EmbeddingPayload, EmbeddingProvider, RelationClassification, RelationClassifier, TranscriptDocument, TranscriptSegment
from podinsight_mvp.validate import validate_card_candidate


TOPIC_KEYWORDS: dict[str, tuple[str, ...]] = {
    "ai coding": (
        "claude code",
        "cloud code",
        "cursor",
        "写代码",
        "code",
        "ide",
        "编程",
        "外脑",
        "knowledge base",
    ),
    "agent workflow": (
        "agent",
        "workflow",
        "sub-agent",
        "sub agent",
        "mcp",
        "github action",
        "prompt",
        "交互方式",
        "human-in-the-loop",
        "human in the loop",
        "步骤",
    ),
    "context engineering": (
        "context",
        "knowledge base",
        "外脑",
        "记忆",
        "上下文",
        "documentation",
        "context window",
        "prompt",
        "信息",
    ),
    "ai product strategy": (
        "成本",
        "昂贵",
        "商业化",
        "api",
        "token",
        "startup",
        "创业",
        "to c",
        "to b",
        "市场",
        "定价",
    ),
    "human leverage": (
        "agency",
        "taste",
        "junior",
        "设计师",
        "超级个体",
        "创业者",
        "一人",
        "团队",
        "future",
        "替代",
    ),
}

VIEW_KEYWORDS: dict[str, tuple[str, ...]] = {
    "judgment": (
        "最确定",
        "非常强大",
        "最强",
        "外脑",
        "机会",
        "价值",
        "好用",
        "主力",
        "agent 的价值",
        "交互方式",
    ),
    "controversy": (
        "成本",
        "昂贵",
        "危险",
        "替换",
        "取代",
        "风险",
        "不建议",
        "问题",
        "没有未来",
        "token",
    ),
    "practice": (
        "workflow",
        "prompt",
        "documentation",
        "context window",
        "context,window management",
        "sub-agent",
        "sub agent",
        "mcp",
        "github action",
        "knowledge base",
        "外脑",
        "human in the loop",
        "交互方式",
        "步骤",
        "让 claude code",
        "让 cloud code",
    ),
}

INTRO_MARKERS = ("hello", "欢迎收听", "大家好", "我是主播", "这里是", "我们关注")
POSITIVE_MARKERS = ("最确定", "非常强大", "最强", "好用", "价值", "机会", "外脑", "主力", "不错")
NEGATIVE_MARKERS = ("成本", "昂贵", "危险", "替换", "取代", "风险", "没有未来", "不建议", "高", "难以调试", "难以开发")
DOMAIN_SIGNAL_KEYWORDS = (
    "ai",
    "agent",
    "cursor",
    "claude code",
    "workflow",
    "prompt",
    "mcp",
    "context",
    "memory",
    "外脑",
    "api",
    "创业",
    "startup",
    "product",
    "产品",
    "应用",
    "bottleneck",
    "cost",
    "value",
    "code",
    "coding",
    "o3",
    "模型",
    "工具",
)
LOW_SIGNAL_SEGMENT_MARKERS = ("abcn", "understimulated body and overstimulated mind", "channel sort")
QUESTION_STYLE_MARKERS = (
    "你觉得",
    "有没有机会",
    "什么时候能够实现",
    "你怎么分辨",
    "我举个具体的例子讲",
)
LOW_SIGNAL_LEAD_MARKERS = (
    "我觉得模型机产品",
    "前两天写了个朋友圈",
    "我们前几年聊了很多",
    "抽象出来的一个 ai 的思维链",
    "包括我们产品的一些具体问题",
    "这个问题第一时间",
    "第四次是用了",
    "第五次是用",
    "在大量的被",
    "它是基于 mcp 还是 api",
    "这样的一个 prompt",
    "思考这个问题的价值",
    "会觉得说",
    "我们用 20 个问题",
    "亚哥很快做了那个",
    "而且是一句非常简单的 prompt",
)
DEPENDENCY_MARKERS = (
    "做好",
    "给足",
    "写下来",
    "写清楚",
    "documentation",
    "context window",
    "context,window management",
    "workflow",
    "步骤",
    "需要",
    "先",
    "前提",
    "handoff",
)
RELATION_FOCUS_KEYWORDS: dict[str, tuple[str, ...]] = {
    "claude code": ("claude code", "cloud code"),
    "cursor": ("cursor",),
    "mcp": ("mcp",),
    "api": ("api",),
    "cost": ("成本", "昂贵", "token", "定价", "to c", "to b", "普惠"),
    "prompt": ("prompt",),
    "workflow": ("workflow", "sub-agent", "sub agent", "github action", "agent"),
    "context": ("context", "documentation", "knowledge base", "外脑", "context window", "context,window management"),
    "startup": ("创业", "创业者", "机会"),
    "human": ("agency", "taste", "junior", "超级个体"),
    "programmer": ("程序员",),
    "busy work": ("busy work",),
    "product manager": ("产品经理", "产品文档"),
}
SPECIFIC_RELATION_FOCUSES = {
    "claude code",
    "cursor",
    "mcp",
    "api",
    "cost",
    "prompt",
    "context",
    "startup",
    "human",
    "programmer",
    "busy work",
    "product manager",
}
WORKFLOW_SIGNAL_KEYWORDS = (
    "workflow",
    "sub-agent",
    "sub agent",
    "github action",
    "prompt",
    "步骤",
    "任务规划",
)
CONTEXT_SIGNAL_KEYWORDS = (
    "knowledge base",
    "外脑",
    "documentation",
    "context window",
    "context,window management",
    "上下文",
    "记忆",
)
BUSINESS_SIGNAL_KEYWORDS = (
    "成本",
    "昂贵",
    "token",
    "定价",
    "to c",
    "to b",
    "商业化",
    "市场",
    "创业",
    "创业者",
    "机会",
    "api",
    "performance",
    "value",
    "build for ai",
    "buy ai",
    "价值创造",
    "cost",
)
HUMAN_SIGNAL_KEYWORDS = (
    "agency",
    "taste",
    "情绪价值",
    "超级个体",
    "程序员",
    "产品经理",
    "产品文档",
    "busy work",
    "替代",
    "取代",
)

ANSWER_CLAIM_RE = re.compile(r"^Claim: (?P<claim>.+)$", re.MULTILINE)
ANSWER_TOPIC_RE = re.compile(r"^Topics: (?P<topics>.+)$", re.MULTILINE)


def _normalize_text(text: str) -> str:
    return text.strip().lower()


def _count_keyword_hits(text: str, keywords: tuple[str, ...]) -> int:
    lowered = _normalize_text(text)
    return sum(lowered.count(keyword) for keyword in keywords if keyword in lowered)


def _segment_score(view_name: str, transcript: TranscriptDocument, segment: TranscriptSegment) -> int:
    title_lower = _normalize_text(transcript.title)
    segment_lower = _normalize_text(segment.text)
    score = len(segment.text) // 20
    score += _count_keyword_hits(segment_lower, VIEW_KEYWORDS[view_name]) * 6
    score += _count_keyword_hits(segment_lower, DOMAIN_SIGNAL_KEYWORDS) * 3
    score += min(_count_keyword_hits(title_lower, VIEW_KEYWORDS[view_name]), 1)

    if any(marker in segment_lower for marker in INTRO_MARKERS):
        score -= 8
    if segment.timestamp == "00:00:00":
        score -= 6
    if any(marker in segment_lower for marker in LOW_SIGNAL_SEGMENT_MARKERS):
        score -= 12
    if any(marker in segment_lower for marker in QUESTION_STYLE_MARKERS):
        score -= 7
    if any(marker in segment_lower for marker in LOW_SIGNAL_LEAD_MARKERS):
        score -= 10
    if view_name in {"controversy", "practice"} and _count_keyword_hits(segment_lower, DOMAIN_SIGNAL_KEYWORDS) == 0:
        score -= 6

    if view_name == "judgment" and any(marker in segment_lower for marker in POSITIVE_MARKERS):
        score += 4
    if view_name == "controversy" and any(marker in segment_lower for marker in NEGATIVE_MARKERS):
        score += 5
    if view_name == "practice" and any(marker in segment_lower for marker in ("workflow", "prompt", "外脑", "knowledge base", "sub-agent", "github action", "mcp", "documentation", "context window", "context,window management")):
        score += 5

    return score


def _rank_segments(
    view_name: str,
    transcript: TranscriptDocument,
    used_indices: set[int],
) -> list[tuple[int, TranscriptSegment]]:
    ranked: list[tuple[int, int, TranscriptSegment]] = []
    for index, segment in enumerate(transcript.segments):
        if index in used_indices or len(segment.text.strip()) < 12:
            continue
        ranked.append((_segment_score(view_name, transcript, segment), index, segment))

    ranked.sort(key=lambda item: item[0], reverse=True)
    return [(index, segment) for _, index, segment in ranked]


def _build_claim(segment: TranscriptSegment) -> str:
    text = segment.text.strip().rstrip("，,。！？.!?")
    return f"{text}。"


def _claim_relation_focuses(claim: str) -> set[str]:
    lowered = _normalize_text(claim)
    return {
        focus
        for focus, keywords in RELATION_FOCUS_KEYWORDS.items()
        if any(keyword in lowered for keyword in keywords)
    }


def _claim_has_dependency_signal(claim: str) -> bool:
    lowered = _normalize_text(claim)
    return any(marker in lowered for marker in DEPENDENCY_MARKERS)


def _infer_topics(title: str, claim: str, view_name: str) -> list[str]:
    lowered = _normalize_text(f"{title} {claim}")
    topics = [topic for topic, keywords in TOPIC_KEYWORDS.items() if any(keyword in lowered for keyword in keywords)]
    if topics:
        return topics[:3]

    fallback_topics = {
        "judgment": ["ai coding", "human leverage"],
        "controversy": ["ai product strategy"],
        "practice": ["agent workflow", "context engineering"],
    }
    return fallback_topics[view_name]


def _focus_fallback(topics: list[str], view_name: str) -> str:
    if "agent workflow" in topics:
        return "task-specific workflows"
    if "context engineering" in topics:
        return "documentation and context setup"
    if "ai product strategy" in topics:
        return "an AI product bet"
    if "human leverage" in topics:
        return "human judgment"
    if "ai coding" in topics:
        return "AI coding work"
    if view_name == "controversy":
        return "this rollout decision"
    if view_name == "practice":
        return "the operating steps"
    return "this idea"


def _focus_phrase(claim: str, topics: list[str], view_name: str) -> str:
    lowered = _normalize_text(claim)
    explicit_focuses: tuple[tuple[tuple[str, ...], str], ...] = (
        (("3d 模型", "部署上去", "部署"), "using Claude Code to deploy 3D models"),
        (("技术报告",), "using Claude Code to read technical reports"),
        (("写代码", "coding", "编程"), "AI coding work"),
        (("claude code", "cloud code"), "claude code"),
        (("cursor",), "cursor"),
        (("sub-agent", "sub agent"), "claude code sub-agents"),
        (("任务规划",), "agent task planning"),
        (("workflow",), "task-specific workflows"),
        (("prompt",), "prompt design"),
        (("交互方式",), "new interaction models"),
        (("语音输入法", "build for ai", "buy ai"), "an AI-native voice product"),
        (("mcp",), "using MCP"),
        (("knowledge base", "外脑", "documentation", "context window", "context,window management", "context", "上下文", "记忆"), "documentation and context setup"),
        (("api",), "using the API"),
        (("成本", "昂贵", "token", "定价", "to c", "to b", "商业化", "市场", "performance", "value", "cost"), "the economics of the tool"),
        (("程序员", "busy work", "产品经理", "产品文档", "替代", "取代"), "work ownership between AI and humans"),
        (("agency", "taste", "情绪价值", "超级个体", "平庸"), "human judgment"),
        (("创业", "创业者", "机会"), "startup opportunities"),
    )

    for keywords, label in explicit_focuses:
        if any(keyword in lowered for keyword in keywords):
            return label

    return _focus_fallback(topics, view_name)


def _action_focus(focus: str) -> str:
    for prefix in ("the ", "this ", "an ", "a "):
        if focus.startswith(prefix):
            return focus.removeprefix(prefix)
    return focus


def _build_boundary(title: str, claim: str, topics: list[str], view_name: str) -> str:
    focus = _focus_phrase(claim, topics, view_name)
    flags = _claim_flags(claim)

    if flags["negative"] or view_name == "controversy":
        if flags["human"]:
            return "This matters when the team is deciding which parts of the work can move to AI and which still need human ownership."
        if flags["business"]:
            return f"This matters when the team has to justify {focus} with a concrete customer, cost, or performance case before rollout."
        if flags["negative"]:
            return f"This matters when {focus} could change adoption risk, replacement pressure, or operating cost for the team."
        return f"This matters when the team is still testing where {focus} helps, where it breaks, and which tradeoffs still need human review."

    if flags["context"]:
        return f"This holds when {focus} is explicit enough that another operator can reproduce the setup and verify the result."

    if flags["workflow"] or view_name == "practice":
        return f"This holds when {focus} can be repeated by another operator with the same tools and a clear verification step."

    if flags["human"]:
        if focus == "human judgment":
            return "This works when the result still depends on human judgment, taste, or verification instead of treating the model output as final."
        return f"This works when {focus} still depends on human judgment, taste, or verification instead of treating the model output as final."

    if flags["business"]:
        return f"This works when {focus} can be tied to a specific customer, workflow, or pricing decision that the team can actually test."

    return f"This works when {focus} is being tested inside a bounded task with a clear owner and a way to check the result."


def _build_action(title: str, claim: str, topics: list[str], view_name: str) -> str:
    focus = _focus_phrase(claim, topics, view_name)
    flags = _claim_flags(claim)
    action_focus = _action_focus(focus)

    if flags["negative"] or view_name == "controversy":
        if flags["human"]:
            return "List one part of the workflow that can move to AI and one part that still needs a human owner before broader rollout."
        if not flags["negative"] and not flags["business"]:
            return f"Test {action_focus} in one real workflow and record which tradeoffs or open questions still need human judgment before broader rollout."
        return f"Compare {action_focus} against the current baseline on cost, performance, and failure cases before broader rollout."

    if flags["context"]:
        return f"Write down the {action_focus} steps so another operator can reproduce them without extra context."

    if flags["workflow"] or view_name == "practice":
        return f"Turn {action_focus} into a short reusable workflow or prompt checklist that another operator can follow."

    if flags["human"]:
        if focus == "human judgment":
            return "Run one task with AI assistance and record which judgment calls still have to stay with the human operator."
        return f"Run one task with {action_focus} and record which judgment calls still have to stay with the human operator."

    if flags["business"]:
        return f"Turn {action_focus} into one concrete customer, workflow, or pricing experiment before scaling it."

    return f"Pilot {action_focus} on one bounded task and note the evidence you would need before scaling it."


def _claim_flags(text: str) -> dict[str, bool]:
    lowered = _normalize_text(text)
    return {
        "coding": any(keyword in lowered for keyword in TOPIC_KEYWORDS["ai coding"]),
        "workflow": any(keyword in lowered for keyword in WORKFLOW_SIGNAL_KEYWORDS),
        "context": any(keyword in lowered for keyword in CONTEXT_SIGNAL_KEYWORDS),
        "business": any(keyword in lowered for keyword in BUSINESS_SIGNAL_KEYWORDS),
        "human": any(keyword in lowered for keyword in HUMAN_SIGNAL_KEYWORDS),
        "positive": any(marker in lowered for marker in POSITIVE_MARKERS),
        "negative": any(marker in lowered for marker in NEGATIVE_MARKERS),
    }


class DemoExtractor:
    def build_candidates(self, transcript: TranscriptDocument) -> dict[str, list[CardCandidatePayload]]:
        if not transcript.segments:
            return {"judgment": [], "controversy": [], "practice": []}

        used_indices: set[int] = set()
        view_payloads: dict[str, list[CardCandidatePayload]] = {"judgment": [], "controversy": [], "practice": []}

        for view_name in ("judgment", "controversy", "practice"):
            for index, segment in _rank_segments(view_name, transcript, used_indices):
                claim = _build_claim(segment)
                topics = _infer_topics(transcript.title, claim, view_name)
                payload: CardCandidatePayload = {
                    "claim": claim,
                    "evidence": [{"speaker": segment.speaker, "timestamp": segment.timestamp, "quote": claim}],
                    "boundary": _build_boundary(transcript.title, claim, topics, view_name),
                    "action": _build_action(transcript.title, claim, topics, view_name),
                    "topics": topics,
                    "source_view": view_name,
                }
                try:
                    _ = validate_card_candidate(CardCandidate.model_validate(payload))
                except ValueError:
                    continue

                used_indices.add(index)
                view_payloads[view_name].append(payload)
                break

        return view_payloads


class DemoEmbeddingClient:
    def embed(self, text: str) -> EmbeddingPayload:
        lowered = _normalize_text(text)
        embedding = [
            float(_count_keyword_hits(lowered, TOPIC_KEYWORDS["ai coding"])),
            float(_count_keyword_hits(lowered, TOPIC_KEYWORDS["agent workflow"])),
            float(_count_keyword_hits(lowered, TOPIC_KEYWORDS["context engineering"])),
            float(_count_keyword_hits(lowered, TOPIC_KEYWORDS["ai product strategy"])),
            float(_count_keyword_hits(lowered, TOPIC_KEYWORDS["human leverage"])),
            1.0 if any(marker in lowered for marker in POSITIVE_MARKERS) else 0.0,
            1.0 if any(marker in lowered for marker in NEGATIVE_MARKERS) else 0.0,
            1.0,
        ]
        return {"embedding": embedding}


class DemoRelationClassifier:
    def classify(self, left_claim: str, right_claim: str) -> RelationClassification:
        if left_claim == right_claim:
            return {"label": "unrelated", "confidence": 0.0}

        left_focuses = _claim_relation_focuses(left_claim)
        right_focuses = _claim_relation_focuses(right_claim)
        shared_focuses = left_focuses & right_focuses
        left_flags = _claim_flags(left_claim)
        right_flags = _claim_flags(right_claim)

        if not shared_focuses:
            return {"label": "unrelated", "confidence": 0.0}

        shared_specific_focuses = shared_focuses & SPECIFIC_RELATION_FOCUSES

        if left_flags["negative"] != right_flags["negative"] and shared_specific_focuses:
            return {"label": "conflict", "confidence": 0.86}

        if shared_focuses & {"prompt", "workflow", "context", "mcp"} and (
            (_claim_has_dependency_signal(left_claim) and not right_flags["negative"])
            or (_claim_has_dependency_signal(right_claim) and not left_flags["negative"])
        ):
            return {"label": "prerequisite", "confidence": 0.86}

        if shared_specific_focuses:
            return {"label": "support", "confidence": 0.9}

        if len(shared_focuses) >= 2:
            return {"label": "support", "confidence": 0.86}

        return {"label": "unrelated", "confidence": 0.0}


class DemoAnswerClient:
    def complete(self, messages: list[dict[str, str]]) -> ChatCompletionPayload:
        prompt = messages[-1]["content"] if messages else ""
        claims = ANSWER_CLAIM_RE.findall(prompt)
        topics = ", ".join(ANSWER_TOPIC_RE.findall(prompt)).lower()
        lowered = prompt.lower()

        if "ai coding" in topics or "claude code" in lowered or "cursor" in lowered:
            lead = "Across the demo episodes, AI coding tools are framed as real leverage for small teams and individual builders."
        elif "human leverage" in topics or "agency" in lowered or "taste" in lowered:
            lead = "Across the demo episodes, speakers treat agency and taste as the human advantages that become more important after AI adoption."
        else:
            lead = "Across the demo episodes, speakers repeatedly describe AI as useful when it is tied to concrete work rather than abstract hype."

        if "ai product strategy" in topics or any(marker in lowered for marker in ("成本", "昂贵", "风险", "替换", "取代")):
            caveat = "The main caveat is that cost, replacement risk, and rollout discipline still shape where adoption makes sense."
        else:
            caveat = "The main caveat is that teams still need clear workflows and explicit operator judgment around the tool."

        evidence = " ".join(claims[:2]) if claims else ""
        summary = f"{lead} {caveat}"
        if evidence:
            summary += f" Evidence in the selected cards includes: {evidence}"
        return {"content": summary}


def _should_use_live_clients(chat_api_key: str) -> bool:
    normalized = chat_api_key.strip()
    return bool(normalized) and normalized.lower() != "replace-me"


def _build_runtime_clients(
    project_root: Path,
) -> tuple[str, CandidateExtractor, EmbeddingProvider, RelationClassifier, AnswerProvider]:
    settings = load_settings(project_root)
    if not _should_use_live_clients(settings.chat_api_key):
        return (
            "demo",
            DemoExtractor(),
            DemoEmbeddingClient(),
            DemoRelationClassifier(),
            DemoAnswerClient(),
        )

    cache = FileCache(settings.cache_dir)
    heavy_client = LLMClient(
        config=ModelEndpointConfig(
            base_url=settings.chat_base_url,
            api_key=settings.chat_api_key,
            model=settings.heavy_model,
        ),
        cache=cache,
    )
    light_client = LLMClient(
        config=ModelEndpointConfig(
            base_url=settings.chat_base_url,
            api_key=settings.chat_api_key,
            model=settings.light_model,
        ),
        cache=cache,
    )
    embedding_client = EmbeddingClient(
        config=ModelEndpointConfig(
            base_url=settings.embedding_base_url,
            api_key=settings.chat_api_key,
            model=settings.embedding_model,
        ),
        cache=cache,
    )
    return (
        "live",
        LLMExtractor(heavy_client),
        embedding_client,
        LLMRelationClassifier(light_client),
        light_client,
    )


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    workspace_root = project_root.parents[1]
    output_dir = Path(os.getenv("PODINSIGHT_OUTPUT_DIR", str(project_root / "data" / "derived")))
    mode, extractor, embedding_client, relation_classifier, answer_client = _build_runtime_clients(project_root)
    artifacts = build_demo_artifacts(
        project_root=project_root,
        workspace_root=workspace_root,
        output_dir=output_dir,
        extractor=extractor,
        embedding_client=embedding_client,
        relation_classifier=relation_classifier,
        answer_client=answer_client,
    )
    print(json.dumps({"output_dir": str(output_dir), "card_count": len(cast(list[object], artifacts["cards"])), "mode": mode}))


if __name__ == "__main__":
    main()
