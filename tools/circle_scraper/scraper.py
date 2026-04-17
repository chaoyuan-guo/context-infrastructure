"""Playwright 抓取 Circle.so SPA 页面，拦截 internal_api 响应。"""

import subprocess
import time
from urllib.parse import urlparse

from playwright.sync_api import sync_playwright


PROXY_CANDIDATES = [
    "http://127.0.0.1:7897",  # Surge / Clash Verge
    "http://127.0.0.1:7890",  # Clash
    "http://127.0.0.1:1087",  # ClashX
]


def detect_proxy(domain: str) -> str | None:
    """检测本地是否存在 Surge/Clash 等透明代理。

    判断逻辑：
    1. 用 socket 解析目标域名，如果 IP 在 198.18.0.0/16 则为 Surge 虚拟 IP
    2. 依次尝试常见代理端口，curl 能通就返回
    """
    import socket

    try:
        ip = socket.gethostbyname(domain)
        if not ip.startswith("198.18."):
            return None  # 没被劫持，直连即可
    except Exception:
        pass  # DNS 解析失败也尝试代理

    for proxy in PROXY_CANDIDATES:
        try:
            probe = subprocess.run(
                ["curl", "-x", proxy, "-I", "--max-time", "5",
                 f"https://{domain}"],
                capture_output=True, text=True, timeout=10,
            )
            if probe.returncode == 0:
                return proxy
        except Exception:
            continue
    return None


def _expand_all_comments(page) -> None:
    """反复点击 'Show more comments' 和 'Show more replies' 按钮，直到全部展开。

    Circle.so 评论区默认只加载 15 条评论，嵌套回复默认只显示 3 条。
    点击按钮会触发 internal_api 请求，on_response 回调会自动捕获。
    """
    max_rounds = 20  # 安全上限，防止无限循环
    for i in range(max_rounds):
        # 逐步滚动页面，触发可能的懒加载
        page.evaluate("""() => {
            const step = window.innerHeight;
            const max = document.body.scrollHeight;
            for (let y = 0; y <= max; y += step) {
                window.scrollTo(0, y);
            }
        }""")
        time.sleep(1)

        # 查找并点击所有 "Show more comments/replies" 按钮，返回点击数和文本
        result = page.evaluate("""() => {
            let count = 0;
            const clicked_texts = [];
            const allClickable = document.querySelectorAll('button, a, [role="button"]');
            for (const el of allClickable) {
                const text = (el.textContent || '').trim().toLowerCase();
                if ((text.includes('more comment') || text.includes('more repl') ||
                     text.includes('更多评论') || text.includes('更多回复')) &&
                    el.offsetParent !== null) {
                    el.scrollIntoView({block: 'center'});
                    el.click();
                    clicked_texts.push((el.textContent || '').trim().substring(0, 50));
                    count++;
                }
            }
            return {count, clicked_texts};
        }""")

        if result["count"] == 0:
            break

        print(f"  展开评论/回复 (round {i+1}, 点击 {result['count']} 个: {result['clicked_texts']})...")
        # 等待新的 API 响应返回并渲染
        try:
            page.wait_for_load_state("networkidle", timeout=10000)
        except Exception:
            pass
        time.sleep(2)

    print(f"  评论展开完成")


def fetch_page(url: str, cookies: list[dict] | None = None) -> dict:
    """用 Playwright 加载 Circle.so 页面，返回抓取结果。

    Returns:
        {
            "captured_api": {url: json_data, ...},
            "img_srcs": [str, ...],
            "iframe_srcs": [str, ...],
        }
    """
    captured_api = {}

    def on_response(res):
        if "internal_api" in res.url:
            try:
                ct = res.headers.get("content-type", "")
                if "json" in ct:
                    captured_api[res.url] = res.json()
            except Exception:
                pass

    domain = urlparse(url).netloc
    proxy = detect_proxy(domain)
    launch_kwargs = {"headless": True}
    if proxy:
        launch_kwargs["proxy"] = {"server": proxy}
        print(f"  检测到本地代理（Surge/Clash），使用 {proxy}")

    with sync_playwright() as p:
        browser = p.chromium.launch(**launch_kwargs)
        ctx = browser.new_context(ignore_https_errors=True)
        if cookies:
            ctx.add_cookies(cookies)
        page = ctx.new_page()
        page.on("response", on_response)

        print(f"  加载页面: {url}")
        page.goto(url, wait_until="networkidle", timeout=60000)
        time.sleep(3)

        # 展开所有评论和回复（点击 "Show more" 按钮直到没有更多）
        _expand_all_comments(page)

        # 从 DOM 获取帖子正文的图片和视频真实 URL
        img_srcs = page.eval_on_selector_all(
            "[data-testid='post-body'] img", "els => els.map(e => e.src)"
        )
        iframe_srcs = page.eval_on_selector_all(
            "[data-testid='post-body'] iframe", "els => els.map(e => e.src)"
        )

        # 评论区图片（按评论顺序）
        comment_img_srcs = page.eval_on_selector_all(
            "[data-testid='comment-body'] img", "els => els.map(e => e.src)"
        )

        # 评论区 oembed 链接预览卡片
        # Circle.so 渲染 embed 节点为 .node-embed 内的 <a> 标签
        comment_oembed_links = page.evaluate("""() => {
            const results = [];
            const embeds = document.querySelectorAll('.node-embed a[href]');
            for (const link of embeds) {
                // 取 img alt 作为标题（通常是 og:title），否则用 URL hostname
                const img = link.querySelector('img');
                let text = '';
                if (img && img.alt) {
                    text = img.alt;
                } else {
                    try { text = new URL(link.href).hostname; } catch(e) { text = link.href; }
                }
                results.push({ href: link.href, text: text });
            }
            return results;
        }""")

        browser.close()

    return {
        "captured_api": captured_api,
        "img_srcs": img_srcs,
        "iframe_srcs": iframe_srcs,
        "comment_img_srcs": comment_img_srcs,
        "comment_oembed_links": comment_oembed_links,
    }


def diagnose(captured_api: dict) -> dict:
    """诊断抓取结果，判断是否需要登录、是否拿到正文。

    Returns:
        {
            "has_post": bool,
            "has_tiptap": bool,
            "needs_login": bool,
            "post_data": dict | None,    # 帖子 API 数据
            "comments": list[dict],       # 评论列表
            "diagnosis": str,             # 人可读的诊断信息
        }
    """
    post_apis = [
        u for u in captured_api
        if "/posts/" in u and "post_details" not in u and "comments" not in u
    ]

    post_data = None
    has_tiptap = False
    for u in post_apis:
        d = captured_api[u]
        if isinstance(d, dict) and d.get("tiptap_body"):
            post_data = d
            has_tiptap = True
            break

    # 收集评论（多页去重）
    comments = []
    seen_ids = set()
    # 收集单独返回的 replies（来自 /comments/{id}/replies 端点）
    extra_replies = {}  # parent_comment_id → [reply, ...]

    for u, d in captured_api.items():
        # 子回复端点：/replies 或带 parent_comment_id 参数的 comments
        if "/replies" in u or "parent_comment_id" in u:
            items = d if isinstance(d, list) else d.get("comments", d.get("records", []))
            if isinstance(items, list):
                for item in items:
                    # parent_comment_id 可能在 item 字段里，也可能在 URL 参数里
                    parent_id = item.get("parent_comment_id") or item.get("reply_to_comment_id")
                    if not parent_id:
                        # 从 URL 中提取
                        from urllib.parse import urlparse, parse_qs
                        qs = parse_qs(urlparse(u).query)
                        parent_id = (qs.get("parent_comment_id") or [None])[0]
                        if parent_id:
                            parent_id = int(parent_id)
                    if parent_id:
                        extra_replies.setdefault(parent_id, []).append(item)
            continue

        if "comments" not in u:
            continue
        items = d if isinstance(d, list) else d.get("comments", d.get("records", []))
        if isinstance(items, list):
            for item in items:
                cid = item.get("id")
                if cid and cid not in seen_ids:
                    seen_ids.add(cid)
                    comments.append(item)
                elif cid and cid in seen_ids:
                    # 如果新版本有更多 replies，替换旧的
                    new_replies = item.get("replies") or []
                    for i, existing in enumerate(comments):
                        if existing.get("id") == cid:
                            old_replies = existing.get("replies") or []
                            if len(new_replies) > len(old_replies):
                                comments[i] = item
                            break

    # 合并额外 replies 到对应的评论
    for comment in comments:
        cid = comment.get("id")
        if cid in extra_replies:
            existing_replies = comment.get("replies") or []
            existing_reply_ids = {r.get("id") for r in existing_replies}
            for r in extra_replies[cid]:
                if r.get("id") not in existing_reply_ids:
                    existing_replies.append(r)
                    existing_reply_ids.add(r.get("id"))
            comment["replies"] = existing_replies

    # 判断是否需要登录
    needs_login = False
    diagnosis = ""

    if has_tiptap:
        diagnosis = "✓ 帖子正文已获取"
    elif not post_apis:
        needs_login = True
        diagnosis = "✗ 帖子详情 API 未触发，可能是私有 space，需要登录"
    else:
        # 有 post API 但没有 tiptap_body
        needs_login = True
        diagnosis = "✗ 帖子 API 返回但无正文，可能需要登录"

    # 额外检查 space 的 is_private
    for u, d in captured_api.items():
        if "/spaces/" in u and isinstance(d, dict) and d.get("is_private"):
            needs_login = True
            diagnosis += "（确认为私有 space）"
            break

    return {
        "has_post": bool(post_apis),
        "has_tiptap": has_tiptap,
        "needs_login": needs_login,
        "post_data": post_data,
        "comments": comments,
        "diagnosis": diagnosis,
        "post_id_map": _build_post_id_map(captured_api),
    }


def _build_post_id_map(captured_api: dict) -> dict[str, str]:
    """从 captured API 构建 post_id → URL 的映射。

    用于解析 entity 节点中的内部链接。扫描所有 space posts 列表 API，
    以及 post_details API，提取 id → slug + space_slug 的映射。
    """
    post_id_map = {}  # post_id (str) → full URL

    for url, data in captured_api.items():
        # space posts 列表 API 返回帖子数组
        if "/spaces/" in url and "/posts" in url and "posts/" not in url.split("/posts")[1]:
            posts = data if isinstance(data, list) else data.get("records", [])
            if not isinstance(posts, list):
                continue
            for p in posts:
                pid = str(p.get("id", ""))
                slug = p.get("slug", "")
                # 从 URL 中提取 space_id，然后从 space API 获取 space_slug
                if pid and slug:
                    post_id_map[pid] = slug

        # post_details API
        if "post_details" in url:
            details = data if isinstance(data, list) else data.get("records", [])
            if not isinstance(details, list):
                continue
            for p in details:
                pid = str(p.get("id", ""))
                slug = p.get("slug", "")
                if pid and slug:
                    post_id_map[pid] = slug

        # 单个帖子详情 API
        if "/posts/" in url and "post_details" not in url and "comments" not in url:
            if isinstance(data, dict):
                pid = str(data.get("id", ""))
                slug = data.get("slug", "")
                if pid and slug:
                    post_id_map[pid] = slug

    return post_id_map
