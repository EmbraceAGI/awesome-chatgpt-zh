# API 代理、中转与模型路由

国内开发者使用大模型时，最常遇到三个问题：**网络不通、多家 API 不统一、订阅额度用不满**。于是出现了几类工具：

- **AI 网关**：自部署一个 OpenAI 兼容端点，后面挂多家模型与多个 Key，统一做鉴权、限流、计费与故障转移；
- **订阅转 API / 中转**：把 Claude、ChatGPT（Codex）、Gemini 等订阅账号包装成 API，给 Claude Code、Codex 等工具使用；
- **本地路由**：在本机把编码 Agent 的请求按规则转发到不同模型（例如让 Claude Code 用 DeepSeek）。

> ⚠️ **合规提醒**：把订阅账号转成 API、多人共用（「拼车」）通常违反 Anthropic / OpenAI / Google 的服务条款，可能导致封号；第三方中转站可以看到你的全部请求内容。生产环境优先使用官方 API 或可信云厂商（Amazon Bedrock、Google Vertex AI、Azure OpenAI 等），不要把敏感代码和密钥交给来源不明的中转。

> 相关：[Claude Code & Codex 生态](Claude_Code_Codex.md) 中的 CC Switch 可一键切换这些端点；[ChatGPT 应用开发指南](ChatGPT_dev.md#大模型-api-与聚合网关) 收录了各家官方 API。

## 自部署 AI 网关

| 名称 | 链接 | 简介 |
|------|------|------|
| **New API** | [GitHub](https://github.com/QuantumNous/new-api) | 当前国内最流行的开源 AI 网关（约 5.1 万 star）：OpenAI / Claude / Gemini 兼容接口、渠道管理、用户额度与计费，One API 的继任者 |
| **LiteLLM** | [GitHub](https://github.com/BerriAI/litellm) | 用 OpenAI 格式调用 100+ 家 LLM 的 SDK 与代理服务（Rust 内核 + Python SDK），企业中最常见 |
| One API | [GitHub](https://github.com/songquanpeng/one-api) | 经典的 LLM API 管理与分发系统，支持 OpenAI、Azure、Claude、Gemini、DeepSeek、豆包、GLM 等 |
| GPT-Load | [GitHub](https://github.com/tbphp/gpt-load) | 自托管 AI 网关：多渠道多凭据（API Key 与订阅账号）统一接入，调度容错、请求日志与用量统计 |
| Portkey Gateway | [GitHub](https://github.com/Portkey-AI/gateway) | 高性能 AI 网关，路由到 1600+ 模型，内置 50+ 护栏规则 |
| Higress | [GitHub](https://github.com/higress-group/higress) | 阿里开源的 AI 原生 API 网关，支持 LLM 代理、Token 限流、MCP 托管 |
| uni-api | [GitHub](https://github.com/yym68686/uni-api) | 轻量的 LLM API 统一管理，一个配置文件聚合多个后端并负载均衡 |
| freellmapi | [GitHub](https://github.com/tashfeenahmed/freellmapi) | 把 34 家免费 LLM 供应商、600+ 免费模型端点聚合到一个 `/v1` 接口，智能路由（适合个人尝鲜） |

## 订阅转 API / 编码 Agent 中转

| 名称 | 链接 | 简介 |
|------|------|------|
| **CLIProxyAPI** | [GitHub](https://github.com/router-for-me/CLIProxyAPI) | 把 Codex、Claude Code、Antigravity、Grok Build 等 CLI 的登录态包装成 OpenAI / Gemini / Claude / Codex 兼容 API（Go，约 5.7 万 star） |
| **Sub2API** | [GitHub](https://github.com/Wei-Shaw/sub2api) | 一站式开源中转：Claude、OpenAI、Gemini、Grok 订阅统一接入，原生工具无缝使用（Go，约 4.5 万 star） |
| Claude Relay Service（CRS） | [GitHub](https://github.com/Wei-Shaw/claude-relay-service) | 自建 Claude Code 镜像，统一接入 Claude、OpenAI、Gemini、Droid 订阅 |
| Claude Code Hub | [GitHub](https://github.com/ding113/claude-code-hub) | Claude Code & Codex API 代理服务，带智能负载均衡、用户管理与使用统计 |
| grok2api | [GitHub](https://github.com/chenyme/grok2api) | Grok Build / Grok Web / Grok Console 的多账号 API 网关 |

## 让编码 Agent 换模型（本地路由）

| 名称 | 链接 | 简介 |
|------|------|------|
| **CC Switch** | [GitHub](https://github.com/farion1231/cc-switch) | 桌面 GUI 一键切换 Claude Code / Codex / OpenCode 的供应商（官方、DeepSeek、Kimi、GLM、自建中转等） |
| claude-code-router | [GitHub](https://github.com/musistudio/claude-code-router) | 本地运行，把 Claude Code 的请求按后台任务、长上下文、推理等场景分别路由到不同模型 |
| claude-code-proxy（1rgs） | [GitHub](https://github.com/1rgs/claude-code-proxy) | 把 Anthropic 格式请求转换成 OpenAI / Gemini 格式，让 Claude Code 跑在其他模型上 |
| claude-code-proxy（fuergaosi233） | [GitHub](https://github.com/fuergaosi233/claude-code-proxy) | 同类实现，Claude Code → OpenAI API 代理 |
| opencodex | [GitHub](https://github.com/lidge-jun/opencodex) | Codex / Claude Code 通用模型代理，两条命令接入任意 OpenAI 兼容模型 |

> 许多国产模型已直接提供 Anthropic 兼容端点（DeepSeek、Kimi、GLM、MiniMax 等），在 Claude Code 中设置 `ANTHROPIC_BASE_URL` 与 `ANTHROPIC_AUTH_TOKEN` 即可直接使用，无需代理。详见 [DeepSeek 生态指南](DeepSeek.md#在编程智能体中使用-deepseek)。

## 托管聚合平台

| 名称 | 链接 | 简介 |
|------|------|------|
| OpenRouter | [链接](https://openrouter.ai/) | 最大的模型聚合平台，一个 Key 调用数百个模型，OpenAI 兼容，自动故障转移 |
| Requesty | [链接](https://www.requesty.ai/) | 托管的 OpenAI 兼容网关，接入 30+ 家供应商 |
| 硅基流动 SiliconFlow | [链接](https://siliconflow.cn/) | 国内模型推理云，开源模型 API 价格低，部分模型免费 |
| Amazon Bedrock | [链接](https://aws.amazon.com/bedrock/) | AWS 托管的 Claude 等模型，Claude Code 原生支持 |
| Google Vertex AI | [链接](https://cloud.google.com/vertex-ai) | Google Cloud 托管的 Gemini 与 Claude 模型，Claude Code 原生支持 |
| CodeI Lab | [链接](https://www.codeilab.com) | 面向编码 Agent 的第三方 GPT API 网关：一个 Key 通过 OpenAI 或 Anthropic 协议调用 GPT-6 / GPT-5.6，套餐额度低于官方按量价 |
