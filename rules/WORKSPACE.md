# WORKSPACE.md - 目录路由速查

目标：让 AI 每轮 session 都能快速知道"去哪里找/放什么"。**找任何文件前先查这里。**

## 路由规则

### 项目与代码
- 一次性项目 / 临时脚本代码：`adhoc_jobs/<project>/`
- 工具脚本（邮件、语义搜索、分享报告等）：`tools/`
- 定时任务：`periodic_jobs/`
- 正式项目：`formal_projects/<project>/`
- 已归档正式项目：`formal_projects/archived/<project>/`

### 知识与记录
- 通用调研报告：`contexts/survey_sessions/`
- 思考 / 复盘 / 方法论：`contexts/thought_review/`
- 每日日志：`contexts/daily_records/`

### 系统与规则
- 可复用技术方案 / Skill：`rules/skills/`
- 核心公理（Axioms）：`rules/axioms/`
- 记忆系统：`contexts/memory/` + `periodic_jobs/ai_heartbeat/`

## 命名规则
- 目录和文件名：小写 + 下划线 (snake_case)
- 临时一次性项目：`tmp_<name>/`

## Python 环境
- 根目录 `.venv/` 为工作区级环境，用 `uv pip install` 管理依赖
- 临时工作且需要隔离时在 `adhoc_jobs/<project>/.venv/` 建独立环境
- 正式项目使用的环境以项目目录下文档中实际要求的为准

## 快速查询

正式项目路由补充：进入 `formal_projects/<project>/` 下的具体项目之前，先读该项目根 `AGENTS.md`。

<!-- 随着你的项目增长，在这里添加活跃项目的快捷路由 -->
<!-- 格式参考：- `project-name` → `adhoc_jobs/project_name/` (说明) -->
- `ontology-coding-agent` → `formal_projects/ontology-coding-agent/` (面向本体建模与文档解析的 agent 主项目)
- `tudou-digitaltwin` → `formal_projects/tudou-digitaltwin/` (土豆数字孪生的本体工程与业务系统)
- `interview` → `formal_projects/interview/` (近期面试准备材料)
- `curated_reads` → `formal_projects/curated_reads/` (值得收藏与精读的文章，原名 memo)
- `leetcode` → `formal_projects/leetcode/` (LeetCode 刷题数据与记录，原名 knowledge_data)

<!-- 归档项目（不再活跃维护） -->
- `cortex` → `formal_projects/archived/cortex/` (已归档；个人知识库系统，基于 OpenCode fork，AI agent 驱动的知识问答平台)
- `second_brain` → `formal_projects/archived/second_brain/` (已归档；第二大脑系统，FastAPI + Next.js)
