# Skill: Agent Trace Sync Hygiene

## When to Use

维护 `contexts/agent_traces/`，尤其是执行 `python3 tools/export_opencode_sessions.py --sync` 这类增量同步时使用。

## Goal

把有长期复用价值的 session 落盘，把明显只有瞬时操作痕迹的 session 挡在导出阶段，不让 `agent_traces` 被事务噪声稀释。

## Filtering Rules

默认跳过下面两类低信息量 session：

1. 只有自动命令指令，没有 final assistant output 的 session
2. 纯工作区事务查询，只有短期操作价值，没有长期知识价值的 session

另外有一类是更强的定向规则：对少数已经确认属于运维噪声的 session，按 OpenCode 数据库里的 `session.title` 和首轮 query 组合过滤。这里之所以仍然保留数据库 title，是因为导出的条目标题本来就以数据库 session 记录为准；再叠加首轮 query，是为了避免只因标题相同就误删后来演化出有效内容的会话。

当前明确纳入过滤的例子：

- 数据库 `session.title` 为 `增量同步 agent_traces 会话记录`，且首轮 query 是 `/sync-agent-traces` 自动命令模板
- 数据库 `session.title` 为 `查看未提交的变更`，且首轮 query 是 `查看未提交的变更` / `现在有哪些未提交的变更`
- `/sync-agent-traces` 这类自动 slash command 记录，且导出内容里没有 final assistant output
- `查看未提交的变更` / `现在有哪些未提交的变更` 这类纯工作区状态查询

## Judgment Standard

判断标准不是“轮数少”，而是“有没有可复用的判断、方案、知识或认知变化”。

上面的定向规则是例外：它不是在做通用信息密度判断，而是在排除少数已知会污染 `agent_traces` 的运维型 session 模式。

下面这些通常应该保留：

- 短但高压缩的题解总结
- 短但有明确判断增量的问答
- 标题像 `system-reminder`，但正文里其实有长链路讨论的 session

## Implementation Point

筛选逻辑放在 `tools/export_opencode_sessions.py`，这样同步时会同时做到两件事：

1. 新的低信息量 session 不再落盘
2. 之前已经导出的同类文件，会在后续 `--sync` 时被 prune 掉

标题规则也遵循同一个脚本里的简单约定：

1. OpenCode 数据库里有正常 `session.title` 时，直接用数据库标题
2. 只有数据库标题为空或明显是占位/噪声标题时，才回退到首轮 query
3. 回退出来的标题只做清洗和长度截断，不做主观语义改写
