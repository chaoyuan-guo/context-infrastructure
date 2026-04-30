"""Circle 帖子正文 → Markdown 转换器。"""

import base64
import html
import json
import re

try:
    from bs4 import BeautifulSoup, NavigableString, Tag
except ImportError:  # pragma: no cover - optional dependency
    BeautifulSoup = None
    NavigableString = None
    Tag = None


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

    if t == "mention":
        # mention 节点标记被回复者（@Name），由 main.py extract_reply_to_name 处理
        # 正文中不重复渲染，返回空字符串
        return ""

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


def _normalize_inline_text(text: str) -> str:
    if not text:
        return ""
    if not text.strip():
        return ""
    return re.sub(r"\s+", " ", html.unescape(text))


def _normalize_url(url: str) -> str:
    if not url:
        return ""
    if url.startswith("//"):
        return f"https:{url}"
    return url


def _render_trix_node(node, indent: int = 0) -> str:
    if NavigableString is not None and isinstance(node, NavigableString):
        return _normalize_inline_text(str(node))

    if Tag is None or not isinstance(node, Tag):
        return ""

    name = node.name.lower()

    if name in {"strong", "b"}:
        inner = "".join(_render_trix_node(child, indent) for child in node.children).strip()
        return f"**{inner}**" if inner else ""

    if name in {"em", "i"}:
        inner = "".join(_render_trix_node(child, indent) for child in node.children).strip()
        return f"*{inner}*" if inner else ""

    if name == "code":
        inner = "".join(_render_trix_node(child, indent) for child in node.children).strip()
        return f"`{inner}`" if inner else ""

    if name == "br":
        return "\n"

    if name == "a":
        href = _normalize_url((node.get("href") or "").strip())
        inner = "".join(_render_trix_node(child, indent) for child in node.children).strip() or href
        return f"[{inner}]({href})" if href else inner

    if name == "img":
        src = _normalize_url((node.get("data-src") or node.get("src") or "").strip())
        alt = (node.get("alt") or "image").strip()
        return f"![{alt}]({src})" if src else ""

    if name == "iframe":
        src = _normalize_url((node.get("src") or "").strip())
        return f"[视频]({src})" if src else ""

    if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
        level = int(name[1])
        inner = "".join(_render_trix_node(child, indent) for child in node.children).strip()
        return f"{'#' * level} {inner}\n\n" if inner else ""

    if name == "p":
        inner = "".join(_render_trix_node(child, indent) for child in node.children).strip()
        return f"{inner}\n\n" if inner else "\n"

    if name == "blockquote":
        inner = "".join(_render_trix_node(child, indent) for child in node.children).strip()
        if not inner:
            return ""
        lines = [f"> {line}" if line.strip() else ">" for line in inner.splitlines()]
        return "\n".join(lines) + "\n\n"

    if name == "ul":
        items = []
        for li in node.find_all("li", recursive=False):
            inner = "".join(_render_trix_node(child, indent + 1) for child in li.children).strip()
            if inner:
                items.append(f"{'  ' * indent}- {inner}")
        return "\n".join(items) + "\n\n" if items else ""

    if name == "ol":
        items = []
        for index, li in enumerate(node.find_all("li", recursive=False), 1):
            inner = "".join(_render_trix_node(child, indent + 1) for child in li.children).strip()
            if inner:
                items.append(f"{'  ' * indent}{index}. {inner}")
        return "\n".join(items) + "\n\n" if items else ""

    return "".join(_render_trix_node(child, indent) for child in node.children)


def parse_trix_body(raw_html: str) -> str:
    if not raw_html:
        return ""

    if BeautifulSoup is not None:
        soup = BeautifulSoup(raw_html, "html.parser")
        md = "".join(_render_trix_node(child) for child in soup.contents)
        md = re.sub(r"\n{3,}", "\n\n", md)
        return md.strip()

    # 兜底：在没有 bs4 时保留基础段落结构。
    md = raw_html
    md = re.sub(r"<br\s*/?>", "\n", md, flags=re.IGNORECASE)
    md = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", lambda m: f"{'#' * int(m.group(1))} {re.sub(r'<[^>]+>', '', m.group(2)).strip()}\n\n", md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r"<li[^>]*>(.*?)</li>", lambda m: f"- {re.sub(r'<[^>]+>', '', m.group(1)).strip()}\n", md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r"<p[^>]*>(.*?)</p>", lambda m: f"{re.sub(r'<[^>]+>', '', m.group(1)).strip()}\n\n", md, flags=re.IGNORECASE | re.DOTALL)
    md = re.sub(r"<[^>]+>", "", md)
    md = html.unescape(md)
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def parse_post_body(data: dict) -> str:
    if not data:
        return ""

    if data.get("tiptap_body"):
        return parse_tiptap_body(data.get("tiptap_body"))

    trix_html = data.get("body_trix_content") or data.get("body_for_editor")
    if trix_html:
        return parse_trix_body(trix_html)

    return ""
