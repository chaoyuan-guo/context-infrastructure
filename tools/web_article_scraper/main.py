#!/usr/bin/env python3
"""Web Article Scraper: 社区帖子与公众号文章抓取工具。

用法:
    python tools/web_article_scraper/main.py <URL> [--output-dir <dir>] [--verify] [--json]

示例:
    python tools/web_article_scraper/main.py https://www.superlinear.academy/c/share-your-insights/ai-pattern --verify --json
    python tools/web_article_scraper/main.py https://www.superlinear.academy/c/share-your-insights/ai-pattern --output-dir ./output
    python tools/web_article_scraper/main.py https://mp.weixin.qq.com/s/d1aBQMx-JwLh4H8xlyV0OA --verify
"""

import argparse
import contextlib
import json
import os
import re
import sys
from http.client import IncompleteRead
from datetime import datetime, timedelta, timezone
from urllib.request import Request, urlopen

sys.path.append(os.path.dirname(__file__))

from cookies import load_cookies
from scraper import fetch_page, diagnose
from tiptap import (
    BeautifulSoup,
    decode_entity_fallback_text,
    extract_entity_post_ids,
    parse_post_body,
    parse_tiptap_body,
    parse_trix_body,
)

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
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(markdown)
    return out_path


def verify_output_file(out_path: str, title: str, url: str, body_chars: int) -> list[str]:
    errors = []

    if not os.path.exists(out_path):
        return [f"输出文件不存在: {out_path}"]

    if body_chars <= 0:
        errors.append("正文长度为 0")

    with open(out_path, encoding="utf-8") as f:
        content = f.read()

    expected_header = f"# {title}"
    if expected_header not in content:
        errors.append("文件中缺少标题头")

    expected_source = f"> 来源：<{url}>"
    if expected_source not in content:
        errors.append("文件中缺少来源链接")

    if "---" not in content:
        errors.append("文件中缺少元数据分隔线")

    for text, href in re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content):
        if not text.strip():
            errors.append("存在链接文本为空的 Markdown 链接")
            break
        if not href.strip():
            errors.append("存在链接 URL 为空的 Markdown 链接")
            break

    return errors


def build_result(
    *,
    site: str,
    url: str,
    title: str,
    author: str,
    platform: str,
    published: str,
    output_path: str,
    body_chars: int,
    top_level_comments: int = 0,
    reply_count: int = 0,
) -> dict:
    return {
        "site": site,
        "url": url,
        "title": title,
        "author": author,
        "platform": platform,
        "published": published,
        "output_path": output_path,
        "body_chars": body_chars,
        "top_level_comments": top_level_comments,
        "reply_count": reply_count,
        "total_comments": top_level_comments + reply_count,
        "verified": None,
        "verification_errors": [],
    }


def fetch_space_posts_map(domain: str, space_info: dict, cookies: list[dict] | None, post_ids: set[str]) -> dict[str, dict]:
    if not space_info or not post_ids:
        return {}

    headers = {
        "User-Agent": WECHAT_USER_AGENT,
        "Accept": "application/json, text/plain, */*",
    }
    if cookies:
        headers["Cookie"] = "; ".join(
            f"{cookie['name']}={cookie['value']}" for cookie in cookies if cookie.get("name")
        )

    space_id = space_info.get("id")
    target_ids = set(post_ids)
    post_map = {}
    page = 1
    per_page = 100

    while target_ids:
        req = Request(
            f"https://{domain}/internal_api/spaces/{space_id}/posts?page={page}&per_page={per_page}",
            headers=headers,
        )
        with urlopen(req, timeout=60) as resp:
            data = json.load(resp)

        records = data.get("records", []) if isinstance(data, dict) else data
        if not isinstance(records, list) or not records:
            break

        for post in records:
            pid = str(post.get("id", ""))
            slug = post.get("slug", "")
            if pid and slug and pid in target_ids:
                post_map[pid] = {
                    "slug": slug,
                    "space_slug": post.get("space_slug") or space_info.get("slug", ""),
                    "name": post.get("name", ""),
                }
                target_ids.discard(pid)

        if not data.get("has_next_page"):
            break
        page += 1

    return post_map


def escape_markdown_link_text(text: str) -> str:
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


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
        try:
            html_bytes = resp.read()
        except IncompleteRead as exc:
            # WeChat occasionally closes large responses early. The partial body
            # still contains the article HTML in practice, so keep parsing.
            html_bytes = exc.partial
        html_text = html_bytes.decode("utf-8", "replace")

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


def scrape_wechat_article(url: str, output_dir: str) -> dict:
    print("[1/3] 获取微信公众号文章 HTML...")
    article = parse_wechat_article(url)

    print("[2/3] 解析正文...")
    md = build_wechat_markdown(article, url)

    print("[3/3] 保存文件...")
    out_path = save_markdown(output_dir, article["title"], article["published"], md)
    print(f"  ✓ {out_path}")
    print(f"  标题: {article['title']}")
    print(f"  正文: {len(article['body_md'])} 字符")

    return build_result(
        site="wechat",
        url=url,
        title=article["title"],
        author=article["author"],
        platform="微信公众号",
        published=article["published"],
        output_path=out_path,
        body_chars=len(article["body_md"]),
    )


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


def hydrate_entity_fallbacks(raw, entity_texts: list[str] | None):
    if not raw:
        return raw

    tb = json.loads(raw) if isinstance(raw, str) else raw
    queue = list(entity_texts or [])

    def visit(node):
        if not isinstance(node, dict):
            return
        if node.get("type") == "entity":
            text = queue.pop(0).strip() if queue else ""
            attrs = node.setdefault("attrs", {})
            fallback = attrs.get("circle_ios_fallback_text") or node.get("circle_ios_fallback_text")
            if (not fallback or fallback == "内部链接") and text:
                attrs["circle_ios_fallback_text"] = text
                node["circle_ios_fallback_text"] = text
        for child in node.get("content") or []:
            visit(child)

    visit(tb.get("body", tb))
    return tb


def hydrate_discussion_entities(comments: list[dict], entity_texts: list[str] | None) -> list[dict]:
    queue = list(entity_texts or [])
    hydrated_comments = []

    for comment in comments:
        hydrated_comment = dict(comment)
        if hydrated_comment.get("tiptap_body"):
            hydrated_comment["tiptap_body"] = hydrate_entity_fallbacks(
                hydrated_comment.get("tiptap_body"), queue
            )

        hydrated_replies = []
        for reply in hydrated_comment.get("replies") or []:
            hydrated_reply = dict(reply)
            if hydrated_reply.get("tiptap_body"):
                hydrated_reply["tiptap_body"] = hydrate_entity_fallbacks(
                    hydrated_reply.get("tiptap_body"), queue
                )
            hydrated_replies.append(hydrated_reply)

        hydrated_comment["replies"] = hydrated_replies
        hydrated_comments.append(hydrated_comment)

    return hydrated_comments


def build_markdown(post_data: dict, body_md: str, comments: list, url: str, domain: str,
                   oembed_links: list | None = None, post_id_map: dict | None = None,
                   comment_img_srcs: list | None = None) -> str:
    """组装最终 Markdown 文件。"""
    title = post_data.get("name", "untitled")
    author = (post_data.get("community_member") or {}).get("name", "unknown")
    published = (post_data.get("published_at") or post_data.get("created_at") or "")[:10]

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
        fallback_text = decode_entity_fallback_text(m.group(2)) or "内部链接"
        post_info = post_id_map.get(post_id) or {}
        if isinstance(post_info, str):
            post_info = {"slug": post_info}
        text = escape_markdown_link_text(post_info.get("name") or fallback_text)
        slug = post_info.get("slug")
        space_slug = post_info.get("space_slug")
        if slug and space_slug and domain:
            url = f"https://{domain}/c/{space_slug}/{slug}"
            return f"[{text}]({url})"
        # 没找到，保留为加粗文本
        return f"**{text}**"
    body_md = re.sub(r"\[ENTITY:(\d+):([A-Za-z0-9_-]*)\]", rep_entity, body_md)

    # Clean up empty bold markers left by standalone styled spaces around entity nodes.
    body_md = body_md.replace("** **", "").replace("****", "")

    return body_md


def scrape_circle_article(url: str, output_dir: str) -> dict:
    domain = extract_domain(url)

    print("[1/4] 加载 Cookie...")
    cookies, err = load_cookies(domain)
    if err:
        print(f"  ⚠️  {err}")
        print("  将尝试无 Cookie 抓取（公开帖子可能可行）")

    print("[2/4] 抓取页面...")
    result = fetch_page(url, cookies)
    captured_api = result["captured_api"]
    print(f"  拦截到 {len(captured_api)} 个 API 响应")

    print("[3/4] 诊断与解析...")
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

    entity_post_ids = set()
    entity_post_ids.update(extract_entity_post_ids(post_data.get("tiptap_body")))
    for comment in diag["comments"]:
        entity_post_ids.update(extract_entity_post_ids(comment.get("tiptap_body")))
        for reply in comment.get("replies") or []:
            entity_post_ids.update(extract_entity_post_ids(reply.get("tiptap_body")))

    space_post_map = fetch_space_posts_map(
        domain, diag.get("space_info"), cookies, entity_post_ids
    )
    post_id_map = {**post_id_map, **space_post_map}

    post_data = dict(post_data)
    if post_data.get("tiptap_body"):
        post_data["tiptap_body"] = hydrate_entity_fallbacks(
            post_data.get("tiptap_body"), result.get("post_entity_texts")
        )

    hydrated_comments = hydrate_discussion_entities(
        diag["comments"], result.get("comment_entity_texts")
    )

    body_md = parse_post_body(post_data)
    body_md = replace_media(
        body_md, result["img_srcs"], result["iframe_srcs"],
        oembed_links=list(post_oembed_links),
        post_id_map=post_id_map, domain=domain,
    )

    md = build_markdown(
        post_data, body_md, hydrated_comments, url, domain,
        oembed_links=comment_oembed_links, post_id_map=post_id_map,
        comment_img_srcs=result.get("comment_img_srcs", []),
    )

    print("[4/4] 保存文件...")
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

    return build_result(
        site="circle",
        url=url,
        title=title,
        author=(post_data.get("community_member") or {}).get("name", "unknown"),
        platform="Superlinear Academy",
        published=published,
        output_path=out_path,
        body_chars=len(body_md),
        top_level_comments=top_level_comment_count,
        reply_count=reply_count,
    )


def main():
    parser = argparse.ArgumentParser(description="抓取社区帖子或微信公众号文章并保存为 Markdown")
    parser.add_argument("url", help="帖子 URL")
    parser.add_argument("--output-dir", help="输出目录")
    parser.add_argument("--json", action="store_true", help="将最终结果以 JSON 输出到 stdout")
    parser.add_argument("--verify", action="store_true", help="保存后校验输出文件完整性")
    args = parser.parse_args()

    url = args.url
    site = detect_site(url)
    output_dir = os.path.abspath(args.output_dir or default_output_dir_for_site(site))

    scrape_fn = scrape_wechat_article if site == "wechat" else scrape_circle_article
    if args.json:
        with contextlib.redirect_stdout(sys.stderr):
            result = scrape_fn(url, output_dir)
    else:
        result = scrape_fn(url, output_dir)

    verification_errors = []
    if args.verify:
        verification_errors = verify_output_file(
            result["output_path"], result["title"], result["url"], result["body_chars"]
        )
        result["verified"] = not verification_errors
        result["verification_errors"] = verification_errors
        if args.json:
            pass
        elif verification_errors:
            print("  校验: 失败")
            for error in verification_errors:
                print(f"    - {error}")
        else:
            print("  校验: 通过")

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))

    if verification_errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
