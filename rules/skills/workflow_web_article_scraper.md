# Skill: Web Article Scraper (Circle.so 社区帖子抓取)

## 1. 技能概览

`circle_scraper` 是一个 CLI 工具，用于抓取 Circle.so 等 SPA 社区平台的帖子，保存为 Markdown。所有确定性逻辑（页面抓取、API 拦截、tiptap → Markdown 转换、Cookie 管理、代理检测）已沉淀在 `tools/circle_scraper/` 中。

### 1.1 何时使用

用户给出一个社区帖子 URL（典型触发词："抓取"、"保存文章"、"存成 markdown"），且目标页面是：
- Circle.so 社区帖子（`*.circle.so` 或自定义域名如 `www.superlinear.academy`）
- 或其他 JS 动态渲染的社区页面（WebFetch / curl 拿不到正文的）

如果页面是静态 HTML（WebFetch 直接能拿到正文），直接用 WebFetch + 手动整理即可，无需此工具。

### 1.2 触发建议

**直接执行**（不需要额外判断）：
- 用户给出 `superlinear.academy` 或 `*.circle.so` 的帖子链接
- 用户说"抓取这篇文章"并给出 SPA 社区 URL

**先验证再决定**：
- 不确定是否为 SPA → 先用 WebFetch 试一下，拿不到正文再用此工具

---

## 2. 使用说明

### 2.1 核心命令

```bash
python tools/circle_scraper/main.py <URL> [--output-dir <dir>]
```

### 2.2 参数规范

- `<URL>`：必需。帖子完整 URL。
- `--output-dir`：可选。输出目录，默认为 `formal_projects/curated_reads/`。

### 2.3 前置依赖

```bash
pip install playwright beautifulsoup4
python3 -m playwright install chromium
```

---

## 3. 标准工作流

1. **执行抓取**：
   ```bash
   python tools/circle_scraper/main.py "https://www.superlinear.academy/c/share-your-insights/ai-pattern"
   ```

2. **观察输出**：脚本会自动完成以下步骤并打印进度：
   - 加载 Cookie（从 `~/.config/circle-so/cookies.json`）
   - 检测本地代理（Surge/Clash 虚拟 IP）并自动使用
   - Playwright 加载页面 + 拦截 API
   - 诊断是否拿到正文（需不需要登录）
   - tiptap JSON → Markdown 转换
   - 替换图片/视频占位符为真实 URL
   - 解析评论区（含嵌套回复）
   - 保存到 `formal_projects/curated_reads/<标题>.md`

3. **处理失败情况**：
   - 如果脚本报告"需要登录"，引导用户提供 Cookie（见 §4）
   - 如果网络超时，检查 VPN / 代理状态

---

## 4. Cookie 管理

Cookie 存放在 `~/.config/circle-so/cookies.json`（权限 600），格式：

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

**首次获取或 Cookie 过期时**，引导用户：
1. 在浏览器中打开目标帖子（确保已登录）
2. F12 → Application → Cookies
3. 复制 `user_session_identifier` 和 `remember_user_token` 的值
4. 两个都要，缺一不可

脚本会自动检查过期时间，30 天内到期时发出警告。

---

## 5. 工具架构

```
tools/circle_scraper/
├── main.py       # CLI 入口：参数解析、流程编排、Markdown 组装
├── scraper.py    # Playwright 抓取 + API 拦截 + 代理检测 + 诊断
├── tiptap.py     # tiptap JSON → Markdown 确定性转换
└── cookies.py    # Cookie 加载与过期检查
```

所有确定性逻辑（代理检测、登录诊断、tiptap 转换、Cookie 管理）在代码中处理，**AI 只需要执行命令并处理异常输出**。

---

**版本**: 2.0.0
**最后更新**: 2026-04-17
