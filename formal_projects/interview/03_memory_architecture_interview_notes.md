# Memory 架构面试底稿

## 30 秒版本

我这个 repo 里的 memory 机制，核心是把 agent 需要长期复用的上下文写成文件。
`AGENTS.md` 是启动入口，负责告诉 agent 每次 session 先读什么、遇到不同任务去哪里找信息。
`rules/` 放长期规则，包括用户画像、沟通风格、目录路由、skills 和 axioms。
`contexts/memory/OBSERVATIONS.md` 放动态观测，由每日 observer 追加，再由每周 reflector 做清理和晋升。

## 我会怎么讲这套架构

可以从三层讲起。

```text
L3: rules/                      长期规则层
L1: OBSERVATIONS.md             每日观测层
L2: reflector                   反思和晋升层
```

`L3` 是长期稳定的行为先验。比如 agent 怎么工作、用户是谁、这个 workspace 的目录怎么走、写作风格有什么要求、遇到某类任务应该加载哪个 skill。

`L1` 是近期经验池。每天工作中产生的项目状态、踩坑、技术决策、可复用经验，会被 observer 追加到 `contexts/memory/OBSERVATIONS.md`。

`L2` 是过滤层。reflector 每周检查 `OBSERVATIONS.md`，把有长期价值的内容晋升到 `rules/`，同时清理临时记录。这样记忆不会无限膨胀，也不会把一次性上下文误当成长期规则。

这里真正有价值的是沉淀链路：观测先进入短期池，经过过滤后再变成长期规则。

```text
日常工作产物
  -> observer 记录
  -> OBSERVATIONS.md 暂存
  -> reflector 过滤
  -> rules/ 固化
  -> 后续 session 重新加载
```

## `AGENTS.md` 是 bootloader

在 Codex 和 OpenCode 这类 runtime 里，`AGENTS.md` 是默认会读的文件。所以我把它当成 bootloader，只放启动协议和硬约束。详细长期记忆放到它指向的专门文件里。

它应该放启动协议和硬约束，例如：

```text
每次 session 先读哪些 rules
找文件先看 WORKSPACE.md
遇到“怎么做 X”先查 skills/INDEX.md
正式项目下先读项目级 AGENTS.md
L1/L2 动态记忆在 OBSERVATIONS.md
```

真正详细的内容放在专门文件里。`SOUL.md` 管 agent 身份，`USER.md` 管用户画像，`COMMUNICATION.md` 管表达风格，`WORKSPACE.md` 管目录路由，`skills/` 管可复用流程，`axioms/` 管判断原则。

这样做的好处是启动入口保持稳定，长期记忆也有明确归属。后续要改用户画像，就改 `USER.md`；要改表达风格，就改 `COMMUNICATION.md`；要新增可复用流程，就放进 `skills/`。

## L3：长期规则层

`rules/` 是当前 repo 里最重要的长期记忆层。

它大概分成几类：

```text
rules/SOUL.md                 agent 身份和协作原则
rules/USER.md                 用户画像、偏好、背景
rules/WORKSPACE.md            目录路由
rules/COMMUNICATION.md        沟通和写作风格
rules/skills/                 可复用工作流和工具使用方法
rules/axioms/                 长期判断原则和认知模式
```

这层内容会直接影响 agent 的行为。比如 `WORKSPACE.md` 会改变找文件路径，`COMMUNICATION.md` 会改变写作方式，`skills/INDEX.md` 会决定遇到任务时先加载哪个工作流。

不过 L3 也需要控制密度。`AGENTS.md` 和少数核心 rules 可以默认加载，完整 skill 和 axiom 详情应该按需读取。否则长期规则层会变成另一个上下文垃圾桶。

## L1：每日观测层

`contexts/memory/OBSERVATIONS.md` 是动态记忆池。observer 每天扫描 workspace 变化，然后追加当天观测。

它的格式是：

```text
Date: YYYY-MM-DD

🔴 High: [方法论/约束] 描述
🟡 Medium: [项目状态/决策] 描述
🟢 Low: [任务流水] 描述
```

`🔴 High` 代表跨项目通用经验、硬约束或重大架构决策。比如某个调研方法被反复验证有效，或者某个安全边界必须永久遵守。

`🟡 Medium` 代表近期还会用到的项目状态和技术决策。它不一定值得变成长期规则，但在未来几周内有上下文价值。

`🟢 Low` 代表日常流水、一次性 debug 或临时背景。它的主要价值是短期恢复上下文，过一段时间就应该清理。

这层的原则是只记录未来可能复用的信息。保存一切会让记忆系统变成噪音系统。

## L2：反思和晋升层

reflector 每周处理一次 `OBSERVATIONS.md`。它主要做两件事：把高价值观测晋升到 `rules/`，把过期低价值观测清掉。

当前的晋升门槛可以这样讲：

```text
跨项目通用
多次验证
有明确适用场景
```

晋升时要先判断内容类型。

如果这条观测是在说 agent 应该怎样协作，应该进 `SOUL.md`。如果是在说用户偏好、背景或长期关注，应该进 `USER.md`。如果是在说表达风格，应该进 `COMMUNICATION.md`。如果是在说文件路径或项目路由，应该进 `WORKSPACE.md`。

如果它能变成一套可执行流程，比如步骤、命令、工具调用、检查方式，就应该进 `rules/skills/`。如果它更像一个长期判断原则，可以帮助预测用户在新问题上的取舍，就应该进 `rules/axioms/`。

面试里可以强调这个区分：

```text
skill 是执行资产，回答“怎么做”
axiom 是判断资产，回答“为什么这样判断”
```

比如“深度调研时要并行多个 subagent，并且做交叉验证”，这是 skill。它可以写成工作流。

比如“当测量可得时，用数据而不是观点支撑判断”，这是 axiom。它影响的是决策方式。

## 使用方式

这套 memory 使用时分两种。

第一种是默认加载。每次 session 启动时，根据 `AGENTS.md` 读取核心规则：

```text
rules/SOUL.md
rules/USER.md
rules/WORKSPACE.md
rules/COMMUNICATION.md
rules/skills/INDEX.md
```

第二种是按需检索。`OBSERVATIONS.md` 会越来越大，所以不能全文加载。遇到历史经验、项目延续、用户偏好、方法论复盘时，再搜索相关条目。

理想流程是：

```text
先搜 OBSERVATIONS.md，找到候选历史
如果涉及价值观或长期方法论，再做语义搜索
如果命中 skill 或 axiom，再读对应文件正文
最后区分哪些是已经固化的规则，哪些只是临时观测
```

这样可以保持上下文稀疏，同时保留长期经验。

## 和 OpenClaw 的关系

OpenClaw 的思路和这套 repo 很接近。它也用文件作为长期真源，大概是：

```text
SOUL.md / AGENTS.md / USER.md / MEMORY.md       启动时加载
memory/YYYY-MM-DD.md                            日志和短期记忆
memory_search / memory_get                      检索
memory promote / dreaming                       晋升和反思
```

OpenClaw 更工程化的一点是 `memory promote` 和 `dreaming`。Dreaming 分 Light、REM、Deep 三个阶段。Deep 阶段会根据候选记忆的表现，把短期内容晋升到 `MEMORY.md`。

它的晋升评分更细，会考虑 frequency、relevance、query diversity、recency、consolidation、conceptual richness。这个点我觉得值得借鉴。我的 repo 当前有清楚的分层和晋升方向，但 reflector 的晋升判断还偏规则描述。后续可以补 promotion scoring 和 `promote-explain`，让每次晋升更可解释。

## 和 Hermes 的关系

Hermes 的核心 memory 更小，主要是两个文件：

```text
~/.hermes/memories/MEMORY.md
~/.hermes/memories/USER.md
```

它们在 session start 注入 system prompt。Hermes 的核心 memory 没有 read action，只有 `add`、`replace`、`remove`。它的内置设计强调核心记忆常驻，而大规模历史交给 session search 或外部 provider。

我不认为 Hermes 的 memory 架构本身比 OpenClaw 更强。它更特殊的地方在产品取舍：核心记忆很小、始终在场、可编辑，并且和 skills 分工清楚。再加上它把 persistent memory、self-improving skills、trajectory export / RL pipeline 放在同一个叙事里，所以传播上更容易讲成“agent 会成长”。

对我的 repo 来说，Hermes 值得借鉴的是工作集意识：每次都必须知道、漏掉就会改变行为的内容，才应该进 always-on core。其他内容放到检索层、skill 或 observation 池里。

## 这套设计的优点和不足

优点主要有四个。

第一，透明。所有 memory 都是 Markdown 文件，能读、能改、能 git diff。agent 做错时，可以追到具体是哪条规则或记忆影响了它。

第二，可分层。用户画像、沟通风格、目录路由、执行方法、判断原则、动态观测都有不同位置，避免全部混进一个 `MEMORY.md`。

第三，可晋升。日常观测不会直接变成长期规则，而是先进入 `OBSERVATIONS.md`，再由 reflector 过滤。

第四，适合多 agent。不同 agent 可以通过同一组文件对齐，而不是依赖某个聊天窗口里的历史。

不足主要在工程化程度上。

第一，reflector 的晋升机制还不够工程化。现在有“跨项目通用、多次验证、有明确适用场景”这样的原则，但还没有 OpenClaw 那种明确评分。

第二，`OBSERVATIONS.md` 会增长，需要更强的生命周期策略。比如 `🟢` 多久清理，`🟡` 多久必须合并、降级或晋升。

第三，检索协议还依赖 agent 自觉。后续应该把 retrieve-before-act 写成更强的操作规范。

第四，晋升后的 provenance 还不够。skill 或 axiom 最好能记录来源日期和证据路径，这样长期规则可以追溯。

## 面试问答准备

如果被问：这和普通 RAG 有什么区别？

可以答：

```text
普通 RAG 主要解决回答问题时从文档里找相关信息。我的 memory 系统解决的是 agent 的长期上下文管理。它不只是检索历史，还会把历史经验分层沉淀：短期观测进入 OBSERVATIONS.md，经过 reflector 后，稳定经验晋升为 rules、skills 或 axioms。最后影响的是 agent 之后怎么工作、怎么判断、怎么和用户协作。
```

如果被问：为什么不用数据库或向量库？

可以答：

```text
早期我更看重可控性和可审计性。Markdown + Git 的好处是透明、可 diff、可人工修正。向量检索可以作为增强层，但不应该成为唯一真源。长期规则、用户画像、skills 这些内容需要能被人和 agent 共同维护。
```

如果被问：怎么避免 memory 污染？

可以答：

```text
我主要靠三层过滤。L1 只记录未来可能复用的观测，不保存所有流水。记录时用红黄绿区分长期价值。L2 reflector 定期清理低价值内容，并且只有跨项目通用、多次验证、有明确适用场景的内容才会晋升到 rules。
```

如果被问：和 OpenClaw / Hermes 比有什么特点？

可以答：

```text
OpenClaw 的 memory 更工程化，有 memory_search、promote、dreaming。我这套更轻量，但长期规则分得更细：SOUL、USER、COMMUNICATION、WORKSPACE、skills、axioms 各自承担不同职责。

Hermes 的核心 memory 更小，强调 always-on 的 MEMORY.md 和 USER.md。我这边因为 Codex / OpenCode 本身会加载 AGENTS.md，所以 AGENTS.md 更像 bootloader，负责拉起 rules/ 下的长期规则层。相比 Hermes，我更强调文件化的上下文基础设施，以及从 observation 到 rule 的晋升链路。
```

## 复习关键词

```text
AGENTS.md as bootloader
file-based memory
progressive disclosure
L3 rules
L1 observations
L2 reflector
observer / reflector
append-only daily observation
promotion and garbage collection
skill = procedural memory
axiom = judgment memory
Markdown as source of truth
Git diff as audit trail
retrieve-before-act
OpenClaw dreaming
Hermes always-on core
```
