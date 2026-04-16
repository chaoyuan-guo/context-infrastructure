# Skill: Web Article Scraper (Circle.so / SPA 社区帖子抓取)

## 元数据
- 类型: Workflow
- 适用场景: 从 Circle.so 等 SPA 社区平台抓取文章正文、内部链接、图片、视频嵌入和评论区，保存为 Markdown
- 创建日期: 2026-04-16
- 依赖: Python 3, playwright, markdownify, beautifulsoup4

## When to Use

用户给出一个社区帖子 URL（典型触发词："抓取"、"保存文章"、"存成 markdown"），且目标页面是：
- Circle.so 社区帖子（`*.circle.so` 或自定义域名，HTML 中含 `window.RAILS_ENV`）
- 或其他 JS 动态渲染的社区/博客页面（非静态 HTML）

如果页面是静态 HTML（curl 就能拿到正文），直接用 WebFetch/curl + markdownify 即可，无需此 skill。

## Prerequisites

```bash
pip install playwright markdownify beautifulsoup4
python3 -m playwright install chromium
```

## 核心流程

### 阶段 1：判断页面类型

先用 curl 或 WebFetch 尝试抓取。如果拿到完整正文 → 直接转 markdown，跳过后续步骤。

如果返回的是空 body / JS SPA 骨架 → 进入阶段 2。

### 阶段 2：Playwright 抓取页面 + 拦截 API

用 Playwright headless Chromium 加载页面，同时 **拦截所有 `internal_api` 响应**。Circle.so 的关键 API：

| API 路径 | 内容 |
|----------|------|
| `/internal_api/spaces/{id}/posts/{slug}` | 帖子元数据 + `tiptap_body` 完整结构化正文 |
| `/internal_api/posts/{id}/comments` | 评论列表（分页） |
| `/internal_api/post_details?post_ids=...` | 帖子摘要信息 |

**核心代码模式：**

```python
from playwright.sync_api import sync_playwright
import json, time

captured_api = {}

def on_response(res):
    if 'internal_api' in res.url:
        try:
            ct = res.headers.get('content-type', '')
            if 'json' in ct:
                captured_api[res.url] = res.json()
        except:
            pass

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # 如果有 Cookie，在创建 context 时注入（见阶段 2.1）
    ctx = browser.new_context(ignore_https_errors=True)
    page = ctx.new_page()
    page.on("response", on_response)
    page.goto(URL, wait_until="networkidle", timeout=60000)
    time.sleep(5)
    # captured_api 现在包含所有 API 响应
```

### 阶段 2.1：诊断是否需要登录

抓取完成后，**立即检查是否拿到了帖子详情 API**：

```python
post_api = [u for u in captured_api if '/posts/' in u and 'post_details' not in u]
has_tiptap = any('tiptap_body' in json.dumps(captured_api[u]) for u in post_api)
```

**判断逻辑：**

| 信号 | 含义 | 下一步 |
|------|------|--------|
| `has_tiptap == True` | 帖子 API 已返回正文 | 继续阶段 3 |
| `post_api` 为空 | 帖子详情 API 未被触发 | 很可能是私有 space，需要登录 |
| space API 中 `is_private: true` | 确认为私有 space | 需要登录 |
| 页面文本不含帖子标题，而是显示首页/营销页内容 | 被重定向了 | 需要登录 |

**需要登录时，向用户索取 Cookie：**

引导用户在浏览器中操作：
1. 打开目标帖子页面（确保已登录且能看到内容）
2. F12 → Network 面板 → 随便点一个请求 → 复制请求头中的 `Cookie` 字段值
3. 或者：F12 → Application → Cookies → 复制 `user_session_identifier` 和 `remember_user_token` 的值

**Cookie 存储与读取：**

Cookie 存放在 `~/.config/circle-so/cookies.json`（权限 600），格式如下：

```json
{
  "domain": "www.superlinear.academy",
  "cookies": {
    "user_session_identifier": "<值>",
    "remember_user_token": "<值>"
  },
  "expires_at": "2027-03-07",
  "notes": "..."
}
```

**读取 Cookie 并检查过期的代码：**

```python
import json, os
from datetime import datetime, timezone

def load_circle_cookies():
    """从本地配置文件读取 Circle.so Cookie，并检查过期时间。"""
    path = os.path.expanduser("~/.config/circle-so/cookies.json")
    if not os.path.exists(path):
        return None, "Cookie 文件不存在，需要用户提供 Cookie"
    
    with open(path) as f:
        data = json.load(f)
    
    # 检查过期时间
    expires_at = data.get("expires_at", "")
    if expires_at:
        exp_date = datetime.strptime(expires_at, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        now = datetime.now(timezone.utc)
        remaining = (exp_date - now).days
        if remaining <= 0:
            return None, f"⚠️ Cookie 已过期（{expires_at}），请用户重新提供"
        elif remaining <= 30:
            print(f"⚠️ Cookie 将在 {remaining} 天后过期（{expires_at}），建议尽快更新")
    
    domain = data.get("domain", "")
    cookies = []
    for name, value in data.get("cookies", {}).items():
        cookies.append({"name": name, "value": value, "domain": domain, "path": "/"})
    
    return cookies, None

# 使用
cookies, error = load_circle_cookies()
if error:
    print(error)  # 向用户索取新 Cookie
else:
    ctx = browser.new_context(ignore_https_errors=True)
    ctx.add_cookies(cookies)
```

**首次获取 Cookie 时**，引导用户在浏览器中操作：
1. 打开目标帖子页面（确保已登录且能看到内容）
2. F12 → Network 面板 → 随便点一个请求 → 复制请求头中的 `Cookie` 字段值
3. 或者：F12 → Application → Cookies → 复制 `user_session_identifier` 和 `remember_user_token` 的值

获取后保存到 `~/.config/circle-so/cookies.json`，权限设为 600。

**注意**：两个 Cookie 都必须提供，缺一不可。`remember_user_token` 单独使用无法通过认证。

拿到 Cookie 后重新执行阶段 2。

> 未来安装 1Password CLI 后，建议迁移到 `op://dev/circle-so-cookies/` 管理，与其他 API Key 保持一致。

### 阶段 3：从 API JSON 构建 Markdown（推荐路径）

**优先使用 `tiptap_body` JSON** 而非 HTML → Markdown 转换，因为 tiptap JSON 是结构化数据，能精确还原标题层级、加粗/斜体、列表等格式。

**注意 `tiptap_body` 的数据结构**：API 返回的 `tiptap_body` 可能是字符串（需 `json.loads`），且实际 doc 结构嵌套在 `.body` 字段内：

```python
tiptap = json.loads(data['tiptap_body']) if isinstance(data['tiptap_body'], str) else data['tiptap_body']
body = tiptap.get('body', tiptap)  # 实际 doc 在 .body 下
```

**帖子元数据字段映射：**

| 需要的信息 | 字段路径 | 备注 |
|-----------|---------|------|
| 标题 | `name` | |
| 作者 | `community_member.name` | 不是 `user_name`（该字段通常为 null） |
| 发布日期 | `published_at` 或 `created_at` | ISO 8601 格式，取前 10 位即日期 |
| slug | `slug` | 用于拼接原始 URL |

**tiptap 节点类型映射：**

| tiptap type | Markdown |
|-------------|----------|
| `paragraph` | 段落文本 + `\n\n` |
| `heading` (level=N) | `#` × N + 文本 |
| `bulletList` > `listItem` | `- 文本` |
| `orderedList` > `listItem` | `1. 文本` |
| `blockquote` | `> 文本` |
| `horizontalRule` | `---` |
| `hardBreak` | `\n` |
| `text` with marks | `**bold**`, `*italic*`, `` `code` ``, `[text](href)` |

**特殊节点处理：**

| tiptap type | 处理方式 |
|-------------|----------|
| `entity` | Circle.so 内部帖子链接。`attrs.sgid` 需 Base64 解码提取 post ID，`circle_ios_fallback_text` 是显示文本 |
| `image` | `attrs.signed_id` 是 Circle 内部图片 ID，真实 URL 需从渲染后的 DOM 中 `<img src>` 获取 |
| `embed` | 视频嵌入。真实 URL 需从渲染后的 `<iframe src>` 获取 |

### 阶段 4：解析内部链接（Entity）

Entity 节点只有 `sgid`，不包含 URL。解析步骤：

1. **Base64 解码 sgid** → 提取 `Posts::Basic/{post_id}`

```python
import base64, re
decoded = base64.b64decode(sgid + '==', altchars=b'-_').decode('latin-1', errors='replace')
post_id = re.search(r'Posts::Basic/(\d+)', decoded).group(1)
```

2. **遍历 space 的帖子列表** 匹配 post_id → slug

```python
# 先从当前 space 查找，再扩展到其他公开 space
url = f"https://{domain}/internal_api/spaces/{space_id}/posts?page={pg}&per_page=50"
```

3. **拼接 URL**：`https://{domain}/c/{space_slug}/{post_slug}`

4. 如果在所有公开 space 都找不到 → 帖子在私有 space，降级为 `**加粗文本**`（不可链接）

### 阶段 5：提取图片和视频

- **图片**：从渲染后 DOM 中 `[data-testid='post-body'] img` 获取 `src`，按出现顺序与 tiptap 的 `image` 节点一一对应
- **视频嵌入**：从 `[data-testid='post-body'] iframe` 获取 `src`，YouTube embed URL 转为 watch URL

### 阶段 6：提取评论区

从 API 响应 `/internal_api/posts/{id}/comments` 获取评论列表。如果 API 未捕获，从渲染后 DOM 提取：

1. 找到所有 `[data-testid="comment-body"]` 元素
2. 向上遍历 DOM 树，解析上下文文本提取作者名（格式通常为 `初始字母 | 用户名 | 时间戳 | 评论正文 | 操作按钮`）
3. 跳过单字母（头像首字母）、时间戳、操作按钮等噪声

### 阶段 7：组装 Markdown 文件

```markdown
# {标题}

> 来源：<{原始URL}>
> 作者：{作者名}
> 发布日期：{YYYY-MM-DD}
> 平台：{平台名}

---

{正文（含图片、链接、视频）}

---

## 评论区

### {评论者1}
*{时间}*

{评论内容}

### {评论者2}
...
```

## 关键决策

| 决策点 | 选择 | 原因 |
|--------|------|------|
| 正文来源 | tiptap JSON > HTML 转换 | 结构更精确，不丢失语义 |
| 图片 URL | 从渲染后 DOM 获取 | tiptap JSON 中 URL 通常为 null |
| 内部链接 | Base64 解码 sgid + 遍历 space 匹配 | 无登录态无法调 entity 解析 API |
| 评论作者 | DOM 上下文文本解析 | 评论 API 可能有、可能没有 |
| 保存位置 | `formal_projects/curated_reads/`，文件名用文章标题 | 用户偏好 |

## 踩坑记录

| 问题 | 现象 | 解决方案 |
|------|------|----------|
| TLS 握手失败 | `SSL_ERROR_SYSCALL`，IP 是 `198.18.x.x` | 本地代理拦截，Playwright 加 `ignore_https_errors=True` 可绕过 |
| 正文是空的 | curl 返回 JS 骨架 | Circle.so 是 React SPA，必须用 headless browser 渲染 |
| 私有 space 无帖子 API | 无登录态时帖子详情 API 不触发，页面渲染为首页/营销页 | 检查 captured API 是否包含帖子详情 + space 的 `is_private` 字段，确认后向用户索取 Cookie（见阶段 2.1） |
| 多轮试错才确认需登录 | 第一轮 body 为空，第二轮检查 API 才发现是私有 space | 阶段 2 完成后立即执行诊断（阶段 2.1），不要先尝试解析空数据 |
| `tiptap_body` 多嵌套一层 | 直接解析报错或取不到内容 | 实际结构是 `{"body": {"type": "doc", ...}}`，需要 `tiptap.get('body', tiptap)`；**评论的 `tiptap_body` 结构与帖子完全相同**，同样需要取 `.body` |
| 作者字段为 null | `user_name` 字段为空 | 作者信息在 `community_member.name`，不在 `user_name` |
| 内部链接无 href | entity 用 React state 管理 URL | 从 sgid Base64 解码拿 post ID，再查 space 列表匹配 slug |
| 部分 entity 找不到 | 帖子在私有 space | 降级为加粗文本，备注"需登录" |
| 评论没有加载 | DOM 未滚动到评论区 | 页面加载后等待 3-5 秒，Circle 通常会自动加载评论 |
| 嵌套回复（replies）丢失 | 评论列表只有顶层，子回复消失 | 回复不会单独触发 API，嵌套在顶层评论对象的 `replies` 字段中；处理评论时需递归遍历 `comment.get('replies', [])` |
| markdownify 丢格式 | HTML 中有 React 容器 div | 用 tiptap JSON 直接递归转换，绕过 HTML |

## 适用范围与局限

- **适用**：Circle.so 公开帖子（无需登录即可查看的内容）
- **适用（需 Cookie）**：私有 space 的帖子——向用户索取 `user_session_identifier` + `remember_user_token` Cookie 后注入 Playwright context 即可正常抓取
- **不适用**：纯静态博客（用 curl + markdownify 更简单）
- **可扩展**：其他 TipTap 编辑器的 SPA 平台理论上可复用 tiptap → markdown 的转换逻辑
