## MCP（模型上下文协议）指南

MCP（Model Context Protocol，模型上下文协议）是 Anthropic 于 2024 年 11 月推出的开放协议，被称为 AI 应用的"USB-C 接口"——让大模型以统一方式无缝连接外部工具、数据与系统。它已成为 AI 智能体生态的事实标准之一。

> 📌 本节为精选索引，完整中文资源大全（400+ MCP Servers）见作者维护的 👉 [**Awesome-MCP-ZH**](https://github.com/yzfly/Awesome-MCP-ZH)（持续更新，欢迎 star）

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

### MCP Servers — 数据库与文件

|名称|链接|中文简介|
|---|---|---|
|Postgres MCP Pro|[GitHub](https://github.com/crystaldba/postgres-mcp)|PostgreSQL 的 MCP，提供索引调优、执行计划、健康检查与安全 SQL 执行。|
|Filesystem MCP（官方参考）|[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)|官方文件系统服务器，提供受控的本地文件读写访问。|

### MCP Servers — 搜索与网页抓取

|名称|链接|中文简介|
|---|---|---|
|Brave Search MCP（官方）|[GitHub](https://github.com/brave/brave-search-mcp-server)|Brave 官方搜索 MCP，提供网页、本地 POI、图片、视频、新闻搜索。|
|Firecrawl MCP|[GitHub](https://github.com/mendableai/firecrawl-mcp-server)|Firecrawl 官方网页抓取 MCP，支持批量抓取、结构化提取，可云端或自托管。|
|Context7 MCP|[GitHub](https://github.com/upstash/context7)|为 LLM 提供最新版本的库文档与代码示例，解决依赖文档过时问题。|

### MCP Servers — 云平台与第三方官方服务

|名称|链接|中文简介|
|---|---|---|
|Cloudflare MCP Server（官方）|[GitHub](https://github.com/cloudflare/mcp-server-cloudflare)|Cloudflare 官方 MCP，覆盖 Workers、KV、R2、D1 等服务。|
|Stripe Agent Toolkit|[GitHub](https://github.com/stripe/agent-toolkit)|Stripe 官方 Agent 工具包，含 MCP，安全管理客户、支付与订阅。|
|Sentry MCP|[GitHub](https://github.com/getsentry/sentry-mcp)|Sentry 官方 MCP，让 AI 查询错误监控与问题数据。|
|Slack MCP Server|[GitHub](https://github.com/korotovsky/slack-mcp-server)|功能强大的 Slack 工作区 MCP，可读取频道、汇总会话、发送消息。|

### MCP Servers — 知识与记忆

|名称|链接|中文简介|
|---|---|---|
|Memory / Knowledge Graph MCP（官方）|[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)|官方基于知识图谱的持久化记忆服务器，为 Agent 提供结构化长期记忆。|
|Sequential Thinking MCP（官方）|[GitHub](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)|官方顺序思考服务器，引导模型进行分步结构化推理。|
|llmtrim|[GitHub](https://github.com/fkiene/llmtrim)|本地 MCP 服务器与代理，在请求发往 LLM 前压缩提示词、对话历史与工具输出以降低 token 成本，带质量门控、不改变回答。提供 llmtrim_compress、llmtrim_compress_text、llmtrim_stats 三个工具。|

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

### 重要技术文章

|名称|链接|中文简介|
|---|---|---|
|Introducing the Model Context Protocol|[链接](https://www.anthropic.com/news/model-context-protocol)|Anthropic 官方 MCP 发布文章，理解协议设计理念的必读起点。|
|Code execution with MCP|[链接](https://www.anthropic.com/engineering/code-execution-with-mcp)|Anthropic 工程博客，讲解用代码执行方式构建更高效的 MCP Agent。|
