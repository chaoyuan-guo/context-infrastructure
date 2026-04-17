# 为什么AI只会说正确的废话，以及怎么把它逼出舒适区 

> 来源：<https://www.superlinear.academy/c/ai-resources/context-infrastructure>
> 作者：Yan Wang 鸭哥
> 发布日期：2026-03-16
> 平台：Superlinear Academy

---

三周前，OpenAI发了一篇关于Harness Engineering的博文。我和社区里一个很厉害的朋友老王各自让自己的Agent做了一份深度调研。我们特意用了同档次的LLM（Claude Opus 4.6 vs GPT-5.4），同一个调研skill，同一个搜索工具Tavily，同一个agentic后端OpenCode，甚至同样的prompt，唯一不同的是两个Agent背后的context：我的Agent接入了我过去一年积累的判断框架和认知体系，老王的Agent没有。结果两边的AI给出了风格完全不同的分析。拿OpenAI和Cursor在harness架构上的收敛来举例：

> **第一种报告（行动建议部分）：** 先做知识底座，再做更强agent。给仓库建立清晰的AGENTS.md目录索引；把产品规则、架构规则、执行计划、质量标准写进repo；用CI检查文档freshness和cross-link completeness。
> 
> **第二种报告（同一话题的分析）：** 完美主义是吞吐量的敌人。OpenAI采用最小阻塞合并、后续修复的策略。Cursor发现要求100%正确性会导致系统停滞，接受小而稳定的错误率反而更高效。两者都接受了「纠错比等待便宜」的权衡。

差异在哪？第一种给了一份checklist：正确、安全、换任何人来问AI都能得到差不多的东西。第二种给了一个insight：跨两个不同来源提炼出一个有立场的判断（完美主义是敌人），并归纳出底层权衡（纠错比等待便宜）。一个是搬运工，一个是分析师。两篇完整报告可以在这里对比：[第一种报告](https://challenwang.com/essays/harness-engineering-survey-20260313.html)和[第二种报告](https://yage.ai/share/harness-engineering-survey-20260312.html)。

如果你回忆一下自己用AI做分析性工作的经验，大多数AI的产出其实都像第一种报告：找不出明显的错误，但读完之后没有任何启发。属于正确的废话。第二种极其少见。这种普遍的平庸来自一个LLM训练的底层原因。

## LLM的Consensus天花板

这个原因是：LLM被训练的方式就决定了它的默认输出是consensus（共识）。

LLM训练的本质是next token prediction，它的意思是：每一步输出概率最高的token。概率最高意味着最多人会认同，也就是consensus。RLHF在这个基础上更进了一步：安全对齐专门惩罚有争议的、带有强烈立场的输出，鼓励平衡、全面、没有明显偏向的回答。两层机制叠加，LLM的默认行为就是回归均值。

这个默认行为导致了一个相当严重的缺陷。比如过去两年认知方向最火的产品是Deep Research，但仔细看它做的事情：自动化的高频搜索，多文档综合，扩大信息覆盖面。这其实和都Deep没有关系，充其量是Wide Research。换言之，Deep Research是一个非常有误导性的名字。它解决的问题是**信息**不对称：你以前不知道的，现在知道了。但是真正的深度来自另一个维度，来自**认知**不对称。面对同样一份行业报告，一个从业二十年的老兵和一个刚入行的新手看到的东西完全不一样。老兵的优势在于他有一套经过多年试错沉淀下来的认知系统，知道哪些数据是噪音，哪些异常值预示着趋势。小白没有这个滤镜，就算拿到10倍厚的报告也没办法做出同样质量的决策。

这就是为什么你很少听到有人说「用了AI之后我有了以前从来没有过的深刻判断」。AI可以把一个小白提升到大众平均水平，因为它的训练数据就是大众平均水平的压缩。但对于已经在平均水平之上的人，AI的consensus输出对他的判断几乎没有增量。深刻的定义本来就是非共识，而非共识恰好是LLM被训练去规避的方向。

但是，这个gap意味着一种浪费，一个机会。AI只能输出consensus的话，你就没法把真正的thinking委托给它。不说AGI之类的长远前景，就看日常应用，它能当秘书帮你整理信息，但是当不了顾问/教练，帮你做判断。[之前的AI管理系列文章](https://yage.ai/ai-management.html)里讨论过这个区别，但那时还没有找到系统性的突破口。

那突破口在哪？

## AI已经从CPU Bound走向Memory Bound

面对AI说正确的废话，大家的直觉是去优化模型：换更好更贵的模型、改更复杂的prompt、加更完备的工具，Multi-Agent、Harness全给它整上。这些做法都在优化同一个维度：模型的智能。

但是开头的实验已经告诉我们答案了。两边的模型智能几乎一样，工具一样，prompt一样。唯一不同的是context：第二种报告背后有一年积累的判断框架，第一种没有。结果一个输出checklist，一个输出insight。

变量只有一个，结论很显然：（在模型智能跨过一道坎以后）决定产出性质的是context，而不是模型的智能。其实这种转变在计算机历史上发生过：CPU快到一定程度之后，继续升级CPU就没有意义了，主要的提升都来自内存架构。而LLM现在到了同样的拐点。

这个判断是反直觉的。这是因为一说起AI，大家第一反应就是模型。我们经常看到模型升级了，却从来没看到过context升级了这种说法。但这个不对称本身就揭示了一个更深刻的趋势。每次模型升级，智能就更便宜一点，你用的模型别人也能用。但你的context是只属于你的，模型升级不会让它贬值。所以持续投入在一个不断贬值的维度（模型智能）上，收益递减；投入在一个不贬值的维度（个人context）上，收益累积。

既然瓶颈在context，那要突破consensus天花板，就需要用足够密度的个人认知上下文压过训练时的consensus prior。几句话的system prompt做不到这件事。你的品味、你对优先级的直觉、你在某个领域反复验证过的判断框架，这些东西是高维的，散落在过去无数次决策和反馈里，几句话根本说不清楚，而需要一套系统来采集和精炼。

## 怎么把LLM从Consensus的舒适区域里面逼出来

为了实现这个目标，我花了一年时间，逐渐构建了一整个系统，发展为三个互相支撑的要素。每一个要素都在回应一个具体的问题。

### 大量积累

第一个问题是：你的认知框架到底是什么？

这个问题看起来简单，实际上非常困难。厉害的人通常说不清楚自己哪里厉害，就算能说上来，往往也是错的。很多他觉得「没什么大不了」的肌肉记忆一样判断，恰恰是他最独特的地方。这部分一定要一个第三方才能捕捉到。

所以捕捉Context的起点是采集客观的行为数据，而不是单单靠自己写prompt。我持续了一年相关实验，包括[录音转写](https://yage.ai/life-api.html)、会议记录、[微信对话导出](https://github.com/grapeot/wechat_db_parser/)、和AI的每次对话、每次纠正甚至发飙，都[积累成了本地文件](https://yage.ai/stop-using-chatgpt.html)。这些是我们在真实决策场景下展现出来的判断逻辑。

注意，我们自己很难从里面提取模式，因为我们太接近它了。这往往需要一个旁观者来看，AI在这件事上是个合适的旁观者。因此，我把所有数据放在同一个文件夹里，AI打开就能看到所有内容，对任何项目做cross-reference。这是context density的基础。

### 分层提炼

第二个问题是：原始数据里那么多噪声，怎么把信号找出来？

你今天做的某个决策可能是因为没睡好，可能当时信息不全，也可能就是随机选的。如果把原始数据直接给AI（比如[Mem0](https://mem0.ai/)的做法），AI面对的解读空间太大了。一个具体事件可能体现了很多不同的原则，有些决策甚至是arbitrary的。因此，我们需要一个精炼过程。

这里我用了一个非常简单的筛选标准：稳定性。一个判断如果是跨场景、跨时间反复出现并保持一致的，它大概率是我们认知结构的一部分。不稳定的是情境反应，稳定的才是我自己。

[受OpenClaw启发](https://yage.ai/openclaw.html)，这个精炼分为三层。L1 Observer每天扫描文件变动，提取有意义的观察，写个流水账。L2 Reflector每周合并重复、清理过期信息、识别跨项目模式，负责把信号和噪声分离。L3 Axiom从稳定模式中蒸馏决策原则，只保留真正代表你的东西。经过了一年的积累和几周的精炼，目前我的系统里积累了44条axiom，覆盖我的技术选择、沟通风格、商业判断等等主观偏好。

这里我们和Mem0等等流行记忆系统的核心区别在于蒸馏的深度。Mem0蒸馏到事实层就停了：「你偏好TypeScript」「你住在上海」。但是我们的系统继续往上走，蒸馏到判断原则层：「评估技术方案时，你怎么权衡可维护性和性能，优先级排序是什么」。事实告诉AI你是谁，判断原则告诉AI你怎么想。让AI产出从consensus变成non-consensus，需要的是后者。

### 按需加载

第三个问题是：这么多context，怎么给到AI？

全部塞进去是不行的。Context window有限，而且无关信息会稀释有效信号。一个写代码的任务带入所有的商业判断原则没有意义，一个做调研的任务也不需要加载代码架构偏好。

解决方案是现成的skill系统：每个skill是一个针对特定任务类型的context子集，包含这类任务最相关的axiom，判断标准，和常用工具。做调研时加载调研的分析框架，写代码时加载架构原则和审阅偏好。这和CPU的内存层级也是类似的：L1 [cache是AGENTs.md](http://xn--cacheagents-c98w.md/)，L2对应skill库的索引，告诉AI如果需要什么信息的话往哪找，L3则对应具体的skill文件。按需加载，渐进披露，每层只在需要的时候被调用。

### 循环

三个要素运行起来之后，一件有意思的事情发生了：知识产品开始涌现，而每个产品在消费context的同时也在产生新的context。

[鸭哥AI手记](https://daily.yage.ai/) 是基于这个上下文系统写的每日AI行业简报，每一期都在消费axiom和skill，同时产出新的观察进入observation库。具体的[领域调研报告](https://www.superlinear.academy/c/news/) 是带判断标准的深度分析，每篇报告在生产过程中同时也在更新相关领域的认知框架。这两个系列的报告质量都很高，被大家广泛订阅和转发。这证明了循环可以在足够高的context density下自然形成，在持续运行中不断保持活力。

这个系统的本质是把你的bias注入AI。有品味的bias是深度的来源，但bias也可能是质量不高的偏见。不过把bias显性化这个过程本身就很有意义。在没有这个系统之前，你的bias散落在决策里，你意识不到它的形态，甚至存在。经过采集、精炼、蒸馏之后，你能看到自己面对某类问题时倾向于优先考虑什么、倾向于忽略什么。这种自我认知的进步，单独就有价值。

回到开头的实验。老王的AI输出consensus，因为它能看到的context几乎是空的，训练时的prior没有被任何个人认知覆盖。我的AI输出有判断力的分析，因为它有一年积累的判断框架在背后。同一个模型，context density不同，产出的性质就不同。

### 开源的参考实现

但是注意，这个系统需要时间积累，需要一定的技术能力，需要持续维护的意愿。但换一个角度理解这个成本：「改一下system prompt就让AI瞬间懂你」或者「换一个更好的模型就够了」，这些捷径从原理上就走不通。Consensus prior太强，几句话压不过去，换模型只是换了一个consensus的来源。对于一个这么重要的问题，it deserves a system。从源头采集、分层精炼、按需加载、循环更新，每一步都有它的理由。并不简单，但特别有帮助。

我们把这个系统的完整结构开源了：[github.com/grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure)。这个repo是一个参考实现，包含了我们实际在用的44条axiom、核心skill文件、三层记忆系统的代码、以及文章里提到的所有组件。

需要说清楚的是：这个repo的主要价值是让你看到一个运行了一年的系统长什么样，而非让你克隆下来就能直接用。你可以打开它跟AI对话，问「这个观点鸭哥会怎么看」，立刻体验到有context和没有context的差异。但要想让AI真正变成你自己的，没有捷径。你需要从头开始采集你的行为数据，设置你自己的计划任务，让系统从你的决策历史中蒸馏出属于你的判断原则。别人的skills是别人的视角，参考可以，替代不行。

## 偏见与硅基大脑

总之，AI变得更聪明，并不自动让它变得更深刻。更聪明的consensus依然是consensus。突破天花板的路径只有一条：注入非共识的视角。

每个人都有自己的非共识视角。你的判断标准，你的审美偏好，你从失败中提炼出的教训，你对什么重要什么次要的直觉。这些东西在AI的训练数据里不存在，永远不会被任何版本的模型自动学到，因为它们只属于你。

硅基大脑的绝对客观最终只能抵达聪明的平庸，能将其重塑的，唯有你积累数十年、充满偏见与品味的人类灵魂。


---

## 评论区

### Vivi Zou
*2026-04-15*

写的真好呀，最近也在思考，以后世界需要什么样的人，构建自己独特的个性和审美，这些变得异常重要

---

### Alfred
*2026-04-13*

鸭哥，看到你很多次在blog里提到了一个群聊？想知道怎么加入，想一起讨论问题。

**↳ Yuanchang** *2026-04-13*

同问

**↳ Yan Wang 鸭哥** *2026-04-13*

这是一个微信群。人已经满了，但是里面大多数的讨论我们都已经蒸馏了出来，发在社区的 DeepNews 和 Knowledge Bank 两个模块里面。如果感兴趣的话也可以订阅这个 newsletter。[https://daily.yage.ai/](https://daily.yage.ai/)

---

### 提姆
*2026-04-13*

一个直观感受taste这个事情一定是跟自己高度相关的。最后一段对于非共识还有个理解是非共识往往是要有自己的原则驱动的，这个需要足够的数据集积累。鸭哥开源的下载到本地跟自己的系统做了一下深度耦合，效果太棒了！

---

### Nana
*2026-04-06*

这篇太神了！值得反复精读！

---

### Corrine Zou
*2026-04-02*

感觉鸭哥的分享！这对我的启发实在太大了。
我理解这个context的架构，本质可以应用在不同领域搭建知识库。
最近在思考如何做一个系统可以把我工作经验提炼转化，并帮助我进行数据分析，达到一个可以交付的分析报告。一直被经验知识如何提炼转化卡住。
鸭哥的文章是指明灯，给了一个可以持续探索的方向。😄

**↳ Yan Wang 鸭哥** *2026-04-03*

很高兴有启发！

---

### Karry Wang
*2026-03-30*

感谢鸭哥分享，很有启发，已经在本地配置上了！

有一个问题请教，对于自己的项目文件，是推荐放在这个目录内还是目录外呢？因为如果放在目录内，每天的自动扫描会扫到很多项目的代码变动，可能对于记忆的更新并没什么帮助。如果放在目录外的话，又用不到目录本身的context。想看看有没有推荐的做法～～

**↳ Yan Wang 鸭哥** *2026-03-30*

我是都放在目录内的，但是扫描的时候只扫描 MD 文件。

**↳ Karry Wang** *2026-03-31*

好滴，谢谢～

---

### Tina Wang
*2026-03-30*

，我又有一个问题，我发现你把skills放在了rules下，而不是.claude或.opencode下，这样做，我猜是为了减少token读取skills的消耗，我知道OC还不能做lazyloading。但同时，也失去了让LLM自己主动调用skills的机会。

不知鸭哥是怎么想单独存workflows，还是直接生成skills

**↳ Yan Wang 鸭哥** *2026-03-30*

你的观察很敏锐。我这么做是两个原因：

第一是不希望做平台绑定，放到 .cloud 下面只有 cloud 能用，codex 用不了，放到 .opencode 下面只有 opencode 能用，cloud 用不了。

第二是，不喜欢 Anthropic 的 skill 设计，它的设计其实特别面向编码，比如元数据的格式一定要写成一个特定的 YAML 文件，由 claude code 在一个黑盒里进行 parse，然后注入到 context window 里面去。

这件事情很符合直觉，如果一个码农来写代码他就会写成这样，但是并不 AI-native。在 AI 时代更关键的是，让 AI 有自己的主观能动性，动态地决定我去读什么 skill，而不是用代码来决定。

这是为什么我选择了现在这种让 AI 自主通过读取文件来做 lazy loading 的方式，或者直接回答你的问题，这样恰恰是为了让 LLM 能够自己决定调用什么 skill，而不是像 claude code 那样用程序去把所有 skill 的 yaml parse以后 注入进去。

---

### tomwong
*2026-03-29*

我是非技术背景，目前主要是用kiro把自己软件项目需求写进去，vibecoding开发。日常用deepseek、豆包都有、claude的客户端、微信、邮件都用的很多，怎么把我的日常这些都接入到项目中？小白问题，请各位资深的专业人士帮忙解答😊😊

**↳ Yan Wang 鸭哥** *2026-04-03*

我的建议是就用Claude的客户端，用它的cowork或者code功能作为hub接入所有的东西。这样你也可以做vibe coding开发，也可以读到你本地的项目文档，也可以和邮件用connector接上。微信可能比较难搞。

---

### Mandy
*2026-03-27*

很棒的分享，我日常也在自己的agent在做自我本体蒸馏哈哈。不知道调研报告部分的测试prompt可否分享下，想对比下自己agent的表现~

**↳ Yan Wang 鸭哥** *2026-03-27*

都分享在文章里提到的github里啦～

---

### Tina Wang
*2026-03-27*

，我在建立L1/L2的记忆系统，发现通过py和OpenCode Server说话不是很稳定，我用opencode run “prompt.md”代替，然后将这个sh放在crontab里运用。想问下为什么选择OC的API来实现呢？

**↳ Yan Wang 鸭哥** *2026-03-27*

这有好几个原因。第一opencode的架构就是服务器端-客户端架构。用opencode命令行，本质上也是在用web api在和后端通信，其实区别不大。第二是好像是在mac上它的命令行有点bug，不支持设置了密码的server。这是我为什么用api的原因。我的claude code和codex用的还都是命令行～

**↳ Tina Wang** *2026-03-27*

谢谢鸭哥，我再测试几周命令行，看看稳定性。关于记忆系统，龙虾的日记+周报+semantic sesrch的形式鸭哥怎么看。

我积累了几天observation，发现很多都是stale的，比如我今天改成A，明天改成B，一周后又改成C。ABC互相矛盾，这种全部context给LLM让他reason的成功率，比起结构性的daily entry，然后扫no of day再提取公里的模式。这之间的选择，想去听听你的意见。

**↳ Yan Wang 鸭哥** *2026-03-28*

这是蛮常见的，因为迭代的过程中肯定会有从 A 到 B 到 C 的历史。这个就可以让 Reflector 干两件事情：第一是只记录最新的状态，保持我们的 memory 和最新的状态相吻合；第二是尤其关注稳定下来的东西。就是迭代中的东西，就说明它还没有形成稳定的个人偏好，根据文章里的叙述，它的优先级就不高。我们的 Reflector 尤其关注这些长期稳定的个人偏好，这些是最有用的。

---

### nz
*2026-03-25*

感謝鴨哥的文章解答我之前使用AI時，常常覺得沒有「得到洞見」的疑惑和失落：為共識而訓練出的模型是沒法主動給出非共識的。

很喜歡最後一句話的總結！

---

### DJ
*2026-03-23*

做一个长期记忆系统，很有借鉴意义

---

### Tina Wang
*2026-03-17*

太感谢了，可以把我自己的work-os转到yage的repo clone里了。请问鸭哥，平时都怎么用这个repo，你会开一个opencode session，直接在这个repo里工作么？

**↳ Yan Wang 鸭哥** *2026-03-23*

是的，其实我所有的 opencode session 全都是放在这个 repo 的根目录的，然后用它的 web 界面就可以非常方便地用手机管理多个 session，配合 iOS client 和 Android client 效果更好。
[https://github.com/grapeot/opencode_ios_client](https://github.com/grapeot/opencode_ios_client)
[https://github.com/grapeot/opencode_android_client/](https://github.com/grapeot/opencode_android_client/)

**↳ Tina Wang** *2026-03-23*

请问鸭哥，这个oberservation文件，不会随着时间的推移，越来越大么？他看起来却每次都generate一些文字呀

**↳ Yan Wang 鸭哥** *2026-03-23*

是的observation会增大，但实际的影响其实还好。有两个原因：1. observation只是一个中间层，不会被AI直接使用，它只是用来生成axoim这一层的。2. 我们的reflector也会定期缩减/删除不重要的observation。

**↳ 免疫蛋白** *2026-03-26*

你好。我在第一步**1a. 填写 ****[USER.md](http://user.md/)**结束后，在claude code里“介绍一下你对我的了解”。它并不能输出期待的结果。我必须要说“介绍一下你对我的了解，基于USER.md”，它才能输出期待的记过。我的claude code是在context-infrastracture的根目录下。这样是expected的吗？谢谢

**↳ Yan Wang 鸭哥** *2026-03-26*

这个可能是 expected 的，因为 Claude Code 它加载的是 [claude.md](http://cloud.md/) 而不会自动加载 [agents.md](http://agents.md/)。Opencode、Cursor 和 Codex 应该都没有这样的问题。我的建议是把 [agents.md](http://agents.md/) 做个软链接或者拷贝一份叫 [claude.md](http://cloud.md/)，它应该就知道了。

**↳ guochaoyuan** *2026-03-27*

鸭哥，我再追问一个很细节的问题。

对于一些比较正式的项目，在做重度编码和复杂架构时，肯定是得在项目专属目录里开 session 更合适吧？

那这样又会带来一个问题：正式项目里的 session 怎么继承你这个 context repo 里的长期认知资产？以及项目里新产生的经验，又怎么回流到这个 context repo？

我理解这些操作还得依赖人主动去触发，想听听鸭哥实际的 workflow。

**↳ Yan Wang 鸭哥** *2026-03-27*

对于一些比较正式的项目，在做重度编码和复杂架构时，肯定是得在项目专属目录里开 session 更合适吧？

好奇这个有什么特别的原因或者试了有什么痛点吗？为什么这么想呢？

**↳ guochaoyuan** *2026-03-28*

我有疑问的点主要是如果默认在 context repo 根目录开 session，那这个 session 应该不会默认加载某一个具体项目自己的 [AGENTS.md](http://agents.md/)，除非我们在新开 session 后先明确清楚我们要做哪个具体项目了，这在针对某个项目重度编码（可能会频繁新开 session）时会显得不太方便。

简单来说，我的疑问点主要就是怎么能尽量自动的利用好 context repo 中积累的认知资产，又能在开展具体项目时减少切换摩擦

**↳ Yan Wang 鸭哥** *2026-03-28*

懂你的问题了～这个比较简单，就是在根目录的agents.md里面明确说，当你到了一个repo或者项目里面，你先看一下它自己的agents就可以了。

那怎么验证这个有没有生效呢？我做了个小实验。我在某一个项目的agents.md里面加了一条，说你下面都要用全大写的英文跟我对话，然后直接在根目录跟它说你去看一下那个repo，然后给我解释一下一个什么问题，然后下面它就用全英文给我解释了。

![image](https://app.circle.so/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCS3FvWHdrPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--6eea74734103fea8e7d76ebcfbe42992bf9eec80/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJNEJEQTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--7535ef66ff04b52d1ea165e904a77a64f9cc7389/67A7A704-2243-4D5F-9288-194D91A3E335.png)

![image](https://app.circle.so/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCTFdvWHdrPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--d949d5f06180191f324e4e3968024f2a2fd449eb/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJNEJEQTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--7535ef66ff04b52d1ea165e904a77a64f9cc7389/8DE1DE67-EB94-4970-A1FD-8CCBF9A18055.png)

**↳ guochaoyuan** *2026-03-29*

明白了，感谢鸭哥解答～

---

### Alfred
*2026-03-17*

鸭哥我有几点疑惑，可能是蠢问题：
1 context 不够好的人，怎么用这个框架呢？ 比如说我本身还在积累，很多领域我没有足够的决策样本，我蒸馏出来的是judgment还是我个人的误见？
2 精英共识的位置。我在使用很多产品的时候，发现每家产品其实就体现了团队的consensus。 比如Claude code，在system prompt，tool，每次新功能发布，甚至训练模型本身，都能体现出，这是Claude code 团队内部顶尖工程师凝结的精华。 对我来说，我直接理解，用，学习他们的方式，可能是ROI更高的路径。 如果我要加个人context，只加（我的偏好？我的价值和审美？）
3 bias 滑坡。比如axiom 涉及的领域缺乏快速反馈，第二个场景是做内容生成而非决策。

**↳ Alfred** *2026-03-17*

哈哈哈，写的时候就清晰多了，后面把鸭哥repo 下了下来，直接问了repo，有了反馈，但还是想听听鸭哥本人怎么说的。 来看看是否有差异。

**↳ Yan Wang 鸭哥** *2026-03-23*

都是很好的问题！

1. context不够好,可以直接使用repo里面的axioms。比如你就把它当做一个start point。如果你觉得有些context用得不爽,你就可以让AI去改,这样就有了一个非常好的start point。

1. 这些共识我们反正改不了,它就一直在那里。所以我们什么都不用做，就在以它们做基础了。当你觉得什么东西在你的应用场景下水土不服的时候再改。
2. 这个我觉得不用特别担心,或者说,它是一个优先级在蛮后面的担心。当然如果你要有非常直接的发现这个问题很重要,要立刻解决,我们也可以探讨一下具体的场景。

---

### 轶静
*2026-03-17*

以及好奇，我们各个地方的各种信息，怎么能够自动地喂给这个系统呢？ 

尤其是和 AI 的 conversation，我觉得这个非常有价值。

但是，比如说 ChatGPT 的这种 conversation history 好像不是很好爬取和批量导出。应该怎么解决这个问题呢？

**↳ Yan Wang 鸭哥** *2026-03-17*

首先对你的问题，ChatGPT有个邪招可以导出，就是

[How do I export my ChatGPT history and data? | OpenAI Help Center](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data)

但是我觉得解决方法是不用ChatGPT，不开玩笑：**#用好AI的第一步：停止使用ChatGPT**

**↳ 轶静** *2026-03-17*

感谢分享！已经不用了🤣。

但目前还有一个点很依赖的就是，GPT 的TTS模型确实做得很好，目前我用 Claude Code 最大的限制就是它没有办法在 terminal 语音读出我的 output🤔

**↳ Yan Wang 鸭哥** *2026-03-17*

这个确实！不过我猜可以换成opencode或者codex这种开源的，然后让AI给你写一个～不过确实不是开箱即用比较麻烦～

**↳ Alfred** *2026-03-17*

配一个stop hooks 试一下？

**↳ Roy Chung** *2026-03-17*

看了你這篇文章 **#用好AI的第一步：停止使用ChatGPT** 之後，再去review 一下AI Builders and Agentic AI 兩部份課件，已經在剛剛兩周內幾乎完全脫離Chat GPT, 現在已成cursor 的重度用戶。但是，真的還有機會是在用手機上使用Chat GPT 與AI進行溝通。例如，我早餐和午餐的前後時間也會找Chat GPT查詢，記錄，和calibrate當時的進食安排和策略。這是在廚房實時生成的。  所以怎樣自動化把從手機那邊生成的conversation導入context library 就是我需要解決的問題。你有什麼建議或者替代方案？謝謝

**↳ Yan Wang 鸭哥** *2026-03-18*

这个问题特别好。而且这exactly就是为什么我做了OpenCode Client的原因。基本的思路是你可以在电脑上跑一个OpenCode Server，然后用这个App连到电脑上，这样你在手机上随时随地就可以用OpenCode/Cursor/Codex了。我争取近期出一个视频教程出来。

iOS:

app：[https://testflight.apple.com/join/2cWrmPVq](https://testflight.apple.com/join/2cWrmPVq)

代码：[https://github.com/grapeot/opencode_ios_client](https://github.com/grapeot/opencode_ios_client)

Android：

apk：[https://github.com/grapeot/opencode_android_client/releases](https://github.com/grapeot/opencode_android_client/releases)

代码：[https://github.com/grapeot/opencode_android_client](https://github.com/grapeot/opencode_android_client)

**↳ Zhidong Sun** *2026-03-18*

今天正好也在想cursor或者open code也需要一个可以随时随地沟通和跟踪进度的工具，结果鸭哥都已经做出来了，真是太赞了

**↳ Er Shen** *2026-03-18*

我也是同样的使用场景。生活的coversations或者quick questions还是用到chatGPT。我想，所有场景融合到一个输入和系统里是肯定要发生的，openai可能已经在做这类的事情了。对于我们现在而言，要么等等，要么自己建一个pipeline，无论语音，文字都先通过这个层，统一汇总到AI可以access的一个文件系统，然后再走鸭哥讲过的分析-总结-分类-归纳成mds。

**↳ Er Shen** *2026-03-19*

可以试试折衷的方案。Codex App介于ChatGPT和Codex CLI两者之间，我这个星期在试用。它保留了ChatGPT的基本界面又添加了文件（记忆）和Skills的管理功能。

**↳ 村里小伙** *2026-03-22*

每个Axiom是不是也可以设定一些类似于evolver的信号的东西。这样agent看到这些就能条件反射地去看这些Axiom

**↳ Er Shen** *2026-03-22*

我越来越相信类似于自我演进和迭代的核心知识架构这样方法论。我想强调的是，人类和AI的一个最大不同是，人类的知识容量是有限的，知识学习是一个不断学习和遗忘更新的过程，而AI的预设知识是无限的（相对人而言），和人类学习有本质的区别，它是一个引导（点亮）的过程。这就是为什么promting以及高级prompting(skills)越来越显示出在应用上的核心驱动的地位。

**↳ Yan Wang 鸭哥** *2026-03-23*

现在是有这样的机制的，可以看看

[context-infrastructure/rules/axioms/INDEX.md at main · grapeot/context-infrastructure](https://github.com/grapeot/context-infrastructure/blob/main/rules/axioms/INDEX.md)

---

### 轶静
*2026-03-17*

感谢分享。我刚好在做类似的事情，把过去10年所有的笔记加起来一共100多万字。喂给AI确实真的能够获取很多很多意想不到的自我觉察。

鸭哥提出的这个三层的记忆结构，正好解决了我想解决的问题。 

不过一个想法是，我真的想让这个系统变成我自己的吗？因为我并不觉得我比鸭哥聪明，所以可能不希望我得到的结果充满了我自己的 bias哈哈

---

### 蒋林林儿
*2026-03-16*

看完这期帖子再回过去看鸭哥之前写的openclaw爆火分析，openclaw值得借鉴的地方在这里面都有了。今晚继续学习ai builders课程！努力奋斗！

---

### 立正
*2026-03-16*

![image](https://app.circle.so/rails/active_storage/representations/redirect/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaHBCS3FvWHdrPSIsImV4cCI6bnVsbCwicHVyIjoiYmxvYl9pZCJ9fQ==--6eea74734103fea8e7d76ebcfbe42992bf9eec80/eyJfcmFpbHMiOnsibWVzc2FnZSI6IkJBaDdDRG9MWm05eWJXRjBTU0lJY0c1bkJqb0dSVlE2RkhKbGMybDZaVjkwYjE5c2FXMXBkRnNIYVFJNEJEQTZDbk5oZG1WeWV3WTZDbk4wY21sd1ZBPT0iLCJleHAiOm51bGwsInB1ciI6InZhcmlhdGlvbiJ9fQ==--7535ef66ff04b52d1ea165e904a77a64f9cc7389/67A7A704-2243-4D5F-9288-194D91A3E335.png)

**↳ Er Shen** *2026-03-16*

Cool! 适合印在T-Shirt上。

**↳ 立正** *2026-03-16*

就是我们ai builders hoodie的背面图案！

---

### Er Shen
*2026-03-16*

非常棒的文章，我看到了一个AI下的知识体系的雏形。如果人类只是AI智能的引导层的话，这些知识的抽象就是引导层的模样。我在周末和ChatGPT讨论了如何构建AI下的个人或公司知识体系，我的初始问题是： Is intelligence only the abstract of knowledge? 这对于人类显然不是，因为知识学习到抽象，行动，结果，反馈再抽象再学习是一个费时费力的过程。而对于AI，知识的抽象有可能就是它行动需要的全部，它在行动-反馈-总结-再学习再抽象上，只要算力足够，它不费力，不倦怠，不被情绪困扰。再考虑到AI已经压缩到模型里的无所不包的知识库，它的学习也不是学习而是一点激发性的“引导程序”。我和chatgpt的讨论一直延伸到人类的知识体系和AI知识体系的交错和衔接问题，最后的结论是我们需要建立一个AI和人类共享共生的知识分享系统…知识的抽象或许就是核心。

**↳ Yan Wang 鸭哥** *2026-03-23*

我觉得这是一个非常好的想法。

而且有一个很有意思的地方是，AI需要的是知识的抽象，但是当我们build the infrastructure以后，AI其实是实践知识的抽象的特别好的渠道。

这是什么意思呢？比如公司里有一个org，org里现在要推行某种culture，我们就随便举个例子，bias for action好了。在AI时代之前，我们贯彻、宣传这些culture的主要方法就是开会和role model，比如在公司大会上反复强调这个culture，或者让senior IC以身作则带头贯彻这个culture。

但是有了AI之后，完全可以把这种抽象的文化编码到它的prompt里面。这样当你每次写代码的时候，它突然蹦出来说：你这里能不能bias for action？你处理会议记录的时候，它蹦出来说：你这里能不能bias for action？你给客户打完电话复盘的时候，它蹦出来说：这里能不能bias for action？就可以非常有效地把一些非常抽象的culture和standard practice给贯彻下去，变成实际的输出。这个是我觉得特别有意思的一点。

**↳ Er Shen** *2026-03-23*

bias for action这个说法很棒。那些新员工的公司介绍会，那些发全公司的文件/email，那些领导发言，那些公司年会…想努力灌输的其实就是公司文化。公司文化就像大学校训一样，就那么几句话，甚至是几个字，但是为什么要反复讲，天天讲，其实就是人类的自我意识带来的损耗让这种bias for action无法贯彻。如果把公司作为一个商业机构来看，它应该是一个可建模，可预测，可反馈-改进的“有机体”，其根本eval指标是明确的，就是利润-money。而公司拼命想做的是把个体的意识打磨淡化，组合成一个更有效运行的个体。从这个角度来看，Agentic AI的商业应用确实非常宏大，而大公司里被异化的员工也需要被解放出来，真正成为为自己而活的人。当然，最后失业问题，生活的意义问题也是需要我们花费很久时间来重塑的东西。

**↳ Yan Wang 鸭哥** *2026-03-23*

是的是的！很深刻的见解！

**↳ Tina Wang** *2026-03-24*

重启一个semantic search的话题，请问  ，为什么选择自己写semantic的代码，而不是用现成的package呢，比如最近小火的 qmd https://github.com/tobi/qmd，好奇这里有什么衡量么？

**↳ Yan Wang 鸭哥** *2026-03-25*

这是个很好的问题。

QMD它主要是三个核心功能或者说组件：

一个是Plaintext Search，用的是BM25这种经典算法；

一个是Semantic Search，用的是Embedding Search这种方式；

一个是LLM Re-ranker。

但是在我们的场景里，因为我们本来就是通过LLM调用的，所以Re-ranker这个已经包含在我们的架构里了。同时因为我们会用Grep这个工具去做Text Matching，所以BM25这个组件也已经包含了。

所以如果我们直接把QMD拿过来用的话反而得不偿失。一方面它会造成功能冗余，另外一方面冲突可能是更重要的。会让我们的AI困惑：我到底应该用它去做Plaintext Search，还是说应该用我们自己的Grep或者RG Tool，或者我应该用我的LLM去做Re-rank，还是用它的LLM去做Re-rank，就会有很多困惑。

因此我们真正需要的并不是一个完整的像QMD这样的工具链，而是把整个系统唯一的短板也就是Semantic Search补上就可以了。而且Semantic Search也是一个二十年历史的东西了，一点技术含量都没有，现在基本上几行code就可以写出来。

这是我们为什么自己写了个CLI的原因。

---

### 村里小伙
*2026-03-16*

OpenAI的harness Engineering中也是把软件的架构放到context中，这也是一种较为抽象的知识框架，用不了多少token，就能使模型对软件的认识更深了。感觉模型更需要抽象，浓缩的知识，而不是细节，小点。

---

### qp
*2026-03-16*

好奇原始的prompt是什么，我也想去试试我的AI会返回什么结果

**↳ Yan Wang 鸭哥** *2026-03-16*

我的prompt：

[https://openai.com/index/harness-engineering/](https://openai.com/index/harness-engineering/)

我觉得这是一个值得放到 survey 类或者说 survey sessions 里面的东西。那这样我们做一个系统性的调研，以这个文章为基础去做 harness engineering 的调研。也可以在我们当前就是 survey sessions 下面找找有没有已有的针对 harness engineering 的调研。如果有的话你直接改动，如果没有的话就创建一个。就是一个是以这个，然后还有 Cursor 最近有一篇文章讲的是好像是 self-driving codebase 之类的东西。你也把关键是这两篇文章看一下。看完了以后呢再做一个调研，然后用中文总结一个 harness engineering 到底是什么东西，它和我们当前比如说我们的 blog 呀我们的功力系统啊哪些东西有相关之处，把它写成一个 survey session 的文章。

---

### Shirley
*2026-03-16*

**天啊，真是太有共鸣了！** **！**

**我真的有去把鸭哥的文章载下来，把自己的日记也放在资料夹，开成一个** workspace**，用** happy app (**民间开发的**claude code iOS client) **每天語音写日记，让** agent **触发** skill **去** link **我的哪些观察或想法可以对应到鸭哥的哪一篇文章。**

**我一定要下载来试试看用这个** context infrastructure **去问鸭哥怎么看，会不会跟我原本沉淀的** markdown **不一样？**

**↳ Yan Wang 鸭哥** *2026-03-16*

非常期待实验！

---

### Neon Wong
*2026-03-16*

非常有启发。我最近把法律问题交给AI去分析的时候，感觉不论怎么引导它，都像是在跟一个很仔细但没有经验的junior在沟通，它的报告仿佛啥都写了又啥都没写。我还在庆幸AI替代律师的时刻还没到来，原来发现还是自己没用对。

**↳ Yan Wang 鸭哥** *2026-03-16*

也非常期待如果开始积累context的话能不能有改善。

**↳ Neon Wong** *2026-03-18*

刚才我改了一个合同，把修改交给AI请它把我的思考方式总结成下次可以提醒AI的prompt，发现它总结出来的东西特别像我自己积累经验时候的“错题集”，简直就是在模拟我自己的成长经历。当然有些地方AI的总结有点overfitting，如果直接用会出现以偏概全的问题，但是可以看出来反复iterate之后的potential。非常感谢鸭哥的分享！

**↳ Yan Wang 鸭哥** *2026-03-18*

真的太棒了！

---

### LIN CHIH YANG
*2026-03-16*

模型交給大廠去卷，品味只能從自身卷起，而鴨哥則是 AI 界卷王之一啊！

**↳ Yan Wang 鸭哥** *2026-03-16*

😂

---

### Zhidong Sun
*2026-03-16*

也有个好奇：未来除了大模型本身的竞争，会不会还有一层 AI入口的竞争？因为谁掌握入口，谁就更容易长期积累用户的 context。

不知道鸭哥怎么看这个方向？

**↳ Zhidong Sun** *2026-03-16*

龙虾也可以看作这个方向的一个尝试

**↳ Woody** *2026-03-16*

AI会像计算存储一样作为默认能力接入所有应用。能够更好利用AI能力的应用会变成新入口，能快速适应这种变化的老入口也会继续存在。

**↳ Yan Wang 鸭哥** *2026-03-16*

是的，我很赞成，这篇文章有一些更多的讨论：**#Manus爆火的背后，Agentic AI产品如何构筑持久的竞争优势？ **

---

### Zhidong Sun
*2026-03-16*

我自己之前也有一些零散的尝试，但还没有像鸭哥分享的项目那样系统地去记录。接下来也打算参考这个思路，把个人 context 的记录和整理做得更好一些。感谢分享，很有启发。

**↳ Yan Wang 鸭哥** *2026-03-16*

期待实验的结果！有问题欢迎讨论～

---

### Robin Shi
*2026-03-16*

又一次跪着看完鸭哥的文章，每一次都带给我更深刻的思考。

**↳ Yan Wang 鸭哥** *2026-03-16*

客气啦！很高兴有启发！

---

### Nicole Chen
*2026-03-16*

说得太好了，很有启发！最近🦞的感受是不同的model面对同样prompt的回复不仅不一样，在错误记忆的情况也很难修正，进化时刻。

**↳ Yan Wang 鸭哥** *2026-03-16*

龙虾这个特定的情况可能是三个因素的交叠。第一是它自己的Agentic Engine写得很混乱，本身限制了模型的发挥。一个是每个模型确实有不同的个性，比如Gemini特别讨厌搜索，但是GPT会做特别完备的搜索。另外，context确实也是一个问题。
