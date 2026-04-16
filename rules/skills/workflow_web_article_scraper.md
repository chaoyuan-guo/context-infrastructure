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
    page = browser.new_page()
    page.on("response", on_response)
    page.goto(URL, wait_until="networkidle", timeout=30000)
    time.sleep(3)
    # captured_api 现在包含所有 API 响应
```

### 阶段 3：从 API JSON 构建 Markdown（推荐路径）

**优先使用 `tiptap_body` JSON** 而非 HTML → Markdown 转换，因为 tiptap JSON 是结构化数据，能精确还原标题层级、加粗/斜体、列表等格式。

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
| 保存位置 | 当前工作目录，文件名用文章标题 | 用户偏好 |

## 踩坑记录

| 问题 | 现象 | 解决方案 |
|------|------|----------|
| TLS 握手失败 | `SSL_ERROR_SYSCALL`，IP 是 `198.18.x.x` | 本地代理拦截，Playwright 用自己的网络栈可绕过 |
| 正文是空的 | curl 返回 JS 骨架 | Circle.so 是 React SPA，必须用 headless browser 渲染 |
| 内部链接无 href | entity 用 React state 管理 URL | 从 sgid Base64 解码拿 post ID，再查 space 列表匹配 slug |
| 部分 entity 找不到 | 帖子在私有 space | 降级为加粗文本，备注"需登录" |
| 评论没有加载 | DOM 未滚动到评论区 | 页面加载后等待 3-5 秒，Circle 通常会自动加载评论 |
| markdownify 丢格式 | HTML 中有 React 容器 div | 用 tiptap JSON 直接递归转换，绕过 HTML |

## 适用范围与局限

- **适用**：Circle.so 公开帖子（无需登录即可查看的内容）
- **部分适用**：需要登录的帖子（正文可能抓到，内部链接可能不全）
- **不适用**：纯静态博客（用 curl + markdownify 更简单）、需要登录才能看到的完全私有内容
- **可扩展**：其他 TipTap 编辑器的 SPA 平台理论上可复用 tiptap → markdown 的转换逻辑
