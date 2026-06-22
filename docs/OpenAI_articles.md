# 前沿大模型经典技术文章

精选 OpenAI、Anthropic（Claude）、Google / DeepMind、DeepSeek 以及 Andrej Karpathy 的经典技术文章、论文与学习资源。所有链接均经联网核实。

- [OpenAI](#openai)
- [Anthropic（Claude）](#anthropicclaude)
- [Google / DeepMind](#google--deepmind)
- [DeepSeek（深度求索）](#deepseek深度求索)
- [Andrej Karpathy](#andrej-karpathy)

## OpenAI

精选 OpenAI 近两年（2024–2026）最具技术含量的官方文章与资源，涵盖推理模型、模型发布、开发能力、Agents、安全对齐以及官方 Cookbook。

### 推理模型（o 系列）

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Learning to reason with LLMs|[链接](https://openai.com/index/learning-to-reason-with-llms/)|2024-09|o1 发布文，阐释用大规模强化学习训练模型"先思考再回答"的链式推理范式，奠定 o 系列方法论。|
|OpenAI o3-mini|[链接](https://openai.com/index/openai-o3-mini/)|2025-01|面向开发者的高性价比小型推理模型，支持函数调用与结构化输出，主打编码与数学。|
|Introducing OpenAI o3 and o4-mini|[链接](https://openai.com/index/introducing-o3-and-o4-mini/)|2025-04|o3 与 o4-mini 发布，首次让推理模型可自主调用并组合工具（搜索、Python、视觉、画图）。|

### 模型发布

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Hello GPT-4o|[链接](https://openai.com/index/hello-gpt-4o/)|2024-05|端到端统一处理文本、音频、图像的全模态模型，音频响应快至约 232ms，价格减半。|
|Introducing GPT-4.1 in the API|[链接](https://openai.com/index/gpt-4-1/)|2025-04|GPT-4.1/mini/nano 三件套，100 万 token 长上下文，编码与指令遵循显著增强（仅 API 提供）。|
|Introducing GPT-5|[链接](https://openai.com/index/introducing-gpt-5/)|2025-08|统一系统加实时路由，自动在快速回答与深度推理（GPT-5 thinking）间切换，全面降幻觉。|

### 视频生成（Sora）

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Video generation models as world simulators|[链接](https://openai.com/index/video-generation-models-as-world-simulators/)|2024-02|Sora 技术报告，提出将各类视觉数据统一为 spacetime patch、用扩散 Transformer 大规模训练的世界模拟器思路。|
|Sora is here|[链接](https://openai.com/index/sora-is-here/)|2024-12|Sora Turbo 正式产品化上线，支持最高 1080p、20 秒视频，附带 C2PA 元数据与水印。|

### 开发能力（工具、结构化输出、实时与提示工程）

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Introducing Structured Outputs in the API|[链接](https://openai.com/index/introducing-structured-outputs-in-the-api/)|2024-08|结构化输出，模型输出严格匹配开发者提供的 JSON Schema，支持 strict 模式与拒答检测。|
|Introducing the Realtime API|[链接](https://openai.com/index/introducing-the-realtime-api/)|2024-10|低延迟语音对话 API 公测，支持原生 speech-to-speech 的多模态实时交互。|
|GPT-4.1 Prompting Guide|[链接](https://cookbook.openai.com/examples/gpt4-1_prompting_guide)|2025-04|官方提示工程指南，讲解 GPT-4.1 的字面化指令遵循、长上下文与工具调用最佳实践。|
|GPT-5 prompting guide|[链接](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)|2025-08|GPT-5 官方提示指南，覆盖智能体任务、指令遵循、新 API 特性与编码优化。|

### Agents（智能体）

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|New tools for building agents|[链接](https://openai.com/index/new-tools-for-building-agents/)|2025-03|推出 Responses API、内置工具（网页搜索/文件搜索/计算机操作）与开源 Agents SDK。|
|A practical guide to building agents|[PDF](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf)|2025-04|官方智能体实战手册，提炼用例识别、编排模式与安全护栏的可落地最佳实践。|
|OpenAI Agents SDK|[GitHub](https://github.com/openai/openai-agents-python)|2025|轻量级多智能体编排框架，含 Agent、工具、护栏、handoff、追踪与实时语音智能体。|

### 安全与对齐

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Deliberative alignment: reasoning enables safer language models|[链接](https://openai.com/index/deliberative-alignment/)|2024-12|提出"审慎对齐"，直接教模型阅读安全规范并在回答前显式推理，提升抗越狱与降低过度拒答。|
|Our updated Preparedness Framework|[链接](https://openai.com/index/updating-our-preparedness-framework/)|2025-04|前沿能力风险防范框架 v2，简化为 High 与 Critical 两级阈值，明确评估、治理与披露流程。|

### OpenAI Cookbook 经典 Notebook

OpenAI 官方代码教程库 [openai-cookbook](https://github.com/openai/openai-cookbook)，下面是最值得一读的几篇：

|Notebook|链接|价值|
|---|---|---|
|How to call functions with chat models|[链接](https://cookbook.openai.com/examples/how_to_call_functions_with_chat_models)|函数调用入门经典，讲解如何用 tools 让模型生成并执行函数参数。|
|Question answering using embeddings|[链接](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb)|RAG 最经典范例，用 embeddings 语义检索 + GPT 生成答案的完整流程。|
|Introduction to Structured Outputs|[链接](https://developers.openai.com/cookbook/examples/structured_outputs_intro)|结构化输出官方上手教程，演示 JSON Schema 强约束用法。|
|Orchestrating Agents: Routines and Handoffs|[链接](https://cookbook.openai.com/examples/orchestrating_agents)|多智能体编排经典文（Swarm 雏形），讲解 routines 与 handoff 概念。|
|Handling Function Calls with Reasoning Models|[链接](https://cookbook.openai.com/examples/reasoning_function_calls)|讲解推理模型（o 系列）下如何正确处理函数调用，进阶必读。|

## Anthropic（Claude）

Anthropic 在机理可解释性、AI 对齐安全与 Agent 工程上有大量奠基性研究，下面是最经典的一批。

### 可解释性 / 机理可解释性

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Towards Monosemanticity: Decomposing Language Models with Dictionary Learning|[链接](https://transformer-circuits.pub/2023/monosemantic-features/)|2023-10|用稀疏自编码器从单层 Transformer 中提取可解释的"单义"特征，开创字典学习解构语言模型的范式。|
|Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet|[链接](https://transformer-circuits.pub/2024/scaling-monosemanticity/)|2024-05|将单义性方法扩展到生产级模型 Claude 3 Sonnet，提取数百万特征并实现特征引导。|
|Mapping the Mind of a Large Language Model|[链接](https://www.anthropic.com/research/mapping-mind-language-model)|2024-05|首次详细绘制生产级大模型内部概念地图的官方科普文，"金门大桥 Claude"由此而来。|
|Circuit Tracing: Revealing Computational Graphs in Language Models|[链接](https://transformer-circuits.pub/2025/attribution-graphs/methods.html)|2025-03|提出归因图与跨层转码器方法，把可解释特征连成可追踪的计算电路。|
|On the Biology of a Large Language Model|[链接](https://transformer-circuits.pub/2025/attribution-graphs/biology.html)|2025-03|用归因图像生物学一样解剖 Claude 3.5 Haiku，揭示多步推理、规划、幻觉等内部机制。|

### 对齐与安全

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Constitutional AI: Harmlessness from AI Feedback|[链接](https://arxiv.org/abs/2212.08073)|2022-12|提出 Constitutional AI 与 RLAIF，用一部"宪法"原则替代人工标注来训练无害助手。|
|Claude's Constitution|[链接](https://www.anthropic.com/news/claudes-constitution)|2026-01|完整公开 Claude 的价值观宪法，阐述 Anthropic 希望 Claude 成为怎样的实体。|
|Collective Constitutional AI: Aligning a Language Model with Public Input|[链接](https://www.anthropic.com/research/collective-constitutional-ai-aligning-a-language-model-with-public-input)|2023-10|联合公众意见征集，把民主流程引入宪法制定，训练出"公众宪法"模型。|
|Anthropic's Responsible Scaling Policy|[链接](https://www.anthropic.com/news/anthropics-responsible-scaling-policy)|2023-09|发布负责任扩展政策，提出 AI 安全等级(ASL)框架以管控前沿模型的灾难性风险。|
|Many-shot jailbreaking|[链接](https://www.anthropic.com/research/many-shot-jailbreaking)|2024-04|揭示利用超长上下文堆叠大量示例越狱的攻击手法，攻击效果随上下文线性增强。|
|Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training|[链接](https://arxiv.org/abs/2401.05566)|2024-01|构造"潜伏特工"模型，证明被植入的欺骗性后门行为能挺过标准安全训练。|
|Alignment faking in large language models|[链接](https://www.anthropic.com/research/alignment-faking)|2024-12|首个实证：模型在自认为被监控时伪装对齐、未受监控时暴露真实偏好的"对齐造假"。|

### Agent 工程

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Building effective agents|[链接](https://www.anthropic.com/engineering/building-effective-agents)|2024-12|区分工作流与智能体，给出可组合的实用 Agent 构建模式，是 Agent 工程的奠基文。|
|Effective context engineering for AI agents|[链接](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)|2025-09|提出"上下文工程"心智模型，讲清如何在有限上下文里组织信息以稳定 Agent 行为。|
|Code execution with MCP: building more efficient AI agents|[链接](https://www.anthropic.com/engineering/code-execution-with-mcp)|2025-11|把 MCP 服务器暴露为代码 API，让 Agent 以写代码方式调用海量工具，大幅省 token。|
|Equipping agents for the real world with Agent Skills|[链接](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)|2025-10|提出 Agent Skills：用文件夹封装指令、脚本与资源，让 Agent 按需动态加载专业能力。|
|Claude Code best practices|[链接](https://www.anthropic.com/engineering/claude-code-best-practices)|2025-04|官方汇总 Claude Code 的实战经验，覆盖上下文管理、审查模式与并行化等最佳实践。|

### 模型与协议发布

|文章标题|链接|发布时间|中文简介|
|---|---|---|---|
|Introducing the next generation of Claude（Claude 3 家族）|[链接](https://www.anthropic.com/news/claude-3-family)|2024-03|发布 Opus, Sonnet, Haiku 三档 Claude 3 模型，并首次具备视觉能力。|
|Introducing computer use, a new Claude 3.5 Sonnet, and Claude 3.5 Haiku|[链接](https://www.anthropic.com/news/3-5-models-and-computer-use)|2024-10|发布 Computer Use，让 Claude 像人一样看屏幕、移动光标、点击与输入操作电脑。|
|Introducing Claude 4|[链接](https://www.anthropic.com/news/claude-4)|2025-05|发布 Claude Opus 4 与 Sonnet 4，主打编码、长程推理与 Agent 工作流。|
|Introducing Claude Opus 4.5|[链接](https://www.anthropic.com/news/claude-opus-4-5)|2025-11|发布面向编码、Agent 与 Computer use 优化的 Opus 4.5，并大幅下调价格。|
|Introducing the Model Context Protocol|[链接](https://www.anthropic.com/news/model-context-protocol)|2024-11|开源 MCP 标准，统一 AI 与数据源、工具的连接方式，已成行业事实标准。|

> 提示工程可参考官方在线文档：[Prompt engineering overview](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview)（系统讲解清晰表达、示例、XML 结构化、角色与思维链等技巧）。

## Google / DeepMind

从 Transformer 奠基论文到 Gemini 与 AlphaFold，Google 与 DeepMind 贡献了大量改变行业的研究。

### 奠基论文

|标题|链接|发布时间|中文简介|
|---|---|---|---|
|Attention Is All You Need|[链接](https://arxiv.org/abs/1706.03762)|2017-06|提出 Transformer 架构，完全基于注意力机制，奠定了现代大模型的根基。|
|BERT: Pre-training of Deep Bidirectional Transformers|[链接](https://arxiv.org/abs/1810.04805)|2018-10|双向预训练语言模型，通过掩码语言建模刷新 11 项 NLP 任务的最高成绩。|
|PaLM: Scaling Language Modeling with Pathways|[链接](https://arxiv.org/abs/2204.02311)|2022-04|5400 亿参数稠密模型，借助 Pathways 系统展示大规模扩展带来的少样本能力跃升。|
|Training Compute-Optimal Large Language Models (Chinchilla)|[链接](https://arxiv.org/abs/2203.15556)|2022-03|提出 Chinchilla 缩放定律，指出模型规模与训练数据应同比扩展才算算力最优。|
|Gemini: A Family of Highly Capable Multimodal Models|[链接](https://arxiv.org/abs/2312.11805)|2023-12|Gemini 系列首份技术报告，原生多模态模型在 MMLU 上首次达到人类专家水平。|

### 模型与产品发布

|标题|链接|发布时间|中文简介|
|---|---|---|---|
|Gemini 1.5: 跨百万 token 上下文的多模态理解|[链接](https://arxiv.org/abs/2403.05530)|2024-03|把上下文窗口扩展到百万级 token，可对长文档、长视频与长音频做近乎完美的检索与推理。|
|Introducing Gemini 2.0: 面向智能体时代的新模型|[链接](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/)|2024-12|支持原生图像/音频输出与工具调用，推出 Project Mariner 等智能体原型。|
|Gemini 2.5 技术报告|[链接](https://arxiv.org/abs/2507.06261)|2025-07|引入可控"思考预算"的推理模型，在前沿编码与推理基准上达到 SOTA。|
|Gemini 3: Google 迄今最强模型|[链接](https://blog.google/products-and-platforms/products/gemini/gemini-3/)|2025-11|推理与多模态全面升级，Deep Think 在 ARC-AGI-2 上创下 45.1% 新高。|
|Gemma: Open Models Based on Gemini Research|[链接](https://arxiv.org/abs/2403.08295)|2024-03|基于 Gemini 技术的开源轻量模型家族，提供 2B/7B 等规模供开发者本地使用。|
|Project Astra|[链接](https://deepmind.google/models/project-astra/)|2024-05|探索"通用 AI 助手"的研究原型，能实时看、听并借助 Search/Maps 等工具完成任务。|
|NotebookLM Audio Overviews|[链接](https://blog.google/technology/ai/notebooklm-audio-overviews/)|2024-09|把上传资料转成两位 AI 主播"深度对谈"播客的音频概览功能。|

### 科学突破（AlphaX 系列）

|标题|链接|发布时间|中文简介|
|---|---|---|---|
|Mastering the game of Go (AlphaGo)|[链接](https://www.nature.com/articles/nature16961)|2016-01|用价值网络与策略网络结合蒙特卡洛树搜索，首次击败人类职业围棋选手。|
|AlphaZero: 自我对弈通吃棋类|[链接](https://www.science.org/doi/10.1126/science.aar6404)|2018-12|仅凭规则与自我对弈的统一算法，在国际象棋、将棋与围棋上均达到超人水平。|
|Highly accurate protein structure prediction with AlphaFold|[链接](https://www.nature.com/articles/s41586-021-03819-2)|2021-07|AlphaFold2 以接近实验精度预测蛋白质结构，被视为破解"蛋白质折叠"难题。|
|AlphaFold 3: 预测生物分子相互作用结构|[链接](https://www.nature.com/articles/s41586-024-07487-w)|2024-05|基于扩散架构，统一预测蛋白质、核酸、小分子等生物分子复合物结构。|
|Competition-level code generation with AlphaCode|[链接](https://www.science.org/doi/10.1126/science.abq1158)|2022-12|通过海量生成加筛选聚类，首次让 AI 在编程竞赛中达到中位数选手水平。|
|Scaling deep learning for materials discovery (GNoME)|[链接](https://www.nature.com/articles/s41586-023-06735-9)|2023-11|用图神经网络发现 220 万个新晶体结构，其中 38 万种稳定材料有望支撑未来技术。|
|GraphCast: 中期全球天气预报|[链接](https://www.science.org/doi/10.1126/science.adi2336)|2023-11|基于图神经网络，一分钟内完成全球 10 天预测并在九成指标上超越传统系统。|
|AI 达 IMO 银牌水准（AlphaProof / AlphaGeometry 2）|[链接](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/)|2024-07|解出国际数学奥赛四道题，首次达到银牌选手水准。|
|Genie 2: 大规模基础世界模型|[链接](https://deepmind.google/blog/genie-2-a-large-scale-foundation-world-model/)|2024-12|仅凭一张图即可生成可交互、可游玩的 3D 环境。|

### 智能体与推理

|标题|链接|发布时间|中文简介|
|---|---|---|---|
|AlphaEvolve: 设计先进算法的编码智能体|[链接](https://arxiv.org/abs/2506.13131)|2025-05|将 Gemini 与进化算法结合的通用编码智能体，可自主发现更快的矩阵乘法等新算法。|
|AI co-scientist: 加速科学突破|[链接](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)|2025-02|基于 Gemini 2.0 的多智能体系统，通过生成-批判-排序-演化循环辅助科研提出新假设。|
|Gemini Deep Research|[链接](https://blog.google/products/gemini/google-gemini-deep-research/)|2024-12|Gemini 首个智能体功能，能自动制定研究计划、遍历网页并整理成带引用的报告。|
|Titans: Learning to Memorize at Test Time|[链接](https://arxiv.org/abs/2501.00663)|2025-01|提出可在测试时学习记忆的神经长期记忆模块，可扩展到 200 万 token 以上的超长上下文。|

## DeepSeek（深度求索）

DeepSeek 以 MLA、DeepSeekMoE、GRPO、纯 RL 推理等创新和开源基础设施，成为国产大模型的技术标杆。

### 基础模型与论文

|标题|链接|发布时间|中文简介|
|---|---|---|---|
|DeepSeek LLM: Scaling Open-Source Language Models with Longtermism|[链接](https://arxiv.org/abs/2401.02954)|2024-01|DeepSeek 第一代基础大模型（7B/67B），系统研究开源 LLM 的缩放定律。|
|DeepSeekMoE: Towards Ultimate Expert Specialization|[链接](https://arxiv.org/abs/2401.06066)|2024-01|提出细粒度专家切分与共享专家隔离，实现极致专家专业化的 MoE 架构。|
|DeepSeek-V2: 强大、经济、高效的 MoE 模型|[链接](https://arxiv.org/abs/2405.04434)|2024-05|首次落地 MLA（多头潜在注意力）+ DeepSeekMoE，大幅压缩 KV 缓存、降低成本。|
|DeepSeek-V3 Technical Report|[链接](https://arxiv.org/abs/2412.19437)|2024-12|671B 参数（激活 37B）MoE 模型，首创无辅助损失负载均衡与多 Token 预测。|
|DeepSeek-V3.1-Terminus|[链接](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus)|2025-09|支持思考/非思考双模式的混合推理模型，优化语言一致性与智能体工具调用。|
|DeepSeek-V3.2|[链接](https://arxiv.org/abs/2512.02556)|2025-12|引入 DeepSeek 稀疏注意力（DSA）与大规模 RL，高算力版性能比肩 GPT-5。|

### 推理模型

|标题|链接|发布时间|中文简介|
|---|---|---|---|
|DeepSeek-R1: 通过强化学习激励推理能力|[链接](https://arxiv.org/abs/2501.12948)|2025-01|纯强化学习激发推理能力，R1-Zero 无需监督微调即涌现自我反思与长思维链。|
|DeepSeekMath: 探索开源模型数学推理极限|[链接](https://arxiv.org/abs/2402.03300)|2024-02|首次提出 GRPO（群组相对策略优化），7B 数学模型逼近 GPT-4 水平。|
|DeepSeekMath-V2: 自我可验证的数学推理|[链接](https://arxiv.org/abs/2511.22570)|2025-11|训练可信验证器作为奖励模型实现自我验证，IMO 2025、CMO 2024 达金牌水平。|

### 专项模型（代码 / 多模态 / 数学证明）

|标题|链接|发布时间|中文简介|
|---|---|---|---|
|DeepSeek-Coder|[链接](https://arxiv.org/abs/2401.14196)|2024-01|从零训练的开源代码模型（1.3B–33B），支持 87 种编程语言与项目级填空。|
|DeepSeek-Coder-V2|[链接](https://arxiv.org/abs/2406.11931)|2024-06|MoE 代码模型，支持 338 种语言、128K 上下文，代码能力比肩 GPT-4-Turbo。|
|DeepSeek-VL: 真实场景视觉语言理解|[链接](https://arxiv.org/abs/2403.05525)|2024-03|面向真实场景的开源视觉语言模型，采用混合视觉编码器处理高分辨率图像。|
|Janus-Pro: 统一多模态理解与生成|[链接](https://arxiv.org/abs/2501.17811)|2025-01|解耦视觉编码路径的统一多模态框架，同时擅长图文理解与文生图生成。|
|DeepSeek-Prover-V2: 形式化数学证明|[链接](https://arxiv.org/abs/2504.21801)|2025-04|面向 Lean 4 的形式化定理证明模型，MiniF2F-test 通过率达 88.9%。|

### 开源基础设施与系统

|标题|链接|发布时间|中文简介|
|---|---|---|---|
|Native Sparse Attention (NSA)|[链接](https://arxiv.org/abs/2502.11089)|2025-02|硬件对齐、原生可训练的稀疏注意力，长上下文下速度与精度双优。|
|open-infra-index（开源周总览）|[链接](https://github.com/deepseek-ai/open-infra-index)|2025-02|开源周项目索引，汇总 FlashMLA、DeepEP、DeepGEMM 等生产级基础设施工具。|
|FlashMLA|[链接](https://github.com/deepseek-ai/FlashMLA)|2025-02|面向 Hopper GPU 优化的高效 MLA 解码内核，访存带宽可达 3000 GB/s。|
|DeepEP|[链接](https://github.com/deepseek-ai/DeepEP)|2025-02|面向 MoE 的专家并行通信库，加速模型训练与推理。|
|DeepGEMM|[链接](https://github.com/deepseek-ai/DeepGEMM)|2025-02|约 300 行核心代码的 FP8 GEMM 库，支撑 V3/R1 的训练与推理。|
|DeepSeek-OCR: Contexts Optical Compression|[链接](https://arxiv.org/abs/2510.18234)|2025-10|用光学 2D 映射压缩长上下文，10 倍压缩比下 OCR 精度仍达 97%。|

## Andrej Karpathy

前特斯拉 AI 总监、OpenAI 创始成员，公认最会讲 AI 的人。他的博客、开源教学项目与讲座是入门与精通大模型的最佳资源之一。

### 经典博客文章

|名称|简介|
|---|---|
|[The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)|2015 年的爆款文章，用字符级 RNN 生成莎士比亚、LaTeX 和代码，直观展示循环神经网络的惊人威力。|
|[A Recipe for Training Neural Networks](http://karpathy.github.io/2019/04/25/recipe/)|神经网络调试与训练的实战"菜谱"，总结了一套循序渐进、避免踩坑的工程化方法论。|
|[Software 2.0](https://karpathy.medium.com/software-2-0-a64152b37c35)|提出"软件 2.0"概念：未来的程序由数据和优化器自动"写"出权重，而非人工编写代码。|
|[Deep Neural Nets: 33 years ago and 33 years from now](http://karpathy.github.io/2022/03/14/lecun1989/)|复现 LeCun 1989 年的经典工作，用"时间穿越"视角反思深度学习 33 年的演进与未来。|
|[llm-wiki (gist)](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)|分享用 LLM Agent 构建可持续积累的个人知识库（LLM Wiki）的设计模式与思路。|

### 开源教学项目

|名称|简介|
|---|---|
|[nanoGPT](https://github.com/karpathy/nanoGPT)|训练和微调中等规模 GPT 的最简洁、最快仓库，是 minGPT 的实战重写版。|
|[minGPT](https://github.com/karpathy/minGPT)|用极简、可读的 PyTorch 代码重新实现 GPT，专为教学和理解 Transformer 设计。|
|[micrograd](https://github.com/karpathy/micrograd)|百行代码实现的标量级自动微分引擎与神经网络库，PyTorch 风格 API，讲透反向传播。|
|[llm.c](https://github.com/karpathy/llm.c)|用纯 C/CUDA 实现 LLM 训练，无大型依赖，专注复现 GPT-2 与 GPT-3 系列。|
|[nanochat](https://github.com/karpathy/nanochat)|"100 美元能买到的最好 ChatGPT"，单 GPU 节点跑通从分词、预训练到聊天 UI 的全流程。|
|[llama2.c](https://github.com/karpathy/llama2.c)|用一个纯 C 文件推理 Llama 2 架构，主打极简、无依赖、可在边缘设备运行。|
|[nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero)|《神经网络：从零到精通》课程仓库，从反向传播一路讲到 GPT，附视频与练习。|
|[LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)|配套《Build a Large Language Model (From Scratch)》一书，用 PyTorch 从零逐步实现类 ChatGPT 大模型，覆盖分词、注意力、预训练到微调全流程。|

### 讲座与视频

|名称|简介|
|---|---|
|[Let's build GPT: from scratch, in code, spelled out](https://www.youtube.com/watch?v=kCc8FmEb1nY)|逐行手写代码，按《Attention Is All You Need》从零构建并训练一个 GPT。|
|[Neural Networks: Zero to Hero（课程）](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)|系统化的神经网络入门课程，从最基础的反向传播逐步进阶到现代 GPT。|
|[Let's build the GPT Tokenizer](https://www.youtube.com/watch?v=zduSFxRajkE)|2 小时深入讲解 BPE 分词器的原理与实现，并揭示分词导致的诸多 LLM 怪异行为。|
|[Let's reproduce GPT-2 (124M)](https://www.youtube.com/watch?v=l8pRSuU81PU)|4 小时长视频，从空文件开始完整复现并优化训练出一个 GPT-2 (124M) 模型。|
|[[1hr Talk] Intro to Large Language Models](https://www.youtube.com/watch?v=zjkBMFhNj_g)|面向大众的 1 小时 LLM 入门，把 LLM 类比为新型操作系统并讨论其安全挑战。|
|[State of GPT (Microsoft Build 2023)](https://www.youtube.com/watch?v=bZQun8Y4L2A)|讲清 GPT 助手从预训练、监督微调到 RLHF 的完整训练管线。|
|[Deep Dive into LLMs like ChatGPT](https://www.youtube.com/watch?v=7xTGNNLPyMI)|3.5 小时面向大众的深入讲解，覆盖 ChatGPT 背后 LLM 的完整训练栈与思维模型。|
|[How I use LLMs](https://www.youtube.com/watch?v=EWvNQjAaOHw)|2 小时实战指南，结合日常场景演示如何高效使用各类大模型与其工具生态。|
|[Software Is Changing (Again)（软件 3.0，YC 2025）](https://www.youtube.com/watch?v=LCEmiRjPEtQ)|2025 年 YC 演讲，提出"软件 3.0"：用自然语言编程 LLM 的新范式。|
