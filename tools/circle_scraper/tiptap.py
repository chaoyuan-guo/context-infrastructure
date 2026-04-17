"""tiptap JSON → Markdown 确定性转换器。"""

import base64
import json
import re


def marks_wrap(text: str, marks: list | None) -> str:
    if not marks:
        return text
    for m in marks:
        t = m.get("type", "")
        if t == "bold":
            text = f"**{text}**"
        elif t == "italic":
            text = f"*{text}*"
        elif t == "code":
            text = f"`{text}`"
        elif t == "link":
            href = m.get("attrs", {}).get("href", "")
            text = f"[{text}]({href})"
    return text


def tiptap_to_md(node: dict | None, indent: int = 0) -> str:
    """递归将 tiptap JSON 节点转为 Markdown 字符串。"""
    if not node:
        return ""
    t = node.get("type", "")
    content = node.get("content") or []
    attrs = node.get("attrs") or {}

    if t == "doc":
        return "\n\n".join(filter(None, [tiptap_to_md(c) for c in content]))

    if t == "paragraph":
        return "".join(tiptap_to_md(c) for c in content)

    if t == "heading":
        level = attrs.get("level", 2)
        inner = "".join(tiptap_to_md(c) for c in content)
        return "#" * level + " " + inner

    if t == "bulletList":
        items = []
        for li in content:
            inner = " ".join(
                tiptap_to_md(c).strip() for c in (li.get("content") or [])
            ).strip()
            items.append("  " * indent + "- " + inner)
        return "\n".join(items)

    if t == "orderedList":
        items = []
        for i, li in enumerate(content, 1):
            inner = " ".join(
                tiptap_to_md(c).strip() for c in (li.get("content") or [])
            ).strip()
            items.append("  " * indent + f"{i}. " + inner)
        return "\n".join(items)

    if t == "listItem":
        return " ".join(tiptap_to_md(c).strip() for c in content)

    if t == "blockquote":
        inner = "\n\n".join(filter(None, [tiptap_to_md(c) for c in content]))
        return "\n".join("> " + line for line in inner.splitlines())

    if t == "horizontalRule":
        return "---"

    if t == "hardBreak":
        return "\n"

    if t == "codeBlock":
        lang = attrs.get("language", "") or ""
        inner = "".join(tiptap_to_md(c) for c in content)
        return f"```{lang}\n{inner}\n```"

    if t == "text":
        return marks_wrap(node.get("text", ""), node.get("marks"))

    if t == "image":
        signed_id = attrs.get("signed_id", "")
        return f"![image](IMAGE:{signed_id})"

    if t == "embed":
        src = attrs.get("src", "") or attrs.get("url", "")
        sgid = attrs.get("sgid", "")
        if src:
            return f"[视频嵌入]({src})"
        # 无 src 的 oembed（链接预览卡片），用 sgid 占位，由 main.py 从 DOM 数据替换
        return f"[OEMBED:{sgid}]"

    if t == "entity":
        sgid = attrs.get("sgid", "")
        # circle_ios_fallback_text 可能在 attrs 内，也可能在节点顶层
        fallback = (
            attrs.get("circle_ios_fallback_text")
            or node.get("circle_ios_fallback_text")
            or "内部链接"
        )
        post_id = None
        try:
            decoded = base64.b64decode(sgid + "==", altchars=b"-_").decode(
                "latin-1", errors="replace"
            )
            m = re.search(r"Posts::Basic/(\d+)", decoded)
            if m:
                post_id = m.group(1)
        except Exception:
            pass
        if post_id:
            # 用占位符，由 main.py 从 post_id_map 替换为真实 URL
            return f"[ENTITY:{post_id}:{fallback}]"
        return f"**{fallback}**"

    # fallback: recurse into children
    return "".join(tiptap_to_md(c) for c in content)


def parse_tiptap_body(raw) -> str:
    """解析 tiptap_body 字段（可能是 str 或 dict），返回 Markdown。

    Circle.so 的 tiptap_body 实际 doc 结构嵌套在 .body 字段内。
    帖子和评论的结构相同。
    """
    if not raw:
        return ""
    tb = json.loads(raw) if isinstance(raw, str) else raw
    body = tb.get("body", tb)
    return tiptap_to_md(body)
