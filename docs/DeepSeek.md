# DeepSeek 生态指南

DeepSeek（深度求索）是当下最具影响力的开源大模型团队：从 2024 年的 V2/V3 到 2025 年掀起全球开源推理浪潮的 R1，再到 2026 年 4 月发布、8 月正式 GA 的 **DeepSeek-V4**（1M 上下文、开放权重、MIT 协议），DeepSeek 已经从"模型提供方"演进为覆盖 **模型 → API → 编程智能体 → Agent 框架（deepseek-harness）→ 开源基础设施** 的完整生态。本章汇总官方资源、模型谱系、API 用法、编程智能体接入、本地部署、第三方平台、应用工具、开源基建与学习资源，帮助中文用户把 DeepSeek 用起来、用得好。

> 相关：论文与技术报告见 [前沿大模型经典技术文章](OpenAI_articles.md#deepseek深度求索)，各家模型横向对比见 [LLMs 大模型](LLMs.md)，编程智能体总览见 [Coding Agents](Coding_Agents.md)，MCP 见 [MCP 指南](MCP.md)。
>
> 信息截至 2026 年 8 月，DeepSeek 迭代极快，价格与模型名请以 [官方文档](https://api-docs.deepseek.com/) 为准。

- [官方资源](#官方资源)
- [模型谱系（2024–2026）](#模型谱系20242026)
- [DeepSeek-V4：当前旗舰](#deepseek-v4当前旗舰)
- [API 使用指南](#api-使用指南)
- [在编程智能体中使用 DeepSeek](#在编程智能体中使用-deepseek)
- [deepseek-harness：官方 Agent 框架](#deepseek-harness官方-agent-框架)
- [本地部署与推理](#本地部署与推理)
- [第三方云平台与聚合 API](#第三方云平台与聚合-api)
- [客户端与应用工具](#客户端与应用工具)
- [开源基础设施（Open Infra）](#开源基础设施open-infra)
- [复现、微调与学习资源](#复现微调与学习资源)
- [社区与资源列表](#社区与资源列表)

## 官方资源

| 资源 | 链接 | 说明 |
|------|------|------|
| 官网 | [deepseek.com](https://www.deepseek.com/) | 公司官网与产品入口 |
| 网页版 / App | [chat.deepseek.com](https://chat.deepseek.com/) | 免费使用 V4 系列，支持"深度思考"与联网搜索；iOS / Android App 同名 |
| 开放平台 | [platform.deepseek.com](https://platform.deepseek.com/) | 申请 API Key、充值与用量查询 |
| API 文档 | [api-docs.deepseek.com](https://api-docs.deepseek.com/) | 快速开始、价格、模型说明、各类接入指南 |
| 更新日志 | [Change Log](https://api-docs.deepseek.com/updates) | 模型升级、价格变更的权威时间线 |
| 新闻公告 | [News](https://api-docs.deepseek.com/news/news260813) | 每次模型发布的官方说明 |
| GitHub | [github.com/deepseek-ai](https://github.com/deepseek-ai) | 全部开源模型、基础设施与 awesome 列表 |
| Hugging Face | [huggingface.co/deepseek-ai](https://huggingface.co/deepseek-ai) | 开放权重下载（V4 集合见 [deepseek-v4](https://huggingface.co/collections/deepseek-ai/deepseek-v4)） |
| 服务状态 | [status.deepseek.com](https://status.deepseek.com/) | API 可用性与故障公告 |
| X / Twitter | [@deepseek_ai](https://x.com/deepseek_ai) | 官方发布渠道 |

## 模型谱系（2024–2026）

| 时间 | 模型 | 规模 / 架构 | 要点 | 链接 |
|------|------|-------------|------|------|
| 2024-01 | DeepSeek LLM / Coder / MoE | 7B–67B Dense、16B MoE | 第一代基础模型、代码模型与 DeepSeekMoE 架构 | [LLM](https://github.com/deepseek-ai/DeepSeek-LLM) ・[Coder](https://github.com/deepseek-ai/DeepSeek-Coder) ・[MoE](https://github.com/deepseek-ai/DeepSeek-MoE) |
| 2024-02 | DeepSeekMath | 7B | 首次提出 **GRPO**，后来成为 R1 的核心 RL 算法 | [GitHub](https://github.com/deepseek-ai/DeepSeek-Math) |
| 2024-05 | DeepSeek-V2 | 236B / 21B 激活 | 首次落地 **MLA** + DeepSeekMoE，把 API 价格打到"百万 token 一元"级 | [GitHub](https://github.com/deepseek-ai/DeepSeek-V2) |
| 2024-06 | DeepSeek-Coder-V2 | 236B / 21B 激活 | 338 种语言、128K 上下文，代码能力对标 GPT-4-Turbo | [GitHub](https://github.com/deepseek-ai/DeepSeek-Coder-V2) |
| 2024-12 | DeepSeek-V3 | 671B / 37B 激活 | FP8 训练、无辅助损失负载均衡、多 Token 预测，约 558 万美元训练成本震动业界 | [GitHub](https://github.com/deepseek-ai/DeepSeek-V3) |
| 2025-01 | DeepSeek-R1 | 671B / 37B 激活 | 纯 RL 激发推理，比肩 o1；附 1.5B–70B 蒸馏版（Qwen/Llama），引发"DeepSeek 时刻" | [GitHub](https://github.com/deepseek-ai/DeepSeek-R1) |
| 2025-01 | Janus-Pro | 1B / 7B | 统一多模态理解与生成（文生图） | [GitHub](https://github.com/deepseek-ai/Janus) |
| 2025-03 | DeepSeek-V3-0324 | 671B | V3 升级版，推理与前端代码能力大幅提升 | [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3-0324) |
| 2025-04 | DeepSeek-Prover-V2 | 7B / 671B | Lean 4 形式化定理证明，MiniF2F 88.9% | [GitHub](https://github.com/deepseek-ai/DeepSeek-Prover-V2) |
| 2025-05 | DeepSeek-R1-0528 | 671B | R1 升级，推理深度与工具调用增强，幻觉率下降 | [HF](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) |
| 2025-08 | DeepSeek-V3.1 | 671B | **混合推理架构**（思考 / 非思考双模式），面向 Agent 时代 | [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) |
| 2025-09 | DeepSeek-V3.1-Terminus | 671B | 修复中英混杂、优化 Code/Search Agent | [HF](https://huggingface.co/deepseek-ai/DeepSeek-V3.1-Terminus) |
| 2025-09 | DeepSeek-V3.2-Exp | 671B | 首次引入 **DSA（DeepSeek 稀疏注意力）**，长上下文成本大降，API 降价 50%+ | [GitHub](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) |
| 2025-10 | DeepSeek-OCR | 3B | "上下文光学压缩"，10 倍压缩比下 OCR 精度 97% | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR) |
| 2025-11 | DeepSeekMath-V2 | 685B | 自我可验证数学推理，IMO 2025 / CMO 2024 金牌水平，Putnam 2024 118/120 | [GitHub](https://github.com/deepseek-ai/DeepSeek-Math-V2) |
| 2025-12 | DeepSeek-V3.2 / V3.2-Speciale | 685B | 正式版 V3.2 比肩 GPT-5；Speciale 在 IMO / IOI / ICPC WF 2025 达金牌水平 | [论文](https://arxiv.org/abs/2512.02556) |
| 2026-01 | DeepSeek-OCR-2 | 3B | DeepEncoder V2 + **Visual Causal Flow**，按语义重排视觉 token | [GitHub](https://github.com/deepseek-ai/DeepSeek-OCR-2) |
| 2026-01 | Engram | 27B（研究） | "条件记忆"作为 MoE 之外的新稀疏维度，N-gram 常数时间查表 | [GitHub](https://github.com/deepseek-ai/Engram) |
| 2026-04 | **DeepSeek-V4-Pro / V4-Flash（预览）** | 1.6T / 49B 激活；284B / 13B 激活 | 1M 上下文、开放权重（MIT）、Agent 能力跃升 | [HF 集合](https://huggingface.co/collections/deepseek-ai/deepseek-v4) |
| 2026-07-31 | DeepSeek-V4-Flash（正式版） | 284B / 13B | Agent 基准大幅超越 V4-Pro 预览版，原生 Responses API | [公告](https://api-docs.deepseek.com/updates) |
| 2026-08-13 | **DeepSeek-V4-Pro（GA，V4-Pro-0813）** | 1.6T / 49B | Agent 能力"生产级"增强，支持 low / high / max 推理强度 | [公告](https://api-docs.deepseek.com/news/news260813) |
| 2026-08-21 | DeepSeek-V4-Flash-Vision-Exp | 284B（多模态实验版） | 首个 V4 视觉模型，多模态 Agent 基准逼近 Opus 4.8；同期上线 Files API | [公告](https://api-docs.deepseek.com/news/news260821) |

## DeepSeek-V4：当前旗舰

- **两个版本**：`deepseek-v4-pro`（1.6T 总参 / 49B 激活，旗舰）与 `deepseek-v4-flash`（284B / 13B 激活，快速经济）；均为 MoE、开放权重、MIT 协议，可在 Hugging Face 下载。
- **架构**：Token-wise 压缩 + **DSA 稀疏注意力**（Compressed Sparse Attention + Heavily Compressed Attention 混合），处理 1M 上下文时单 token 推理 FLOPs 仅为前代 27%、KV 缓存仅 10%；权重为 FP4（MoE 专家）+ FP8 混合精度。
- **上下文与输出**：标准 **1M（1,048,576）token 上下文**，最大输出 384K token。
- **推理模式**：思考 / 非思考双模式；V4-Pro 与 V4-Flash 支持 **reasoning effort = low / high / max**（简单任务 low，日常 Agent 工作流 high，复杂任务 max）。
- **能力定位**：V4-Pro 在开源模型中世界知识第一（仅次于 Gemini 3.1 Pro），数学 / STEM / 编码领先；V4-Flash 推理能力逼近 V4-Pro，在复杂编码与自主软件任务上接近 Claude Opus 4.8。
- **视觉版**：`deepseek-v4-flash-vision-exp`（2026-08-21），每张图最多 384 token，按 V4-Flash 价格计费，支持 base64 / URL / Files API 传图。
- **技术报告与模型卡**：[DeepSeek-V4-Pro 模型卡](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro)（含架构、基准与推理代码）・[V4 预览发布公告](https://api-docs.deepseek.com/news/news260424)。

## API 使用指南

### 端点与模型名

| 项目 | 值 |
|------|----|
| OpenAI 兼容端点 | `https://api.deepseek.com`（或 `https://api.deepseek.com/v1`） |
| Anthropic 兼容端点 | `https://api.deepseek.com/anthropic` |
| 当前模型 | `deepseek-v4-flash`、`deepseek-v4-pro`、`deepseek-v4-flash-vision-exp` |
| 已下线模型 | `deepseek-chat`、`deepseek-reasoner` 于 **2026-07-24** 停用——旧代码请改为 V4 模型名（`deepseek-chat` → `deepseek-v4-flash`；`deepseek-reasoner` → V4 思考模式） |
| 支持的接口 | Chat Completions、**Responses API**（原生，Codex 一键接入）、Anthropic Messages、FIM 补全、Files API |

```python
from openai import OpenAI

client = OpenAI(api_key="<DEEPSEEK_API_KEY>", base_url="https://api.deepseek.com")
resp = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[{"role": "user", "content": "用一句话介绍 DeepSeek-V4"}],
)
print(resp.choices[0].message.content)
```

### 价格（2026-08-16 起，每百万 token，美元）

| 项目 | V4-Flash / Flash-Vision | V4-Pro |
|------|------------------------|--------|
| 输入・缓存命中（高峰 / 低谷） | $0.014 / $0.007 | $0.044 / $0.022 |
| 输入・缓存未命中（高峰 / 低谷） | $0.44 / $0.22 | $1.32 / $0.66 |
| 输出（高峰 / 低谷） | $1.32 / $0.66 | $3.96 / $1.98 |
| 并发上限 | 2,500 | 500 |

- **峰谷计费**：高峰时段为 UTC 01:00–04:00 与 06:00–10:00（周一至周五，约合北京时间 09:00–12:00、14:00–18:00），其余时间（含周末）为低谷价，**低谷价为高峰价的 50%**，适合把批量 / 离线任务排到低谷跑。
- **上下文硬盘缓存**：DeepSeek 首创、默认开启、无需改代码；命中部分只收未命中价格的约 1/30，长系统提示、多轮对话与 Agent 工作流可省 80%+ 成本。详见 [Context Caching](https://api-docs.deepseek.com/guides/kv_cache)。
- **免费额度**：新注册账号赠送试用额度；网页版 / App 完全免费，没有付费订阅档。
- 提示写法与思考模式技巧见 [DeepSeek V4 思考模式提示技巧](ChatGPT_prompts.md#deepseek-v4-思考模式提示技巧)。
- 官方价格页：[Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)。

### 官方指南索引

| 指南 | 说明 |
|------|------|
| [Reasoning / Thinking Mode](https://api-docs.deepseek.com/guides/reasoning_model) | 思考模式与 reasoning effort 用法 |
| [Function Calling](https://api-docs.deepseek.com/guides/function_calling) | 工具调用，V4 大幅加强 |
| [JSON Output](https://api-docs.deepseek.com/guides/json_mode) | 结构化输出 |
| [FIM Completion](https://api-docs.deepseek.com/guides/fim_completion) | 代码中间填空补全 |
| [Anthropic API 兼容](https://api-docs.deepseek.com/guides/anthropic_api) | 用 Anthropic SDK / Claude Code 调用 DeepSeek；Claude Opus 名称自动映射为 V4-Pro，Sonnet / Haiku 映射为 V4-Flash |
| [Context Caching](https://api-docs.deepseek.com/guides/kv_cache) | 硬盘缓存机制与命中策略 |

## 在编程智能体中使用 DeepSeek

DeepSeek 同时兼容 OpenAI 与 Anthropic 两种协议，因此几乎所有主流编程智能体都能一行配置切换到 V4。官方维护的 [awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) 列出了每个工具的接入方法。

### Claude Code

```bash
export ANTHROPIC_BASE_URL=https://api.deepseek.com/anthropic
export ANTHROPIC_API_KEY=<DEEPSEEK_API_KEY>
export ANTHROPIC_MODEL=deepseek-v4-pro      # 或 deepseek-v4-flash
claude
```

也可写入 `~/.claude/settings.json` 的 `env` 字段持久化。Claude Code 的 Skills、Hooks、子 Agent 等能力均可正常使用；不支持 document 内容块与 MCP 工具透传（本地 MCP 由 Claude Code 自身处理，不受影响）。

### Codex / OpenAI 兼容工具

V4 原生支持 **OpenAI Responses API**，OpenAI Codex CLI 可通过自定义 provider 一键接入：在 `~/.codex/config.toml` 中添加 `[model_providers.deepseek]`，`base_url = "https://api.deepseek.com"`，`model = "deepseek-v4-pro"`。OpenCode、Crush、Cline、Roo Code、Kilo Code、Continue、Qwen Code、GitHub Copilot（BYOK）等同理，选择 OpenAI-compatible 提供方并填入端点与模型名即可。

### 主流工具一览

| 工具 | 类型 | 接入方式 | 链接 |
|------|------|----------|------|
| Claude Code | 终端 Agent | Anthropic 兼容端点 | [GitHub](https://github.com/anthropics/claude-code) |
| OpenAI Codex CLI | 终端 Agent | Responses API（原生） | [GitHub](https://github.com/openai/codex) |
| OpenCode | 终端 / Web Agent | OpenAI 兼容 provider | [GitHub](https://github.com/sst/opencode) |
| OpenClaw（"龙虾"） | 个人 AI 助理（飞书 / 微信） | `onboard` 向导直接选 DeepSeek | [GitHub](https://github.com/openclaw/openclaw) |
| Cline / Roo Code / Kilo Code | VS Code Agent | 内置 DeepSeek provider | [Cline](https://github.com/cline/cline) |
| Crush | 终端 Agent | OpenAI 兼容 | [GitHub](https://github.com/charmbracelet/crush) |
| pi / Oh My Pi | 极简 Agent harness | 模型供应商配置 | [GitHub](https://github.com/earendil-works/pi) |
| Qwen Code | 终端 Agent | 内置 DeepSeek 支持 | [GitHub](https://github.com/QwenLM/qwen-code) |
| GitHub Copilot / Copilot CLI | IDE / 终端 | BYOK 自定义模型 | [链接](https://github.com/features/copilot) |
| Hermes Agent | 自我改进 Agent（Nous Research） | OpenAI 兼容 | [GitHub](https://github.com/NousResearch/hermes-agent) |
| Deep Code | DeepSeek-V4 专用终端编码助手，深度思考 / 推理强度可控，支持 Agent Skills 与 MCP | 原生 | [GitHub](https://github.com/lessweb/deepcode-cli) ・[官网](https://deepcode.vegamo.cn/) |
| DeepSeek-TUI | Rust 终端编码工具，沙箱工具与 MCP | 原生 | [awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) |
| DeepSeek-Reasonix | DeepSeek 原生终端编码 Agent（Go），围绕前缀缓存稳定性设计 | 原生 | [GitHub](https://github.com/esengine/DeepSeek-Reasonix) |
| Langcli | 100% 兼容 Claude Code 的多模型 CLI | Anthropic 兼容 | [awesome-deepseek-agent](https://github.com/deepseek-ai/awesome-deepseek-agent) |
| cc-connect | 把 Claude Code / Codex 接入微信、飞书、钉钉 | 桥接器 | [GitHub](https://github.com/chenhg5/cc-connect) |

> 提示：Agent 工作流大量重复发送系统提示与工具定义，DeepSeek 的硬盘缓存对这类负载命中率极高，实际成本往往只有标价的 10%–20%。

## deepseek-harness：官方 Agent 框架

2026 年 8 月 13 日（与 V4-Pro GA 同日），DeepSeek 开源了官方 Agent 框架 **deepseek-harness（dsh）**，发布不到两周即突破 19 万 star，成为 GitHub 史上增长最快的项目之一。它的口号是 **"Everything is a Plugin"**：模型适配器、工具注册表、会话日志、Agent 循环本身乃至 Web UI 全部是可替换的插件，底层由 Cordis 框架驱动（其设计见论文 *A Programming Paradigm for Spatiotemporal Composability*）。目前处于开发者预览（v0.1.x），官方明确提示会有破坏性变更。

### 核心概念

| 概念 | 说明 |
|------|------|
| Profile / Bundle | 运行中的 dsh 是启动时按层组合出的插件树：`dsh-base`（模型适配、工具、持久化、沙箱与审批策略）→ `dsh-web-app` 或 `dsh-headless` → 用户的 `cordis.patch.yml` 覆盖；`dsh --profile web --dump-config` 可打印本机实际启动的插件树，任一行都能被 patch 替换 |
| Capability Seam（能力接缝） | 每个能力由"服务定义 + 服务提供者 + 消费者"三角构成，换一个 provider 即可整体切换——例如把文件系统与子进程 provider 指向远程沙箱，Bash / PTY / LSP 全部随之迁移 |
| MCP 客户端 | 内置 MCP 桥接第三方工具服务器 |
| Hook 协议 | 拦截 Agent 动作的钩子，**兼容 Claude Code 与 Codex 的 Hook 格式** |
| Skill 系统 | Markdown 指令集，由 SkillRegistry 管理，支持全局 / Agent 级作用域，兼容 Agent Skills 开放标准 |
| 子 Agent / Agent Teams | 子 Agent provider 可从"新建子进程"到"委托给另一产品"自由替换；实验性 Agent Teams 提供名册、任务板与邮箱 |
| 会话日志 | 追加式事件日志是模型上下文的唯一来源（"模型可见即已记录"），fork / resume / 转录 / 遥测都由此派生 |
| Python SDK | 官方提供 Python SDK，可在脚本中驱动 dsh |

### 快速上手

```bash
npx @deepseek-ai/dsh web        # 启动 Web UI，默认 http://127.0.0.1:3080
# 或从源码运行
git clone https://github.com/deepseek-ai/deepseek-harness.git && cd deepseek-harness
pnpm install && pnpm run build && pnpm dsh web
```

默认使用 DeepSeek 官方 API（在 Providers 页面填 Key），也可在 Providers 中添加任意 OpenAI 兼容端点或本地模型。

### 资源

| 资源 | 链接 | 说明 |
|------|------|------|
| deepseek-harness | [GitHub](https://github.com/deepseek-ai/deepseek-harness) | 官方仓库（MIT），README 提供中文版 |
| 用户指南（中文） | [Web UI 指南](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/user/guide/index.zh.md) ・[模型供应商](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/user/guide/providers.zh.md) ・[Python SDK](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/user/guide/python-sdk.zh.md) | 安装、配置 API Key、接入自定义供应商与 SDK 用法 |
| 架构文档（中文） | [架构](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/architecture.zh.md) ・[Cordis 入门](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/cordis-primer.zh.md) ・[工具目录](https://github.com/deepseek-ai/deepseek-harness/blob/main/docs/tool-catalog.zh.md) | 插件树、事件模型、Turn / Step 流程、能力接缝，写插件前必读 |
| dsh-plugin topic | [GitHub Topics](https://github.com/topics/dsh-plugin) | 官方指定的插件发现入口，发布插件请打上此 topic |
| awesome-dsh-skills | [GitHub](https://github.com/yzfly/awesome-dsh-skills) | 本项目作者维护：700+ dsh 技能 / 插件仓库自动收录与每日校验、DSH Skill Spec 规范、`dsh-skill-lint` 校验器、2026 Q3 精选版，可搜索站点 [code.jiangshu.ai/awesome-dsh-skills](https://code.jiangshu.ai/awesome-dsh-skills) |
| awesome-deepseek-harness | [0xsline](https://github.com/0xsline/awesome-deepseek-harness) ・[Dominic789654](https://github.com/Dominic789654/awesome-deepseek-harness) | 社区整理的 DSH 插件、技能、MCP 服务器、patch / profile 层与 UI 列表 |
| dsh-find-plugins | [GitHub](https://github.com/Nagi-ovo/dsh-find-plugins) | 让 dsh 自己搜索、安装并验证 GitHub 插件的技能 |
| deepseek-harness-plugin-mcp | [GitHub](https://github.com/bobleer/deepseek-harness-plugin-mcp) | 把 dsh 插件目录暴露为 MCP 服务器 |
| GitHub Discussions | [链接](https://github.com/deepseek-ai/deepseek-harness/discussions) | 官方反馈与问题讨论区 |
| DeepSeek Harness Discord | [Discord](https://discord.gg/Ycq5dCaS4) | 官方社区 |

## 本地部署与推理

V4 系列为开放权重，可自建服务。V4-Flash（13B 激活）是本地 / 私有化部署的甜点：

| 方案 | 说明 | 链接 |
|------|------|------|
| vLLM | Day-0 支持 V4，OpenAI 兼容服务，官方推荐 | [GitHub](https://github.com/vllm-project/vllm) |
| SGLang | Day-0 支持 V4，高性能推理，DeepSeek 团队深度参与 | [GitHub](https://github.com/sgl-project/sglang) |
| llama.cpp | 主线已支持 V4 与量化 KV 缓存，CPU / 消费级显卡可跑 GGUF | [GitHub](https://github.com/ggml-org/llama.cpp) |
| Ollama | `ollama run` 一行拉起 V4-Flash GGUF（可直接拉取 Unsloth 量化版） | [ollama.com](https://ollama.com/library/deepseek-v4-flash) |
| LM Studio / Jan | 桌面 GUI，加载 GGUF 量化版 | [LM Studio](https://lmstudio.ai/) ・[Jan](https://jan.ai/) |
| Unsloth 量化与部署文档 | V4 各精度 GGUF（Q4_K_M 约需 1×80GB 或 2×48GB）、微调教程 | [文档](https://unsloth.ai/docs/models/deepseek-v4) ・[GitHub](https://github.com/unslothai/unsloth) |
| ktransformers | CPU/GPU 异构推理，单卡 + 大内存跑 MoE 大模型的经典方案 | [GitHub](https://github.com/kvcache-ai/ktransformers) |
| DeepSeek-R1 蒸馏版 | 1.5B–70B 蒸馏模型（Qwen / Llama 底座），入门级显卡即可 | [HF](https://huggingface.co/collections/deepseek-ai/deepseek-r1-678e1e131c0169c0bc89728d) |

硬件参考（V4-Flash）：重度量化约 33 GB 显存（2×4090 级）；FP8 约 80 GB（单张 H100）；全精度 + KV 缓存约 170 GB（2×H200）。V4-Pro（1.6T）需多机多卡，建议直接使用 API 或云平台。

## 第三方云平台与聚合 API

国内外主流云厂商均已上线 DeepSeek-V4（部分平台首发日与官方同步），对需要企业合规、发票、更高并发或备用通道的用户尤其实用：

| 平台 | 链接 | 说明 |
|------|------|------|
| 阿里云百炼 | [aliyun.com](https://www.aliyun.com/benefit/scene/deployment-deepseek) | 4 月 24 日同步上线 V4-Pro / V4-Flash，支持 1M 上下文，价格与官网基本一致 |
| 火山引擎（方舟） | [volcengine.com](https://www.volcengine.com/product/ark) | 字节云平台，DeepSeek 全系列，联网插件与高并发 |
| 腾讯云 TI / 混元 | [cloud.tencent.com](https://cloud.tencent.com/product/ti) | 腾讯元宝也内置 DeepSeek 模型 |
| 百度智能云千帆 | [qianfan](https://cloud.baidu.com/product/qianfan) | DeepSeek 系列 API 与私有化 |
| 华为云 ModelArts | [huaweicloud.com](https://www.huaweicloud.com/product/modelarts.html) | 昇腾算力适配版 DeepSeek |
| 硅基流动 SiliconFlow | [siliconflow.cn](https://siliconflow.cn/) | 开源模型云，DeepSeek 上线最快的第三方之一，OpenAI 兼容 |
| NVIDIA NIM | [build.nvidia.com](https://build.nvidia.com/deepseek-ai) | NVIDIA 托管推理，含 V3.2 / V4 |
| Together AI / Fireworks | [Together](https://www.together.ai/) ・[Fireworks](https://fireworks.ai/) | 海外高性能开源模型托管 |
| OpenRouter | [openrouter.ai](https://openrouter.ai/deepseek) | 聚合数百模型的统一 API，可对比各家 DeepSeek 供应方价格与延迟 |
| Groq / Cerebras | [Groq](https://groq.com/) ・[Cerebras](https://www.cerebras.ai/) | 专用芯片推理，提供 DeepSeek 蒸馏 / Flash 级模型的超高速版本 |
| Models.dev | [models.dev](https://models.dev/) | 查询各平台 DeepSeek 模型的上下文、价格与能力 |

## 客户端与应用工具

以下均内置 DeepSeek 供应方（填 Key 即用），更完整的 100+ 集成列表见官方 [awesome-deepseek-integration](https://github.com/deepseek-ai/awesome-deepseek-integration)。

### 桌面 / 网页聊天客户端

| 名称 | 链接 | 简介 |
|------|------|------|
| Cherry Studio | [GitHub](https://github.com/CherryHQ/cherry-studio) | 国产多模型桌面客户端，300+ 助手、知识库、MCP，DeepSeek 用户首选 |
| Chatbox | [GitHub](https://github.com/chatboxai/chatbox) | 跨平台轻量桌面客户端 |
| LobeChat / LobeHub | [GitHub](https://github.com/lobehub/lobe-chat) | 现代化聊天与 Agent 框架，支持知识库与多模态 |
| Open WebUI | [GitHub](https://github.com/open-webui/open-webui) | 自托管聊天 UI，配合 Ollama 本地跑 DeepSeek |
| NextChat | [GitHub](https://github.com/ChatGPTNextWeb/NextChat) | 轻量跨端客户端，一键部署 |
| LibreChat | [GitHub](https://github.com/danny-avila/LibreChat) | 多模型自托管平台，Agent + MCP |
| DeepChat | [GitHub](https://github.com/ThinkInAIXYZ/deepchat) | 面向 DeepSeek 的免费桌面助手，联网搜索与知识库 |
| 5ire | [GitHub](https://github.com/nanbingxyz/5ire) | 跨平台桌面助手，MCP 支持完善 |
| eechat | [GitHub](https://github.com/Lucassssss/eechat) | 本地部署 DeepSeek-R1 等开源模型的桌面工具 |
| Enconvo | [链接](https://www.enconvo.com/) | macOS AI 启动器 |
| AnyModelBot | [GitHub](https://github.com/modelflare-ai/AnyModelBot) | 本地优先的 AI 机器人应用（MIT），经 Modelflare Key 使用 DeepSeek 等模型，可按对话切换；支持微信、飞书、文件读写与电脑操作；界面支持英文和中文，模型按量付费 |

### 知识库 / RAG / 工作流平台

| 名称 | 链接 | 简介 |
|------|------|------|
| Dify | [GitHub](https://github.com/langgenius/dify) | LLMOps 平台，可视化搭建 RAG 与 Agent |
| FastGPT | [GitHub](https://github.com/labring/FastGPT) | 国产知识库问答与工作流编排 |
| RAGFlow | [GitHub](https://github.com/infiniflow/ragflow) | 深度文档理解 RAG 引擎 |
| MaxKB | [GitHub](https://github.com/1Panel-dev/MaxKB) | 开箱即用的 RAG 聊天机器人 |
| DB-GPT | [GitHub](https://github.com/eosphoros-ai/DB-GPT) | 数据库 AI 应用框架（Text2SQL） |
| KAG | [GitHub](https://github.com/OpenSPG/KAG) | 蚂蚁开源的逻辑推理知识增强框架 |
| DeepSearcher | [GitHub](https://github.com/zilliztech/deep-searcher) | 私有数据 Deep Research |
| n8n / Coze | [n8n](https://github.com/n8n-io/n8n) ・[Coze](https://www.coze.cn/) | 工作流自动化 / 字节 Bot 平台 |
| One API / New API | [GitHub](https://github.com/songquanpeng/one-api) | 多渠道 API 管理与分发 |

### IM 机器人与办公

| 名称 | 链接 | 简介 |
|------|------|------|
| AstrBot | [GitHub](https://github.com/AstrBotDevs/AstrBot) | 多平台聊天机器人（QQ / 飞书 / Telegram），记忆、RAG、MCP |
| LangBot | [GitHub](https://github.com/RockChinQ/LangBot) | IM 机器人框架 |
| chatgpt-on-wechat | [GitHub](https://github.com/zhayujie/chatgpt-on-wechat) | 微信 / 企微 / 飞书 / 钉钉机器人 |
| HuixiangDou 茴香豆 | [GitHub](https://github.com/InternLM/HuixiangDou) | 微信 / 飞书群知识助手 |
| NoneBot DeepSeek 插件 | [GitHub](https://github.com/KomoriDev/nonebot-plugin-deepseek) | NoneBot 生态 |
| 钉钉 / 飞书 / 企业微信 | 官方 | 三大办公平台均已内置 DeepSeek 模型 |
| Obsidian Tars / SiYuan | [Tars](https://github.com/TarsLab/obsidian-tars) ・[SiYuan](https://github.com/siyuan-note/siyuan) | 笔记软件集成 |
| Zotero / PapersGPT | [PapersGPT](https://github.com/papersgpt/papersgpt-for-zotero) | 文献阅读与翻译 |
| Bob / Easydict / Pot / PDFMathTranslate | [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate) | 翻译与 PDF 双语翻译 |
| Raycast DeepSeek | [链接](https://www.raycast.com/) | macOS 效率工具扩展 |

### SDK 与语言客户端

官方推荐直接用 OpenAI / Anthropic SDK；社区维护：[deepseek-go](https://github.com/cohesion-org/deepseek-go)、[DeepSwiftSeek](https://github.com/tornikegomareli/DeepSwiftSeek)、[deepseek-php-client](https://github.com/deepseek-php/deepseek-php-client)、[deepseek-laravel](https://github.com/deepseek-php/deepseek-laravel)、[DeepSeek MCP Server](https://github.com/DMontgomery40/deepseek-mcp-server)。

## 开源基础设施（Open Infra）

2025 年 2 月"开源周"起，DeepSeek 陆续开源了支撑 V3 / R1 / V4 训练推理的生产级组件，是学习大规模 MoE 系统工程的一手资料。

| 项目 | 链接 | 简介 |
|------|------|------|
| open-infra-index | [GitHub](https://github.com/deepseek-ai/open-infra-index) | 开源基础设施总索引 |
| FlashMLA | [GitHub](https://github.com/deepseek-ai/FlashMLA) | Hopper GPU 上的 MLA 解码内核，访存 3000 GB/s |
| DeepEP | [GitHub](https://github.com/deepseek-ai/DeepEP) | MoE 专家并行通信库（NVLink / RDMA） |
| DeepGEMM | [GitHub](https://github.com/deepseek-ai/DeepGEMM) | 约 300 行核心代码的 FP8 GEMM 库 |
| DualPipe | [GitHub](https://github.com/deepseek-ai/DualPipe) | 双向流水并行，计算通信完全重叠 |
| EPLB | [GitHub](https://github.com/deepseek-ai/EPLB) | 专家并行负载均衡器 |
| LPLB | [GitHub](https://github.com/deepseek-ai/LPLB) | 面向 MoE 的线性规划负载均衡 |
| 3FS（Fire-Flyer File System） | [GitHub](https://github.com/deepseek-ai/3FS) | 高性能分布式文件系统，聚合读吞吐 6.6 TiB/s |
| smallpond | [GitHub](https://github.com/deepseek-ai/smallpond) | 基于 DuckDB + 3FS 的轻量数据处理框架 |
| profile-data | [GitHub](https://github.com/deepseek-ai/profile-data) | V3 / R1 训练推理的性能剖析数据 |
| DeepSpec | [GitHub](https://github.com/deepseek-ai/DeepSpec) | 投机解码（speculative decoding）训练评测全栈 |
| TileKernels | [GitHub](https://github.com/deepseek-ai/TileKernels) | 基于 tilelang 的内核库 |
| ESFT | [GitHub](https://github.com/deepseek-ai/ESFT) | 专家专用微调（Expert Specialized Fine-Tuning） |

## 复现、微调与学习资源

| 资源 | 链接 | 简介 |
|------|------|------|
| Open R1 | [GitHub](https://github.com/huggingface/open-r1) | Hugging Face 完整复现 R1 训练流水线（SFT + GRPO） |
| TinyZero | [GitHub](https://github.com/Jiayi-Pan/TinyZero) | 30 美元复现 R1-Zero "顿悟时刻"，入门 RL 推理必看 |
| simpleRL-reason | [GitHub](https://github.com/hkust-nlp/simpleRL-reason) | 港科大用 8K 样本复现长思维链推理 |
| verl | [GitHub](https://github.com/volcengine/verl) | 字节开源 RL 训练框架，GRPO 等算法工业级实现 |
| TRL GRPO Trainer | [文档](https://huggingface.co/docs/trl/grpo_trainer) | Hugging Face TRL 内置 GRPO |
| Unsloth GRPO / 微调教程 | [文档](https://unsloth.ai/docs) | 消费级显卡微调 DeepSeek / 蒸馏模型 |
| LLaMA-Factory | [GitHub](https://github.com/hiyouga/LLaMA-Factory) | 一站式微调框架，支持 DeepSeek 全系 |
| DeepSeek-R1 论文精读（李沐） | [B 站](https://www.bilibili.com/video/BV1KcPoeUEFy) | 逐段精读 R1 论文 |
| DeepSeek 技术解读合集 | [知乎](https://www.zhihu.com/topic/27974644) | MLA / DSA / GRPO 等中文解析 |

## 社区与资源列表

| 资源 | 链接 | 简介 |
|------|------|------|
| awesome-deepseek-integration | [GitHub](https://github.com/deepseek-ai/awesome-deepseek-integration) | 官方维护：接入 DeepSeek 的 100+ 应用、框架、插件（中英双语） |
| awesome-deepseek-agent | [GitHub](https://github.com/deepseek-ai/awesome-deepseek-agent) | 官方维护：可直接切换到 V4 的编程智能体 / Agent 平台接入指南 |
| awesome-deepseek-coder | [GitHub](https://github.com/deepseek-ai/awesome-deepseek-coder) | 官方维护：DeepSeek Coder 相关项目 |
| DeepSeek Harness Discord | [Discord](https://discord.gg/Ycq5dCaS4) | 官方社区 |
| DeepSeek 微信公众号 | 「DeepSeek」 | 官方公告中文渠道 |
| 本项目电报群 | [ChatGPT 精选](https://t.me/AwesomeChatGPT) | 交流 DeepSeek / ChatGPT 使用心得 |
