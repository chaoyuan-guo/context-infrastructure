#!/usr/bin/env python3
"""Circle.so 社区帖子抓取工具。

用法:
    python tools/circle_scraper/main.py <URL> [--output-dir <dir>]

示例:
    python tools/circle_scraper/main.py https://www.superlinear.academy/c/share-your-insights/ai-pattern
    python tools/circle_scraper/main.py https://www.superlinear.academy/c/share-your-insights/ai-pattern --output-dir ./output
"""

import argparse
import json
import os
import re
import sys

sys.path.append(os.path.dirname(__file__))

from cookies import load_cookies
from scraper import fetch_page, diagnose
from tiptap import parse_tiptap_body

DEFAULT_OUTPUT_DIR = os.path.join(
    os.path.dirname(__file__), "..", "..", "formal_projects", "curated_reads"
)


def extract_domain(url: str) -> str:
    from urllib.parse import urlparse
    return urlparse(url).netloc


def build_markdown(post_data: dict, body_md: str, comments: list, url: str, domain: str,
                   oembed_links: list | None = None, post_id_map: dict | None = None,
                   comment_img_srcs: list | None = None) -> str:
    """组装最终 Markdown 文件。"""
    title = post_data.get("name", "untitled")
    author = (post_data.get("community_member") or {}).get("name", "unknown")
    published = (post_data.get("published_at") or post_data.get("created_at") or "")[:10]
    slug = post_data.get("slug", "")

    oembed_links = list(oembed_links or [])
    post_id_map = post_id_map or {}
    comment_img_srcs = list(comment_img_srcs or [])

    # 评论区
    comments_section = ""
    if comments:
        parts = []
        for c in comments:
            ca = (c.get("community_member") or {}).get("name", "unknown")
            ct = (c.get("created_at") or "")[:10]
            cb = parse_tiptap_body(c.get("tiptap_body"))
            cb = replace_media(cb, comment_img_srcs, [],
                               oembed_links=oembed_links,
                               post_id_map=post_id_map, domain=domain)
            lines = [f"### {ca}", f"*{ct}*", "", cb.strip()]

            # 嵌套回复
            for r in c.get("replies") or []:
                ra = (r.get("community_member") or {}).get("name", "unknown")
                rt = (r.get("created_at") or "")[:10]
                rb = parse_tiptap_body(r.get("tiptap_body"))
                rb = replace_media(rb, comment_img_srcs, [],
                                   oembed_links=oembed_links,
                                   post_id_map=post_id_map, domain=domain)
                lines += ["", f"**↳ {ra}** *{rt}*", "", rb.strip()]

            parts.append("\n".join(lines))
        comments_section = "\n\n---\n\n## 评论区\n\n" + "\n\n---\n\n".join(parts)

    return f"""# {title}

> 来源：<{url}>
> 作者：{author}
> 发布日期：{published}
> 平台：Superlinear Academy

---

{body_md.strip()}
{comments_section}
"""


def replace_media(body_md: str, img_srcs: list, iframe_srcs: list,
                   oembed_links: list | None = None,
                   post_id_map: dict | None = None,
                   domain: str = "") -> str:
    """将各类占位符替换为真实 URL。

    处理的占位符类型：
    - ![image](IMAGE:...) → 真实图片 URL（从 DOM 按序匹配）
    - [视频嵌入](...) → 真实视频 URL（从 DOM iframe 按序匹配）
    - [OEMBED:sgid] → 链接预览（从 DOM oembed 渲染数据匹配）
    - [ENTITY:post_id:text] → 内部帖子链接（从 API post_id_map 匹配）
    """
    oembed_links = oembed_links or []
    post_id_map = post_id_map or {}

    # 图片占位符
    idx = [0]
    def rep_img(m):
        if idx[0] < len(img_srcs):
            src = img_srcs[idx[0]]
            idx[0] += 1
            return f"![image]({src})"
        return m.group(0)
    body_md = re.sub(r"!\[image\]\(IMAGE:.*?\)", rep_img, body_md)

    # iframe 视频占位符
    idx2 = [0]
    def rep_iframe(m):
        if idx2[0] < len(iframe_srcs):
            src = iframe_srcs[idx2[0]]
            idx2[0] += 1
            yt = re.search(r"youtube\.com/embed/([^?]+)", src)
            if yt:
                src = f"https://www.youtube.com/watch?v={yt.group(1)}"
            return f"[视频]({src})"
        return m.group(0)
    body_md = re.sub(r"\[视频嵌入\]\(.*?\)", rep_iframe, body_md)

    # oembed 占位符：[OEMBED:sgid] → 链接
    def rep_oembed(m):
        sgid = m.group(1)
        # 尝试通过 sgid 匹配 DOM 中的 oembed 数据
        for ol in oembed_links:
            if ol.get("sgid") == sgid and ol.get("href"):
                text = ol.get("text") or ol["href"]
                return f"[{text}]({ol['href']})"
        # 没匹配到，尝试按顺序消费
        if oembed_links:
            ol = oembed_links.pop(0)
            text = ol.get("text") or ol.get("href", "链接")
            href = ol.get("href", "")
            if href:
                return f"[{text}]({href})"
        return ""  # 无法解析，移除占位符
    body_md = re.sub(r"\[OEMBED:(.*?)\]", rep_oembed, body_md)

    # entity 占位符：[ENTITY:post_id:text] → 帖子链接
    def rep_entity(m):
        post_id = m.group(1)
        text = m.group(2)
        slug = post_id_map.get(post_id)
        if slug and domain:
            # 不知道 space_slug，用通用搜索路径
            url = f"https://{domain}/c/{slug}"
            return f"[{text}]({url})"
        # 没找到，保留为加粗文本
        return f"**{text}**"
    body_md = re.sub(r"\[ENTITY:(\d+):(.*?)\]", rep_entity, body_md)

    return body_md


def main():
    parser = argparse.ArgumentParser(description="抓取 Circle.so 社区帖子并保存为 Markdown")
    parser.add_argument("url", help="帖子 URL")
    parser.add_argument("--output-dir", default=DEFAULT_OUTPUT_DIR, help="输出目录")
    args = parser.parse_args()

    url = args.url
    domain = extract_domain(url)
    output_dir = os.path.abspath(args.output_dir)

    print(f"[1/4] 加载 Cookie...")
    cookies, err = load_cookies(domain)
    if err:
        print(f"  ⚠️  {err}")
        print("  将尝试无 Cookie 抓取（公开帖子可能可行）")

    print(f"[2/4] 抓取页面...")
    result = fetch_page(url, cookies)
    captured_api = result["captured_api"]
    print(f"  拦截到 {len(captured_api)} 个 API 响应")

    print(f"[3/4] 诊断与解析...")
    diag = diagnose(captured_api)
    print(f"  {diag['diagnosis']}")

    if diag["needs_login"] and not diag["has_tiptap"]:
        print("\n需要登录才能抓取此帖子。")
        print("请在浏览器中操作：")
        print("  1. 打开目标帖子页面（确保已登录）")
        print("  2. F12 → Application → Cookies")
        print("  3. 复制 user_session_identifier 和 remember_user_token 的值")
        print(f"  4. 保存到 {os.path.expanduser('~/.config/circle-so/cookies.json')}")
        sys.exit(1)

    post_data = diag["post_data"]
    post_id_map = diag["post_id_map"]
    oembed_links = list(result.get("comment_oembed_links") or [])  # mutable copy

    body_md = parse_tiptap_body(post_data.get("tiptap_body"))
    body_md = replace_media(
        body_md, result["img_srcs"], result["iframe_srcs"],
        oembed_links=list(oembed_links),  # copy for post body
        post_id_map=post_id_map, domain=domain,
    )

    md = build_markdown(
        post_data, body_md, diag["comments"], url, domain,
        oembed_links=oembed_links, post_id_map=post_id_map,
        comment_img_srcs=result.get("comment_img_srcs", []),
    )

    print(f"[4/4] 保存文件...")
    os.makedirs(output_dir, exist_ok=True)
    title = post_data.get("name", "untitled")
    safe_title = re.sub(r'[/\\:*?"<>|]', "", title).strip()
    out_path = os.path.join(output_dir, f"{safe_title}.md")
    with open(out_path, "w") as f:
        f.write(md)
    print(f"  ✓ {out_path}")
    print(f"  标题: {title}")
    print(f"  正文: {len(body_md)} 字符, 评论: {len(diag['comments'])} 条")


if __name__ == "__main__":
    main()
