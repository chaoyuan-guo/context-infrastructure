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

还有一类是项目内 agent 执行痕迹：这些 session 是某个项目调用 OpenCode 产生的批量记录，不代表 chaoyuan 本人的交互历史。过滤时优先看 OpenCode 数据库里的 `session.directory`，再用 `session.title` 前缀兜底。

当前明确纳入过滤的例子：

- 数据库 `session.title` 为 `增量同步 agent_traces 会话记录`，且首轮 query 是 `/sync-agent-traces` 自动命令模板
- 数据库 `session.title` 为 `查看未提交的变更`，且首轮 query 是 `查看未提交的变更` / `现在有哪些未提交的变更`
- `/sync-agent-traces` 这类自动 slash command 记录，且导出内容里没有 final assistant output
- `查看未提交的变更` / `现在有哪些未提交的变更` 这类纯工作区状态查询
- `session.directory` 位于 `adhoc_jobs/tmp_moganshyan_eval/`，或 `session.title` 以 `tmp_moganshyan_eval` 开头的项目内 agent eval 记录
- `session.title` 以 `historical-` 开头的历史回填流水线内部任务，例如 `historical-l1-trace-observer`、`historical-l2-filter-only`

导出轮次内部，默认还会剔除这些不属于“你的真实输入”的伪 user turns：

- `<system-reminder>` 后台任务提醒、完成通知、结果 ready 通知
- `<ultrawork-mode>`、`ultrawork [SYSTEM DIRECTIVE: ...]`、`ralph loop`、verification loop 这类运行时注入指令
- `Continue if you have next steps...`、`[restore checkpointed session agent configuration after compaction]` 这类 continuation / compaction 控制消息
- `<!-- OMO_INTERNAL_INITIATOR -->` 这类内部注释标记

对应地，assistant 侧现在优先按 OpenCode 原始数据库字段做筛选，而不是主要靠正文 regex 清洗：

- 只把 `message.data.role = assistant` 且 `message.data.finish = stop` 的 child message 视为候选最终回复
- 只提取 `part.data.type = text` 的文本内容
- 默认忽略 `tool`、`step-start`、`step-finish`、`reasoning`、`patch`、`compaction`、`file`、`subtask` 这类执行/过程 part

在这个字段层过滤之后，下面这些 assistant 内容自然不会再单独保留为导出轮次：

- 纯内部等待/轮询状态，例如“还在等 background task 完成”“不能主动轮询”
- 混在执行态消息里的 process/status 广播，例如 `What changed:`、`Verified:`、`Remaining wait:`、`Oracle re-reviewed ...`、`I already launched a background explore task ...`
- `_No final assistant output found._` 这类空输出占位
- 只有 `<promise>DONE</promise>` / `<promise>VERIFIED</promise>` 之类 loop 协议信号的回复

当前实现不再把 control-only user turn 后面的 assistant 文本并回上一轮；assistant 侧只保留明确落在 `finish = stop` 上的最终回复。这样结构更稳，也减少了 process text 混入真实答复的概率。

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

另外，导出文件带 `export_format_version`。当清洗规则升级时，后续 `--sync` 会基于版本自动重写旧文件，避免 manifest 里看起来“没变”但磁盘内容仍是旧格式。当前这轮字段驱动重构和 user preamble 清洗后，脚本里的版本已提升到 `10`。

标题规则也遵循同一个脚本里的简单约定：

1. OpenCode 数据库里有正常 `session.title` 时，直接用数据库标题
2. 只有数据库标题为空或明显是占位/噪声标题时，才回退到首轮 query
3. 回退出来的标题只做清洗和长度截断，不做主观语义改写
