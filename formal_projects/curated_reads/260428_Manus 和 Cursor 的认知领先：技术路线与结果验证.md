# Manus 和 Cursor 的认知领先：技术路线与结果验证

> 来源：<https://www.superlinear.academy/c/news/manus-cursor>
> 作者：Superlinear Academy
> 发布日期：2026-04-28
> 平台：Superlinear Academy

---

2026-04-28

---

## 一种常见的判断

Meta [花了 20 亿美元买 Manus](https://www.cnbc.com/2025/12/30/meta-acquires-singapore-ai-agent-firm-manus-china-butterfly-effect-monicai.html)，Elon Musk [给 Cursor 开了 600 亿美元的收购选项](https://techcrunch.com/2026/04/21/spacex-is-working-with-cursor-and-has-an-option-to-buy-the-startup-for-60-billion/)。这两个数字公布之后，中文互联网上最常见的反应可以归结为两句话：第一，这俩不都是套壳吗？底层用的是别人的模型，有什么了不起。第二，Zuckerberg 和 Musk 这是冲动消费，一个是"Meta 已经错过了 AI 所以高价买进"，一个是"Musk 就是什么热买什么"。

这种判断的潜台词是：Manus 和 Cursor 本身没什么特别的，和市面上一大堆 AI agent 工具、AI 编程工具没有本质区别，只是营销做得好、时机赶得巧。

这篇文章想说的是，这个判断错了。不是小错，是方向性的错。Manus 和 Cursor 在各自领域里的认知水平，领先了行业至少一个身位，而且这个认知领先有具体的技术路线和竞品对比可以验证。Meta 和 SpaceX/xAI 的出价不是冲动，是对这种认知领先的定价。

## Manus：从第一性原理出发

Manus 从 2025 年 3 月发布起就伴随争议。最常见的批评是套壳：它不训练自己的模型，用的是 Claude 和 Qwen，只是在外面包了一层 agent 调度框架。[MIT 博士秦增益的评论](https://www.ctdsb.net/c1716_202503/2389983.html)代表了一类观点：这是一个很好的产品，但并不是一项技术突破。

要理解 Manus 做对了什么，最有效的方式是把它和同期的竞品放在一起看。

### 认知差异一：不搞角色扮演

2023 年到 2025 年初，多数 multi-agent 系统的设计思路是照搬人类组织架构。[MetaGPT](https://arxiv.org/abs/2308.00352) 是这类思路的典型代表：它把 LLM agent 分成产品经理、架构师、项目经理、工程师、QA 五个角色，每个角色有固定的职责和工作流，按照人类软件公司的流程串行执行。这就是所谓的 hat wearing。

这种设计的问题出在起点。人类社会之所以需要专业分工，是因为一个人的能力带宽有限，需要花十几年训练才能成为一个资深的产品经理或资深的工程师。分工是对人类认知局限性的补偿。但 LLM 不是这样。任何一个 LLM off the shelf 就是一个 generalist，它懂所有领域的知识。在 prompt 里告诉它"你是一个资深的 software engineer"，这句话除了限制它的能力以外没有任何意义。

从第一性原理出发想这件事，结论完全不同：不应该让多个 agent 各自扮演一个人类角色然后串行协作，而应该让每个 agent 都保持 generalist 的完整能力，只在任务层面做分割。Manus 的 wide research 机制就是这个思路的产品化。它的主 planner agent 把用户请求拆成若干独立子任务，然后为每个子任务启动一个独立的、完整能力的 Manus 实例，每个实例有自己独立的 context window，在云端虚拟机沙盒里自主执行。没有"产品经理 agent"或"工程师 agent"这样的角色标签，每个 sub-agent 都能规划、执行和验证。

这不是 UI 层面的差别，也不是产品策略层面的差别，是对 LLM 本质的理解不同。MetaGPT 从人类组织架构出发设计系统，Manus 从 LLM 的能力特征出发设计系统。后者对了，前者错了。这个判断在 2025 年 3 月是少数派，到 2026 年已经成为行业共识：OpenAI 的 Codex 用 Plan/Spec Mode（planner 分析请求，executor 在沙盒里执行），Anthropic 的 Claude Code 用 orchestrator-worker（lead agent 制定计划，sub-agent 并行执行），Cursor 用 Planner-Worker-Judge。所有头部玩家都收敛到了按功能分工（规划、执行、评估）的架构，没有一家在给 agent 戴人类职业的帽子。

Manus 在产品层面的判断也体现了同样的认知水平。2025 年 3 月，在多数 agent 产品还在垂直领域里各做各的时候（调研的只能调研，生成的只能生成），Manus 是第一个把端到端链路打通的产品，从自主搜索到代码生成到数据可视化一条线走完。这件事今天已经是 agent 产品的标配，但在当时是少数派判断。我在那一周[写过一篇分析](https://yage.ai/manus.html)，讨论了 Agentic AI 在工具、数据和智能三个维度上的复利效应，Manus 是当时唯一一个把这三层复利都做出来的产品。

### 认知差异二：User Generated Software 的创建和分发

软件行业有一个长期存在的供需错配：专业软件公司生产的产品满足的是头部需求，大量长尾需求没有人管。这和媒体行业在 YouTube 出现之前的状态类似：电视台满足头部内容需求，长尾的内容创作需求被忽略，直到 User Generated Content 平台出现。

Manus 敏锐地判断了这一点，并且在产品层面做了一个当时看起来不太常规的决定：让用户能把 Manus 生成的应用直接部署和分发。用户描述一个需求，Manus 自动生成前端、后端、数据库，然后一键部署到云端，返回一个可分享的链接。这件事做到这一步已经超过了同期的多数 agent 产品。但 Manus 还做了一层：它提供了 API，让部署出去的应用能够调用 Manus 自身的 AI 能力。换句话说，用户不光能用 AI 生成软件，生成出来的软件本身还能继续使用 AI。

这个判断在当时不是显而易见的。2025 年 3 月，多数 AI agent 产品把自己定位为"帮你完成一个任务的工具"，产出物是报告、代码或幻灯片，用完就结束。Manus 的定位是"帮你创建一个可以持续运行和分发的软件产品"，而且这个产品自带智能。这是两种完全不同的产品逻辑。前者把 AI 当作一次性的生产力工具，后者把 AI 当作 User Generated Software 的基础设施。

市场反应验证了这个判断。[Manus 的 waitlist 在公开演示后突破了 200 万](https://www.taskade.com/blog/manus-ai-review)，那次演示中最让用户兴奋的不只是 AI 能做调研和写代码，而是它能一键把成品部署出去，变成一个真正可用的在线产品。到 2025 年底，vibe coding 和 AI app builder 已经成为一个 [47 亿美元的市场](https://www.taskade.com/blog/state-of-vibe-coding)，Manus 是最早把"创建加部署加智能注入"这条完整链路做出来的产品之一。

这个设计选择背后的认知水平，体现在它对整条价值链的完整性判断上。多数竞品停留在生成这一步，Manus 一直想到了分发和持续运行。这和第一个认知差异（不做 hat wearing）指向同一个根源：这个团队从第一性原理出发思考问题，而不是沿着现有产品形态做增量优化。

### 结果和回应

商业回报直接反映了这些认知：8 个月做到 [$100M ARR，处理量 147 万亿 token，创建超过 8000 万台虚拟计算机](https://www.businessinsider.com/what-is-manus-ai-meta-acquisition-chinese-startup-singapore-agent-2025-12)。GAIA Level 3 基准测试 57.7% 的成绩，领先 OpenAI Deep Research 的 47.6%。

两个常见的追问需要回应。

第一，"agent 产品已经满大街了，Manus 是上一代的产品形态，对 Meta 没有直接用途。"这个说法有一半是对的。Manus 代表的是云端沙盒 agent 形态，而 2026 年的主流方向已经转向了 Claude Code、OpenClaw 这类本地终端 agent 和 Amazon Q 这类企业级集成 agent。从产品代际来看，Manus 的形态确实不是最新的。但收购的逻辑从来不是买最新一代的产品。Meta 买的是这支团队的认知水平、工程能力、用户基础和基础设施积累。产品形态可以迭代，团队对 agent AI 的理解和实践经验不会因为新一代产品出现就过期。Meta 在 2026 年 2 月已经把 [Manus 的 agent 能力整合进了 Ads Manager 的工作流](https://www.mediapost.com/publications/article/412845/meta-integrates-manus-ai-in-ads-manager.html)，这说明 Manus 的技术资产在 Meta 的产品体系里找到了实际的着陆点。

Manus 团队在 2025 年 7 月发表的 [context engineering 博文](https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus)是一个更直接的证据。这篇文章的信息密度极高，从中可以直接看到 Manus 团队对 agentic AI 的理解领先行业一个身位。它提出的三条核心原则（keep prefix stable、make context append-only、mask tools don't remove them）后来被整个 harness engineering 领域广泛引用和采纳。更重要的是，这篇文章在开头就回答了一个关键的技术路线问题：是应该基于开源模型训练一个端到端的 agentic model，还是应该在 frontier model 的 in-context learning 能力之上构建 agent？Manus 选了后者，并且用产品结果证明了这条路线的可行性。这个判断在 2025 年中不是共识，到 2026 年已经成为行业的主流做法。一篇技术博文能做到这种程度的前瞻性和影响力，本身就是团队认知水平的证明。

第二，"Manus 从头到尾就是套壳，没有技术含量。"2026 年 4 月发改委动用了[《外商投资安全审查办法》五年来的第一次"禁止加撤销"](https://www.guancha.cn/economy/2026_04_27_815117.shtml)来叫停这笔收购。如果 Manus 真的只是一个没有核心技术的套壳产品，监管没有理由用最强档位的法律工具来保护它。监管认定这家公司的核心团队、研发能力、训练数据和 IP 构成需要保护的国家安全资产。这份认定的分量，比任何技术评测或媒体争论都重。

## Cursor：唯一自己训练模型的第三方选手

Cursor 面对的套壳质疑和 Manus 类似：底层用的是别人的模型，自己只做了一个编辑器。但 Cursor 做了一个同赛道的竞品都没有做的判断，并且围绕这个判断建立了完整的技术壁垒。

### 认知差异一：判断自训模型是产品的必要条件，然后把它做出来了

编程 agent 的核心循环是高频的工具调用：读文件、写代码、跑命令，每一轮都有延迟，累积起来直接决定产品体验。Cursor 团队很早就判断，在这个场景下，依赖外部 frontier model 的 API 在速度和成本上都无法做到让开发者满意的交互体验，自训模型是产品层面绕不过去的一步。Cursor 官方博客的原话是，他们的目标是训练出一个[能支撑交互式使用的最聪明的模型，让开发者保持在编程的 flow 里](https://cursor.com/blog/composer)。

这里可能会有一个疑问：前面说 Manus 用外部模型 API 是正确判断，怎么到 Cursor 这里自训模型反而成了必要条件？区别在于两个领域的核心约束不同。Manus 所在的通用 agent 领域，核心差异化在 agent 架构和 context engineering 这一层，底层模型的能力差异被 agent 框架吸收了。编程领域不一样，延迟和成本直接决定产品可用性。两者的共同点恰恰是：都从自己领域的实际约束出发做了正确的 build vs. buy 判断。

认准了这个方向之后，Cursor 把它做出来了，而且产品体验验证了这个判断。[Composer 1](https://cursor.com/blog/composer) 发布之后，我在大量项目中用它替代了 Sonnet 4.5。体感上，大概 90% 的日常编程任务（改 bug、写 CRUD、重构、加功能），Composer 1 和 Sonnet 4.5 的完成质量没有明显差别。日常编程中真正需要 rocket science 级别推理的场景占比很小，多数时候是体力活，模型之间的能力差距体现不出来。但速度优势是碾压式的：同一个任务，Sonnet 4.5 要等一两分钟，Composer 1 几秒到十几秒就回来了。质量差不多，速度快数倍，这在高频使用场景下带来的体验差异是巨大的。这正是 Cursor 一开始做出的那个判断：编程领域的产品体验瓶颈在模型的速度和成本，不在能力上限。

做法上，Cursor 没有从零预训练一个模型，而是拿开源的 MoE 底座，在模拟 Cursor 生产环境的 agent harness 里做大规模 RL post-training，训练模型的工具调用决策和响应效率。

这里有一个常见的质疑：这不就是 fine-tuning 吗？

从 Composer 1 到 2 的五个月演进回答了这个问题。Cursor 的训练链路经历了三次迭代，每一次都不是简单的调参，而是训练方法论本身的升级。1 和 1.5 阶段的路线是纯 RL：拿开源底座做大规模后训练。到 [Composer 1.5](https://cursor.com/blog/composer-1-5)，RL 的计算量扩大了 20 倍，后训练消耗的算力甚至超过了底座预训练本身，同时引入了 thinking tokens（自适应推理深度）和 self-summarization（长上下文自动压缩）两个新训练行为。但他们发现 RL-only 路线的边际收益在递减：CursorBench 从 1 到 1.5 只提升了 6.2 分，算力却投入了 20 倍。

到 [Composer 2](https://cursor.com/blog/composer-2)，Cursor 做了一个关键的方法论转向：在 RL 之前加入 continued pretraining，改变 RL 探索的起点质量。底座换成了 [Kimi K2.5](https://x.com/Kimi_Moonshot/status/2035074972943831491)（Moonshot 官方已确认），先做继续预训练再做 RL，结果 CursorBench 一口气提升了 17.1 分。Composer 2 的[技术报告](https://cursor.com/blog/composer-2-technical-report)说得很明确：它在推理成本显著低于同级别模型的前提下达到了 Pareto 最优。换句话说，Cursor 的 post-training 链路做到的不是在底座上加一层 fine-tune 然后性能打折，而是在压缩成本和延迟的同时保持了可比的编程能力。

这个方法论的自我修正有学术上的支撑。ICML 2025 的研究（[SFT Memorizes, RL Generalizes](https://arxiv.org/abs/2501.17161)）和 Moonshot 自己的 [Kimi K2 技术报告](https://moonshotai.github.io/Kimi-K2/)都指向同一个方向：预训练建立先验，RL 在先验上做高效探索，continued pretraining 改变的是起点质量。Cursor 团队在 Composer 2 之前就独立发现了这一点并落地到产品里。

回过头来看竞品的选择。AI 编程工具领域里创业公司很多：Cline 是开源的 VS Code 插件，接各种第三方模型；Trae 是字节做的，用 Claude 3.5 Sonnet 和 GPT-4o；Windsurf 是 Cognition 做的，前身 Codeium。它们的产品差异化来自 UI 设计、工作流编排和定价策略，不来自模型能力本身。Cognition 的 [SWE-1.5](https://cognition.ai/blog/swe-1-5)（Windsurf 背后的模型）在开源底座上做了 RL，但没有走到 continued pretraining。Cline 和 Trae 完全不做模型训练。在 AI 编程工具领域，只有 LLM provider 的第一方产品（OpenAI 的 Codex、Anthropic 的 Claude Code）和 Cursor 走通了底座选型、继续预训练、RL 后训练、产品集成这条完整的四环节链路。Cursor 是第三方创业公司里唯一的一个。这些竞品不是不够努力，是没有做出"自训模型是产品必要条件"这个判断。

### 认知差异二：Harness Engineering 落地到产品

Cursor 的认知领先还体现在对 harness engineering 和 agent scaling 的探索上，而且这些探索已经直接落地到了产品里。

2026 年 2 月发布的 [self-driving codebases](https://cursor.com/blog/self-driving-codebases) 实验中，Cursor 用递归 Planner-Worker 架构让数百个 agent 并行工作，峰值吞吐量约 [1000 commits/hour，生成超过一百万行 Rust 代码](https://cursor.com/blog/scaling-agents)。这个实验解决的问题不是"怎么让一个 agent 写好代码"，而是"怎么让投入 10 倍算力获得 10 倍有意义的吞吐量"。这个问题的提出本身就领先了行业。

这个实验后来引发了一轮争议。有人去看了公开 repo，发现最近的 commit 没有一个能编译通过，GitHub Actions CI 全部失败。Reddit 和 Hacker News 上出现了大量批评，认为 Cursor 在造假。

这个批评抓到了一个真实的差距，但"造假"这个标签不准确。Cursor 在博客原文里主动讨论了这些问题。博客开头就写明这个浏览器不是给外部使用的，预期代码会有瑕疵。正文里专门分析了为什么系统设计上要接受一定的错误率：当他们要求每个 commit 100% 正确时，整个系统的有效吞吐量暴跌，agent 会越界去修不相关的问题，多个 agent 互相踩踏。博客还提到了 agent 的依赖幻觉问题（agent 拉了不该用的依赖），并解释了后续的修正方案。Cursor 不是被发现了问题然后找借口，而是在发布实验结果的同时就把 failure pattern 摆出来分析了。

这件事更合理的读法是：这是一个对 agent 空间扩展性的前沿实验，Cursor 在博客里诚实地记录了当前的能力边界和失败模式。实验产出的代码质量确实不够好，公开 repo 的状态比博客的措辞暗示的更差。但实验本身回答的问题（多 agent 并行的吞吐量 scaling 规律、错误率控制、任务分配策略）在行业里没有第二家在同等规模上探索过。

同期的 Cline 在优化单个 agent 的权限控制和工具调用流程。Trae 在优化 Builder Mode 的项目脚手架体验。这些工作都有价值，但它们回答的问题和 Cursor 回答的问题不在一个层面上。Cursor 已经在思考 agent 的空间可扩展性，竞品还在优化单个 agent 的交互质量。

Cursor 还很早就在产品中引入了 background agents 和并行任务执行，并且把这些能力直接体现在了 UI 上。当多数 AI 编程工具还在讨论单轮对话质量的时候，Cursor 已经在解决用户离开之后 agent 怎么继续工作这个更远的问题。这个产品判断在 Cline、Trae 等竞品中到 2026 年中才开始出现类似的探索。

### 回应套壳论

LLM provider 的第一方产品（OpenAI Codex、Anthropic Claude Code、Google Gemini Code Assist）投入了远超 Cursor 的资源，但 Cursor 在产品层面仍然和它们正面竞争。Fortune 杂志 2026 年 3 月的分析标题是 [Cursor's crossroads](https://fortune.com/2026/03/21/cursor-ceo-michael-truell-ai-coding-claude-anthropic-venture-capital/)，讨论的不是 Cursor 能不能跟 LLM provider 竞争，而是它怎么在 LLM provider 全面下场之后保持优势。一个真正的套壳产品不会被放在这个位置上讨论。SpaceX/xAI 出 600 亿美元也不是在买一个编辑器皮肤。

## 共同的模式

把 Manus 和 Cursor 放在一起看，共同的模式变得清晰。

第一，两个团队都在各自领域的认知上领先了行业。Manus 对 LLM 本质的理解（不做 hat wearing，做 wide research）、对 User Generated Software 的判断（创建加部署加智能注入的完整链路）、对端到端 agent 能力组合的理解，Cursor 对 post-training 链路的理解（四环节完整链路）、对 harness engineering 的理解（空间可扩展性）、对 agent 工作模式的理解（background agents 和并行执行），都早于同行至少半年到一年。和竞品的对比验证了这一点：同一时间段里，竞品在解决的问题和这两家在解决的问题，经常不在同一个层面上。这种领先不是靠堆资源实现的，是对 AI 这个介质的本质理解不同。

第二，认知领先最终转化成了结果差异。Manus 做到了 $100M ARR 和 GAIA 基准测试的领先成绩，Cursor 做到了 AI 编程工具领域除 LLM provider 第一方产品以外最强的位置。这两个结果分别被全球顶级买方以真金白银背书：Meta 出 20 亿美元，SpaceX/xAI 出 600 亿美元。

第三，两个团队都面对了套壳的质疑。这个质疑反映了一种正在过时的技术分类法。2023 年，有没有自训模型是判断 AI 公司技术含量的核心标准。到 2025 年，训练链路的设计、agent 架构的工程化、context engineering 的方法论、harness engineering 的实践能力，这些维度的重要性已经和自训模型并列甚至超越。用 2023 年的框架去评判 2025 年的产品，会系统性地低估这类公司的技术深度。

这两家公司各自面对的挑战也很真实。Manus 的收购已经被发改委叫停，路径层面的不确定性很大。Cursor 面对 Claude Code 和 Codex 的正面竞争，核心工程人员已经开始流向 xAI。挑战不改变一个事实：这两个团队在 Agent AI 时代展现出的技术判断力，在整个行业中属于第一梯队。Zuckerberg 和 Musk 的出价不是冲动消费，是对这种判断力的定价。

---

## 个人阅读笔记

### 文章结构拆解

中文互联网上对 Manus 和 Cursor 的主流判断是套壳和估值泡沫 → 作者反驳这个判断，认为两家公司真正被定价的是认知领先 → Manus 的领先体现在从 LLM generalist 本质出发，不做 hat wearing，而是做 wide research 和端到端 User Generated Software 链路 → Cursor 的领先体现在判断 AI coding 的核心瓶颈是延迟和成本，因此自训专用模型，并用 continued pretraining、RL post-training 和 harness engineering 建立系统壁垒 → 两家公司路线不同，但共同点是都从各自场景的真实约束出发做了正确的 build vs buy 判断 → 商业结果、基准成绩、收购报价和监管反应共同构成结果验证。核心论点：AI Agent 时代的技术含量不再只由是否自训 foundation model 决定，而由团队能否在模型、runtime、context、evaluation、分发和用户闭环之间找到正确的系统杠杆决定。

### 值得带走的

**套壳论的分类错误。** 这篇文章最有解释力的地方，是把套壳论暴露为一种旧技术分类法。2023 年的判断框架把技术含量主要绑定在是否自训模型上，但到 2025 年以后，agent 架构、context engineering、harness engineering、post-training、evaluation、runtime 和分发链路都成为技术深度的组成部分。一个产品即使用外部模型，也可能在运行时层和系统设计层创造实质差异。

**场景约束决定 build vs buy。** Manus 选择外部 frontier model，Cursor 选择自训专用模型，看起来路线相反，实际上遵循同一个原则：先识别场景中的主瓶颈，再决定哪一层必须自己做。通用 agent 的差异化主要在任务拆解、context 管理、工具编排和端到端交付，因此 Manus 买模型是合理的。AI coding 的瓶颈高度受延迟、成本和高频交互影响，因此 Cursor 自训模型是合理的。这个区分比自研或外采本身更值得记住。

**从角色分工到功能分工。** Manus 不做产品经理 agent、工程师 agent、QA agent 这类人类岗位模拟，而是让每个 sub-agent 保持完整 generalist 能力，只在任务层面分割。这个判断解释了为什么早期 multi-agent 系统里的人类组织隐喻容易走偏。LLM 的能力结构和人类不同，照搬人类岗位分工往往是在用旧组织形态限制新介质。

**User Generated Software 的完整链路。** Manus 的关键不是能生成代码，而是把创建、部署、分享、持续运行和 AI 能力注入放进同一个闭环。多数 agent 产品停在任务产出物，Manus 更早把用户产出物视为可分发、可运行、可继续调用智能的软件。这解释了为什么它超出了单次生产力工具的范畴，更接近 User Generated Software 的基础设施。

**Harness 和 evaluation 是新主战场。** Cursor 的价值不只是 Composer 模型，也不只是 IDE 体验，而是它把模型、工具格式、上下文策略、background agents、并行任务和 evaluation system 绑定成一个组合系统。结合 Cursor evaluation-first 的交叉阅读来看，真正值得关注的是它能否持续用 CursorBench、Keep Rate、线上 A/B、tool error baseline 等机制判断每次 harness 改动是否真的变好。

**认知领先需要结果验证。** 作者没有停留在主观赞赏，而是尝试用 ARR、GAIA、token 处理量、虚拟机数量、Composer 迭代、竞品对比、收购报价和监管反应来支撑判断。这个写法值得学习：判断一个团队是否领先，不能只看它说了什么理念，要看理念是否落进产品、用户、数据和外部买方行为里。

### 行动指导

1. **评估 AI 产品时先定位 runtime 层级。** 不要先问它用了哪个模型，而要问用户使用时 AI 到底承担了什么职责：只是回答，还是检索、调用工具、嵌入流程、自主循环、持续运行、主动触发。runtime 深度比模型名字更接近产品本质。

2. **把注意力从工具名迁移到系统杠杆。** 看一个 AI 工作流时，拆成模型、post-training、context、tool、runtime、eval、权限、分发、记忆和用户数据闭环。判断真正的瓶颈在哪一层，再决定该自建、外包还是组合现成能力。

3. **不要用人类组织结构直接设计 agent。** 设计 multi-agent 系统时，优先按功能拆分，例如 planning、execution、verification、research、summarization、judging，而不是按产品经理、工程师、QA 这类岗位命名。LLM 是 generalist，任务边界比角色标签更重要。

4. **把生成能力延伸到交付链路。** 如果做 AI 产品或个人 agent 工作流，不要只优化生成结果，还要问结果如何部署、分发、复用、监控、回滚和写回系统。生成只是链路中间的一步，能持续运行和被下一轮继承才有复利。

5. **把 evaluation 放到每次改动之前。** 换模型、改 prompt、加工具、撤 guardrail、换上下文策略之前，先定义什么叫变好。即使没有 Cursor 级别的评测系统，也至少要有代表任务、成功标准、失败样例和复盘记录。

6. **把 harness 当耗材，把验证标准当资产。** Prompt、workflow 和具体 agent 编排会随模型版本变化而过时。测试、质量标准、权限边界、上下文架构、确定性工具链和事故复盘机制更稳定，个人和团队应该优先积累这些东西。

7. **用场景约束训练 build vs buy 判断。** 每次面对新工具或自研冲动时，问三个问题：这一层是不是核心瓶颈，外部产品是否已经足够好，自研后是否能形成可复利资产。没有清楚回答之前，不要因为技术焦虑去重造 runtime。

8. **区分认知领先和宣传领先。** 一个团队提出新概念不等于领先。真正的领先要同时满足三个条件：问题抽象更准确，工程路线能落地，结果数据能验证。缺任何一个，都只是叙事优势。

### 存疑

**估值和收购意向不能直接证明技术判断正确。** Meta 出价、SpaceX/xAI 给收购选项、发改委叫停交易，都能说明这些公司具有战略价值或敏感性，但不能单独证明每项技术路线都正确。估值背后可能包含用户基础、人才密度、数据资产、地缘因素和防御性收购动机。文章把外部定价和技术认知之间连接得较紧，中间缺少更细的因果拆分。

**认知领先这个概念过于压缩。** 文中把第一性原理判断、工程实现能力、产品时机、商业增长和外部验证都归入认知领先。这个词解释力强，但可证伪性偏弱。更精确的拆法应该区分方向判断、问题抽象、系统设计、执行速度、数据闭环和商业分发，否则容易把结果好反推为认知高。

**Manus 的长期护城河仍需更强论证。** 文章证明 Manus 在 2025 年初做出了领先判断，但没有充分回答这些判断是否能持续转化为长期优势。端到端 agent、部署分发、wide research 很快会被头部厂商吸收。若长期资产主要在数据外化、用户工作流、基础设施和团队 know-how，文章需要更明确地区分哪些是可复制功能，哪些是可复利资产。

**Cursor 的 agent scaling 实验需要 evaluation 补强。** self-driving codebases 展示了空间扩展性的探索价值，但公开 repo 编译失败和 CI 失败说明吞吐量本身不是质量。文章承认这不是造假，但仍然把它作为认知领先的重要证据。更严谨的论证应进一步说明 Cursor 如何通过 evaluation 区分有意义吞吐量和错误放大。

**套壳论被反驳，但替代标准仍在形成中。** 文章指出自训模型不是唯一技术含量标准，这是对的。但新的标准应该如何加权仍未完全展开。模型训练、post-training、harness、context、eval、数据闭环、分发入口各自的重要性会随场景变化。没有场景化权重，新的多层技术框架也可能变成另一种泛化判断。
