## AGI: 通用人工智能之路

- [AGI: 通用人工智能之路](#agi-通用人工智能之路)
  - [Awesome-AGI](#awesome-agi)
  - [Auto-GPT](#auto-gpt)
  - [ChatGPT 控制所有AI模型: HuggingGPT](#chatgpt-控制所有ai模型-hugginggpt)
  - [babyagi](#babyagi)
  - [MiniGPT-4](#minigpt-4)
  - [更多 AGI 项目](#更多-agi-项目)

### [Awesome-AGI](https://github.com/EmbraceAGI/Awesome-AGI)
 AGI 精选资源，持续更新中，欢迎关注和 star~

### [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)
AutoGPT: prompt 工程的下一个前沿，通向 AGI 之路！

具体来说，AutoGPT 相当于给基于 GPT 的模型一个内存和一个身体。有了它，你可以把一项任务交给 AI 智能体，让它自主地提出一个计划，然后执行计划。此外其还具有互联网访问、长期和短期内存管理、用于文本生成的 GPT-4 实例以及使用 GPT-3.5 进行文件存储和生成摘要等功能。AutoGPT 用处很多，可用来分析市场并提出交易策略、提供客户服务、进行营销等其他需要持续更新的任务。

特斯拉前 AI 总监、刚刚回归 OpenAI 的 Andrej Karpathy 也大力宣传，并在推特赞扬：「AutoGPT 是 prompt 工程的下一个前沿。」

AutoGPT 正在互联网上掀起一场风暴，它无处不在。很快，已经有网友上手实验了，该用户让 AutoGPT 建立一个网站，不到 3 分钟 AutoGPT 就成功了。期间 AutoGPT 使用了 React 和 Tailwind CSS，全凭自己，人类没有插手。看来程序员之后真就不再需要编码了。

[在线体验](https://www.cognosys.ai/) 目前免费

### [ChatGPT 控制所有AI模型: HuggingGPT](https://arxiv.org/abs/2303.17580)

[GitHub](https://github.com/microsoft/JARVIS)

[Arxiv 论文]((https://arxiv.org/abs/2303.17580))

大语言模型LLM在语言理解、生成、交互和推理方面的表现，让人想到：

> 可以将它们作为中间控制器，来管理现有的所有AI模型，通过“调动和组合每个人的力量”，来解决复杂的AI任务。

在这个系统中，语言是通用的接口。

于是，HuggingGPT就诞生了。

它的工程流程分为四步：

* 首先，任务规划。ChatGPT将用户的需求解析为任务列表，并确定任务之间的执行顺序和资源依赖关系。

* 其次，模型选择。ChatGPT根据HuggingFace上托管的各专家模型的描述，为任务分配合适的模型。

* 接着，任务执行。混合端点（包括本地推理和HuggingFace推理）上被选定的专家模型根据任务顺序和依赖关系执行分配的任务，并将执行信息和结果给到ChatGPT。

* 最后，输出结果。由ChatGPT总结各模型的执行过程日志和推理结果，给出最终的输出。

### [babyagi](https://github.com/yoheinakajima/babyagi)

[在线体验](https://godmode.space/)

babyagi 是一个智能任务管理和解决工具，它结合了OpenAI GPT-4和Pinecone向量搜索引擎的力量，以自动完成和管理一系列任务，从一个初始任务开始，babyagi使用GPT4生成解决方案和新任务，并将解决方案存储在Pinecone中以便进一步检索。

[中文博客-babyagi: 人工智能任务管理系统](https://juejin.cn/post/7218815501433946173)

![babyagi](imgs/babyagi.jpg)

### [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4)

MiniGPT-4 项目破解了 GPT4 的魔法，树立了很好的一个示范和方向。借助各种基础开源模型模型的组合，迈出了可能实现多模态识别的一步。

1.NLP 部分采用 LLaMA, 效果虽然不如 GPT-4，但是基本合格

2.CV 部分采用了开源的诸多模型如 Timm，DeiT 等，展现了开源的力量

代码、文档、视频、演示网站等内容齐全完善，开源质量很高，代码编写也很精妙，值得关注学习！

### 更多 AGI 项目
|名称|Stars|简介| 备注 |
-|-|-|-
|[Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT) |![GitHub Repo stars](https://badgen.net/github/stars/Significant-Gravitas/Auto-GPT)|An experimental open-source attempt to make GPT-4 fully autonomous.|-|
|[Auto-GPT-Plugins](https://github.com/Significant-Gravitas/Auto-GPT-Plugins) |![GitHub Repo stars](https://badgen.net/github/stars/Significant-Gravitas/Auto-GPT-Plugins)|Plugins for Auto-GPT.|-|
|[AutoGPT.js](https://github.com/zabirauf/AutoGPT.js)|![GitHub Repo stars](https://badgen.net/github/stars/zabirauf/AutoGPT.js)|Auto-GPT on the browser.|-|
|[AutoGPT-GUI](https://github.com/thecookingsenpai/autogpt-gui)|![GitHub Repo stars](https://badgen.net/github/stars/thecookingsenpai/autogpt-gui)|A graphical user interface for AutoGPT.|AutoGPT 项目的图形界面|
|[AgentGPT](https://github.com/reworkd/AgentGPT) |![GitHub Repo stars](https://badgen.net/github/stars/reworkd/AgentGPT)|Assemble, configure, and deploy autonomous AI Agents in your browser.|-|
|[JARVIS](https://github.com/microsoft/JARVIS)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/JARVIS)|A system to connect LLMs with ML community.|-|
|[babyagi](https://github.com/yoheinakajima/babyagi)|![GitHub Repo stars](https://badgen.net/github/stars/yoheinakajima/babyagi)|Use OpenAI and Pinecone APIs to create, prioritize, and execute tasks.|[中文博客-babyagi: 人工智能任务管理系统](https://juejin.cn/post/7218815501433946173)|
|[OpenAGI](https://github.com/agiresearch/OpenAGI) |![GitHub Repo stars](https://badgen.net/github/stars/agiresearch/OpenAGI)|When LLM (Large Language Models) Meets Domain Experts.|-|
|[AI-legion](https://github.com/eumemic/ai-legion)|![GitHub Repo stars](https://badgen.net/github/stars/eumemic/ai-legion)|An LLM-powered autonomous agent platform.|-|
|[MicroGPT](https://github.com/muellerberndt/micro-gpt)|![GitHub Repo stars](https://badgen.net/github/stars/muellerberndt/micro-gpt)|A minimal generic autonomous agent based on GPT3.5/4. Can analyze stock prices, perform network security tests, create art, and order pizza.|-|
|[MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4)|![GitHub Repo stars](https://badgen.net/github/stars/Vision-CAIR/MiniGPT-4)|MiniGPT-4: Enhancing Vision-language Understanding with Advanced Large Language Models.|-|
|[Agent-LLM](https://github.com/Josh-XT/Agent-LLM)|![GitHub Repo stars](https://badgen.net/github/stars/Josh-XT/Agent-LLM)|An Artificial Intelligence Automation Platform. AI Instruction management from various providers, has an adaptive memory, and a versatile plugin system with many commands including web browsing.| 人工智能自动化平台。https://agent-llm.com/|
|[Free-AUTO-GPT-with-NO-API](https://github.com/IntelligenzaArtificiale/Free-AUTO-GPT-with-NO-API)|![GitHub Repo stars](https://badgen.net/github/stars/IntelligenzaArtificiale/Free-AUTO-GPT-with-NO-API)|Free Auto GPT with NO paids API is a repository that offers a simple version of Auto GPT, an autonomous AI agent capable of performing tasks independently. Unlike other versions, our implementation does not rely on any paid OpenAI API, making it accessible to anyone.|不用花大价钱使用API key 跑 AutoGPT, BabyAGI, AgentGPT 项目啦。 需要有 ChatGPT 账号，然后浏览器登陆拿到 Cookie Value 使用。 或者使用 huggingFace 的 chat 模型，详情参照项目说明。|
|[opencog](https://github.com/opencog/opencog)|![GitHub Repo stars](https://badgen.net/github/stars/opencog/opencog)|A framework for integrated Artificial Intelligence & Artificial General Intelligence (AGI).|集成人工智能和通用人工智能(AGI)的框架。|
|[mini-agi](https://github.com/muellerberndt/mini-agi)|![GitHub Repo stars](https://badgen.net/github/stars/muellerberndt/mini-agi)|MiniAGI is a minimal general-purpose autonomous agent based on GPT-3.5 / GPT-4. Can analyze stock prices, perform network security tests, create art, and order pizza.|基于 GPT-3.5 / GPT-4 的迷你AGI。 可以分析股票价格、执行网络安全测试、创作艺术品和订购比萨。|
|[big-agi](https://github.com/enricoros/big-agi)|![GitHub Repo stars](https://badgen.net/github/stars/enricoros/big-agi)|Personal AI application powered by GPT-4 and beyond, with AI personas, AGI functions, text-to-image, voice, response streaming, code highlighting and execution, PDF import, presets for developers, much more. Deploy and gift #big-AGI-energy! Using Next.js, React, Joy.|GPT-4 驱动的个人 AI 应用，[big-agi](https://big-agi.com/)|
|[LocalAGI](https://github.com/EmbraceAGI/LocalAGI)|![GitHub Repo stars](https://badgen.net/github/stars/EmbraceAGI/LocalAGI)|Locally run AGI powered by LLaMA, ChatGLM and more.|基于 LLMDA, ChatGLM 等模型的本地 AGI 项目|