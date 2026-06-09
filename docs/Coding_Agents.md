# Coding Agents 编程智能体

2025 年起，AI 编程从"代码补全/对话"全面走向"编程智能体（Coding Agent）"——以 **Claude Code**、**OpenAI Codex** 为代表的终端 Agent 能自主读写代码库、运行命令、跑测试、提交 PR，把多步骤工程任务端到端交付。本章汇总当下主流的编程智能体、IDE 工具、自主软件工程 Agent、评测基准与学习资源。

> 相关：通用智能体见 [AGI](AGI.md)，Agent 开发框架见 [应用开发指南](ChatGPT_dev.md)，工具连接协议见 [MCP 指南](MCP.md)。

## 命令行 / 终端编码 Agent

终端原生的编程智能体，可直接在你的代码仓库里规划、改码、执行与验证，是目前最受重视的形态。

| 名称 | 链接 | 简介 |
|------|------|------|
| **Claude Code** | [GitHub](https://github.com/anthropics/claude-code) | Anthropic 官方出品的终端编码 Agent，由 Claude 驱动，可读写代码、执行命令、完成多步开发任务（官网 code.claude.com） |
| **OpenAI Codex CLI** | [GitHub](https://github.com/openai/codex) | OpenAI 出品的轻量级本地终端编码 Agent，支持 ChatGPT 订阅或 API Key，在命令行进行 AI 辅助开发 |
| Gemini CLI | [GitHub](https://github.com/google-gemini/gemini-cli) | Google 出品的开源终端 AI Agent，把 Gemini 带入命令行，内置文件操作、Shell、联网搜索并支持 MCP |
| aider | [GitHub](https://github.com/Aider-AI/aider) | 社区开源的终端 AI 结对编程工具，自动构建仓库地图与 Git 提交，支持多家模型 |
| **pi** | [GitHub](https://github.com/earendil-works/pi) ・[官网](https://pi.dev/) | libGDX 作者 Mario Zechner 发起、现归属 Earendil 的极简可扩展开源编码 Agent（agent harness，MIT，约 6 万 star）。奉行 **"primitives, not features"**：内核只暴露 Read/Write/Edit/Bash 四个工具（刻意不内置 MCP/子 Agent/沙箱），靠 TypeScript 扩展、Skills（兼容 Claude Code/Codex）、模板自由定制，接入 28+ 模型供应商；下文"龙虾" OpenClaw 即构建于其上 |
| oh-my-pi | [GitHub](https://github.com/can1357/oh-my-pi) | pi 生态最热门的"全家桶"增强分支（MIT，约 1.1 万 star），在 pi 之上补齐 LSP、调试器、浏览器、子 Agent、跨会话记忆与 Zed 集成 |
| OpenCode | [GitHub](https://github.com/sst/opencode) | SST 团队出品的开源终端编码 Agent（Go），客户端-服务端架构，支持 75+ 模型 |
| Crush | [GitHub](https://github.com/charmbracelet/crush) | Charm 出品的"颜值派"终端编码 Agent，基于 TUI，支持多模型、LSP 与 MCP |
| Goose | [GitHub](https://github.com/block/goose) | Block 出品的开源可扩展 AI Agent（Rust），可自主执行/编辑/测试代码，兼容任意 LLM |
| Qwen Code | [GitHub](https://github.com/QwenLM/qwen-code) | 阿里通义千问团队出品，基于 Gemini CLI 改造并适配 Qwen3-Coder |
| Amp | [链接](https://sourcegraph.com/amp) | Sourcegraph 出品的 AI 编码 Agent，提供 CLI 与 VS Code 扩展 |
| Cursor CLI | [链接](https://cursor.com/cli) | Cursor 的命令行版 Agent，可在终端、CI/CD 与自动化脚本中运行 |
| Warp | [链接](https://www.warp.dev) | AI 原生终端，将终端延伸为支持多模型的提示驱动 Agent 平台 |

## IDE / 编辑器编码 Agent

| 名称 | 链接 | 简介 |
|------|------|------|
| Cursor | [链接](https://cursor.com) | Anysphere 出品的 AI 原生代码编辑器，集成多模型 Agent，支持跨文件改动 |
| Windsurf | [链接](https://windsurf.com) | 原 Codeium 团队出品的 AI 原生编辑器，核心是可跨文件协调改动的 Cascade Agent |
| GitHub Copilot | [链接](https://github.com/features/copilot) | GitHub（微软）出品，提供补全、聊天与 Agent 模式，深度集成主流 IDE |
| Cline | [GitHub](https://github.com/cline/cline) | 开源自主编码 Agent，以侧边栏运行于 VS Code、JetBrains，含 SDK 与 CLI |
| Continue | [GitHub](https://github.com/continuedev/continue) | 开源 AI 编码助手，可在 VS Code / JetBrains 中自由接入任意 LLM（含本地模型） |
| Roo Code | [GitHub](https://github.com/RooCodeInc/Roo-Code) | 由 Cline 衍生的开源 VS Code Agent，提供 Code/Architect/Ask/Debug 多模式 |
| Kilo Code | [GitHub](https://github.com/Kilo-Org/kilocode) | 融合 Cline 与 Roo Code 特性的开源 VS Code 编码 Agent，支持编排与行内补全 |
| Trae | [链接](https://www.trae.ai) | 字节跳动出品的免费 AI 原生 IDE，内置 Claude、GPT 等模型 |
| Zed | [链接](https://zed.dev) | 高性能 AI 代码编辑器，原生支持 Agent 面板，可运行 Claude Code、Amp 等（ACP 协议） |
| Augment Code | [链接](https://www.augmentcode.com) | 面向大型代码库的 AI 编码平台，核心是 Context Engine，提供 Auggie CLI |
| 通义灵码 | [链接](https://lingma.aliyun.com) | 阿里云基于通义大模型的智能编码助手，实时续写、生成代码与单测 |
| CodeGeeX | [GitHub](https://github.com/THUDM/CodeGeeX) | 清华 THUDM 开源的多语言代码生成模型与编程助手 |

## 通用自主 Agent / 个人 AI 助理

> 这类是"通用型"自主智能体（个人助理），并非纯编程工具，但都能编排/委派编程 Agent（如 Codex、OpenCode）完成开发任务，2026 年热度极高。更多通用 Agent 见 [AGI](AGI.md)。

| 名称 | 链接 | 简介 |
|------|------|------|
| OpenClaw | [GitHub](https://github.com/openclaw/openclaw) ・[官网](https://openclaw.ai/) | 开源自托管的个人 AI 助理，通过 WhatsApp/Telegram/Discord/Slack 等聊天软件交互，能真正动手执行任务（操作设备、文件、邮件、浏览网页）。模型无关，吉祥物是只龙虾🦞，**中文社区俗称"龙虾"**；由 Peter Steinberger 等发起 |
| Hermes Agent | [GitHub](https://github.com/NousResearch/hermes-agent) ・[官网](https://hermes-agent.nousresearch.com/) | Nous Research 出品的**自我进化型**自主 Agent：内置学习循环，能从经验生成技能、持续改进、检索历史对话并建立长期记忆，可多平台触达、委派编程 agent |

## 自主软件工程 Agent（开源 / 产品）

更"自主"的软件工程智能体，目标是从一个 issue / 需求直接产出可交付的工程结果。

| 名称 | 链接 | 简介 |
|------|------|------|
| Devin | [链接](https://devin.ai/) | Cognition 推出的商用自主 AI 软件工程师，可自主规划、编写、测试并交付生产代码 |
| OpenHands（原 OpenDevin） | [GitHub](https://github.com/All-Hands-AI/OpenHands) | All Hands AI 开源的自主软件开发智能体平台，可在沙箱中写代码、跑命令、浏览网页并提交 PR |
| SWE-agent | [GitHub](https://github.com/SWE-agent/SWE-agent) | 普林斯顿团队开源，接收 GitHub issue 并用所选 LLM 自动定位、修复与测试（NeurIPS 2024） |
| gpt-pilot | [GitHub](https://github.com/Pythagora-io/gpt-pilot) | 多智能体协作（架构师/技术主管/开发/调试），像真人开发者一样逐步从零构建应用 |
| GPT Engineer | [GitHub](https://github.com/AntonOsika/gpt-engineer) | 用自然语言描述需求即可生成完整代码库的 CLI 工具，后续演化为 Lovable |
| Lovable | [链接](https://lovable.dev/) | GPT Engineer 的商业化产品，面向非技术用户用自然语言构建 Web 应用 |
| Factory（Droid） | [链接](https://factory.ai/) | 企业级"Agent-Native"开发平台，在终端/IDE 中端到端规划、编码、测试与交付 |
| Plandex | [GitHub](https://github.com/plandex-ai/plandex) | 面向大型项目的开源终端 AI 编码 Agent，支持超大上下文与累积 diff 沙箱审查 |
| Devika | [GitHub](https://github.com/stitionai/devika) | 早期开源的"Agentic 软件工程师"实现，曾作为 Devin 的开源替代 |

## 编码 Agent 评测基准

| 名称 | 链接 | 简介 |
|------|------|------|
| SWE-bench | [GitHub](https://github.com/SWE-bench/SWE-bench) | 衡量模型能否为真实 GitHub issue 生成可通过测试的修复补丁，含 2294 个 issue-PR 样本 |
| SWE-bench Verified | [链接](https://www.swebench.com/verified.html) | OpenAI 与人工标注协作筛出的 500 条高质量子集，修正原集的错判 |
| Terminal-Bench | [链接](https://www.tbench.ai/) | 衡量 Agent 在真实命令行环境中完成软件工程、运维等高难度终端任务的能力 |
| Aider Polyglot Leaderboard | [链接](https://aider.chat/docs/leaderboards/) | 用 225 道多语言题衡量模型的代码编写与按报错修改能力 |
| LiveCodeBench | [链接](https://livecodebench.github.io/) | 持续收集竞赛新题、按时间标注以防数据污染，覆盖生成、自修复、执行预测 |
| SWE-Lancer | [GitHub](https://github.com/openai/SWELancer-Benchmark) | OpenAI 推出，用 1400+ 个总值 100 万美元的真实外包任务衡量工程交付价值 |

## 资源与文章

| 名称 | 链接 | 简介 |
|------|------|------|
| Claude Code Best Practices | [链接](https://www.anthropic.com/engineering/claude-code-best-practices) | Anthropic 官方总结的 Claude Code 智能体编码最佳实践（上下文管理、先研究再规划、TDD 等） |
| Building Effective Agents | [链接](https://www.anthropic.com/research/building-effective-agents) | Anthropic 经典文章，讲解 workflow 与 agent 的区别及可组合的实用 Agent 设计模式 |
| Writing Tools for Agents | [链接](https://www.anthropic.com/engineering/writing-tools-for-agents) | 讲如何为 AI Agent 设计清晰、节省上下文、可组合的工具 |
| awesome-claude-code | [GitHub](https://github.com/hesreallyhim/awesome-claude-code) | 高人气 Claude Code 资源合集，收录 skills、hooks、slash 命令、编排器与插件 |
| pi-vs-claude-code | [GitHub](https://github.com/disler/pi-vs-claude-code) | 系统对比开源 pi 与闭源 Claude Code 工程实践的教学仓库，适合理解"agent harness"差异 |
| awesome-code-ai | [GitHub](https://github.com/sourcegraph/awesome-code-ai) | Sourcegraph 维护的 AI 编码工具列表（助手、补全、重构等） |
| anthropic-cookbook（agents patterns） | [GitHub](https://github.com/anthropics/anthropic-cookbook/tree/main/patterns/agents) | Anthropic 官方 cookbook 中的 Agent 设计模式示例代码 |
