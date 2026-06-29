# Agent-First / Agent-Friendly：为智能体而构建

> **为什么要为 Agent 而构建？**
>
> 互联网正在迎来它的"第二类用户"——AI 智能体（Agent）。当人把任务交给 Agent，它不再用人眼浏览你的网页、用鼠标点击你的按钮，而是直接查阅它"已经接好线"的工具：MCP server、API、CLI、SDK。**在那张清单里，你的产品要么被调用，要么根本不存在。** 这正是 Netlify CEO Mathias Biilmann 提出 **Agent Experience（AX，智能体体验）** 的缘由：继 UX、DX 之后，软件需要为 Agent 设计第三种体验。围绕这一理念，一批新标准正在成形——`llms.txt` 为模型提供内容地图，`AGENTS.md` 为编码 Agent 写下规则，`MCP` 成为 Agent 连接万物的"USB-C"，微软 `NLWeb` 让每个网站都能成为 Agent 可调用的工具。它们之于 Agent，正如 `robots.txt` 之于爬虫。从 Agent-Friendly 到 Agent-First，这不只是给产品"穿层新衣"，而是从地基开始，重新思考"谁在使用软件"。

## 核心理念

- **Agent-Friendly（对 agent 友好）**：在面向人的产品之上做改造，让 agent 也能用（语义化 HTML、机器可读文档、清晰 API）。
- **Agent-Ready（agent 就绪）**：产品已具备让 agent 可发现、可调用、可执行操作的完整能力。
- **Agent-First（agent 优先）**：从零开始就把 agent 当作"主要消费者"——先设计 agent 用的接口与契约，再设计人用的 UI。类比 2009 年 Luke Wroblewski 的"Mobile First"。
- **AX（Agent Experience，智能体体验）**：由 Netlify CEO Mathias Biilmann 于 2025 年提出，类比 Don Norman 的 "User Experience"。四大支柱：**Access（可访问）、Context（上下文）、Tools（工具）、Orchestration（编排）**。AX 不取代 DX，而是延伸 DX。

> 关键类比：**`robots.txt` 之于爬虫（能不能进），正如 `llms.txt` / `AGENTS.md` / `MCP` 之于 agent（进来后怎么高效用）**。

## 关键标准与规范

| 标准 | 链接 | 提出方 | 作用 |
|------|------|--------|------|
| llms.txt | [llmstxt.org](https://llmstxt.org/) | Jeremy Howard / Answer.AI（2024-09） | 网站根目录放一份 Markdown 格式的 `/llms.txt`，为 LLM 提供精简的内容地图，解决"上下文装不下整站 HTML" |
| AGENTS.md | [agents.md](https://agents.md/) | Google/OpenAI/Factory/Sourcegraph/Cursor 等，现归 Agentic AI Foundation | 给编码 agent 的"README"，写明构建、测试、规范与边界，支持目录层级就近读取 |
| MCP（模型上下文协议） | [Anthropic 公告](https://www.anthropic.com/news/model-context-protocol) | Anthropic（2024-11） | agent 连接数据/工具/工作流的开放标准，"AI 应用的 USB-C"，已成事实标准（详见本仓库 [MCP 指南](MCP.md)） |
| NLWeb（自然语言 Web） | [GitHub](https://github.com/microsoft/NLWeb) | 微软（2025） | 复用网站已有的 Schema.org/RSS 数据 + LLM，把网站变成可对话的 AI 应用，每个实例自带 MCP server |
| Build agent-friendly websites | [web.dev](https://web.dev/articles/ai-agent-site-ux) | Chrome 团队 | 实操指南：agent 通过截图/HTML/无障碍树理解网站，建议语义化 HTML、稳定布局、ARIA、完整 OpenAPI |

## 实践框架与清单

| 名称 | 链接 | 简介 |
|------|------|------|
| **Agents First** | [agentsfirst.dev](https://agentsfirst.dev/) ・[GitHub](https://github.com/capitalthought/agentsfirst) | Capital Factory 创始人 Joshua Baer 发起的"Agent 优先"设计框架与宣言。提出**九大原则**（Interface First、Contract First、Prep Gates、Typed State、Visible Outputs、Multi-Model Verification、Perspective Dispatch、Autonomous Recovery、Inspectable State）、**成熟度 0–4 级**、工具设计规范与可量化指标，并配套 MCP 评分服务与脚手架。引用 Vercel 数据：58.9% 的 token 已流经工具调用请求。 |
| AX 六层栈（如何把产品做成 Agent-Friendly） | [X 长文 @chg80333](https://x.com/chg80333/status/2062532427734810756) | 中文实操长文，把 AX 拆成**六层 checklist**：Surface（接入形态 CLI>MCP>SDK>API）、Auth（OAuth2.1+PKCE/短命 token）、Capability（按用户目标封装工具+渐进披露）、Behavior（幂等/结构化错误/读写分离）、Safety（L0–L3 风险分级+确认 token+undo）、Transparency（暴露 reasoning/可观测）。核心：用一份 capability 真源代码生成多种 surface。 |
| Agent Readiness Score / a14y.dev | [a14y.dev](https://a14y.dev/) | 检测网页对 agent 的可读性/可用性的评分工具（如 38 项检查） |

## 代表文章与观点

| 标题 | 链接 | 作者 / 出处 | 简介 |
|------|------|------------|------|
| Introducing AX: Why Agent Experience Matters | [biilmann.blog](https://biilmann.blog/articles/introducing-ax/) | Mathias Biilmann（Netlify CEO） | AX 的奠基性文章，类比 UX 提出"为 agent 设计"的体验范式 |
| One Year of AX | [biilmann.blog](https://biilmann.blog/articles/one-year-of-ax/) | Mathias Biilmann | AX 提出一年后的复盘与 2026 预测 |
| Agent Experience（AX）资源站 | [agentexperience.ax](https://agentexperience.ax/) | Netlify + 社区 | AX 标准资源站，含概念与文章 |
| Agent Experience: Building an Open Web for the AI Era | [a16z](https://a16z.com/podcast/agent-experience-building-an-open-web-for-the-ai-era/) | a16z × Biilmann（2025-03） | VC 视角讨论 AX 与 AI 时代的开放网络 |
| Build agent-friendly websites | [web.dev](https://web.dev/articles/ai-agent-site-ux) | Chrome 团队 | agent 如何理解网站，及网站该如何配合 |
| Agentic Engine Optimization (AEO) | [addyosmani.com](https://addyosmani.com/blog/agentic-engine-optimization/) | Addy Osmani（Google） | 提出"为 agent 引擎做优化"，SEO 的演进形态 |
| The age of agent experience | [stytch.com](https://stytch.com/blog/the-age-of-agent-experience/) | Stytch | 从身份认证/授权角度谈 AX（Access 支柱） |

## 代表项目与工具

| 名称 | 链接 | 简介 |
|------|------|------|
| NLWeb | [GitHub](https://github.com/microsoft/NLWeb) | 微软开源，把网站变成自然语言/agent 可用的对话接口，自带 MCP server |
| AGENTS.md | [GitHub](https://github.com/agentsmd/agents.md) | 统一的编码 agent 指令文件开放格式 |
| awesome-web-agents | [GitHub](https://github.com/steel-dev/awesome-web-agents) | 构建 AI web agent 的工具/框架/资源清单 |
| Steel.dev | [GitHub](https://github.com/steel-dev) | 专为 AI agent 打造的开源无头浏览器 API |
| Casdoor | [GitHub](https://github.com/casdoor/casdoor) | 开源的 Agent-First 身份与访问管理（IAM）/ 认证服务器与 MCP、agent 网关，带 Web UI，支持 MCP、OAuth、OIDC、SAML、LDAP、SCIM、WebAuthn、MFA 等 |
| monlite | [GitHub](https://github.com/qataruts/monlite) | 面向 AI agent 的「本地后端」（TypeScript，MIT）：把文档、向量、缓存、队列与 cron 定时任务全部集成进单个 SQLite 文件，零外部依赖即可为 agent 提供持久化、检索与任务调度能力 |
