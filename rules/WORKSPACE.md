# WORKSPACE.md - 目录路由速查

目标：让 AI 每轮 session 都能快速知道"去哪里找/放什么"。**找任何文件前先查这里。**

## 路由规则

### 项目与代码
- 一次性项目 / 临时脚本代码：`adhoc_jobs/<project>/`
- 工具脚本（邮件、语义搜索、分享报告、力扣导出等）：`tools/`
- 定时任务：`periodic_jobs/`
- 正式项目：`formal_projects/<project>/`
- 已归档正式项目：`formal_projects/archived/<project>/`

### 知识与记录
- 通用调研报告：`contexts/survey_sessions/`
- 收藏与精读文章：`contexts/curated_reads/`
- 思考 / 复盘 / 方法论：`contexts/thought_review/`
- 每日日志：`contexts/daily_records/`
- 多平台 AI 会话统一原始归档：`contexts/ai_sessions/`
- 经过本地 Hygiene 过滤的 OpenCode 对话轨迹：`contexts/agent_traces/`

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
<!-- 格式参考：- `project-name` → `formal_projects/project_name/` (说明) -->
- `career-dev` → `formal_projects/career-dev/` (职业发展学习材料)
- `colaos` → `formal_projects/colaos/` (ColaOS 调研、产品反馈、评测与面试材料)
- `interview` → `formal_projects/interview/` (近期面试准备材料)
- `mem0` → `formal_projects/mem0/` (面向 AI Agent 与助手的持久化记忆层)
- `memos` → `formal_projects/memos/` (面向 LLM Agent 的记忆操作系统)
- `hindsight` → `formal_projects/hindsight/` (具备 retain、recall 与 reflect 的 AI Agent 长期记忆系统)

<!-- 归档项目（不再活跃维护） -->
- `daily-briefing-agent` → `formal_projects/archived/daily-briefing-agent/` (已归档；两阶段每日语音简报生成器)
- `deputy-agent` → `formal_projects/archived/deputy-agent/` (已归档；自监督 master-worker agent 框架)
- `hermes-agent` → `formal_projects/archived/hermes-agent/` (已归档；具备跨会话记忆与技能学习闭环的个人 AI agent)
- `letta-code` → `formal_projects/archived/letta-code/` (已归档；Letta 的有状态自主编程 agent)
- `memu` → `formal_projects/archived/memu/` (已归档；面向 AI Agent 的 embedding-only 记忆框架)
- `ontology-coding-agent` → `formal_projects/archived/ontology-coding-agent/` (已归档；面向本体建模与文档解析的 agent 项目)
- `openviking` → `formal_projects/archived/openviking/` (已归档；OpenViking 开源贡献与研发)
- `podinsight_mvp` → `formal_projects/archived/podinsight_mvp/` (已归档；播客观点抽取与证据浏览 demo)
- `promotion` → `formal_projects/archived/promotion/` (已归档；晋升与职级申报材料)
- `tudou-digitaltwin` → `formal_projects/archived/tudou-digitaltwin/` (已归档；土豆数字孪生的本体工程与业务系统)
- `leetcode` → `formal_projects/archived/leetcode/` (已归档；LeetCode 刷题数据与记录，原名 knowledge_data)
- `cortex` → `formal_projects/archived/cortex/` (已归档；个人知识库系统，基于 OpenCode fork，AI agent 驱动的知识问答平台)
- `second_brain` → `formal_projects/archived/second_brain/` (已归档；第二大脑系统，FastAPI + Next.js)
