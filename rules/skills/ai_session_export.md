# AI Session Export（本地配置）

通用实现位于 [`../../tools/ai_session_export/`](../../tools/ai_session_export/)，同步自
[`grapeot/ai_session_export`](https://github.com/grapeot/ai_session_export)。完整能力契约见
[`skill.md`](../../tools/ai_session_export/skill.md)。当前同步基线为
`master@78f9fd3da0c95efea1a798fd508635d0d4a8a539`。

本文件只保存当前 workspace 的归档路径、运行命令和本地边界，不修改通用实现。

## 本地边界

- 统一原始归档：`contexts/ai_sessions/<source>/`
- 增量状态：`contexts/ai_sessions/.export_state.json`
- OpenCode 精选归档：`contexts/agent_traces/`

`ai_sessions` 用统一格式覆盖 Codex、OpenCode 和 Claude Code，适合跨来源检索；
`agent_traces` 继续承载经过本地 Hygiene 深度过滤的 OpenCode 高质量记录。两者暂不互相覆盖。

真实会话包含标题、正文、项目路径和 session id，只能保存在 Git 忽略的私有目录中。

## 安装

```bash
uv python install 3.12
uv venv --python 3.12 tools/ai_session_export/.venv
uv pip install --python tools/ai_session_export/.venv/bin/python \
  -e 'tools/ai_session_export[dev]'
```

## 导出

先 dry-run 单个来源：

```bash
tools/ai_session_export/.venv/bin/python tools/ai_session_export/export_sessions.py \
  --source codex \
  --since-date 2026-07-01 \
  --dry-run \
  --base-dir contexts/ai_sessions \
  --state-file contexts/ai_sessions/.export_state.json
```

确认规模后执行增量导出：

```bash
tools/ai_session_export/.venv/bin/python tools/ai_session_export/export_sessions.py \
  --source codex \
  --since-date 2026-07-21 \
  --base-dir contexts/ai_sessions \
  --state-file contexts/ai_sessions/.export_state.json
```

试用阶段保留 `--since-date 2026-07-21`。如果后续去掉该参数，状态文件中从未记录过的更早 session
也会被视为待导出内容；只有明确决定全量回填时才这样做。

`--source all` 会依次导出 Codex、OpenCode 和 Claude Code。若本机缺少某个来源的数据文件，
改为按已配置的来源分别执行，避免单个来源失败中止整次导出。

## 数据质量

通用 exporter 主要统一格式，不包含 `Agent Trace Sync Hygiene` 的本地深度清洗。Codex 导出中可能出现
评估任务、内部控制消息等低价值 session。先保留原始归档，在检索 file list 和后续本地清洗层过滤，
不要直接修改 vendored upstream 实现。

导出后按 [AI Session Search & Archive](./ai_session_search_archive.md) 刷新索引并检索。
