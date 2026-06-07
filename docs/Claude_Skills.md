## Claude Skills（Agent Skills）指南

Claude Skills（Agent Skills）是 Anthropic 推出的让 AI 智能体按需加载专业能力的机制：通过 `SKILL.md` 加资源文件，把领域知识、脚本与最佳实践打包成可复用、可组合的"技能"，并采用渐进式披露（progressive disclosure）按需注入上下文，是构建实用智能体的新范式。

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
|Hacker0x01/claude-power-user|[GitHub](https://github.com/Hacker0x01/claude-power-user)|HackerOne 开源的 Claude Code 核心技能库。|

### 工具与基础设施

|名称|链接|中文简介|
|---|---|---|
|skill-creator（官方元技能）|[GitHub](https://github.com/anthropics/skills/tree/main/skills/skill-creator)|官方"创建技能的技能"，用于生成、改进、验证与打包新技能。|
|obra/superpowers-marketplace|[GitHub](https://github.com/obra/superpowers-marketplace)|superpowers 配套的精选 Claude Code 插件市场。|
|aiskillstore/marketplace|[GitHub](https://github.com/aiskillstore/marketplace)|经安全审计的技能市场，支持 Claude、Codex、Claude Code 一键安装与质量校验。|
|manutej/luxor-claude-marketplace|[GitHub](https://github.com/manutej/luxor-claude-marketplace)|专业 Claude Code 市场，含 67 技能、28 命令、30 agents、15 工作流共 140 个开发工具。|
|Claude Code Marketplaces 目录站|[链接](https://claudemarketplaces.com/)|聚合插件、技能与 MCP 服务器的市场目录站，便于发现与安装。|

### 文章与教程

|名称|链接|中文简介|
|---|---|---|
|Claude Skills are awesome, maybe a bigger deal than MCP|[链接](https://simonwillison.net/2025/Oct/16/claude-skills/)|Simon Willison 的经典文章，论证 Skills 比 MCP 更轻量高效，入门必读。|
|Skills explained（官方对比）|[链接](https://claude.com/blog/skills-explained)|官方文章，系统对比 Skills 与 Prompts、Projects、MCP、Subagents 的区别与适用场景。|
|Understanding Claude Code's Full Stack: MCP, Skills, Subagents, Hooks|[链接](https://alexop.dev/posts/understanding-claude-code-full-stack/)|全面梳理 Claude Code 技术栈中 MCP、Skills、子代理与 Hooks 的关系。|
