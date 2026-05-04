#!/usr/bin/env python3
"""Web Article Scraper: 社区帖子与公众号文章抓取工具。

用法:
    python tools/web_article_scraper/main.py <URL> [--output-dir <dir>]

示例:
    python tools/web_article_scraper/main.py https://www.superlinear.academy/c/share-your-insights/ai-pattern
    python tools/web_article_scraper/main.py https://www.superlinear.academy/c/share-your-insights/ai-pattern --output-dir ./output
    python tools/web_article_scraper/main.py https://mp.weixin.qq.com/s/d1aBQMx-JwLh4H8xlyV0OA
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen

sys.path.append(os.path.dirname(__file__))

from cookies import load_cookies
from scraper import fetch_page, diagnose
from tiptap import BeautifulSoup, parse_post_body, parse_tiptap_body, parse_trix_body

DEFAULT_OUTPUT_ROOT = os.path.join(
    os.path.dirname(__file__), "..", "..", "formal_projects", "curated_reads"
)
WECHAT_USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/136.0.0.0 Safari/537.36"
)


def extract_domain(url: str) -> str:
    from urllib.parse import urlparse
    return urlparse(url).netloc


def detect_site(url: str) -> str:
    domain = extract_domain(url)
    if domain == "mp.weixin.qq.com":
        return "wechat"
    return "circle"


def default_output_dir_for_site(site: str) -> str:
    if site == "wechat":
        return os.path.join(DEFAULT_OUTPUT_ROOT, "wechat")
    return os.path.join(DEFAULT_OUTPUT_ROOT, "superlinear")


def save_markdown(output_dir: str, title: str, published: str, markdown: str) -> str:
    os.makedirs(output_dir, exist_ok=True)
    safe_title = re.sub(r'[/\\:*?"<>|]', "", title).strip() or "untitled"
    date_prefix = published[:10].replace("-", "")[2:] + "_" if published else ""
    out_path = os.path.join(output_dir, f"{date_prefix}{safe_title}.md")
    with open(out_path, "w") as f:
        f.write(markdown)
    return out_path


def extract_wechat_publish_time(html_text: str) -> str:
    create_time_match = re.search(r"var\s+createTime\s*=\s*'([^']+)'", html_text)
    if create_time_match:
        return create_time_match.group(1)

    timestamp_match = re.search(r'var\s+ct\s*=\s*"?(\d{10})"?', html_text)
    if not timestamp_match:
        return ""

    dt = datetime.fromtimestamp(
        int(timestamp_match.group(1)), tz=timezone(timedelta(hours=8))
    )
    return dt.strftime("%Y-%m-%d %H:%M")


def parse_wechat_article(url: str) -> dict:
    if BeautifulSoup is None:
        raise RuntimeError("缺少 beautifulsoup4，无法解析微信公众号文章 HTML")

    req = Request(
        url,
        headers={
            "User-Agent": WECHAT_USER_AGENT,
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Referer": "https://mp.weixin.qq.com/",
        },
    )

    with urlopen(req, timeout=60) as resp:
        html_text = resp.read().decode("utf-8", "replace")

    soup = BeautifulSoup(html_text, "html.parser")
    content = soup.find(id="js_content")
    if content is None:
        raise RuntimeError("未找到微信公众号正文容器 #js_content")

    for node in content.select("script, style"):
        node.decompose()

    title = ""
    title_node = soup.select_one("#activity-name .js_title_inner")
    if title_node:
        title = title_node.get_text(" ", strip=True)
    if not title:
        meta_title = soup.select_one('meta[property="og:title"]')
        title = (meta_title.get("content") or "").strip() if meta_title else ""

    author = ""
    author_node = soup.select_one("#js_author_name")
    if author_node:
        author = author_node.get_text(" ", strip=True)
    if not author:
        meta_author = soup.select_one('meta[name="author"]')
        author = (meta_author.get("content") or "").strip() if meta_author else ""

    account_name = ""
    account_node = soup.select_one("#js_name")
    if account_node:
        account_name = account_node.get_text(" ", strip=True)
    if not account_name:
        nickname_match = re.search(r'var\s+nickname\s*=\s*htmlDecode\("([^"]*)"\)', html_text)
        if nickname_match:
            account_name = nickname_match.group(1)

    body_md = parse_trix_body(content.decode_contents())

    return {
        "title": title or "untitled",
        "author": author or "unknown",
        "account_name": account_name or "unknown",
        "published": extract_wechat_publish_time(html_text),
        "body_md": body_md,
    }


def build_wechat_markdown(article: dict, url: str) -> str:
    return f"""# {article['title']}

> 来源：<{url}>
> 作者：{article['author']}
> 公众号：{article['account_name']}
> 发布日期：{article['published']}
> 平台：微信公众号

---

{article['body_md'].strip()}
"""


def scrape_wechat_article(url: str, output_dir: str) -> None:
    print("[1/3] 获取微信公众号文章 HTML...")
    article = parse_wechat_article(url)

    print("[2/3] 解析正文...")
    md = build_wechat_markdown(article, url)

    print("[3/3] 保存文件...")
    out_path = save_markdown(output_dir, article["title"], article["published"], md)
    print(f"  ✓ {out_path}")
    print(f"  标题: {article['title']}")
    print(f"  正文: {len(article['body_md'])} 字符")


def extract_reply_to_name(tiptap_body) -> str | None:
    """从 reply 的 tiptap_body 中提取被回复者的名字。

    Circle.so 在每条 reply 的正文开头插入一个 mention 节点，
    其 circle_ios_fallback_text 字段值为 "@被回复者"。
    提取该名字（去掉 @ 前缀）作为 "回复谁" 的信息来源。
    """
    if not tiptap_body:
        return None
    tb = json.loads(tiptap_body) if isinstance(tiptap_body, str) else tiptap_body
    body = tb.get("body", tb)
    for node in (body.get("content") or []):
        if node.get("type") == "paragraph":
            for child in (node.get("content") or []):
                if child.get("type") == "mention":
                    fallback = child.get("circle_ios_fallback_text", "")
                    if fallback.startswith("@"):
                        return fallback[1:]
            break  # 只看第一个 paragraph
    return None


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

                # 从 mention 节点提取被回复者名字（"谁对谁说"）
                reply_to_name = extract_reply_to_name(r.get("tiptap_body"))
                if reply_to_name:
                    reply_header = f"**↳ {ra} → {reply_to_name}** *{rt}*"
                else:
                    reply_header = f"**↳ {ra}** *{rt}*"

                lines += ["", reply_header, "", rb.strip()]

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
        # 有些 Circle embed 在 API 中没有 src/url，但 DOM 实际渲染成 iframe 视频。
        # 这时回退复用 iframe 列表，避免把正文开头的视频链接吞掉。
        if idx2[0] < len(iframe_srcs):
            src = iframe_srcs[idx2[0]]
            idx2[0] += 1
            yt = re.search(r"youtube\.com/embed/([^?]+)", src)
            if yt:
                src = f"https://www.youtube.com/watch?v={yt.group(1)}"
            return f"[视频]({src})"
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


def scrape_circle_article(url: str, output_dir: str) -> None:
    domain = extract_domain(url)

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
    if result.get("challenge_detected"):
        print("  ✗ 页面被 Cloudflare 人机验证拦截")
        print("  请先在浏览器中通过验证，或补充最新的 cf_clearance Cookie")
        sys.exit(1)

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
    post_oembed_links = list(result.get("post_oembed_links") or [])
    comment_oembed_links = list(result.get("comment_oembed_links") or [])

    body_md = parse_post_body(post_data)
    body_md = replace_media(
        body_md, result["img_srcs"], result["iframe_srcs"],
        oembed_links=list(post_oembed_links),
        post_id_map=post_id_map, domain=domain,
    )

    md = build_markdown(
        post_data, body_md, diag["comments"], url, domain,
        oembed_links=comment_oembed_links, post_id_map=post_id_map,
        comment_img_srcs=result.get("comment_img_srcs", []),
    )

    print(f"[4/4] 保存文件...")
    title = post_data.get("name", "untitled")
    published = (post_data.get("published_at") or post_data.get("created_at") or "")[:10]
    out_path = save_markdown(output_dir, title, published, md)
    top_level_comment_count = len(diag["comments"])
    reply_count = sum(len(c.get("replies") or []) for c in diag["comments"])
    total_comment_count = top_level_comment_count + reply_count

    print(f"  ✓ {out_path}")
    print(f"  标题: {title}")
    print(
        f"  正文: {len(body_md)} 字符, 评论: {total_comment_count} 条"
        f"（{top_level_comment_count} 条评论 + {reply_count} 条回复）"
    )


def main():
    parser = argparse.ArgumentParser(description="抓取社区帖子或微信公众号文章并保存为 Markdown")
    parser.add_argument("url", help="帖子 URL")
    parser.add_argument("--output-dir", help="输出目录")
    args = parser.parse_args()

    url = args.url
    site = detect_site(url)
    output_dir = os.path.abspath(args.output_dir or default_output_dir_for_site(site))

    if site == "wechat":
        scrape_wechat_article(url, output_dir)
        return

    scrape_circle_article(url, output_dir)


if __name__ == "__main__":
    main()
