## AGI: 通用人工智能之路

2023 年，AutoGPT、BabyAGI、AgentGPT、HuggingGPT 等"自主 Agent"项目掀起第一波浪潮——人们第一次看到大模型可以自己拆解目标、循环规划、调用工具。但那一代实验大多停留在演示阶段：容易跑偏、难以收敛、缺乏可靠的工程闭环。

2024 至 2026 年，方向从"会不会自己跑起来"转向"能不能真正把活干完"。Anthropic 在 2024 年底推出 Model Context Protocol、Google 推出 Agent2Agent，工具调用与智能体协作开始有了标准；OpenAI、Anthropic、Google 相继推出 Computer Use / Operator 这类直接操作屏幕的通用智能体；Manus、Devin、OpenHands 等"通用 Agent / 编码 Agent"把长时程、多步骤、可交付成果的能力推向实用。2025 年被广泛称为"智能体元年"——AGI 之路，从单点的自主实验，走向通用智能体的规模化落地。

> 相关：AI Agent 开发框架见 [ChatGPT 应用开发指南](ChatGPT_dev.md)，工具连接协议见 [MCP 指南](MCP.md)。

### 通用 AI Agent（产品与开源）

| 名称 | 链接 | 简介 |
|------|------|------|
| Manus | [链接](https://manus.im/) | 主打"通用 AI Agent"的产品，能自主规划并交付完整成果（PPT、网站、研报等），在 GAIA 基准上一度达到 SOTA |
| OpenManus | [链接](https://github.com/FoundationAgents/OpenManus) | MetaGPT 核心团队发起的开源通用 Agent 框架，无需邀请码即可复现"Manus 式"能力，MIT 协议 |
| OpenHands | [链接](https://github.com/All-Hands-AI/OpenHands) | 原名 OpenDevin，开源软件开发智能体平台，可执行真实工程任务而非仅建议代码，支持自由切换 Claude/GPT/本地模型 |
| Devin | [链接](https://www.cognition.ai/) | Cognition AI 推出的商业化自主编码智能体，可异步执行长达数小时的复杂工程任务 |
| AutoGPT | [链接](https://github.com/Significant-Gravitas/AutoGPT) | 从最早的自主 Agent 实验演进为可视化的智能体构建与部署平台（低代码前端 + 服务端 + Forge 工具包） |
| Suna | [链接](https://github.com/kortix-ai/suna) | Kortix AI 开源的通用智能体，具备浏览器自动化、文件管理、网页爬取、命令行执行等能力，可自托管 |
| OpenAI Operator / ChatGPT Agent | [链接](https://openai.com/index/introducing-operator/) | OpenAI 的 Computer-Using Agent，可自主操作浏览器完成任务，现已并入 ChatGPT Agent |
| Claude Computer Use | [链接](https://www.anthropic.com/news/3-5-models-and-computer-use) | Anthropic 推出的电脑操作能力，Claude 通过"看屏幕、移动光标、点击、输入"直接操作计算机 |
| AgentSpace | [GitHub](https://github.com/HKUDS/AgentSpace) | 港大数据智能实验室出品，"人 + 多 Agent，一个团队、一个工作空间"的统一协同工作台，让人类与多智能体在同一空间内分工协作 |
| lemma-platform | [GitHub](https://github.com/lemma-work/lemma-platform) | 开源工作空间，让人类与 AI Agent 作为同一个团队协作（AGPL-3.0） |

### AGI 相关基准与研究

| 名称 | 链接 | 简介 |
|------|------|------|
| Qwen-AgentWorld | [GitHub](https://github.com/QwenLM/Qwen-AgentWorld) | 阿里通义团队出品，面向通用 Agent 的"语言世界模型"（Language World Models），用语言建模智能体所处的世界以支持规划与决策 |
| awesome-evals | [GitHub](https://github.com/benchflow-ai/awesome-evals) | BenchFlow 维护的"构建与评测 AI Agent"精选资源库，汇集论文、博客、演讲、工具与 benchmark |
| LLM-Agent-Paper-List | [GitHub](https://github.com/WooooDyy/LLM-Agent-Paper-List) | 复旦 NLP 团队 86 页综述《The Rise and Potential of LLM Based Agents》的配套必读论文清单，按智能体构建（大脑/感知/行动）、应用、智能体社会等维度系统梳理 |
| ARC Prize / ARC-AGI | [链接](https://arcprize.org/) | 专注"人类轻松、机器困难"的抽象推理基准，已成为各大厂在模型卡中公开报告的行业基准 |
| GAIA benchmark | [链接](https://huggingface.co/gaia-benchmark) | Meta FAIR、HuggingFace、AutoGPT 等提出的"通用 AI 助手"基准，466 道真实世界问题，考察推理、多模态、网页浏览与工具使用 |
| GAIA 论文 | [arxiv](https://arxiv.org/abs/2311.12983) | GAIA 原始论文，主张 AGI 的关键在于系统能否在"对人类简单"的问题上展现与普通人相当的稳健性 |

### 经典自主 Agent（历史）

> 以下为 2023 年第一波自主 Agent 浪潮的代表项目，作为历史存档保留。

| 名称 | Stars | 简介 |
|------|-------|------|
| [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) | ![GitHub Repo stars](https://badgen.net/github/stars/Significant-Gravitas/AutoGPT) | 引爆自主 Agent 浪潮的开创性项目，让 GPT-4 自主拆解目标、循环规划与执行 |
| [babyagi](https://github.com/yoheinakajima/babyagi) | ![GitHub Repo stars](https://badgen.net/github/stars/yoheinakajima/babyagi) | 极简任务驱动的自主 Agent，依据上一步结果与既定目标动态生成任务队列 |
| [AgentGPT](https://github.com/reworkd/AgentGPT) | ![GitHub Repo stars](https://badgen.net/github/stars/reworkd/AgentGPT) | 可在浏览器中配置并部署自主 AI Agent，命名目标即自动思考、执行、学习 |
| [HuggingGPT (JARVIS)](https://github.com/microsoft/JARVIS) | ![GitHub Repo stars](https://badgen.net/github/stars/microsoft/JARVIS) | 微软提出，以 LLM 为控制器、HuggingFace 上众多专家模型为执行器的协作系统 |
| [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4) | ![GitHub Repo stars](https://badgen.net/github/stars/Vision-CAIR/MiniGPT-4) | 将视觉编码器与 Vicuna/Llama 等大语言模型对齐，复现 GPT-4 式的图文理解能力 |
| [XAgent](https://github.com/OpenBMB/XAgent) | ![GitHub Repo stars](https://badgen.net/github/stars/OpenBMB/XAgent) | 面壁智能 OpenBMB 出品的自主 LLM 智能体，面向复杂任务求解，采用调度器/规划器双循环架构与人机协作机制 |
