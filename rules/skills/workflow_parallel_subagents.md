# 并行 Subagent 工作流

## 元数据

- **类型**: Workflow
- **适用场景**: 用当前运行环境的 subagent 并行执行多个独立子任务
- **创建日期**: 2026-02-20
- **最后更新**: 2026-07-27

---

## 核心判断

Subagent 的主要价值不是模拟人类团队，也不是把一个普通任务包装得更复杂。它解决的是三类具体问题：

1. **上下文窗口隔离**：让不同 agent 各自持有一段可控上下文，避免主线程同时塞入大量文件、网页、日志和中间判断。
2. **并行读与独立探索**：让多个 agent 同时搜索、阅读、定位、复核，减少单一路径依赖。
3. **交叉验证**：让不同 agent 在有意重叠的范围内独立得出结论，用一致和分歧暴露遗漏、误读和假设冲突。

外部经验也指向同一个结论：multi-agent 在 research-heavy、read-heavy、高价值任务上更容易成立；在需要多个 agent 共享大量状态、连续协调写入、实时互相修正的任务上成本高且脆弱。Anthropic 的 multi-agent research system 把它定位为用更多 token 换更强的并行探索和压缩能力，并明确提到 multi-agent 可能消耗约 15 倍于普通 chat 的 token；LangChain 的经验则强调 read-heavy 比 write-heavy 更适合并行，因为写操作会携带隐含决策，合并冲突代价高。

调研依据：Anthropic Engineering《How we built our multi-agent research system》（https://www.anthropic.com/engineering/multi-agent-research-system）、LangChain《How and when to build multi-agent systems》（https://www.langchain.com/blog/how-and-when-to-build-multi-agent-systems）、Cemri et al.《Why Do Multi-Agent LLM Systems Fail?》（https://arxiv.org/abs/2503.13657）。

## 何时使用并行模式

满足以下条件中的至少 2 条，并且没有命中下方反模式时，优先考虑 subagent：

1. **信息面宽**：需要查多个文件、多个网页、多个数据源、多个时间段，主线程一次性读完会污染上下文。
2. **可拆分为独立读任务**：能分成至少 2 个相对独立的探索方向，每个方向预期需要 ≥5 个 tool call。
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
| 外部调研、论文/产品/市场 survey | 高 | 3-5 个 agent，按证据功能切分，30-50% overlap |
| 大型代码库理解、文件定位、架构梳理 | 高 | 代码探索 Agent 并行按模块或问题切分，主线程整合 |
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

不要把 overlap 理解成重复劳动。好的 overlap 是让相邻 agent 在最容易出错的边界区域共同覆盖，例如官方 claim 和独立证据的交界、模块接口、数据口径、反对意见。

### 2. 并行启动

当任务彼此独立时，应尽早同时启动多个 subagent，并明确要求等待全部结果后再整合。具体启动、等待和恢复方式以当前运行环境的能力为准，不在本 workflow 中固化调用格式。

每个 subagent 的 prompt 应包含：

- 具体负责的维度/范围
- 预期的 overlap 区域（让 agent 知道其他人也在看这部分）
- 输出格式要求
- 输出落盘路径（例如 `tmp/<session_slug>/tier3_independent.md`）
- 验证标准：哪些证据算有效，哪些情况必须标注不确定

### 2.2 文件优先的 Agent 交接

主 Agent 与 subagent 之间默认通过 workspace 文件交换实质信息，而不是在 prompt 中复制大段 context，或依赖 subagent 最后一条消息承载完整结果。

具体原则：

1. **Prompt 传目标、边界和路径。** 告诉 subagent 要解决什么、验收标准是什么、应读取哪些文件；已有材料只要已经在 workspace，就传路径，不再粘贴全文。
2. **Subagent 自己读取并迭代文件。** 让 subagent 从 source artifact、scratchpad、claim table 或代码中建立上下文。需要修改时写入自己的 namespaced 输出路径，不让多个 agent 同时覆盖 canonical 文件。
3. **结果先落盘，再返回 manifest。** Subagent 的完整研究、判断、代码或审稿结果写入指定 artifact；最后一条消息只需返回路径、状态、关键结论和未解决问题，不能让聊天摘要成为唯一交付。
4. **Parent 从 artifact 合并。** 主 Agent 读取 child artifacts、验证证据并统一写回 canonical output。Agent 间信息传递以可检查文件为准，不把前一个 agent 的自然语言总结直接当 source of truth。
5. **为失败恢复保留边界。** 长任务按阶段更新 scratchpad、checkpoint 或部分输出。Subagent 中断后，后续 agent 应能从文件继续，而不是只能重跑整段 conversation。

这种 file-first 交接有三个目的：减少 prompt 预处理和 context 复制；让 Agent 能在现有材料上反复读写；让中断、换模型和 parent 接管时仍有可审计的恢复点。只有结果极短、无 workspace 或纯一次性判断时，才允许直接在返回消息中完整交付。

主线程责任：

1. 设计任务分割和验收标准。
2. 保留最终判断权，不把 subagent 输出直接拼接成最终答案。
3. 处理冲突、补查关键来源、运行最终验证。
4. 控制成本，避免把轻量任务变成多 agent 仪式。

### 2.1 语言继承规则

**subagent 默认继承用户当前对话语言。** 用户用中文，就用中文给 subagent 写 prompt，并要求它用中文输出；用户用英文，就用英文写 prompt，并要求它用英文输出。

不要把语言留给 subagent 自己猜。很多模型会在没有明确约束时回到英文默认值，结果就会出现主线程是中文、后台结果是英文的错位。

推荐做法：在每个 subagent prompt 里显式写一条语言要求，例如：

- `LANGUAGE: 用中文思考与输出，除非引用原文标题或 API 名称`
- `LANGUAGE: Respond in English. Keep source titles in their original language when needed`

如果任务需要双语，必须明确写成双语交付，不要让 subagent 自行决定。

### 3. 等待与整合

等待方式由当前运行环境负责；主线程只需在所有承诺的结果可用后再整合。每个 subagent 返回的消息只作为 artifact manifest 和状态通知，完整结果优先从 artifact 读取。

整合步骤：

1. 读取每个 subagent 写入的 artifact 文件；subagent 返回消息只作为 artifact manifest 和状态通知。
2. 对重叠区域做交叉验证：多 agent 共同发现 → 可信度高；单一来源 → 标注待验证；矛盾信息 → 标注并分析原因。
3. 把整合结果写入 session 目录，例如 `phase3_synthesis.md`、`fact_check.md`、`brainstorm_synthesis.md`。
4. 如果 subagent 只在返回消息里总结，没有落盘，主线程应立即把关键结论落盘，避免证据链丢失。

---

## 路由决策

先按数据敏感性分流，再按任务能力分流：

1. 高隐私、不能出本机：优先使用本地执行能力；本地能力不足时，暂停并让用户决定是否扩大数据通道。
2. 可以走云但有数据保留要求：只使用已经确认满足要求的通道。
3. 写作质量优先且内容不敏感：选择更适合目标语言和文体的 Agent。
4. 复杂工程判断、计划、架构和代码审查：选择推理和工具能力更强的 Agent。
5. 便宜、可粗糙、可重跑的初筛任务：优先使用低成本 Agent。
6. 代码库探索、定位文件和回答内部结构问题：优先使用擅长搜索和代码理解的 Agent。

具体 Agent 名、模型名和参数以当前运行环境实际暴露的能力为准。不要为了“稳定”默认固定采样参数；只有明确知道某个模型需要特定设置时再配置。

---

## 示例

### 调研任务（30-50% overlap）

```
调研「某技术框架的采用情况」
├─ Agent 1：官方叙事 + 产品定义
├─ Agent 2：独立使用体验 + 社区反馈
├─ Agent 3：失败边界 + 竞品对比
└─ Overlap：社区和企业案例都有覆盖，可交叉验证
```

### 代码任务（0-20% overlap）

```
实现「用户认证系统」
├─ Task 1：认证核心逻辑 + Token 管理
├─ Task 2：数据库模型 + 迁移脚本
├─ Task 3：API 端点 + 测试用例
└─ Overlap：接口定义处有少量重叠，确保对接正确
```

### 审查任务（30% overlap）

```
审查「一个 PR 是否可靠」
├─ Agent 1：代码行为和边界条件
├─ Agent 2：测试覆盖、缺失 fixture、回归风险
├─ Agent 3：架构一致性和隐含依赖
└─ Overlap：所有 agent 都看核心 diff，但外围文件按职责分开
```

### 不适合并行的任务

```
修复「一个函数里的 off-by-one」
└─ 主线程直接读文件、改代码、跑测试。subagent 的启动和整合成本高于任务本身。
```

---

## 注意事项

- **不要过度并行**：2-3 个精心设计的 subagent 通常优于 5 个松散的
- **prompt 质量**：subagent 的 prompt 要足够具体，否则结果会很浅
- **成本意识**：并行会消耗更多 token，评估是否值得
- **中间结果**：默认不需要把每个 subagent 的原始输出都落盘；但如果任务属于 research / writing workflow，主线程应把关键中间工件整理到 `tmp/<session_slug>/` 这类 session 目录中
- **当前 schema 优先**：文档中的 agent 名必须以当前工具 schema 为准；不要复制其他 workspace 的私有 agent 名
