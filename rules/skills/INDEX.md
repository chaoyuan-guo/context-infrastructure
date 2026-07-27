# Skills Index

本索引指向可复用的 Skills（技能）—— AI 可以调用的工具、流程和最佳实践。

- **想使用某个能力** → 浏览下方分类，找到对应的 skill 文件
- **想添加新 skill** → 参考现有文件格式，添加到对应分类
- **想安装更多工具型能力** → 看 [`../../docs/SKILL_ECOSYSTEM.md`](../../docs/SKILL_ECOSYSTEM.md)，那里列出可单独安装的 public skill repo

## Multi-Agent 能力提示

当前环境支持后台 subagent。不要默认使用，但遇到大型、可并行、调研重、代码库探索重、需要独立交叉验证的任务时，应先读 [并行 Subagent 工作流](./workflow_parallel_subagents.md)。

快速判断：subagent 适合并行读、独立探索、反方审稿、事实核查和上下文窗口隔离；不适合单点小任务、强顺序依赖任务，以及多个 agent 同时写同一份状态或同一批文件。

---

## 分类索引

### API Guide（API 指南）

调用外部系统或工具的操作手册。

- [AI CLI Agent 实用指南](./ai_agent_cli_guide.md) — CLI Agent 设计原则、工具对比（Claude Code / Codex / OpenCode）、文件响应模式、AI 调用 AI

### Workflow（工作流）

特定任务的完整工作流程。

#### 从 upstream 同步

- [并行 Subagent 工作流](./workflow_parallel_subagents.md) ✅ — 并行执行多个独立 subagent 子任务
  - **必读**：初次使用并行 subagent 前，必须先读此 skill
  - **核心标准**：适合并行读、独立探索、交叉验证和上下文隔离；不适合强顺序依赖或共享状态写入
  - 判断标准：任务命中信息面宽、独立读任务、独立判断、高价值不确定性、主线程需保留整合能力中的至少 2 条
  - 核心参数：并行度 ≤5，调研 overlap 30-50%，代码 overlap 0-20%
- [Workflow Watchdog](./workflow_watchdog.md) — 派出 workflow/后台 agent 后设 ~30 分钟巡检，区分"真忙 vs 鬼打墙"，卡住就 kill 并用部分结果推进。触发词："watchdog"、"workflow 卡住"、"后台任务巡检"
- [深度调研工作流](./workflow_deep_research_survey.md) ✅ — 多 Agent 并行 + 交叉验证（Phase 1-3 信息采集）
- [科研论文调研与写作工作流](./workflow_research_paper_survey_writing.md) — 把科研论文转化为面向技术从业者的分析文章。核心：按读者重要性排序（不按论文章节）、三层分离（paper claim / 外部验证 / 我们的判断）、强制生态位分析（bottleneck / 替代路径 / stack 层级 / 相邻影响）。触发词："分析这篇论文"、"写论文解读"、"paper analysis"
- [外部写作工作流](./workflow_external_writing.md) ⚙️ — 将已核实的调研转化为 external-facing 中文分析文章；依赖 Antigravity 候选生成与分离冷读验收
- [内部写作工作流](./workflow_internal_writing.md) ✅ — 面向共享项目背景的协作者与 AI Agent，按问题、方案、决策建立低认知负担文档
- [认知画像提取工作流](./workflow_cognitive_profile_extraction.md) — 从非结构化对话数据提取可预测的认知公理
  - 适用：群聊/Slack/Discord/邮件/播客转录等任意对话数据
  - 流程：Round 驱动的迭代引擎（Discover / Verify / Finalize / Restructure），动态滚动
  - 含口号检测、R01 可信度虚高警告、候选重构等陷阱对策
- [语义搜索技能](./semantic_search.md) — 本地文本 embedding + cosine 相似度检索；通用实现同步自 [semantic-search-skill](https://github.com/grapeot/semantic-search-skill)，本地 overlay 保留 endpoint、模型和搜索路径
- [知识飞轮设计模式](./workflow_knowledge_flywheel.md) — 笨数据+笨方法+笨模型=精知识
- [项目脚手架与重整](./project_scaffold.md) ✅ — 把散装目录升级成标准项目结构：`docs/`、`src/`、`scripts/`、`tests/`、`AGENTS.md` 与独立 git
- [AI Session Search & Archive](./ai_session_search_archive.md) — 在 OpenCode、Claude Code、Codex、Antigravity 与 Second Mind 的统一 Markdown 归档中按来源检索；named entity 先走 lexical search，模糊记忆再走 semantic search

#### 本地自建 / 自用

- [Web Article Scraper](./workflow_web_article_scraper.md) ✅ — Circle.so 等社区帖子与微信公众号文章抓取，保存为 Markdown（含图片/链接/视频，Circle 路径含评论）
- [收藏文章精读工作流](./workflow_curated_article_reading.md) ✅ — 用 `x → f → f(x)` 精读用户明确指定的本地 Markdown 文章，结果直接回复当前会话，不另存文件
- [Agent Trace Sync Hygiene](./workflow_agent_trace_sync.md) — 增量同步 `contexts/agent_traces/` 时的低信息量 session 过滤与 prune 规则
- [自画像](./workflow_self_portrait.md) ✅ — 从自身 AI 会话历史提取多维度认知画像，每月一次。**区别于上面的"认知画像提取"（面向外部非结构化对话→公理），这个是面向自身→画像**

### BestPractice（最佳实践）

通用的最佳实践和经验教训。

- [外部中文 Prose 诊断词汇表](./bestpractice_external_prose.md) ✅ — 供 Main Agent 诊断教材声、认知负担与表演式口语，用于压缩成本题 voice contract
- [外部文章启发性分析视角（Thesis Catalog）](./reference_writing_thesis_catalog.md) ✅ — L1-L8 启发性分析视角及相关 axiom 映射
- [内部文档排版与视觉组件](./bestpractice_internal_visuals.md) ✅ — 内部 Memo/RFC/周报的自适应布局、暗色模式和视觉组件规范
- [AI 编程核心方法论](./bestpractice_ai_programming_mindset.md) ✅ — 70%问题、成功标准、可验证性
- [Skill 写作指南（Meta-Skill）](./bestpractice_skill_writing.md) ✅ — 创建或重写 skill 时使用，强调结果确定性、验收标准和边界条件
- [API Key 管理与调用](./bestpractice_api_key_management_1password_cli.md) ✅ — 使用 1Password CLI 安全管理密钥
- [面试评估框架](./bestpractice_interview_evaluation.md) ✅ — Trait > Skill、AI 作弊识别、技术深度探测
- [Markdown 转 HTML 最佳实践](./bestpractice_markdown_html_conversion.md) ✅
- [PDF 转 Markdown](./bestpractice_pdf_to_markdown.md) ✅ — 默认用 Docling，避免 PDF 场景下 MarkItDown / PyMuPDF4LLM / Marker 的质量或许可问题
- [时间敏感信息验证](./bestpractice_temporal_info_verification.md) ✅ — 验证可能超出 knowledge cutoff 的信息
- [分阶段工作法](./bestpractice_staged_approach.md) ✅ — 隔离-处理-验证闭环，破坏性操作前 Dry Run
- [GUI 自动化方法论](./bestpractice_gui_automation.md) ✅ — 把没有 API 的界面转化为可编程接口
- [AI 辅助调试诊断](./bestpractice_ai_debugging_diagnosis.md) ✅ — "代码改不好"的根因诊断决策树
- [AI 产品设计原则](./bestpractice_ai_product_design.md) ✅ — 线性聊天 vs 知识工作、感知规则解耦
- [产品/技术决策逆向工程](./bestpractice_product_decision_analysis.md) ✅ — 从设计空间、约束和 trade-off 分析产品或技术决策
- [Playwright E2E 测试方法论](https://github.com/grapeot/playwright-test-skill) 🔗 — CDP step-by-step debugging CLI + E2E methodology。独立 public repo，CLI: `pw-test`。触发词："Playwright E2E"、"CDP debugging"、"SSO login test"、"browser step debugging"

---

## 如何添加你自己的 Skill

创建或重写 skill 前，先读 [`bestpractice_skill_writing.md`](./bestpractice_skill_writing.md)。它说明如何用目标、验收标准、可用资源和输出规格定义一个 skill，而不是把 skill 写成机械步骤清单。

文件命名建议采用 `<category>_<name>.md`，例如 `workflow_my_process.md`、`bestpractice_my_insight.md`。写完后在本 INDEX 的对应分类下添加入口，确保后续 agent 能找到。

## Progressive Disclosure

Skills 采用渐进式披露原则：
- **INDEX.md** 提供概览，快速定位
- **具体 skill 文件** 包含完整的操作步骤和示例
