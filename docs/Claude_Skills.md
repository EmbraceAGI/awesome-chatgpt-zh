## Claude Skills（Agent Skills）指南

Claude Skills（Agent Skills）是 Anthropic 推出的让 AI 智能体按需加载专业能力的机制：通过 `SKILL.md` 加资源文件，把领域知识、脚本与最佳实践打包成可复用、可组合的"技能"，并采用渐进式披露（progressive disclosure）按需注入上下文，是构建实用智能体的新范式。2025 年底 Anthropic 将其发布为**开放标准（agentskills.io）**，到 2026 年中已有 40+ 产品采纳——Claude / Claude Code、ChatGPT & Codex、GitHub Copilot、VS Code、Cursor、Gemini CLI、OpenCode、Goose、Trae、OpenClaw、Hermes、DeepSeek Harness 与 Deep Code 等——**一次编写、到处可用**。

> 🤝 与 MCP 的关系：MCP 负责"连接工具与数据"，Skills 负责"教会 Agent 怎么做"，两者互补，见 [MCP 指南](MCP.md)。DeepSeek 侧的技能生态见下方 [DeepSeek Harness 技能生态](#deepseek-harness-技能生态)。

> 📌 本节为精选索引，完整中文资源大全见作者维护的 👉 [**awesome-claude-skills-zh**](https://github.com/yzfly/awesome-claude-skills-zh)（持续更新，欢迎 star）

### 官方资源

|名称|链接|中文简介|
|---|---|---|
|anthropics/skills|[GitHub](https://github.com/anthropics/skills)|Anthropic 官方 Agent Skills 公开仓库，含文档处理（pdf/docx/pptx/xlsx）、skill-creator 等示例技能，最权威的参考实现。|
|Agent Skills 规范|[链接](https://github.com/anthropics/skills/blob/main/spec/agent-skills-spec.md)|官方发布的 Agent Skills 开放标准规范，定义 SKILL.md 格式与渐进式披露机制。|
|Equipping agents for the real world with Agent Skills|[链接](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)|Anthropic 工程博客，深入讲解 Skills 的设计理念、架构与渐进式披露原理。|
|Introducing Agent Skills（产品公告）|[链接](https://claude.com/blog/skills)|官方产品发布公告，介绍 Skills 如何在 Claude 应用、Claude Code 与 API 间通用。|
|Agent Skills 官方文档（API）|[链接](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)|官方 API 文档，介绍如何通过 API 使用与管理 Agent Skills。|
|Extend Claude with skills（Claude Code 文档）|[链接](https://code.claude.com/docs/en/skills)|Claude Code 官方文档，讲解如何在 Claude Code 中编写、安装与使用技能。|
|claude-plugins-official|[GitHub](https://github.com/anthropics/claude-plugins-official)|官方 Claude Code 插件市场仓库，可一键安装官方维护的技能与插件。|

### 开放标准与跨平台采纳

|名称|链接|中文简介|
|---|---|---|
|agentskills.io（官网）|[链接](https://agentskills.io/)|Agent Skills 开放标准官网：规范、快速上手、客户端展示（Client Showcase）列出全部采纳产品及各家的接入文档。|
|agentskills/agentskills（规范仓库）|[GitHub](https://github.com/agentskills/agentskills)|规范与文档源码，社区通过 GitHub / Discord 共同演进标准。|
|规范全文|[链接](https://agentskills.io/specification)|`SKILL.md` 的 frontmatter 字段、目录结构（scripts / references / assets）、渐进式披露三阶段（发现 → 激活 → 执行）。|
|skills.sh|[链接](https://skills.sh)|最主要的技能分发中心与排行榜，`npx skills add <owner/repo>` 一键安装到各主流 Agent。|
|OpenAI Codex Skills 文档|[链接](https://developers.openai.com/codex/skills/)|Codex / ChatGPT 对 Agent Skills 标准的官方支持说明。|
|Gemini CLI Skills 文档|[链接](https://geminicli.com/docs/cli/skills/)|Google Gemini CLI 的技能加载与管理。|
|Cursor Skills 文档|[链接](https://cursor.com/docs/context/skills)|Cursor 2.4+ 原生支持 `SKILL.md`。|
|GitHub Copilot Agent Skills|[链接](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills)|Copilot / VS Code 的技能支持。|
|OpenClaw Skills 文档|[链接](https://docs.openclaw.ai/tools/skills)|"龙虾" OpenClaw 的技能体系，配套 ClawHub 技能市场。|

> ⚠️ **安全提醒**：技能本质是注入上下文的指令 + 可执行脚本。2026 年初 Snyk 的 ToxicSkills 研究在 ClawHub / skills.sh 抽样中发现约 36% 的技能存在提示注入，另有大规模审计在 2 万余个技能中发现十余万问题。安装第三方技能前请阅读 `SKILL.md` 与脚本，优先选择官方或经审计的市场。

### 聚合列表

|名称|链接|中文简介|
|---|---|---|
|ComposioHQ/awesome-claude-skills|[GitHub](https://github.com/ComposioHQ/awesome-claude-skills)|由 Composio 维护的精选 Claude Skills 列表，涵盖技能、资源与工具。|
|karanb192/awesome-claude-skills|[GitHub](https://github.com/karanb192/awesome-claude-skills)|"权威合集"，50+ 已验证技能，覆盖 TDD、调试、Git 工作流、文档处理等，持续维护。|
|VoltAgent/awesome-agent-skills|[GitHub](https://github.com/VoltAgent/awesome-agent-skills)|1000+ 官方与社区 agent 技能合集，兼容 Claude Code、Codex、Gemini CLI、Cursor 等。|
|travisvn/awesome-claude-skills|[GitHub](https://github.com/travisvn/awesome-claude-skills)|社区导向的精选清单，侧重 Claude Code，附详细 FAQ 与最佳实践。|
|BehiSecc/awesome-claude-skills|[GitHub](https://github.com/BehiSecc/awesome-claude-skills)|按类别（文档处理、安全、媒体生成等）组织的 30+ 技能精选列表。|

### 精选 Skills 仓库

|名称|链接|中文简介|
|---|---|---|
|obra/superpowers|[GitHub](https://github.com/obra/superpowers)|Jesse Vincent 打造的"超能力"技能框架与软件开发方法论，含 20+ 经久验证的技能（头脑风暴、TDD、调试等），生态最活跃之一。|
|obra/superpowers-skills|[GitHub](https://github.com/obra/superpowers-skills)|superpowers 插件的社区可编辑技能库，便于扩展与贡献。|
|anthropics/skills（文档技能）|[GitHub](https://github.com/anthropics/skills/tree/main/skills)|官方文档处理技能集（docx/pdf/pptx/xlsx），支持公式、图表、表单填写、OCR 等生产级能力。|
|alirezarezvani/claude-skills|[GitHub](https://github.com/alirezarezvani/claude-skills)|含 330+ 技能、30+ agents、70+ 命令的大型合集，覆盖工程、营销、产品、研究等多领域。|
|wanshuiyin/Auto-claude-code-research-in-sleep|[GitHub](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep)|ARIS（Auto-Research-In-Sleep）：用于自主 ML 研究的纯 Markdown 轻量技能，无框架、无锁定，内置 13 个研究工作流与持久化 Research Wiki，可跨 Claude Code、Codex、Cursor、Kimi、DeepSeek、GLM 等多种模型使用。|
|Hacker0x01/claude-power-user|[GitHub](https://github.com/Hacker0x01/claude-power-user)|HackerOne 开源的 Claude Code 核心技能库。|
|JuliusBrussee/caveman|[GitHub](https://github.com/JuliusBrussee/caveman)|"原始人语气"省 token 的 Claude Code 技能（MIT）：让模型用极简的"原始人"句式表达（why use many token when few token do trick），自称可削减约 65% 输出 token，趣味十足又能省钱。|
|BuilderIO/skills|[GitHub](https://github.com/BuilderIO/skills)|Builder.io 出品的小而可组合的编码 Agent 技能集（MIT），一条命令安装推荐技能。|
|jakubkrehel/skills|[GitHub](https://github.com/jakubkrehel/skills)|设计工程师 Jakub Krehel 的界面技能集：UI、排版、色彩、无障碍、布局与产品文案，`better-interface` 一键做整体评审。|
|JimLiu/baoyu-design|[GitHub](https://github.com/JimLiu/baoyu-design)|宝玉把 Claude Design（claude.ai/design 背后的设计引擎）打包成可移植 Agent Skill，在 Cursor、Claude Code 等本地 Agent 里产出精致 UI。|
|petergyang/no-ai-slop|[GitHub](https://github.com/petergyang/no-ai-slop)|去除写作中 20+ 种「AI 味」套路而不抹平个人语气的技能（MIT）。|
|firecrawl/anydoc（skill）|[GitHub](https://github.com/firecrawl/anydoc)|Firecrawl 的文档转 Markdown 库以 Agent Skill 形式分发，让 Agent 直接读懂 Word / PPT / Excel / PDF / EPUB。|
|Hahaknight/claude-skills-pro|[GitHub](https://github.com/Hahaknight/claude-skills-pro)|工程师工作流技能包（15 个：代码审查、测试锻造、根因调试、安全审查、安全重构等），7 个免费 MIT，附《中文实战手册》与场景速查表，`npx skills add` 一键装进 78+ agent。|
|Hahaknight/digital-employee-pack|[GitHub](https://github.com/Hahaknight/digital-employee-pack)|「数字员工」中文提效技能包：面向非程序员的 6 个办公技能（周报、会议纪要、PPT 大纲等）+ 防护 Hooks + 工作流 SOP。|

### DeepSeek Harness 技能生态

DeepSeek 官方 Agent 框架 [deepseek-harness（dsh）](DeepSeek.md#deepseek-harness官方-agent-框架) 内置 Skill 系统（Markdown 指令集，由 SkillRegistry 管理，支持全局 / Agent 级作用域），并兼容 Agent Skills 开放标准与 Claude Code / Codex 的 Hook 协议；社区以 GitHub `dsh-plugin` topic 为索引，两周内已涌现数百个技能与插件仓库。

|名称|链接|中文简介|
|---|---|---|
|awesome-dsh-skills|[GitHub](https://github.com/yzfly/awesome-dsh-skills)|本项目作者维护的 dsh 技能 / 插件中文精选：700+ 仓库自动收录并每日校验、11 大分类、**DSH Skill Spec 0.1** 规范、`dsh-skill-lint` 零依赖校验器（缺失触发词 / 失效引用 / 泄露密钥）与 2026 Q3 精选版；可搜索站点 [code.jiangshu.ai/awesome-dsh-skills](https://code.jiangshu.ai/awesome-dsh-skills)。|
|0xsline/awesome-deepseek-harness|[GitHub](https://github.com/0xsline/awesome-deepseek-harness)|从 dsh-external/hub 与 `dsh-plugin` topic 整理的 DSH 插件、工具与基础设施列表。|
|Dominic789654/awesome-deepseek-harness|[GitHub](https://github.com/Dominic789654/awesome-deepseek-harness)|按可视化 / PPT / 编码 / Agents / Loops（auto-research）分类的 DSH 插件、技能、MCP 服务器与 UI 精选。|
|dsh-find-plugins|[GitHub](https://github.com/Nagi-ovo/dsh-find-plugins)|一个"找插件的技能"：让 dsh 自己在 GitHub 搜索、安装并验证插件。|
|deepseek-harness-plugin-mcp|[GitHub](https://github.com/bobleer/deepseek-harness-plugin-mcp)|把 dsh 插件目录暴露为 MCP 服务器，任意 Agent 都能发现与运行 DSH 插件。|
|Deep Code Agent Skills|[链接](https://deepcode.vegamo.cn/en/docs/configuration/agent-skills)|面向 DeepSeek-V4 的终端编码助手 [Deep Code](https://github.com/lessweb/deepcode-cli) 的技能配置文档，已登上 agentskills.io 采纳名单。|
|dsh-plugin topic|[GitHub](https://github.com/topics/dsh-plugin)|官方指定的插件发现入口，发布插件请打上此 topic。|

### 工具与基础设施

|名称|链接|中文简介|
|---|---|---|
|skill-creator（官方元技能）|[GitHub](https://github.com/anthropics/skills/tree/main/skills/skill-creator)|官方"创建技能的技能"，用于生成、改进、验证与打包新技能。|
|obra/superpowers-marketplace|[GitHub](https://github.com/obra/superpowers-marketplace)|superpowers 配套的精选 Claude Code 插件市场。|
|aiskillstore/marketplace|[GitHub](https://github.com/aiskillstore/marketplace)|经安全审计的技能市场，支持 Claude、Codex、Claude Code 一键安装与质量校验。|
|manutej/luxor-claude-marketplace|[GitHub](https://github.com/manutej/luxor-claude-marketplace)|专业 Claude Code 市场，含 67 技能、28 命令、30 agents、15 工作流共 140 个开发工具。|
|Claude Code Marketplaces 目录站|[链接](https://claudemarketplaces.com/)|聚合插件、技能与 MCP 服务器的市场目录站，便于发现与安装。|
|Skillselion 技能目录站|[链接](https://skillselion.com)|聚合 Claude Code 技能、MCP 服务器与插件市场的目录站，按安装量与 GitHub stars 排名，便于发现与安装。|
|microsoft/SkillOpt|[GitHub](https://github.com/microsoft/SkillOpt)|微软开源的文本空间优化器，为冻结参数的 LLM 智能体训练可复用的自然语言技能：基于轨迹驱动迭代、验证门控更新，产出可直接部署的 best_skill.md 技能文件。|
|microsoft/skill-recorder|[GitHub](https://github.com/microsoft/skill-recorder)|微软开源的桌面应用（MIT）：录一遍你在屏幕上的操作（点击、切窗、访问页面、口述），用 Copilot CLI 自动生成可复用的 Agent Skill。|

### 文章与教程

|名称|链接|中文简介|
|---|---|---|
|Claude Skills are awesome, maybe a bigger deal than MCP|[链接](https://simonwillison.net/2025/Oct/16/claude-skills/)|Simon Willison 的经典文章，论证 Skills 比 MCP 更轻量高效，入门必读。|
|Skills explained（官方对比）|[链接](https://claude.com/blog/skills-explained)|官方文章，系统对比 Skills 与 Prompts、Projects、MCP、Subagents 的区别与适用场景。|
|Understanding Claude Code's Full Stack: MCP, Skills, Subagents, Hooks|[链接](https://alexop.dev/posts/understanding-claude-code-full-stack/)|全面梳理 Claude Code 技术栈中 MCP、Skills、子代理与 Hooks 的关系。|
