# AI 生图指南

2025–2026 年，AI 生图从「抽卡出美图」进化到「听懂指令、精准改图」：GPT Image 与 Nano Banana 让对话式改图成为日常，文字渲染、多图参考、角色一致性基本可用；开源侧 Qwen-Image、FLUX.2、HunyuanImage、Z-Image 等也快速追近。本页整理主流闭源模型、开源模型、本地工具与提示词资源（数据截至 2026-11，版本更迭很快，以官方页面为准）。

> 相关：[AI 生产力工具 · 绘画/图像](AI_tools.md#ai-绘画图像) · [Sora 与 AI 视频生成](Sora.md) · 多模态提示词见 [Awesome-Multimodal-Prompts](https://github.com/yzfly/Awesome-Multimodal-Prompts)

## 闭源 / 商用模型

| 名称 | 链接 | 简介 |
|------|------|------|
| **GPT Image 2** | [文档](https://platform.openai.com/docs/guides/image-generation) | OpenAI 第三代图像模型（2026-04 发布，ChatGPT 中称 Images 2.0，API 模型名 `gpt-image-2`），指令遵循、文字排版与对话式编辑表现领先，多个竞技场榜单居首；前代为 GPT Image 1（2025-04）与 1.5（2025-12） |
| **Nano Banana 2 / Pro** | [Gemini](https://gemini.google.com) ・[AI Studio](https://aistudio.google.com) | Google 的 Gemini 图像模型家族：Nano Banana（Gemini 2.5 Flash Image）引爆「一句话改图」，Pro 版（Gemini 3 Pro Image）擅长高分辨率与信息图，Nano Banana 2 系列面向速度与成本 |
| Seedream 5.0 | [即梦](https://jimeng.jianying.com) ・[火山引擎](https://www.volcengine.com/product/ark) | 字节跳动 Seed 团队图像模型，中文理解与海报文字出色，集成于即梦、豆包与火山方舟 API |
| Midjourney | [链接](https://www.midjourney.com) | 审美与画面质感的行业标杆，V8 系列 2026 年上线，网页端支持编辑与视频 |
| FLUX.2 [pro] | [官网](https://bfl.ai) | Black Forest Labs 旗舰，最高 4MP 输出、多图参考，适合商用产品图 |
| Imagen | [链接](https://deepmind.google/models/imagen/) | Google DeepMind 的高保真文生图模型，可在 Vertex AI / Gemini API 调用 |
| Ideogram | [链接](https://ideogram.ai) | 以图中文字与排版见长，适合 Logo、海报 |
| Recraft | [链接](https://www.recraft.ai) | 面向设计师，支持矢量图（SVG）生成与品牌风格统一 |
| Adobe Firefly | [链接](https://www.adobe.com/products/firefly.html) | 版权安全的商用生成模型，深度集成 Photoshop，也可调用第三方模型 |
| 可灵 Kling / 通义万相 / 文心一格 / 混元 | [可灵](https://klingai.com) ・[通义万相](https://tongyi.aliyun.com/wanxiang) ・[文心一格](https://yige.baidu.com) | 国产主流生图平台，中文提示词友好，大多同时提供视频生成 |

## 开源 / 开放权重模型

| 名称 | 链接 | 简介 |
|------|------|------|
| **Qwen-Image** | [GitHub](https://github.com/QwenLM/Qwen-Image) | 阿里通义千问图像基座模型，复杂文字渲染（尤其中文）与精准编辑能力突出，Apache-2.0 |
| **FLUX.2** | [GitHub](https://github.com/black-forest-labs/flux2) | Black Forest Labs 新一代模型官方推理仓库，含 [dev] 与可在消费级显卡上亚秒出图的蒸馏版 [klein] |
| FLUX.1 | [GitHub](https://github.com/black-forest-labs/flux) | FLUX.1 系列（含 Kontext 编辑模型）官方推理仓库，社区 LoRA 生态最丰富 |
| Z-Image | [GitHub](https://github.com/Tongyi-MAI/Z-Image) | 通义实验室的高效图像模型，参数量小、出图快，适合本地部署 |
| HunyuanImage 3.0 | [GitHub](https://github.com/Tencent-Hunyuan/HunyuanImage-3.0) | 腾讯混元原生多模态图像生成模型 |
| BAGEL | [GitHub](https://github.com/ByteDance-Seed/Bagel) | 字节 Seed 开源的统一多模态模型，理解与生成一体 |
| Step1X-Edit | [GitHub](https://github.com/stepfun-ai/Step1X-Edit) | 阶跃星辰开源的图像编辑模型，对标闭源编辑效果 |
| Infinity | [GitHub](https://github.com/FoundationVision/Infinity) | 字节开源的比特级自回归高分辨率生图模型（CVPR 2025 Oral） |

## 本地工具与 WebUI

| 名称 | 链接 | 简介 |
|------|------|------|
| **ComfyUI** | [GitHub](https://github.com/Comfy-Org/ComfyUI) | 节点式工作流的事实标准（约 14 万 star），新模型通常首日支持，图像、视频、音频全覆盖 |
| Stable Diffusion WebUI | [GitHub](https://github.com/AUTOMATIC1111/stable-diffusion-webui) | 经典 A1111 WebUI，插件生态庞大（更新已放缓） |
| Forge | [GitHub](https://github.com/lllyasviel/stable-diffusion-webui-forge) | A1111 的高性能分支，显存占用更低 |
| InvokeAI | [GitHub](https://github.com/invoke-ai/InvokeAI) | 面向专业创作者的画布式生图引擎 |
| SwarmUI | [GitHub](https://github.com/mcmonkeyprojects/SwarmUI) | 模块化 WebUI，前端简洁，后端由 ComfyUI 驱动 |
| Fooocus | [GitHub](https://github.com/lllyasviel/Fooocus) | 「专注提示词」的极简生图工具，开箱即用 |
| Stability Matrix | [GitHub](https://github.com/LykosAI/StabilityMatrix) | 多平台 SD 包管理器，一键安装各种 WebUI 并共享模型 |
| DiffSynth-Studio | [GitHub](https://github.com/modelscope/DiffSynth-Studio) | ModelScope 的扩散模型推理与训练框架，对 Qwen-Image、Wan 等国产模型支持好 |
| ai-toolkit | [GitHub](https://github.com/ostris/ai-toolkit) | 扩散模型微调 / LoRA 训练工具，支持 FLUX、Qwen-Image 等 |
| sd-scripts | [GitHub](https://github.com/kohya-ss/sd-scripts) | 经典 LoRA / DreamBooth 训练脚本 |
| ControlNet | [GitHub](https://github.com/lllyasviel/ControlNet) | 用姿态、线稿、深度图等精确控制构图的经典方案 |

## 提示词与案例合集

| 名称 | 链接 | 简介 |
|------|------|------|
| Awesome-Nano-Banana-images | [GitHub](https://github.com/PicoTrex/Awesome-Nano-Banana-images) | Nano Banana / Pro 创意案例与提示词合集（约 2.4 万 star），中英双语 |
| awesome-nano-banana-pro-prompts | [GitHub](https://github.com/YouMind-OpenLab/awesome-nano-banana-pro-prompts) | 1 万+ 条带预览图的 Nano Banana Pro 提示词库，持续更新 |
| awesome-nano-banana | [GitHub](https://github.com/JimmyLv/awesome-nano-banana) | Nano Banana（Gemini 2.5 Flash Image）图片与提示词精选 |
| gpt4o-image-prompts | [GitHub](https://github.com/songguoxs/gpt4o-image-prompts) | GPT-4o / GPT Image / Nano Banana 中文提示词合集 |
| awesome-gpt4o-images | [GitHub](https://github.com/jamez-bondos/awesome-gpt4o-images) | GPT-4o 与 gpt-image-1 生成图与提示词精选 |
| Awesome-GPT-Image-2-API-Prompts | [GitHub](https://github.com/Anil-matcha/Awesome-GPT-Image-2-API-Prompts) | 针对 `gpt-image-2` API 的提示词合集：人像、海报、UI 稿、游戏截图等 |
| AgentCraft GPT Image 2.6 提示词 | [链接](https://agentcraft.dev/zh/prompts/image/gpt-image-2-6/) | 64 条 GPT Image 2.6 提示词，原样摘自 OpenAI 官方指南和创作者帖子，每条附成图（含 GIF 动图）和出处，中英双语 |
| Nano-Bananary（香蕉超市） | [GitHub](https://github.com/ZHO-ZHO-ZHO/Nano-Bananary) | 各种 Nano Banana 玩法一键生成，无需写提示词，支持局部涂选与连续编辑 |
| 多模态 prompts 精选 | [GitHub](https://github.com/yzfly/Awesome-Multimodal-Prompts) | 本项目作者维护的多模态（图像 / 视频）提示词合集 |

## 评测榜单

| 名称 | 链接 | 简介 |
|------|------|------|
| LMArena Text-to-Image | [链接](https://lmarena.ai/leaderboard/text-to-image) | 匿名对战投票的文生图 / 图像编辑排行榜 |
| Artificial Analysis Image Arena | [链接](https://artificialanalysis.ai/text-to-image) | 生图模型质量、速度与价格对比 |
| GenExam | [GitHub](https://github.com/OpenGVLab/GenExam) | 上海 AI Lab 的「考试式」多学科文生图基准 |
