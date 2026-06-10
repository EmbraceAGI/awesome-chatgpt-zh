## LLMs

本章节收录主流大语言模型。先是 2024–2026 年最具影响力的旗舰、开源与国产模型，随后保留早期经典开源 LLM 供学习参考。

### 2024–2026 主流大模型

> 时间与版本截至 2026 年初，模型迭代极快，请以官方渠道为准。

#### 国外闭源旗舰模型

| 模型 | 开发方 | 链接 | 中文简介（关键能力与发布时间） |
|------|--------|------|--------------------------------|
| GPT-5 | OpenAI | [openai.com](https://openai.com/index/introducing-gpt-5/) | 2025 年 8 月发布，OpenAI 新一代旗舰，统一推理与对话（自动调度"思考"模式），取代 GPT-4o/o3 成为 ChatGPT 默认模型。 |
| o3 / o4-mini | OpenAI | [openai.com](https://openai.com/index/introducing-o3-and-o4-mini/) | 2025 年 4 月发布的 o 系列推理模型，"先思考后回答"，o4-mini 主打高性价比快速推理。 |
| GPT-4.1 | OpenAI | [openai.com](https://openai.com/index/gpt-4-1/) | 2025 年 4 月发布，专精编码，100 万 token 长上下文，指令遵循强。 |
| Claude Opus 4.5 | Anthropic | [anthropic.com](https://www.anthropic.com/news/claude-opus-4-5) | 2025 年 11 月发布，Anthropic 最强模型，编码与智能体能力顶尖。 |
| Claude Sonnet 4.5 | Anthropic | [anthropic.com](https://www.anthropic.com/news/claude-sonnet-4-5) | 2025 年 9 月发布，平衡性能与成本，长程智能体任务表现优异。 |
| Claude 4（Opus 4 / Sonnet 4） | Anthropic | [anthropic.com](https://www.anthropic.com/news/claude-4) | 2025 年 5 月发布的第 4 代，Opus 4 号称"世界最佳编码模型"。 |
| Gemini 3 Pro | Google DeepMind | [blog.google](https://blog.google/products/gemini/gemini-3/) | 2025 年 11 月发布，Google 最强多模态旗舰，"推理优先"，含 Deep Think 模式。 |
| Gemini 2.5 Pro / Flash | Google DeepMind | [developers.googleblog.com](https://developers.googleblog.com/en/gemini-2-5-thinking-model-updates/) | "思考型"系列，Pro 主打高智能、Flash 主打低延迟低成本。 |
| Grok 4 | xAI | [x.ai](https://x.ai/news) | 2025 年 7 月发布，256K 上下文，原生工具调用（代码、联网与 X 搜索）。 |

#### 国外开源 / 开放权重模型

| 模型 | 开发方 | 链接 | 中文简介（关键能力与发布时间） |
|------|--------|------|--------------------------------|
| Llama 4（Scout / Maverick） | Meta | [ai.meta.com](https://ai.meta.com/blog/llama-4-multimodal-intelligence/) | 2025 年 4 月发布，原生多模态 MoE，Scout 上下文达 10M，Maverick 多模态超 GPT-4o。 |
| Llama 3.3 70B | Meta | [llama.com](https://www.llama.com/) | 2024 年 12 月发布，70B 性能对标 3.1 的 405B，推理成本大幅降低。 |
| Mistral Large 3 | Mistral AI | [mistral.ai](https://mistral.ai/news/mistral-3/) | 2025 年 12 月发布，稀疏 MoE，41B 激活 / 675B 总参，开放权重前沿模型。 |
| Gemma 3 | Google | [ai.google.dev](https://ai.google.dev/gemma) | Google 开源小模型系列，基于 Gemini 技术，可单卡运行、多模态。 |

#### 国产大模型

| 模型 | 开发方 | 链接 | 中文简介（关键能力与发布时间） |
|------|--------|------|--------------------------------|
| DeepSeek-V3 | 深度求索 | [GitHub](https://github.com/deepseek-ai/DeepSeek-V3) | 2024 年 12 月发布，671B/37B 激活 MoE，以极高性价比对标 GPT-4 级别。 |
| DeepSeek-R1 | 深度求索 | [GitHub](https://github.com/deepseek-ai/DeepSeek-R1) | 2025 年 1 月发布的开源推理模型，比肩 o1，掀起全球开源推理浪潮。 |
| Qwen3（通义千问 3） | 阿里巴巴 | [GitHub](https://github.com/QwenLM/Qwen3) | 2025 年 4 月发布，Apache 2.0 开源，0.6B–235B 多规格，首推混合推理，支持 119 种语言与 MCP。 |
| GLM-4.6 / GLM-4.5 | 智谱 AI | [HuggingFace](https://huggingface.co/zai-org/GLM-4.5) | GLM-4.5（2025 年 7 月）355B/32B MoE，MIT 协议开源，面向智能体；GLM-4.6 进一步升级。 |
| Kimi K2 / K2 Thinking | 月之暗面 | [GitHub](https://github.com/moonshotai/Kimi-K2) | K2（2025 年 7 月）1T/32B MoE 开源；K2 Thinking（11 月）多项基准超 GPT-5、Sonnet 4.5。 |
| MiniMax M2 | MiniMax | [GitHub](https://github.com/MiniMax-AI) | 2025 年 10 月发布的开源大模型，主打高效推理与智能体能力。 |
| ERNIE 4.5 / 文心一言 | 百度 | [yiyan.baidu.com](https://yiyan.baidu.com/) | 2025 年 3 月发布，MoE 架构最高 424B/47B；配套 ERNIE X1 深度推理模型。 |
| 混元（Hunyuan / T1） | 腾讯 | [hunyuan.tencent.com](https://hunyuan.tencent.com/) | 腾讯自研大模型家族，T1 推理模型开放使用，覆盖文本与多模态。 |
| 豆包（Doubao） | 字节跳动 | [doubao.com](https://www.doubao.com/) | 字节 C 端 AI 应用，月活领先，背后为字节自研大模型矩阵。 |

#### 评测榜单与资源

| 资源 | 链接 | 中文简介 |
|------|------|----------|
| LMArena（原 Chatbot Arena） | [lmarena.ai](https://lmarena.ai/) | 众包匿名对战 + Elo 评分的权威 LLM 排行榜，业界最受认可的横向对比之一。 |
| Open LLM Leaderboard | [HuggingFace](https://huggingface.co/open-llm-leaderboard) | 基于标准化基准的开源模型自动评测榜单，适合硬指标对比。 |
| SuperCLUE | [superclueai.com](https://www.superclueai.com/) | 中文通用大模型综合性测评基准，中文场景的主流权威榜单。 |
| Artificial Analysis | [artificialanalysis.ai](https://artificialanalysis.ai/) | 第三方独立评测，汇总智能指数、速度、价格等维度，便于按性价比选型。 |
| Models.dev | [models.dev](https://models.dev/) / [GitHub](https://github.com/sst/models.dev) | SST 团队开源的 AI 模型数据库，收录各家模型的上下文窗口、输出上限、价格、能力（推理/工具调用/结构化输出）与开闭源信息；提供免费 JSON API（`models.dev/api.json`），是 opencode 等开源项目的模型数据源，数据以 TOML 文件社区共建。 |

### 早期经典开源 LLM（历史存档）

> 以下为 2023 年前后的开源模型，多数已被新版取代，保留供学习与参考。

### 大模型

|名称|Stars|简介| 备注 |
|-------|-------|-------|------|
|[grok-1](https://github.com/xai-org/grok-1) | ![GitHub Repo stars](https://badgen.net/github/stars/xai-org/grok-1) | Grok open release.|马斯克 X 开源大模型|
|[Mistral-7B](https://github.com/mistralai/mistral-src) | ![GitHub Repo stars](https://badgen.net/github/stars/mistralai/mistral-src) | Reference implementation of Mistral AI 7B v0.1 model.|Mistral-7B 开源模型，性能评价不错|
|[Alpaca](https://github.com/tatsu-lab/stanford_alpaca) | ![GitHub Repo stars](https://badgen.net/github/stars/tatsu-lab/stanford_alpaca) | Code and documentation to train Stanford's Alpaca models, and generate the data. |-|
|[WizardLM](https://github.com/nlpxucan/WizardLM) | ![GitHub Repo stars](https://badgen.net/github/stars/nlpxucan/WizardLM) | Family of instruction-following LLMs powered by Evol-Instruct: WizardLM, WizardCoder and WizardMath. |数学能力与 ChatGPT 相差无几的开源大模型|
|[BELLE](https://github.com/LianjiaTech/BELLE) | ![GitHub Repo stars](https://badgen.net/github/stars/LianjiaTech/BELLE) | A 7B Large Language Model fine-tune by 34B Chinese Character Corpus, based on LLaMA and Alpaca. |-|
|[Bloom](https://github.com/bigscience-workshop/model_card) | ![GitHub Repo stars](https://badgen.net/github/stars/bigscience-workshop/model_card) | BigScience Large Open-science Open-access Multilingual Language Model |-|
|[dolly](https://github.com/databrickslabs/dolly) | ![GitHub Repo stars](https://badgen.net/github/stars/databrickslabs/dolly) | Databricks’ Dolly, a large language model trained on the Databricks Machine Learning Platform |Databricks 发布的 Dolly 2.0 大语言模型。业内第一个开源、遵循指令的 LLM，它在透明且免费提供的数据集上进行了微调，该数据集也是开源的，可用于商业目的。这意味着 Dolly 2.0 可用于构建商业应用程序，无需支付 API 访问费用或与第三方共享数据。|
|[Falcon 40B](https://huggingface.co/tiiuae/falcon-40b-instruct) | | Falcon-40B-Instruct is a 40B parameters causal decoder-only model built by TII based on Falcon-40B and finetuned on a mixture of Baize. It is made available under the Apache 2.0 license. |-|
|[FastChat (Vicuna)](https://github.com/lm-sys/FastChat) | ![GitHub Repo stars](https://badgen.net/github/stars/lm-sys/FastChat) | An open platform for training, serving, and evaluating large language models. Release repo for Vicuna and FastChat-T5. |继草泥马（Alpaca）后，斯坦福联手CMU、UC伯克利等机构的学者再次发布了130亿参数模型骆马（Vicuna），仅需300美元就能实现ChatGPT 90%的性能。|
|[GLM-130B (ChatGLM)](https://github.com/THUDM/GLM-130B) | ![GitHub Repo stars](https://badgen.net/github/stars/THUDM/GLM-130B) | An Open Bilingual Pre-Trained Model (ICLR 2023) |
|[GPT-NeoX](https://github.com/EleutherAI/gpt-neox) | ![GitHub Repo stars](https://badgen.net/github/stars/EleutherAI/gpt-neox) | An implementation of model parallel autoregressive transformers on GPUs, based on the DeepSpeed library. |
|[Luotuo](https://github.com/LC1332/Luotuo-Chinese-LLM) | ![GitHub Repo stars](https://badgen.net/github/stars/LC1332/Luotuo-Chinese-LLM) | An Instruction-following Chinese Language model, LoRA tuning on LLaMA| 骆驼，中文大语言模型开源项目，包含了一系列语言模型。|
|[minGPT](https://github.com/karpathy/minGPT) |![GitHub Repo stars](https://badgen.net/github/stars/karpathy/minGPT)|A minimal PyTorch re-implementation of the OpenAI GPT (Generative Pretrained Transformer) training。|karpathy大神发布的一个 OpenAI GPT(生成预训练转换器)训练的最小 PyTorch 实现，代码十分简洁明了，适合用于动手学习 GPT 模型。|
|[ChatGLM-6B](https://github.com/THUDM/ChatGLM-6B) |![GitHub Repo stars](https://badgen.net/github/stars/THUDM/ChatGLM-6B)|ChatGLM-6B: An Open Bilingual Dialogue Language Model |ChatGLM-6B 是一个开源的、支持中英双语的对话语言模型，基于 General Language Model (GLM) 架构，具有 62 亿参数。结合模型量化技术，用户可以在消费级的显卡上进行本地部署（INT4 量化级别下最低只需 6GB 显存）。 ChatGLM-6B 使用了和 ChatGPT 相似的技术，针对中文问答和对话进行了优化。经过约 1T 标识符的中英双语训练，辅以监督微调、反馈自助、人类反馈强化学习等技术的加持，62 亿参数的 ChatGLM-6B 已经能生成相当符合人类偏好的回答。|
|[li-plus/chatglm.cpp](https://github.com/li-plus/chatglm.cpp)|![GitHub Repo stars](https://badgen.net/github/stars/li-plus/chatglm.cpp)|C++ implementation of ChatGLM-6B & ChatGLM2-6B|ChatGLM-6B & ChatGLM2-6B 模型的 C++ 高效实现|
|[Open-Assistant](https://github.com/LAION-AI/Open-Assistant)|![GitHub Repo stars](https://badgen.net/github/stars/LAION-AI/Open-Assistant)|-|知名 AI 机构 LAION-AI 开源的聊天助手，聊天能力很强，目前中文能力较差。|
|[llama.cpp](https://github.com/ggerganov/llama.cpp)|![GitHub Repo stars](https://badgen.net/github/stars/ggerganov/llama.cpp)|-|实现在MacBook上运行模型。|
|[EasyLM](https://github.com/young-geng/EasyLM#koala)|![GitHub Repo stars](https://badgen.net/github/stars/young-geng/EasyLM)|在羊驼基础上改进的新的聊天机器人考拉。|[介绍页](https://bair.berkeley.edu/blog/2023/04/03/koala/)|
|[FreedomGPT](https://github.com/ohmplatform/FreedomGPT) |![GitHub Repo stars](https://badgen.net/github/stars/ohmplatform/FreedomGPT)|-|自由无限制的可以在 windows 和 mac 上本地运行的 GPT，基于 Alpaca Lora 模型。|
|[FinGPT](https://github.com/AI4Finance-Foundation/FinGPT)|![GitHub Repo stars](https://badgen.net/github/stars/AI4Finance-Foundation/FinGPT)|Data-Centric FinGPT. Open-source for open finance! Revolutionize 🔥 We'll soon release the trained model.|金融领域大模型|
|[baichuan-7B](https://github.com/baichuan-inc/baichuan-7B) |![GitHub Repo stars](https://badgen.net/github/stars/baichuan-inc/baichuan-7B)|A large-scale 7B pretraining language model developed by Baichuan |baichuan-7B 是由百川智能开发的一个开源可商用的大规模预训练语言模型。基于 Transformer 结构，在大约1.2万亿 tokens 上训练的70亿参数模型，支持中英双语，上下文窗口长度为4096。在标准的中文和英文权威 benchmark（C-EVAL/MMLU）上均取得同尺寸最好的效果。|
|[baichuan-inc/Baichuan-13B](https://github.com/baichuan-inc/Baichuan-13B)|![GitHub Repo stars](https://badgen.net/github/stars/baichuan-inc/Baichuan-13B)|A 13B large language model developed by Baichuan Intelligent Technology|-|
|[open_llama](https://github.com/openlm-research/open_llama) |![GitHub Repo stars](https://badgen.net/github/stars/openlm-research/open_llama)|OpenLLaMA, a permissively licensed open source reproduction of Meta AI’s LLaMA 7B trained on the RedPajama dataset. |OpenLLaMA，允许开源复制Meta AI的LLaMA-7B 模型，在red睡衣数据集上训练得到。|
|[Chinese-LLaMA-Alpaca](https://github.com/ymcui/Chinese-LLaMA-Alpaca)|![GitHub Repo stars](https://badgen.net/github/stars/ymcui/Chinese-LLaMA-Alpaca)|中文LLaMA模型和经过指令精调的Alpaca大模型。|-|
|[gemma.cpp](https://github.com/google/gemma.cpp)|![GitHub Repo stars](https://badgen.net/github/stars/google/gemma.cpp)|用于 Google Gemma 模型的轻量级独立 C++ 推理引擎。|-|
|[gemma_pytorch](https://github.com/google/gemma_pytorch)|![GitHub Repo stars](https://badgen.net/github/stars/google/gemma_pytorch)|Google Gemma 模型的官方 PyTorch 实现。|-|

### Llama 官方仓库（2024.11.5更新） 
|名称|Stars|简介| 备注 |
|-------|-------|-------|------|
|[llama-models](https://github.com/meta-llama/llama-models) | ![GitHub Repo stars](https://badgen.net/github/stars/meta-llama/llama-models) | Llama模型的核心仓库，包含Llama 3等基础模型、工具、模型卡片、许可证和使用政策。 |Llama Stack的基础仓库|
|[PurpleLlama](https://github.com/meta-llama/PurpleLlama) | ![GitHub Repo stars](https://badgen.net/github/stars/meta-llama/PurpleLlama) | Llama Stack的安全组件，专注于安全风险管理和推理时间的缓解措施。 |处理模型安全相关问题|
|[llama-toolchain](https://github.com/meta-llama/llama-toolchain) | ![GitHub Repo stars](https://badgen.net/github/stars/meta-llama/llama-toolchain) | 提供模型开发全流程工具，包括推理、微调、安全防护和合成数据生成的接口和标准实现。 |开发者工具链|
|[llama-agentic-system](https://github.com/meta-llama/llama-agentic-system) | ![GitHub Repo stars](https://badgen.net/github/stars/meta-llama/llama-agentic-system) | 端到端的独立Llama Stack系统，提供了智能应用开发的底层接口和实现。 |用于构建智能应用|
|[llama-recipes](https://github.com/meta-llama/llama-recipes) | ![GitHub Repo stars](https://badgen.net/github/stars/meta-llama/llama-recipes) | 社区驱动的脚本和集成方案集合，提供各种实用工具和最佳实践。 |社区贡献的实用工具|

### Llama 2 系列 [2023.08.05 更新]

|名称|Stars|简介| 备注 |
|-------|-------|-------|------|
|[llama 2](https://github.com/facebookresearch/llama) | ![GitHub Repo stars](https://badgen.net/github/stars/facebookresearch/llama) | Inference code for LLaMA models. |llama 系列模型官方开源地址|
|[codellama](https://github.com/facebookresearch/codellama) | ![GitHub Repo stars](https://badgen.net/github/stars/facebookresearch/codellama) | Inference code for CodeLlama models |编程专用 llama 系列模型官方开源地址|
|[Llama 2中文社区](https://github.com/FlagAlpha/Llama2-Chinese)| ![GitHub Repo stars](https://badgen.net/github/stars/FlagAlpha/Llama2-Chinese) |-|Llama中文社区,最好的中文Llama大模型,完全开源可商用|
|[ollama](https://github.com/jmorganca/ollama)| ![GitHub Repo stars](https://badgen.net/github/stars/jmorganca/ollama)| Get up and running with Llama 2 and other large language models locally|本地运行 llama|
|[Firefly](https://github.com/yangjianxin1/Firefly)| ![GitHub Repo stars](https://badgen.net/github/stars/yangjianxin1/Firefly)|-|Firefly(流萤): 中文对话式大语言模型(全量微调+QLoRA),支持微调Llma2、Llama、Qwen、Baichuan、ChatGLM2、InternLM、Ziya、Bloom 等大模型|
|[Azure ChatGPT](https://github.com/microsoft/azurechatgpt)| ![GitHub Repo stars](https://badgen.net/github/stars/microsoft/azurechatgpt) | 🤖 Azure ChatGPT: Private & secure ChatGPT for internal enterprise use 💼|-|
|[LLaMA2-Accessory](https://github.com/Alpha-VLLM/LLaMA2-Accessory)| ![GitHub Repo stars](https://badgen.net/github/stars/Alpha-VLLM/LLaMA2-Accessory)| An Open-source Toolkit for LLM Development|-|

### 端侧模型(手机等设备运行)

|名称|Stars|简介| 备注 |
|-------|-------|-------|------|
|[Llama 3](https://github.com/meta-llama/llama-models) | ![GitHub Repo stars](https://badgen.net/github/stars/meta-llama/llama-models) | Meta最新发布的大语言模型系列。支持128K上下文窗口，基于TikToken分词。包含8B、70B等不同规模。发布于2024年3月。 |最新一代Llama模型，性能显著提升，需申请使用|
|[Danube3](https://h2o.ai/platform/danube/) | - | H2O.ai开发的高性能开源大语言模型系列。4B参数版本在10-shot HellaSwag基准测试中达到80%以上的准确率，性能超越Apple，与Microsoft相当。 |体现了小型模型通过优化也能达到优秀性能|
|[Gemma](https://github.com/google-deepmind/gemma) | ![GitHub Repo stars](https://badgen.net/github/stars/google-deepmind/gemma) | Google DeepMind基于Gemini技术开发的开源大语言模型系列。包含2B和7B两种规格，每种规格提供Base和Instruction-tuned两个版本。 |提供详细的技术报告和多框架的参考实现|
|[Phi-3](https://github.com/microsoft/Phi-3CookBook) | ![GitHub Repo stars](https://badgen.net/github/stars/microsoft/Phi-3CookBook) | 微软开发的小型语言模型系列。包含Phi-3-mini(3.8B)、Phi-3-small(7B)两种规格，在同等规模和更大规模模型的对比中展现出优秀性能。 |在语言理解、推理、编程和数学等基准测试中表现出色，提供详细的使用指南CookBook|
|[Qwen2.5](https://github.com/QwenLM/Qwen2.5) | ![GitHub Repo stars](https://badgen.net/github/stars/QwenLM/Qwen2.5) | 阿里云通义千问团队开发的大语言模型系列。包含0.5B、1.8B、4B、7B、14B、72B等多种规模，每个规模都提供Base和Chat版本。 |支持中英等多语言，适用场景从移动设备到企业级高性能部署|
|[SmolLM](https://huggingface.co/collections/HuggingFaceTB/smollm-6695016cad7167254ce15966) | - | 轻量级语言模型系列，包含135M、360M和1.7B三种规模，每种规格都提供base和instruct版本。开源了训练语料库。 |特别优化用于移动设备和WebGPU运行，支持浏览器中直接运行demo|


### 自由不受限制模型
|名称|Stars|简介| 备注 |
|-------|-------|-------|------|
|[dolphin](https://erichartford.com/dolphin) | - | Dolphin, an open-source and uncensored, and commercially licensed dataset and series of instruct-tuned language models based on Microsoft's Orca paper. | 海豚（Dolphin），是一个基于微软的Orca论文的开源且未受审查的，以及商业许可的数据集和一系列经过指令调整的语言模型。|
|[dolphin-2.5-mixtral-8x7b](https://huggingface.co/cognitivecomputations/dolphin-2.5-mixtral-8x7b) | - | Dolphin, an open-source and uncensored, and commercially licensed dataset and series of instruct-tuned language models based on Microsoft's Orca paper. | 海豚（Dolphin），是一个基于微软的Orca论文的开源且未受审查的，以及商业许可的数据集和一系列经过指令调整的语言模型。|

### 大模型训练和微调
|名称|Stars|简介| 备注 |
|-------|-------|-------|------|
|[transformers](https://github.com/huggingface/transformers) | ![GitHub Repo stars](https://badgen.net/github/stars/huggingface/transformers) | 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. |HuggingFace 经典之作, Transformers 模型必用库|
|[peft](https://github.com/huggingface/peft) | ![GitHub Repo stars](https://badgen.net/github/stars/huggingface/peft) | PEFT: State-of-the-art Parameter-Efficient Fine-Tuning. |HuggingFace 出品——PEFT:最先进的参数高效微调。|
|[OpenLLM](https://github.com/bentoml/OpenLLM) | ![GitHub Repo stars](https://badgen.net/github/stars/bentoml/OpenLLM) |An open platform for operating large language models (LLMs) in production. Fine-tune, serve, deploy, and monitor any LLMs with ease. |微调，服务，部署和监控所有LLMS。用于运营大型语言模型（LLM）的开放平台。|
|[MLC LLM](https://github.com/mlc-ai/mlc-llm)|![GitHub Repo stars](https://badgen.net/github/stars/mlc-ai/mlc-llm)|Enable everyone to develop, optimize and deploy AI models natively on everyone's devices.|陈天奇大佬力作——MLC LLM，在各类硬件上原生部署任意大型语言模型。可将大模型应用于移动端（例如 iPhone）、消费级电脑端（例如 Mac）和 Web 浏览器。|
|[languagemodels](https://github.com/jncraton/languagemodels)|![GitHub Repo stars](https://badgen.net/github/stars/mlc-ai/mlc-llm)|Explore large language models on any computer with 512MB of RAM.|在512MB RAM的计算机上探索大型语言模型使用|
|[ChatGLM-Efficient-Tuning](https://github.com/hiyouga/ChatGLM-Efficient-Tuning) | ![GitHub Repo stars](https://badgen.net/github/stars/hiyouga/ChatGLM-Efficient-Tuning) | Fine-tuning ChatGLM-6B with PEFT | 基于 PEFT 的高效 ChatGLM 微调|
|[LLaMA-Efficient-Tuning](https://github.com/hiyouga/LLaMA-Efficient-Tuning) | ![GitHub Repo stars](https://badgen.net/github/stars/hiyouga/LLaMA-Efficient-Tuning) | Fine-tuning LLaMA with PEFT (PT+SFT+RLHF with QLoRA) |支持多种模型 LLaMA (7B/13B/33B/65B) ，BLOOM & BLOOMZ (560M/1.1B/1.7B/3B/7.1B/176B)，baichuan (7B)，支持多种微调方式LoRA，QLoRA|
|[微调中文数据集 COIG](https://github.com/BAAI-Zlab/COIG) | ![GitHub Repo stars](https://badgen.net/github/stars/BAAI-Zlab/COIG) | Chinese Open Instruction Generalist (COIG) project aims to maintain a harmless, helpful, and diverse set of Chinese instruction corpora. |中文开放教学通才(COIG)项目旨在维护一套无害、有用和多样化的中文教学语料库。|
|[LLaMA-Adapter🚀](https://github.com/ZrrSkywalker/LLaMA-Adapter) | ![GitHub Repo stars](https://badgen.net/github/stars/ZrrSkywalker/LLaMA-Adapter) | - |高效微调一个聊天机器人|
| [⚡ Lit-LLaMA](https://github.com/Lightning-AI/lit-llama) | ![GitHub Repo stars](https://badgen.net/github/stars/Lightning-AI/lit-llama) | - |Lightning-AI 基于nanoGPT的LLaMA语言模型的实现。支持量化，LoRA微调，预训练。|
| [Intel® Extension for Transformers](https://github.com/intel/intel-extension-for-transformers) | ![GitHub Repo stars](https://badgen.net/github/stars/intel/intel-extension-for-transformers) |⚡ Build your chatbot within minutes on your favorite device; offer SOTA compression techniques for LLMs; run LLMs efficiently on Intel Platforms⚡ |在Intel平台上高效运行llm。|



### 更多模型列表
|名称|Stars|简介| 备注 |
-|-|-|-
|[🤖 LLMs: awesome-totally-open-chatgpt](https://github.com/nichtdax/awesome-totally-open-chatgpt) |![GitHub Repo stars](https://badgen.net/github/stars/nichtdax/awesome-totally-open-chatgpt)|开源LLMs 收集。|-|
|[Open LLMs](https://github.com/eugeneyan/open-llms) |![GitHub Repo stars](https://badgen.net/github/stars/eugeneyan/open-llms)|开源可商用的大模型。|-|
|[Awesome-LLM](https://github.com/Hannibal046/Awesome-LLM) |![GitHub Repo stars](https://badgen.net/github/stars/Hannibal046/Awesome-LLM)|-|大型语言模型的论文列表，特别是与 ChatGPT相关的论文，还包含LLM培训框架、部署LLM的工具、关于LLM的课程和教程以及所有公开可用的LLM 权重和 API。|
|[FindTheChatGPTer](https://github.com/chenking2020/FindTheChatGPTer) |![GitHub Repo stars](https://badgen.net/github/stars/chenking2020/FindTheChatGPTer)|-|本项目旨在汇总那些ChatGPT的开源平替们，包括文本大模型、多模态大模型等|
|[LLMsPracticalGuide](https://github.com/Mooler0410/LLMsPracticalGuide) |![GitHub Repo stars](https://badgen.net/github/stars/Mooler0410/LLMsPracticalGuide)|亚马逊科学家杨靖锋等大佬创建的语言大模型实践指南，收集了许多经典的论文、示例和图表，展现了 GPT 这类大模型的发展历程等|-|
|[awesome-decentralized-llm](https://github.com/imaurer/awesome-decentralized-llm) |![GitHub Repo stars](https://badgen.net/github/stars/imaurer/awesome-decentralized-llm)|能在本地运行的资源 LLMs。|-|
|[OpenChatKit](https://github.com/togethercomputer/OpenChatKit) |![GitHub Repo stars](https://badgen.net/github/stars/togethercomputer/OpenChatKit)|开源了数据、模型和权重，以及提供训练，微调 LLMs 教程。|-|
|[Stanford Alpaca](https://github.com/tatsu-lab/stanford_alpaca) |![GitHub Repo stars](https://badgen.net/github/stars/tatsu-lab/stanford_alpaca)|来自斯坦福，建立并共享一个遵循指令的LLaMA模型。|-|
|[gpt4all](https://github.com/nomic-ai/gpt4all) |![GitHub Repo stars](https://badgen.net/github/stars/nomic-ai/gpt4all)|基于 LLaMa 的 LLM 助手，提供训练代码、数据和演示，训练一个自己的 AI 助手。|-|
|[LMFlow](https://github.com/OptimalScale/LMFlow) |![GitHub Repo stars](https://badgen.net/github/stars/OptimalScale/LMFlow)|共建大模型社区，让每个人都训得起大模型。|-|
|[Alpaca-CoT](https://github.com/PhoebusSi/Alpaca-CoT/blob/main/CN_README.md)|![GitHub Repo stars](https://badgen.net/github/stars/PhoebusSi/Alpaca-CoT)|Alpaca-CoT项目旨在探究如何更好地通过instruction-tuning的方式来诱导LLM具备类似ChatGPT的交互和instruction-following能力。|-|
|[OpenFlamingo](https://github.com/mlfoundations/open_flamingo)|![GitHub Repo stars](https://badgen.net/github/stars/mlfoundations/open_flamingo)|OpenFlamingo 是一个用于评估和训练大型多模态模型的开源框架，是 DeepMind Flamingo 模型的开源版本，也是 AI 世界关于大模型进展的一大步。|大型多模态模型训练和评估开源框架。|
|[LLMs-In-China](https://github.com/wgwang/LLMs-In-China)|![GitHub Repo stars](https://badgen.net/github/stars/wgwang/LLMs-In-China)|中国大模型|-|
|[Visual OpenLLM](https://github.com/visual-openllm/visual-openllm)|![GitHub Repo stars](https://badgen.net/github/stars/visual-openllm/visual-openllm)|基于 ChatGLM + Visual ChatGPT + Stable Diffusion, 以交互方式连接不同视觉模型的开源工具。|-|