# 并行 Subagent 工作流

## 元数据

- **类型**: Workflow
- **适用场景**: 用当前 harness 的 `call_omo_agent` 并行执行多个独立子任务
- **创建日期**: 2026-02-20
- **最后更新**: 2026-06-10

---

## 核心判断

Subagent 的主要价值不是模拟人类团队，也不是把普通任务包装得更复杂。它解决三类具体问题：

1. **上下文窗口隔离**：让不同 agent 各自持有一段可控上下文，避免主线程同时塞入大量文件、网页、日志和中间判断。
2. **并行读与独立探索**：让多个 agent 同时搜索、阅读、定位、复核，减少单一路径依赖。
3. **交叉验证**：让不同 agent 在有意重叠的范围内独立得出结论，用一致和分歧暴露遗漏、误读和假设冲突。

外部经验也指向同一个结论：multi-agent 更适合 research-heavy、read-heavy、高价值不确定任务；不适合多个 agent 共享大量状态、连续协调写入、实时互相修正的任务。参考：Anthropic Engineering《How we built our multi-agent research system》、LangChain《How and when to build multi-agent systems》、Cemri et al.《Why Do Multi-Agent LLM Systems Fail?》。

## 当前工具边界

当前 harness 暴露的 subagent 工具是 `call_omo_agent`，可用 `subagent_type` 只有：

| subagent_type | 适用场景 |
|---|---|
| `explore` | 代码库内部快速搜索、文件定位、架构理解、历史上下文梳理 |
| `librarian` | 外部资料、文档、网页、公开信息调研 |

不要使用旧的 `category="deep"`、`category="artistry"`、`oracle`、`ultrabrain`、`functions.task`、`load_skills` 等写法，除非当前工具 schema 或 OpenCode 配置明确暴露了这些能力。

---

## 何时使用并行模式

满足以下条件中的至少 2 条，并且没有命中下方反模式时，优先考虑 subagent：

1. **信息面宽**：需要查多个文件、多个网页、多个数据源、多个时间段，主线程一次性读完会污染上下文。
2. **可拆分为独立读任务**：能分成至少 2 个相对独立的探索方向，每个方向预期需要 >=5 个 tool call。
3. **需要独立判断**：需要反方审稿、事实核查、竞品对照、代码审查、方案对比，单一路径容易自我确认。
4. **存在高价值不确定性**：任务结果会影响后续决策、公开输出、代码改动或成本较高的行动，多花 token 值得。
5. **主线程需要保留设计/整合能力**：主 agent 应把注意力用在拆分问题、设定标准、整合证据和最终判断，而不是埋在低层搜索或重复读取里。

不满足时，直接串行执行，不要为了并行而并行。

## 反模式

以下情况默认不要用 subagent，除非用户明确要求或任务价值足以覆盖额外成本：

1. **单点小任务**：只需读 1-2 个文件、跑一个命令、改一个局部 bug。
2. **强顺序依赖**：下一步必须依赖上一步输出，拆出去只会制造等待和交接成本。
3. **共享状态写入**：多个 agent 同时改同一批文件、同一张表、同一份文案，冲突和隐含决策难以合并。
4. **上下文必须完整共享**：每个 agent 都必须知道全量背景才能做对，拆分后只会丢条件。
5. **验证标准不清**：没有可核对的输出格式、证据要求或验收条件，多个 agent 只会产出多份模糊总结。

## 任务类型参考

| 任务类型 | 是否适合 | 推荐方式 |
|---|---|---|
| 外部调研、论文/产品/市场 survey | 高 | 3-5 个 `librarian`，按证据功能切分，30-50% overlap |
| 大型代码库理解、文件定位、架构梳理 | 高 | 2-5 个 `explore`，按模块或问题切分，主线程整合 |
| 代码 review、方案审稿、事实核查 | 高 | 2-3 个 agent 独立审查，同一关键区域保留 overlap |
| Brainstorm、反方观点、thesis 压力测试 | 中高 | 不同 agent 指定不同判断视角，输出必须回答同一组问题 |
| 多文件实现 | 中 | 只在模块边界清楚时并行；主线程保留最终合并和测试责任 |
| 单 bug 修复、局部编辑、格式调整 | 低 | 主线程直接做 |
| 多 agent 同时写同一文件或同一状态 | 低 | 避免；改成先并行读/评审，再由主线程或单一 agent 写 |

---

## 并行执行流程

### 1. 评估与分割

识别 2-5 个关键维度后，根据任务类型确定 overlap：

| 任务类型 | Overlap 范围 | 原因 |
|---------|-------------|------|
| 调研/创造性任务 | 30% - 50% | 交叉验证、查漏补缺 |
| 代码/执行任务 | 0% - 20% | 效率优先，减少重复 |

好的 overlap 不是重复劳动，而是让最容易出错的边界区域共同覆盖，例如官方 claim 和独立证据的交界、模块接口、数据口径、反对意见。

### 2. 并行启动

用 `call_omo_agent(run_in_background=true)` 启动后台 subagent。能在同一条 assistant 消息里发出多个 tool call 时，应一次性发出；如果 harness 只能逐个发出，也要保持每个任务 `run_in_background=true`，拿到各自的 `task_id` 后等待系统通知。

示例：

```text
call_omo_agent(
  description="官方叙事",
  subagent_type="librarian",
  run_in_background=true,
  prompt="调研官方来源，提取 claim、URL、原文摘录，写入 tmp/<session>/tier1_official.md"
)

call_omo_agent(
  description="代码结构",
  subagent_type="explore",
  run_in_background=true,
  prompt="定位相关模块、入口和测试，输出文件路径、关键符号和风险点"
)
```

每个 subagent 的 prompt 应包含：

- 具体负责的维度/范围
- 预期的 overlap 区域
- 输出格式要求
- 输出落盘路径或明确的返回结构
- 验证标准：哪些证据算有效，哪些情况必须标注不确定

主线程责任：

1. 设计任务分割和验收标准。
2. 保留最终判断权，不把 subagent 输出直接拼接成最终答案。
3. 处理冲突、补查关键来源、运行最终验证。
4. 控制成本，避免把轻量任务变成多 agent 仪式。

### 3. 等待与整合

启动后台 agent 后不要轮询。系统会在 subagent 完成时自动推送 `<system-reminder>` 通知。收到通知后，再用 `background_output(task_id="...")` 一次性取回结果。

`background_output` 的 `block` 和 `timeout` 参数不会把它变成可靠的等待器。它的核心用途是取回已有结果，不是反复 polling。

整合步骤：

1. 读取每个 subagent 的返回内容或 artifact 文件。
2. 对重叠区域做交叉验证：多 agent 共同发现 -> 可信度高；单一来源 -> 标注待验证；矛盾信息 -> 标注并分析原因。
3. 把整合结果写入 session 目录，例如 `phase3_synthesis.md`、`fact_check.md`、`brainstorm_synthesis.md`。

---

## 示例

### 调研任务（30-50% overlap）

```text
调研「某技术框架的采用情况」
├─ Agent 1（librarian）：官方叙事 + 产品定义
├─ Agent 2（librarian）：独立体验 + 社区反馈
├─ Agent 3（librarian）：失败边界 + 竞品对比
└─ Overlap：社区反馈和失败边界都有覆盖，可交叉验证
```

### 代码库理解任务（0-20% overlap）

```text
理解「用户认证系统」
├─ Agent 1（explore）：认证入口 + Token 管理
├─ Agent 2（explore）：数据库模型 + 迁移脚本
├─ Agent 3（explore）：API 端点 + 测试用例
└─ Overlap：接口定义处有少量重叠，确保对接正确
```

### 审查任务（30% overlap）

```text
审查「一个 PR 是否可靠」
├─ Agent 1（explore）：代码行为和边界条件
├─ Agent 2（explore）：测试覆盖、缺失 fixture、回归风险
├─ Agent 3（librarian）：相关外部 API / 文档约束
└─ Overlap：所有 agent 都看核心 diff，但外围文件按职责分开
```

### 不适合并行的任务

```text
修复「一个函数里的 off-by-one」
└─ 主线程直接读文件、改代码、跑测试。subagent 的启动和整合成本高于任务本身。
```

---

## 注意事项

- **不要过度并行**：2-3 个精心设计的 subagent 通常优于 5 个松散的。
- **prompt 质量**：subagent 的 prompt 要足够具体，否则结果会很浅。
- **成本意识**：并行会消耗更多 token，评估是否值得。
- **中间结果**：research / writing workflow 应把关键中间工件整理到 `tmp/<session_slug>/`。
- **当前 schema 优先**：文档中的 agent 名必须以当前工具 schema 为准；不要复制其他 workspace 的私有 agent 名。
