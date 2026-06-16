# Skill: Web Article Scraper (社区帖子 + 微信公众号)

## 1. 技能概览

`web_article_scraper` 是一个 CLI 工具，用于抓取 Circle.so 等 SPA 社区平台帖子，以及 `mp.weixin.qq.com` 这类微信公众号文章，并保存为 Markdown。所有确定性逻辑（页面抓取、API 拦截、HTML/tiptap → Markdown 转换、Cookie 管理、代理检测）已沉淀在 `tools/web_article_scraper/` 中。

### 1.1 何时使用

用户给出一个社区帖子 URL（典型触发词："抓取"、"保存文章"、"存成 markdown"），且目标页面是：
- Circle.so 社区帖子（`*.circle.so` 或自定义域名如 `www.superlinear.academy`）
- 微信公众号文章（`https://mp.weixin.qq.com/s/...`）
- 或其他 JS 动态渲染的社区页面（WebFetch / curl 拿不到正文的）

如果页面是静态 HTML，且只是一次性整理，直接用 WebFetch + 手动整理也可以。若你希望沉淀成可复用 CLI，并统一输出到 `contexts/curated_reads/`，优先用此工具。

### 1.2 触发建议

- `superlinear.academy`、`*.circle.so`、`mp.weixin.qq.com`：直接执行
- 不确定是否为动态页面：先用 WebFetch，拿不到正文再用此工具

---

## 2. 使用说明

### 2.1 核心命令

```bash
python tools/web_article_scraper/main.py <URL> [--output-dir <dir>] [--verify] [--json]
```

### 2.2 参数规范

- `<URL>`：必需。帖子完整 URL。
- `--output-dir`：可选。显式指定输出目录。
- `--verify`：可选。保存后检查输出文件是否存在、标题/来源/分隔线是否完整，失败时返回非 0 退出码。
- `--json`：可选。将抓取结果以 JSON 输出到 stdout，便于脚本或 agent 直接消费；进度日志会输出到 stderr。
- 默认输出目录按站点分流：
  - 微信公众号 → `contexts/curated_reads/wechat/`
  - Superlinear / Circle → `contexts/curated_reads/superlinear/`

### 2.3 前置依赖

```bash
pip install playwright beautifulsoup4
python3 -m playwright install chromium
```

---

## 3. 标准工作流

1. **执行抓取**：
   ```bash
   python tools/web_article_scraper/main.py "https://www.superlinear.academy/c/share-your-insights/ai-pattern" --verify --json
   ```

2. **观察输出**：
   - 默认会打印抓取进度并保存 Markdown 到对应站点目录
   - `--verify` 会额外校验输出文件结构
   - `--json` 会返回 `output_path`、`title`、`published`、`body_chars`、`total_comments`、`verified` 等结构化字段

3. **处理失败情况**：
   - 如果 Circle.so 路径报告"需要登录"，引导用户提供 Cookie（见 §4）
   - 如果公众号页面结构变动导致找不到 `#js_content`，需要更新解析规则
   - 如果网络超时，检查 VPN / 代理状态

---

## 4. Cookie 管理

Cookie 只用于 Circle.so 等需要登录的社区页面。微信公众号文章抓取不需要 Cookie。

Circle Cookie 存放在 `~/.config/circle-so/cookies.json`（权限 600），格式：

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
tools/web_article_scraper/
├── main.py       # CLI 入口：参数解析、流程编排、Markdown 组装
├── scraper.py    # Playwright 抓取 + API 拦截 + 代理检测 + 诊断
├── tiptap.py     # tiptap JSON → Markdown 确定性转换
└── cookies.py    # Cookie 加载与过期检查
```

确定性逻辑都在代码里，AI 侧直接执行命令即可。

---

**版本**: 2.1.0
**最后更新**: 2026-04-30
