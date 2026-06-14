## ChatGPT 应用开发指南

- [ChatGPT 应用开发指南](#chatgpt-应用开发指南)
  - [OpenAI 官方开发资源](#openai-官方开发资源)
  - [Prompt 开发资源](#prompt-开发资源)
  - [AI Agent 智能体开发框架](#ai-agent-智能体开发框架)
  - [LangChain 开发资源](#langchain-开发资源)
  - [向量数据库](#向量数据库)
  - [中文大模型开发资源](#中文大模型开发资源)
  - [大模型 API 与聚合网关](#大模型-api-与聚合网关)
  - [LLM 应用开发框架与平台](#llm-应用开发框架与平台)
  - [OpenAI 服务替代品](#openai-服务替代品)
  - [API 资源](#api-资源)
  - [一键部署资源](#一键部署资源)
  - [其他开发资源](#其他开发资源)

### OpenAI 官方开发资源

|名称|Stars|简介|备注|
|---|---|---|---|
|[OpenAI API 文档](https://platform.openai.com/docs)|-|OpenAI 官方开发者文档总入口|模型、API 参考、指南与最佳实践|
|[Responses API](https://platform.openai.com/docs/api-reference/responses)|-|当代最先进的模型调用接口|支持有状态对话、内置工具（网页/文件搜索、computer use）与函数调用|
|[openai-python](https://github.com/openai/openai-python)|![GitHub Repo stars](https://badgen.net/github/stars/openai/openai-python)|官方 Python 库，提供对 REST API 的同步与异步访问|OpenAI python 接口|
|[openai-node](https://github.com/openai/openai-node)|![GitHub Repo stars](https://badgen.net/github/stars/openai/openai-node)|官方 JavaScript / TypeScript 库|-|
|[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)|![GitHub Repo stars](https://badgen.net/github/stars/openai/openai-agents-python)|轻量而强大的多智能体编排框架|工具调用、安全护栏、会话管理与内置 tracing|
|[openai-cookbook](https://github.com/openai/openai-cookbook)|![GitHub Repo stars](https://badgen.net/github/stars/openai/openai-cookbook)|使用 OpenAI API 完成常见任务的示例代码与指南合集|OpenAI API 官方使用指南|

### Prompt 开发资源
|名称|Stars|简介|备注|
|---|---|---|---|
|[微软 guidance](https://github.com/microsoft/guidance)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/guidance)|A guidance language for controlling large language models.|更好的控制大模型工具|
|[高质量导师提示词 Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor)|![GitHub Repo stars](https://badgen.net/github/stars/JushBJJ/Mr.-Ranedeer-AI-Tutor)|A GPT-4 AI Tutor Prompt for customizable personalized learning experiences.|极具参考价值的提示词|
|[结构化高质量提示词 LangGPT](https://github.com/yzfly/LangGPT)|![GitHub Repo stars](https://badgen.net/github/stars/yzfly/LangGPT)|LangGPT: Empowering everyone to become a prompt expert!🚀 Structured Prompt，结构化提示词。|使用结构化方式写高质量提示词|
| [吴恩达《面向开发者的 ChatGPT 提示词工程》](https://learn.deeplearning.ai/)|-| DeepLearning.ai 创始人吴恩达与 OpenAI 开发者 Iza Fulford 联手推出了一门面向开发者的技术教程：《**ChatGPT 提示工程**》|[《面向开发者的 ChatGPT 提示词工程》非官方版中英双语字幕](https://github.com/GitHubDaily/ChatGPT-Prompt-Engineering-for-Developers-in-Chinese) - **中文视频地址：[面向开发者的 ChatGPT 提示词工程](https://space.bilibili.com/15467823/channel/seriesdetail?sid=3247315&ctype=0)** - **英文原视频地址：[ChatGPT Prompt Engineering for Developers](https://learn.deeplearning.ai/)**|
|[Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/advanced-prompt-engineering?pivots=programming-language-chat-completions)|-|微软官方教程,介绍了 Prompt 设计和工程中的一些高级玩法，涵盖系统消息、少样本学习、非聊天场景等内容。|-|

### AI Agent 智能体开发框架

构建 AI 智能体（Agent）的主流框架，是 2024 年后 LLM 应用开发的核心方向。

|名称|Stars|简介|备注|
|---|---|---|---|
|[LangGraph](https://github.com/langchain-ai/langgraph)|![GitHub Repo stars](https://badgen.net/github/stars/langchain-ai/langgraph)|Build resilient agents.|LangChain 团队出品，基于图结构编排有状态、可循环的多智能体工作流|
|[LlamaIndex](https://github.com/run-llama/llama_index)|![GitHub Repo stars](https://badgen.net/github/stars/run-llama/llama_index)|The leading framework for building LLM-powered agents over your data.|主打 RAG 与文档智能体，擅长把私有数据接入 LLM|
|[AutoGen](https://github.com/microsoft/autogen)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/autogen)|A programming framework for agentic AI.|微软出品，多智能体对话协作框架|
|[AG2](https://github.com/ag2ai/ag2)|![GitHub Repo stars](https://badgen.net/github/stars/ag2ai/ag2)|AG2 (formerly AutoGen): The Open-Source AgentOS.|由原 AutoGen 社区分支而来的开源 AgentOS|
|[CrewAI](https://github.com/crewAIInc/crewAI)|![GitHub Repo stars](https://badgen.net/github/stars/crewAIInc/crewAI)|Framework for orchestrating role-playing, autonomous AI agents.|以"角色扮演 + 协作"组建智能体团队完成复杂任务|
|[MetaGPT](https://github.com/FoundationAgents/MetaGPT)|![GitHub Repo stars](https://badgen.net/github/stars/FoundationAgents/MetaGPT)|The Multi-Agent Framework: First AI Software Company.|用多智能体模拟软件公司，主打自然语言编程|
|[OpenAI Agents SDK](https://github.com/openai/openai-agents-python)|![GitHub Repo stars](https://badgen.net/github/stars/openai/openai-agents-python)|A lightweight, powerful framework for multi-agent workflows.|OpenAI 官方多智能体编排框架，Swarm 的生产级继任者|
|[Pydantic AI](https://github.com/pydantic/pydantic-ai)|![GitHub Repo stars](https://badgen.net/github/stars/pydantic/pydantic-ai)|AI Agent Framework, the Pydantic way.|Pydantic 团队出品，强类型、结构化输出友好的智能体框架|
|[smolagents](https://github.com/huggingface/smolagents)|![GitHub Repo stars](https://badgen.net/github/stars/huggingface/smolagents)|a barebones library for agents that think in code.|Hugging Face 出品，极简风格、让智能体以写代码方式思考|
|[Agno](https://github.com/agno-agi/agno)|![GitHub Repo stars](https://badgen.net/github/stars/agno-agi/agno)|Build, run, and manage agent platforms.|原 phidata，构建与运维智能体平台的全栈框架|
|[Semantic Kernel](https://github.com/microsoft/semantic-kernel)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/semantic-kernel)|Integrate cutting-edge LLM technology quickly and easily into your apps.|微软出品，面向企业级应用集成 LLM，支持多语言|
|[CAMEL](https://github.com/camel-ai/camel)|![GitHub Repo stars](https://badgen.net/github/stars/camel-ai/camel)|The first and the best multi-agent framework. Finding the Scaling Law of Agents.|研究导向的多智能体框架，探索智能体的 Scaling Law|
|[Coze Studio](https://github.com/coze-dev/coze-studio)|![GitHub Repo stars](https://badgen.net/github/stars/coze-dev/coze-studio)|An AI agent development platform with all-in-one visual tools.|字节扣子开源版，一站式可视化智能体开发平台|
|[Flowise](https://github.com/FlowiseAI/Flowise)|![GitHub Repo stars](https://badgen.net/github/stars/FlowiseAI/Flowise)|Build AI Agents, Visually.|拖拽式可视化构建 LLM 应用与智能体|
|[Langflow](https://github.com/langflow-ai/langflow)|![GitHub Repo stars](https://badgen.net/github/stars/langflow-ai/langflow)|A powerful tool for building and deploying AI-powered agents and workflows.|可视化低代码工具，构建与部署 AI 智能体和工作流|
|[AutoAgent](https://github.com/HKUDS/AutoAgent)|![GitHub Repo stars](https://badgen.net/github/stars/HKUDS/AutoAgent)|Fully-Automated and Zero-Code LLM Agent Framework.|港大数据智能实验室出品，全自动、零代码的 LLM 智能体框架，用自然语言即可创建并运行智能体|

### LangChain 开发资源

|名称|Stars|简介|备注|
|---|---|---|---|
|[langchain](https://github.com/hwchase17/langchain)|![GitHub Repo stars](https://badgen.net/github/stars/hwchase17/langchain)|Building applications with LLMs through composability|开发自己的 ChatGPT 应用|
|[langchain-aiplugin](https://github.com/langchain-ai/langchain-aiplugin)|![GitHub Repo stars](https://badgen.net/github/stars/langchain-ai/langchain-aiplugin)|-| langChain 插件|
|[LangFlow](https://github.com/logspace-ai/langflow)|![GitHub Repo stars](https://badgen.net/github/stars/logspace-ai/langflow)|LangFlow is a UI for LangChain, designed with react-flow to provide an effortless way to experiment and prototype flows.|LangChain的一个UI|
|[langchain-tutorials](https://github.com/gkamradt/langchain-tutorials)|![GitHub Repo stars](https://badgen.net/github/stars/gkamradt/langchain-tutorials)|Overview and tutorial of the LangChain Library|LangChain 教程|
|[LangChain 教程](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/)|-|-|吴恩达与 LangChain 开发者推出的教程，目前免费|
|[LangChain 的中文入门教程](https://github.com/liaokongVFX/LangChain-Chinese-Getting-Started-Guide)|![GitHub Repo stars](https://badgen.net/github/stars/liaokongVFX/LangChain-Chinese-Getting-Started-Guide)|LangChain 的中文入门教程|gitbook地址：https://liaokong.gitbook.io/llm-kai-fa-jiao-cheng/|
|[langchain-ChatGLM](https://github.com/imClumsyPanda/langchain-ChatGLM)|![GitHub Repo stars](https://badgen.net/github/stars/imClumsyPanda/langchain-ChatGLM)|langchain-ChatGLM, local knowledge based ChatGLM with langchain |基于本地知识库的 ChatGLM 问答|
|[awesome-langchain](https://github.com/kyrolabs/awesome-langchain)|![GitHub Repo stars](https://badgen.net/github/stars/kyrolabs/awesome-langchain)|😎 Awesome list of tools and projects with the awesome LangChain framework. |LangChain Awesome 资源列表。|

### 向量数据库

如果说 ChatGPT 是 LLM 的处理核心，prompts 是 code，那么向量数据库就是 LLM 需要的存储。

|名称|Stars|简介| 备注 |
-|-|-|-
|[PineCone](https://www.pinecone.io/) |-|Pinecone为向量数据提供了数据存储解决方案。|提供免费方案，目前注册火爆|
|[chroma](https://github.com/chroma-core/chroma) |![GitHub Repo stars](https://badgen.net/github/stars/chroma-core/chroma)|Chroma 是一个用于 Python / JavaScript LLM 应用程序的本地向量数据库，它具有内存快速访问的优势。|开源免费|
|[qdrant](https://github.com/qdrant/qdrant) |![GitHub Repo stars](https://badgen.net/github/stars/qdrant/qdrant)|QDRANT AI应用程序矢量数据库，也提供云数据库: https://cloud.qdrant.io/|现在注册有 1G 的永久免费数据库|
|[Milvus](https://github.com/milvus-io/milvus) |![GitHub Repo stars](https://badgen.net/github/stars/milvus-io/milvus)|Milvus 是一个开源矢量数据库，旨在为嵌入相似性搜索和 AI 应用程序提供支持。 除了向量，Milvus 还支持布尔型、整数、浮点数等数据类型。 Milvus 中的一个集合可以包含多个字段，用于容纳不同的数据特征或属性。 Milvus 将标量过滤与强大的向量相似性搜索相结合，为分析非结构化数据提供了一个现代、灵活的平台。|目前提供多种部署方式，支持docker, k8s, embed-milvus(pip install嵌入安装)，同时也有[在线云服务](https://cloud.zilliz.com/)。|
|[weaviate](https://github.com/weaviate/weaviate) |![GitHub Repo stars](https://badgen.net/github/stars/weaviate/weaviate)|开源的向量数据库，可以存储对象和向量，允许将向量搜索与结构化过滤相结合，并具有云原生数据库的容错性和可扩展性，可通过 GraphQL、REST 和各种语言客户端进行访问。|-|
|[txtai](https://github.com/neuml/txtai) |![GitHub Repo stars](https://badgen.net/github/stars/neuml/txtai)|用于语义搜索、LLM编排和语言模型工作流的一体化开源嵌入式数据库。|💡 All-in-one open-source embeddings database for semantic search, LLM orchestration and language model workflows|
|[pgvector](https://github.com/pgvector/pgvector) |![GitHub Repo stars](https://badgen.net/github/stars/pgvector/pgvector)|PostgreSQL 的开源向量相似度搜索扩展，在关系数据库中存储向量并支持精确与近似最近邻检索。|无需额外引入新数据库|
|[LanceDB](https://github.com/lancedb/lancedb) |![GitHub Repo stars](https://badgen.net/github/stars/lancedb/lancedb)|面向多模态 AI 的开源嵌入式向量检索库，基于 Lance 列式格式，支持向量、全文与 SQL 检索。|无需独立服务，进程内嵌入|
|[Faiss](https://github.com/facebookresearch/faiss) |![GitHub Repo stars](https://badgen.net/github/stars/facebookresearch/faiss)|Meta FAIR 出品的稠密向量高效相似度搜索与聚类库。|经典底层检索库|

### 中文大模型开发资源

|名称|Stars|简介|备注|
|---|---|---|---|
|[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) |![GitHub Repo stars](https://badgen.net/github/stars/THUDM/ChatGLM-6B)|ChatGLM-6B: An Open Bilingual Dialogue Language Model |ChatGLM-6B 是一个开源的、支持中英双语的对话语言模型，基于 General Language Model (GLM) 架构，具有 62 亿参数。结合模型量化技术，用户可以在消费级的显卡上进行本地部署（INT4 量化级别下最低只需 6GB 显存）。 ChatGLM-6B 使用了和 ChatGPT 相似的技术，针对中文问答和对话进行了优化。经过约 1T 标识符的中英双语训练，辅以监督微调、反馈自助、人类反馈强化学习等技术的加持，62 亿参数的 ChatGLM-6B 已经能生成相当符合人类偏好的回答。|
|[baichuan-7B](https://github.com/baichuan-inc/baichuan-7B) |![GitHub Repo stars](https://badgen.net/github/stars/baichuan-inc/baichuan-7B)|A large-scale 7B pretraining language model developed by Baichuan |baichuan-7B 是由百川智能开发的一个开源可商用的大规模预训练语言模型。基于 Transformer 结构，在大约1.2万亿 tokens 上训练的70亿参数模型，支持中英双语，上下文窗口长度为4096。在标准的中文和英文权威 benchmark（C-EVAL/MMLU）上均取得同尺寸最好的效果。|
|[Huatuo-Llama-Med-Chinese](https://github.com/SCIR-HI/Huatuo-Llama-Med-Chinese)|![GitHub Repo stars](https://badgen.net/github/stars/SCIR-HI/Huatuo-Llama-Med-Chinese)|Repo for BenTsao [original name: HuaTuo (华驼)], Llama-7B tuned with Chinese medical knowledge. |华佗——医疗领域中文大模型|
|[ChatYuan](https://github.com/clue-ai/ChatYuan) |![GitHub Repo stars](https://badgen.net/github/stars/clue-ai/ChatYuan)|ChatYuan: Large Language Model for Dialogue in Chinese and English.|ChatYuan-large-v2是ChatYuan系列中以轻量化实现高质量效果的模型之一，用户可以在消费级显卡、 PC甚至手机上进行推理（INT4 最低只需 400M ）。|
|[langchain-ChatGLM](https://github.com/imClumsyPanda/langchain-ChatGLM)|![GitHub Repo stars](https://badgen.net/github/stars/imClumsyPanda/langchain-ChatGLM)|langchain-ChatGLM, local knowledge based ChatGLM with langchain |基于本地知识库的 ChatGLM 问答|
|[wenda](https://github.com/wenda-LLM/wenda)|![GitHub Repo stars](https://badgen.net/github/stars/wenda-LLM/wenda)|闻达：一个LLM调用平台。|多种大语言模型：目前支持离线部署模型有chatGLM-6B、chatRWKV、llama系列以及moss，在线API访问openai api和chatGLM-130b api|

### OpenAI 服务替代品

|名称|简介|备注|
|---|---|---|
|[Claude 官方文档](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design) |OpenAI 前成员出走创立了Anthropic 公司旗下的大模型 Claude 开发官方文档。|OpenAI 的强有力竞争对手|
|[Cohere](https://docs.cohere.com/docs) |coherence 提供了前沿的语言处理技术 API 服务。|-|
|[AI21](https://docs.ai21.com/) |以色列公司 A21 Labs 开发了一个名为 Jurassic-1 Jumbo 的模型。该模型大小与 1750 亿参数的 GPT-3 类似。该公司还围绕 Jurassic-1 Jumbo 逐渐构建起一系列产品，包括一个名为 AI21 Studio 的“AI-as-a-service”平台。该平台允许客户创建虚拟助手、聊天机器人、内容审核工具等。|-|
|[智谱AI开放平台](https://open.bigmodel.cn/) |中文大模型 API。 基于千亿基座模型 GLM-130B，注入代码预训练，通过有监督微调等技术实现人类意图对齐的中英双语大模型。|-|

### API 资源
|名称|Stars|简介|备注|
|---|---|---|---|
|[gpt4free](https://github.com/xtekky/gpt4free) |![GitHub Repo stars](https://badgen.net/github/stars/xtekky/gpt4free)|decentralising the Ai Industry, just some language model api's...|免费的 ChatGPT API|
|[gpt4free-ts](https://github.com/xiangsx/gpt4free-ts) |![GitHub Repo stars](https://badgen.net/github/stars/xiangsx/gpt4free-ts)|Providing a free OpenAI GPT-4 API ! This is a replication project for the typescript version of xtekky/gpt4free|typescript 版本的免费 ChatGPT API|
|[claude-to-chatgpt](https://github.com/jtsang4/claude-to-chatgpt) |![GitHub Repo stars](https://badgen.net/github/stars/jtsang4/claude-to-chatgpt)|This project converts the API of Anthropic's Claude model to the OpenAI Chat API format.|将 Claude API格式转换为 ChatGPT API 格式|
|[Bard-API](https://github.com/dsdanielpark/Bard-API) |![GitHub Repo stars](https://badgen.net/github/stars/dsdanielpark/Bard-API)|The unofficial python package that returns response of Google Bard through cookie value.|谷歌 bard 网页版 API 封装|
|[claude-in-slack-api](https://github.com/yokonsan/claude-in-slack-api) |![GitHub Repo stars](https://badgen.net/github/stars/yokonsan/claude-in-slack-api)|claude in slack api.|通过 Slack API 来使用 Claude，[保姆级教程](https://mp.weixin.qq.com/s?__biz=Mzg4MjkzMzc1Mg==&mid=2247483961&idx=1&sn=c009f4ea28287daeaa4de17278c8228e&chksm=cf4e68aef839e1b8fe49110341e2a557e0b118fee82d490143656a12c7f85bdd4ef6f65ffd16&token=1094126126&lang=zh_CN#rd)|
|[yiyan-api](https://github.com/zhuweiyou/yiyan-api) |![GitHub Repo stars](https://badgen.net/github/stars/zhuweiyou/yiyan-api)|-|百度文心一言网页版 API |


### 大模型 API 与聚合网关

统一接入多家大模型的网关与各家官方 API（取代早期的"逆向/破解 API"方案）。

|名称|链接|简介|
|---|---|---|
|[LiteLLM](https://github.com/BerriAI/litellm)|![GitHub Repo stars](https://badgen.net/github/stars/BerriAI/litellm)|统一接口调用 100+ 大模型供应商的 Python SDK 与 AI 网关，兼容 OpenAI 格式，可作库或代理服务部署|
|[One API](https://github.com/songquanpeng/one-api)|![GitHub Repo stars](https://badgen.net/github/stars/songquanpeng/one-api)|开源的大模型 API 管理与分发系统，将多家供应商统一为标准接口，支持密钥管理与负载均衡|
|[New API](https://github.com/Calcium-Ion/new-api)|![GitHub Repo stars](https://badgen.net/github/stars/Calcium-Ion/new-api)|新一代大模型网关与 API 管理系统，支持 OpenAI、Claude、Gemini 等格式互转|
|[OpenRouter](https://openrouter.ai/)|-|统一接口聚合数百个大模型，完全兼容 OpenAI 格式，自动故障转移与成本优选|
|[Anthropic Claude API](https://docs.anthropic.com/en/home)|-|Anthropic 官方 Claude 模型 API 与开发者文档|
|[Google Gemini API](https://ai.google.dev/gemini-api/docs)|-|Google 官方 Gemini 模型 API 与开发者文档|
|[DeepSeek API](https://api-docs.deepseek.com/)|-|DeepSeek 官方 API 平台，兼容 OpenAI 与 Anthropic 格式|
|[Moonshot (Kimi) API](https://platform.moonshot.ai/)|-|月之暗面 Kimi 开放平台，提供与 OpenAI 兼容的大模型 API|
|[智谱 BigModel](https://open.bigmodel.cn/)|-|智谱 AI 开放平台，提供 GLM 系列大模型 API 及智能体、知识库等开发能力|

### LLM 应用开发框架与平台

|名称|链接|简介|
|---|---|---|
|[LangChain](https://github.com/langchain-ai/langchain)|![GitHub Repo stars](https://badgen.net/github/stars/langchain-ai/langchain)|构建智能体与 LLM 应用的框架，串联可互操作的组件与海量第三方集成|
|[LlamaIndex](https://github.com/run-llama/llama_index)|![GitHub Repo stars](https://badgen.net/github/stars/run-llama/llama_index)|面向智能体应用的框架，通过数据连接器、索引与高级检索为 LLM 注入私有数据|
|[Dify](https://github.com/langgenius/dify)|![GitHub Repo stars](https://badgen.net/github/stars/langgenius/dify)|开源的生产级 LLM 应用开发平台，集成可视化工作流、RAG 管线、智能体与模型管理|
|[Flowise](https://github.com/FlowiseAI/Flowise)|![GitHub Repo stars](https://badgen.net/github/stars/FlowiseAI/Flowise)|开源可视化/低代码平台，拖拽式构建 AI 智能体与工作流|
|[Vercel AI SDK](https://github.com/vercel/ai)|![GitHub Repo stars](https://badgen.net/github/stars/vercel/ai)|Next.js 团队出品的 TypeScript 工具包，用于在 React/Vue/Svelte 等框架中构建 AI 应用|
|[Haystack](https://github.com/deepset-ai/haystack)|![GitHub Repo stars](https://badgen.net/github/stars/deepset-ai/haystack)|deepset 出品的开源 Python 框架，通过模块化管线构建生产级 LLM 应用、RAG 与智能体|
|[Semantic Kernel](https://github.com/microsoft/semantic-kernel)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/semantic-kernel)|微软开源 SDK，在 Python/.NET/Java 中快速集成 LLM 能力，构建智能体系统|

### 一键部署资源

|名称|Stars|简介|备注|
|---|---|---|---|
|[vercel-labs/ai](https://github.com/vercel-labs/ai) |![GitHub Repo stars](https://badgen.net/github/stars/vercel-labs/ai)|Build AI-powered applications with React, Svelte, and Vue. |使用 Vercel 平台一键部署多种 AI，ChatGPT 应用。|
|[ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web) |![GitHub Repo stars](https://badgen.net/github/stars/Yidadaa/ChatGPT-Next-Web)|One-Click to deploy well-designed ChatGPT web UI on Vercel. |一键拥有你自己的 ChatGPT 网页服务。|
|[ChatGPT-Midjourney](https://github.com/Licoy/ChatGPT-Midjourney) |![GitHub Repo stars](https://badgen.net/github/stars/Licoy/ChatGPT-Midjourney)| Own your own ChatGPT+Midjourney web service with one click |🎨 一键拥有你自己的 ChatGPT+Midjourney 网页服务 |
|[novel](https://github.com/steven-tey/novel) |![GitHub Repo stars](https://badgen.net/github/stars/steven-tey/novel)|Notion-style WYSIWYG editor with AI-powered autocompletions. |AI 驱动的 Notion 风格的所见即所得自动完成编辑器|
|[ai-chatbot](https://github.com/vercel-labs/ai-chatbot) |![GitHub Repo stars](https://badgen.net/github/stars/vercel-labs/ai-chatbot)|A full-featured, hackable Next.js AI chatbot built by Vercel Labs. |由Vercel Labs构建的全功能，可编程的Next.js AI聊天机器人|

### 结构化输出

|名称|Stars|简介|备注|
|---|---|---|---|
|[instructor](https://github.com/jxnl/instructor) |![GitHub Repo stars](https://badgen.net/github/stars/jxnl/instructor)|structured outputs for llms. |将大模型的输出结构化为 Python 的对象。推荐场景：在使用 API 调用大模型时，调用闭源模型时，使用该库。|
|[outlines](https://github.com/outlines-dev/outlines) |![GitHub Repo stars](https://badgen.net/github/stars/outlines-dev/outlines)|Structured Text Generation. |将大模型的输出结构化,从模型输出的 logits 层面限制。推荐场景：调用huggingface上的开源模型、本地部署模型时，使用该库。|

### 数据结构化提取
|名称|Stars|简介|备注|
|---|---|---|---|
|[MinerU](https://github.com/opendatalab/MinerU) |![GitHub Repo stars](https://badgen.net/github/stars/opendatalab/MinerU)|A one-stop, open-source, high-quality data extraction tool, supports PDF/webpage/e-book extraction. |一站式开源高质量数据提取工具，支持PDF/网页/多格式电子书提取。|
|[gptpdf](https://github.com/CosmosShadow/gptpdf) |![GitHub Repo stars](https://badgen.net/github/stars/CosmosShadow/gptpdf)|Using GPT to parse PDF. |使用 GPT-4o 的多模态能力解析pdf|
|[ragflow](https://github.com/infiniflow/ragflow)|![GitHub Repo stars](https://badgen.net/github/stars/infiniflow/ragflow)|RAGFlow is an open-source RAG (Retrieval-Augmented Generation) engine based on deep document understanding.|RAGFlow 是一款基于深度文档理解构建的开源 RAG（Retrieval-Augmented Generation）引擎。RAGFlow 可以为各种规模的企业及个人提供一套精简的 RAG 工作流程，结合大语言模型（LLM）针对用户各类不同的复杂格式数据提供可靠的问答以及有理有据的引用。|
|[deepdoctection](https://github.com/deepdoctection/deepdoctection) |![GitHub Repo stars](https://badgen.net/github/stars/deepdoctection/deepdoctection)|A Repo For Document AI. |文档处理 AI|
|[360LayoutAnalysis](https://github.com/360AILAB-NLP/360LayoutAnalysis) |![GitHub Repo stars](https://badgen.net/github/stars/360AILAB-NLP/360LayoutAnalysis)|360LayoutAnaylsis, a series Document Analysis Models and Datasets deleveped by 360 AI Research Institute. |360 出品的文档版式分享工具|


### 其他开发资源

|名称|Stars|简介|备注|
|---|---|---|---|
|[LlamaIndex](https://github.com/jerryjliu/llama_index) | ![GitHub Repo stars](https://img.shields.io/github/stars/jerryjliu/llama_index.svg?style=social) | Provides a central interface to connect your LLMs with external data. |将llm与外部数据连接起来。|
|[dspy](https://github.com/stanfordnlp/dspy) | ![GitHub Repo stars](https://img.shields.io/github/stars/stanfordnlp/dspy) | DSPy: The framework for programming—not prompting—foundation models. |下一代 Agents 自优化开发框架|
|[llm-numbers](https://github.com/ray-project/llm-numbers) |![GitHub Repo stars](https://badgen.net/github/stars/ray-project/llm-numbers)|Numbers every LLM developer should know.|大模型开发者必知数据|
| [《用ChatGPT API构建系统》课程](https://learn.deeplearning.ai/chatgpt-building-system/lesson/1/introduction)|-| DeepLearning.ai 创始人吴恩达和OpenAI合作的新的“使用ChatGPT API构建系统”的课程|课程链接（中英文字幕）: https://pan.baidu.com/s/1BgUKWwh5YSby3IVkGvLi_w?pwd=22b7 提取码: 22b7|
|[开发指南：ChatGPT 插件开发](https://mp.weixin.qq.com/s/AmNkiLOqJo7tEJZPX34oeg) |-|详细介绍了开发流程，并通过“待办事项列表(to-do list)插件”的案例开发过程进行了演示。|-|
|[gptcache](https://github.com/zilliztech/gptcache)|![GitHub Repo stars](https://badgen.net/github/stars/zilliztech/gptcache)|Semantic cache for LLMs. Fully integrated with LangChain and llama_index.|AIGC 应用程序的memcache,一个强大的缓存库，可用于加速和降低依赖 LLM 服务的聊天应用程序的成本，可用作 AIGC 应用程序的memcache，类似于 Redis 用于传统应用程序的方式。[知乎简介](https://zhuanlan.zhihu.com/p/618630093)：有效果实测图和基本介绍。|
|[dify](https://github.com/langgenius/dify) |![GitHub Repo stars](https://badgen.net/github/stars/langgenius/dify)|One API for plugins and datasets, one interface for prompt engineering and visual operation, all for creating powerful AI applications.|快速创建AI应用程序平台，网站 [dify.ai](dify.ai) |
|[OpenChat](https://github.com/openchatai/OpenChat) |![GitHub Repo stars](https://badgen.net/github/stars/openchatai/OpenChat)|Run and create custom ChatGPT-like bots with OpenChat, embed and share these bots anywhere, the open-source chatbot console. |构建聊天机器人。|
|[gptlink](https://github.com/gptlink/gptlink) |![GitHub Repo stars](https://badgen.net/github/stars/gptlink/gptlink)|-|10分钟搭建自己可免费商用的ChatGPT环境，搭建简单，包含用户，订单，任务，付费等功能.|
|[readme-ai](https://github.com/eli64s/README-AI) |![GitHub Repo stars](https://badgen.net/github/stars/eli64s/readme-ai)|Automated README.md files. |使用 OpenAI 语言模型 API，为编写美观、结构化和信息丰富的 README.md 文件而设计的命令行工具。|
|[dialoqbase](https://github.com/n4ze3m/dialoqbase) |![GitHub Repo stars](https://badgen.net/github/stars/n4ze3m/dialoqbase)|Create chatbots with ease.|轻松创建聊天机器人|
|[privateGPT](https://github.com/imartinez/privateGPT)|![GitHub Repo stars](https://badgen.net/github/stars/imartinez/privateGPT)|基于 Llama 的本地私人文档助手|-|
|[rebuff](https://github.com/woop/rebuff) |![GitHub Repo stars](https://badgen.net/github/stars/woop/rebuff)|Rebuff.ai - Prompt Injection Detector.|Prompt 攻击检测，内容检测|
|[text-generation-webui](https://github.com/oobabooga/text-generation-webui)|![GitHub Repo stars](https://badgen.net/github/stars/oobabooga/text-generation-webui)|-|一个用于运行大型语言模型(如LLaMA, LLaMA .cpp, GPT-J, Pythia, OPT和GALACTICA)的 web UI。|
|[embedchain](https://github.com/embedchain/embedchain)|![GitHub Repo stars](https://badgen.net/github/stars/embedchain/embedchain)|embedchain is a framework to easily create LLM powered bots over any dataset.|Embedchain是一个框架，可轻松在任何数据集上创建LLM驱动的机器人。|
|[aigc](https://github.com/phodal/aigc)|![GitHub Repo stars](https://badgen.net/github/stars/phodal/aigc)|-|《构筑大语言模型应用：应用开发与架构设计》一本关于 LLM 在真实世界应用的开源电子书，介绍了大语言模型的基础知识和应用，以及如何构建自己的模型。其中包括Prompt的编写、开发和管理，探索最好的大语言模型能带来什么，以及LLM应用开发的模式和架构设计。|
|[FLAML](https://github.com/microsoft/FLAML)|![GitHub Repo stars](https://badgen.net/github/stars/microsoft/FLAML)|A fast library for AutoML and tuning. Join our Discord: https://discord.gg/Cppx2vSPVP.|FLAML一个用于机器学习和人工智能操作的高效自动化的轻量级 python 库。它基于大型语言模型、机器学习模型等实现工作流自动化，并优化其性能。|
|[LLMStack](https://github.com/trypromptly/LLMStack)|![GitHub Repo stars](https://badgen.net/github/stars/trypromptly/LLMStack)|No-code platform to build LLM Agents, workflows and applications with your data.|无代码平台，利用您的数据构建 LLM 代理、工作流程和应用程序。|
|[giskard](https://github.com/Giskard-AI/giskard-oss)|![GitHub Repo stars](https://badgen.net/github/stars/Giskard-AI/giskard-oss)|Open-Source Evaluation & Testing library for LLM Agents.|面向 LLM 与智能体的开源评测与测试库，自动检测幻觉、有害内容、提示注入、偏见等问题|
