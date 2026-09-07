## MCP（模型上下文协议）指南

MCP（Model Context Protocol，模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放协议，被称为 AI 应用的"USB-C 接口"——让大模型以统一方式无缝连接外部工具、数据与系统。2025 年底 Anthropic 将 MCP 捐赠给 Linux 基金会旗下的 **Agentic AI Foundation（AAIF，由 Anthropic、OpenAI、Block 共同发起）** 中立治理；2026 年 7 月 28 日发布的新版规范把协议核心改为**无状态**请求 / 响应模型，并引入扩展框架、MCP Apps 与授权加固。MCP 已是 AI 智能体生态的事实标准：Claude、ChatGPT / Codex、Gemini CLI、Cursor、DeepSeek Harness（dsh）等全部原生支持。

> 🤝 与 Skills 的关系：MCP 负责"连接工具与数据"，Agent Skills 负责"教会 Agent 怎么做"，两者互补，见 [Claude Skills 指南](Claude_Skills.md)。

> 📌 本节为精选索引，完整中文资源大全（400+ MCP Servers）见作者维护的 👉 [**Awesome-MCP-ZH**](https://github.com/yzfly/Awesome-MCP-ZH)（持续更新，欢迎 star）

### 协议进展（2025–2026）

|事件|链接|中文简介|
|---|---|---|
|2026-07-28 规范发布|[链接](https://blog.modelcontextprotocol.io/posts/2026-07-28/)|最重要的一次升级：**无状态协议核心**（去掉 initialize 握手与 Mcp-Session-Id，请求可落在任意实例）、多轮往返请求（MRTR，工具中途向用户要输入）、`Mcp-Method` / `Mcp-Name` 头部路由、可缓存的 list 结果、授权加固（RFC 9207、CIMD）、正式的扩展框架与弃用政策（Roots / Sampling / Logging 进入 12 个月弃用期，旧版 HTTP+SSE 传输弃用）。|
|规范全文 2026-07-28|[链接](https://modelcontextprotocol.io/specification/2026-07-28)|当前生效的协议规范。TypeScript / Python / Go / C# 一级 SDK 与 Rust SDK（beta）同步支持。|
|Tasks 扩展|[链接](https://modelcontextprotocol.io/specification/2026-07-28)|长时任务从实验特性升级为官方扩展 `io.modelcontextprotocol/tasks`，轮询式操作 + 统一的 `subscriptions/listen` 流。|
|MCP Apps|[链接](https://modelcontextprotocol.io/)|让 MCP 服务器向宿主返回可交互 UI（表单、可视化）而非纯文本，Claude、ChatGPT 等宿主已支持。|
|2025-11-25 规范|[链接](https://modelcontextprotocol.io/specification/2025-11-25)|上一版主要规范，引入异步任务、增强的授权与 Elicitation（向用户征询输入）。|
|MCP 捐赠 Linux 基金会 / AAIF|[链接](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation)|2025-12，Anthropic 将 MCP 捐给新成立的 Agentic AI Foundation，OpenAI 同时捐出 AGENTS.md，Block 捐出 goose，实现中立治理。|
|Registry 生态|[链接](https://registry.modelcontextprotocol.io)|官方注册中心 + Glama（19,000+ 服务器）、mcp.so（16,000+）等目录，MCP 服务器数量已达数万量级。|

### 官方资源

|名称|链接|中文简介|
|---|---|---|
|MCP 官网|[链接](https://modelcontextprotocol.io)|MCP 协议官方网站，包含协议规范、概念介绍与开发文档。|
|官方 Servers 仓库|[GitHub](https://github.com/modelcontextprotocol/servers)|官方维护的 MCP 参考服务器集合（Filesystem、Memory、Fetch、Git 等），生态入门首选。|
|官方 SDK 文档|[链接](https://modelcontextprotocol.io/docs/sdk)|官方 SDK 列表，覆盖 TypeScript、Python、Go、Java、C#、Rust、Swift、Kotlin、PHP。|
|TypeScript SDK|[GitHub](https://github.com/modelcontextprotocol/typescript-sdk)|官方 TypeScript SDK，用于构建 MCP 服务器与客户端。|
|官方 Registry（注册中心）|[链接](https://registry.modelcontextprotocol.io)|官方 MCP 服务器注册表，相当于 MCP 服务器的"应用商店"，为客户端提供权威发现源。|
|Anthropic 官方公告|[链接](https://www.anthropic.com/news/model-context-protocol)|2024 年 11 月发布 MCP 的官方公告，介绍协议设计初衷。|

### MCP 客户端

|名称|链接|中文简介|
|---|---|---|
|Claude Desktop|[链接](https://claude.ai/download)|Anthropic 官方桌面客户端，MCP 的首发宿主，原生支持本地与远程 MCP 服务器。|
|Cursor|[链接](https://cursor.com)|AI 优先的代码编辑器，内置 MCP 支持，开发者使用最广的客户端之一。|
|Cline|[GitHub](https://github.com/cline/cline)|VS Code 内的开源自主编程 Agent，支持 BYOK 与丰富的 MCP 集成。|
|Cherry Studio|[GitHub](https://github.com/CherryHQ/cherry-studio)|国产开源多模型桌面客户端，支持 MCP，中文用户友好。|
|5ire|[GitHub](https://github.com/nanbingxyz/5ire)|跨平台开源桌面 AI 助手，内置 MCP 工具支持。|
|Windsurf|[链接](https://windsurf.com)|AI IDE，支持 MCP，主打多 Agent 并行工作流。|
|Claude Code|[链接](https://code.claude.com/docs/en/mcp)|Anthropic 终端编码 Agent，`claude mcp add` 一行接入本地 / 远程 MCP 服务器，支持 OAuth 与项目级 `.mcp.json` 共享。|
|OpenAI Codex / ChatGPT|[GitHub](https://github.com/openai/codex)|Codex CLI 通过 `config.toml` 接入 MCP 服务器；ChatGPT 开发者模式与 Apps SDK 亦基于 MCP。|
|Gemini CLI|[GitHub](https://github.com/google-gemini/gemini-cli)|Google 开源终端 Agent，`settings.json` 配置 MCP 服务器。|
|DeepSeek Harness（dsh）|[GitHub](https://github.com/deepseek-ai/deepseek-harness)|DeepSeek 官方 Agent 框架，内置 MCP 客户端桥接第三方工具服务器，并兼容 Claude Code / Codex 的 Hook 协议与 Skills；生态见 [DeepSeek 生态指南](DeepSeek.md#deepseek-harness官方-agent-框架)。|
|OpenClaw（"龙虾"）|[GitHub](https://github.com/openclaw/openclaw)|开源个人 AI 助理，接入飞书 / 微信等 IM，支持 MCP 与 Skills，可直接选 DeepSeek 作为模型。|
|OpenCode / Crush / Goose|[OpenCode](https://github.com/sst/opencode)|主流开源终端编码 Agent 均原生支持 MCP。|

### MCP Servers — 浏览器自动化

> 💡 更全面的浏览器/计算机自动化方案（Browser Use、Computer Use、agent 浏览器基础设施、AI 网页抓取等）见 [浏览器与计算机自动化](Browser_Computer_Use.md) 专章。

|名称|链接|中文简介|
|---|---|---|
|Playwright MCP（微软官方）|[GitHub](https://github.com/microsoft/playwright-mcp)|微软官方 Playwright MCP，基于可访问性树驱动真实浏览器，比截图方案更快更可靠。|
|Chrome DevTools MCP（Google 官方）|[GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp)|Google 官方 MCP，让 Agent 控制真实 Chrome 做调试、性能分析与浏览器自动化。|
|ExecuteAutomation Playwright MCP|[GitHub](https://github.com/executeautomation/mcp-playwright)|流行的 Playwright MCP 实现，支持浏览器与 API 自动化。|
|Browser MCP|[GitHub](https://github.com/browsermcp/mcp)|让 Claude/Cursor/VS Code/Windsurf 等控制你本地浏览器的 MCP server。|

### MCP Servers — 开发与版本控制

|名称|链接|中文简介|
|---|---|---|
|GitHub MCP Server（官方）|[GitHub](https://github.com/github/github-mcp-server)|GitHub 官方 MCP，可读取 PR、提交评审、跨仓库搜索代码、管理 Issue 与触发工作流。|
|Git MCP（官方参考）|[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/git)|官方 Git 仓库读写与操作服务器。|
|codexpro|[GitHub](https://github.com/rebel0789/codexpro)|通过 MCP 把 ChatGPT 开发者模式当作本地编码 Agent，让其读写、操作你本机的代码仓库。|
|FastCtx|[GitHub](https://github.com/yc-duan/fastctx)|Rust 本地工具运行时（Apache-2.0）：为 Agent 提供省上下文的文件读取、内容搜索、批量替换与 Bash 执行，中英文档。|
|Coding Tools MCP|[GitHub](https://github.com/xyTom/coding-tools-mcp)|模型中立的编码运行时，通过 MCP 给任意聊天 / Agent 一双「安全的手」操作代码库。|
|x64dbg-MCP Server|[GitHub](https://github.com/duty1g/x64dbg-mcp-server)|Zig 编写的 x64dbg 原生插件（零依赖单文件），把调试器 84 个能力（反汇编、断点、内存、PE 分析等）暴露给 MCP，做 Agent 逆向。|
|Godot-MCP|[GitHub](https://github.com/IvanMurzak/Godot-MCP)|Godot 编辑器插件（Apache-2.0）：让 Claude / Cursor / Copilot 创建节点、编辑场景、驱动项目，是 Unity-MCP 的 Godot 版。|
|figwright|[GitHub](https://github.com/awdr74100/figwright)|免费的双向 Figma MCP：设计稿→框架感知代码，也能把代码改动推回画布，配套 Figma 插件而非 Dev Mode 席位。|
|OrcaReplay|[GitHub](https://github.com/Continuum-AI-Corp/OrcaReplay)|把录制下来的 coding agent 运行开放给 Agent 读取：在进程与 socket 层记录，模型请求、shell 退出码、每轮文件变更与 MCP 调用在同一条时间线上；可断网离线逐字节重放，或从任一检查点分叉到另一个模型。Apache-2.0。|

### MCP Servers — 数据库与文件

|名称|链接|中文简介|
|---|---|---|
|Postgres MCP Pro|[GitHub](https://github.com/crystaldba/postgres-mcp)|PostgreSQL 的 MCP，提供索引调优、执行计划、健康检查与安全 SQL 执行。|
|Filesystem MCP（官方参考）|[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)|官方文件系统服务器，提供受控的本地文件读写访问。|
|OfficeCLI|[GitHub](https://github.com/iOfficeAI/OfficeCLI)|专为 AI Agent 打造的开源 Office 套件（C#，Apache-2.0），单二进制、无需安装 Office 即可读写 Word/Excel/PowerPoint，可作为 Skills/工具接入 Claude Code、Codex 等。|

### MCP Servers — 搜索与网页抓取

|名称|链接|中文简介|
|---|---|---|
|Brave Search MCP（官方）|[GitHub](https://github.com/brave/brave-search-mcp-server)|Brave 官方搜索 MCP，提供网页、本地 POI、图片、视频、新闻搜索。|
|Firecrawl MCP|[GitHub](https://github.com/mendableai/firecrawl-mcp-server)|Firecrawl 官方网页抓取 MCP，支持批量抓取、结构化提取，可云端或自托管。|
|Context7 MCP|[GitHub](https://github.com/upstash/context7)|为 LLM 提供最新版本的库文档与代码示例，解决依赖文档过时问题。|
|OpenOSINT|[GitHub](https://github.com/OpenOSINT/OpenOSINT)|AI 驱动的 OSINT 情报 Agent（MIT），19 个工具，提供 REPL、MCP server 与 CLI 三种用法。|

### MCP Servers — 云平台与第三方官方服务

|名称|链接|中文简介|
|---|---|---|
|Cloudflare MCP Server（官方）|[GitHub](https://github.com/cloudflare/mcp-server-cloudflare)|Cloudflare 官方 MCP，覆盖 Workers、KV、R2、D1 等服务。|
|Stripe Agent Toolkit|[GitHub](https://github.com/stripe/agent-toolkit)|Stripe 官方 Agent 工具包，含 MCP，安全管理客户、支付与订阅。|
|Sentry MCP|[GitHub](https://github.com/getsentry/sentry-mcp)|Sentry 官方 MCP，让 AI 查询错误监控与问题数据。|
|Slack MCP Server|[GitHub](https://github.com/korotovsky/slack-mcp-server)|功能强大的 Slack 工作区 MCP，可读取频道、汇总会话、发送消息。|
|Model Studio CLI（阿里云百炼官方）|[GitHub](https://github.com/modelstudioai/cli)|阿里云百炼官方 CLI（Apache-2.0），面向 Agent 框架暴露 Qwen 对话、图像 / 视频生成、语音、搜索、记忆与知识检索等能力。|
|Flint（微软）|[GitHub](https://github.com/microsoft/flint-chart)|微软开源的可视化中间语言 + MCP Server（MIT）：Agent 用简单可编辑的图表规格稳定产出美观图表，附多套视觉主题。|

### MCP Servers — 知识与记忆

|名称|链接|中文简介|
|---|---|---|
|Memory / Knowledge Graph MCP（官方）|[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)|官方基于知识图谱的持久化记忆服务器，为 Agent 提供结构化长期记忆。|
|Sequential Thinking MCP（官方）|[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)|官方顺序思考服务器，引导模型进行分步结构化推理。|
|MemPalace|[GitHub](https://github.com/MemPalace/mempalace)|开源、免费的 AI 记忆系统（Python，MIT），自称在公开基准上表现领先，基于 ChromaDB 提供向量化长期记忆，并通过 MCP 接入 Claude、Codex 等 Agent 客户端。社区开发活跃，已合并上千 PR。|

### MCP × DeepSeek

|名称|链接|中文简介|
|---|---|---|
|用 DeepSeek-V4 驱动任意 MCP 客户端|[链接](DeepSeek.md#在编程智能体中使用-deepseek)|V4 同时兼容 OpenAI 与 Anthropic 协议，把 Claude Code / Cursor / Cline 等 MCP 客户端的模型换成 `deepseek-v4-pro` 即可，工具调用开箱即用，单次最多 128 个函数并行。|
|deepseek-harness-plugin-mcp|[GitHub](https://github.com/bobleer/deepseek-harness-plugin-mcp)|把 dsh 插件目录（GitHub `dsh-plugin` topic）暴露为 MCP 服务器，让任意 Agent 发现、安装、运行 DeepSeek Harness 插件。|
|deepseek-mcp-server|[GitHub](https://github.com/DMontgomery40/deepseek-mcp-server)|将 DeepSeek 模型封装为 MCP 服务器，供 Claude Desktop 等宿主把复杂推理任务委托给 DeepSeek。|

### 聚合列表与 MCP 市场/目录

|名称|链接|中文简介|
|---|---|---|
|punkpeye/awesome-mcp-servers|[GitHub](https://github.com/punkpeye/awesome-mcp-servers)|星标最高的 MCP 服务器精选列表，社区事实标准目录。|
|wong2/awesome-mcp-servers|[GitHub](https://github.com/wong2/awesome-mcp-servers)|高质量精选 MCP 服务器列表，按类别清晰组织。|
|appcypher/awesome-mcp-servers|[GitHub](https://github.com/appcypher/awesome-mcp-servers)|另一份广受欢迎的 MCP 服务器精选清单。|
|Smithery|[链接](https://smithery.ai)|拥有数千服务器的 MCP 市场，界面类应用商店，支持一键安装与托管远程服务器。|
|mcp.so|[链接](https://mcp.so)|收录上万社区提交服务器的目录，第三方工具覆盖广。|
|Glama MCP|[链接](https://glama.ai/mcp/servers)|体量最大的目录之一，带可视化预览，每日更新。|
|PulseMCP|[链接](https://www.pulsemcp.com)|人工审核的 MCP 目录，每日维护，质量较高。|
|Prismix|[链接](https://prismix.dev/mcp)|集 AI 服务状态监控、MCP 目录与新闻聚合于一体的三合一 AI 中枢。MCP 目录收录 80+ 精选服务器与 500+ 自动发现资源，支持分组（Bundle）管理与版本发布追踪。|

### 重要技术文章

|名称|链接|中文简介|
|---|---|---|
|Introducing the Model Context Protocol|[链接](https://www.anthropic.com/news/model-context-protocol)|Anthropic 官方 MCP 发布文章，理解协议设计理念的必读起点。|
|Code execution with MCP|[链接](https://www.anthropic.com/engineering/code-execution-with-mcp)|Anthropic 工程博客，讲解用代码执行方式构建更高效的 MCP Agent。|
|The 2026-07-28 Specification|[链接](https://blog.modelcontextprotocol.io/posts/2026-07-28/)|MCP 官方博客对无状态核心、MRTR、扩展框架等变更的完整说明，升级服务器前必读。|
|Skills explained（Skills vs MCP）|[链接](https://claude.com/blog/skills-explained)|官方对比 Skills、MCP、Subagents 的分工与适用场景。|
