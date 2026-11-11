# Claude Code & Codex 生态指南

Claude Code（Anthropic）与 Codex（OpenAI）是 2025–2026 年最主流的两款编程智能体。二者功能已高度趋同：终端 CLI、桌面 App、IDE 插件、云端任务、子代理、Hooks、MCP、Skills / 插件一应俱全。围绕它们长出了庞大的周边生态——配置切换、模型路由、用量统计、多会话管理、移动端遥控、技能与插件市场等。本页按用途整理这些工具（数据截至 2026-11）。

> 相关专题：[Coding Agents 编程智能体](Coding_Agents.md)（更多编码 Agent 横向对比）· [API 代理与模型路由](API_Proxy.md)（中转、网关、订阅转 API）· [Claude Skills 指南](Claude_Skills.md)

## 官方入口

| 名称 | 链接 | 简介 |
|------|------|------|
| **Claude Code** | [GitHub](https://github.com/anthropics/claude-code) ・[文档](https://code.claude.com/docs) | Anthropic 官方编程智能体：终端 CLI、桌面 App、VS Code / JetBrains 插件与网页版共用一套能力，支持子代理、Hooks、MCP、Skills、插件与 Mods |
| Claude Code 更新日志 | [链接](https://code.claude.com/docs/en/changelog) | 官方 changelog，追踪新功能最快的地方 |
| Claude Agent SDK（Python） | [GitHub](https://github.com/anthropics/claude-agent-sdk-python) | 把 Claude Code 的 Agent 循环、工具与上下文管理作为库嵌入自己的程序 |
| Claude Agent SDK（TypeScript） | [GitHub](https://github.com/anthropics/claude-agent-sdk-typescript) | Agent SDK 的 TypeScript 版本 |
| Claude Code GitHub Action | [GitHub](https://github.com/anthropics/claude-code-action) | 在 PR / Issue 中 @claude，让 Claude Code 在 GitHub Actions 里评审代码、实现需求 |
| 官方插件目录 | [GitHub](https://github.com/anthropics/claude-plugins-official) | Anthropic 维护的高质量 Claude Code 插件目录（约 4.5 万 star） |
| knowledge-work-plugins | [GitHub](https://github.com/anthropics/knowledge-work-plugins) | Anthropic 开源的知识工作者插件集，主要面向 Claude Cowork |
| sandbox-runtime | [GitHub](https://github.com/anthropics/sandbox-runtime) | Anthropic 开源的轻量沙箱，在操作系统层面限制任意进程的文件与网络访问，无需容器 |
| **OpenAI Codex** | [GitHub](https://github.com/openai/codex) ・[文档](https://developers.openai.com/codex) | OpenAI 的编程智能体：Codex CLI（Rust，开源）、桌面 App（Windows / macOS）、IDE 插件与云端任务，可用 ChatGPT 订阅或 API Key |
| Codex 更新日志 | [链接](https://developers.openai.com/codex/changelog/) | 官方 changelog，CLI 与桌面 App 更新频率很高 |
| Codex GitHub Action | [GitHub](https://github.com/openai/codex-action) | 在 GitHub Actions 中运行 Codex |
| openai/skills | [GitHub](https://github.com/openai/skills) | OpenAI 官方 Codex Skills 目录 |
| codex-plugin-cc | [GitHub](https://github.com/openai/codex-plugin-cc) | OpenAI 官方出品：在 Claude Code 里调用 Codex 做代码评审或委派任务 |
| Codex Security | [GitHub](https://github.com/openai/codex-security) | OpenAI 的安全审计 CLI 与 TypeScript SDK，用于发现、验证并修复漏洞 |
| AGENTS.md | [GitHub](https://github.com/agentsmd/agents.md) ・[官网](https://agents.md/) | 指导编程智能体的开放格式，Codex、Cursor、OpenCode 等广泛支持；Claude Code 对应文件为 CLAUDE.md |

## 配置切换与多供应商管理

| 名称 | 链接 | 简介 |
|------|------|------|
| **CC Switch** | [GitHub](https://github.com/farion1231/cc-switch) ・[官网](https://ccswitch.io) | 现象级跨平台桌面工具（Rust / Tauri，MIT，约 15 万 star）：一键切换 Claude Code、Codex、OpenCode、DeepSeek Harness 等的 API 供应商与配置，统一管理 MCP、Skills 与提示词 |
| claude-code-router | [GitHub](https://github.com/musistudio/claude-code-router) | 本地 Agent 控制面：把 Claude Code 等 Agent 的请求按场景路由到不同模型（DeepSeek、Gemini、OpenRouter 等），可扩展能力与工具编排 |
| claude-code-templates | [GitHub](https://github.com/davila7/claude-code-templates) | 一条命令安装 Claude Code 的 agents、命令、Hooks、MCP 与设置模板，附带监控面板 |

## 用量统计与状态栏

| 名称 | 链接 | 简介 |
|------|------|------|
| ccusage | [GitHub](https://github.com/ccusage/ccusage) | `npx ccusage` 读取本地日志，按日 / 月 / 会话统计 Claude Code、Codex 的 token 用量与费用，订阅党必备 |
| ccstatusline | [GitHub](https://github.com/sirmalloc/ccstatusline) | 高度可定制的 Claude Code 状态栏，支持 powerline 与主题，实时显示模型、上下文、费用等 |
| CCometixLine | [GitHub](https://github.com/Haleclipse/CCometixLine) | Rust 编写的 Claude Code 状态栏工具，轻量快速 |

## 多会话 / GUI / 移动端

| 名称 | 链接 | 简介 |
|------|------|------|
| Happy | [GitHub](https://github.com/slopus/happy) | 开源（MIT）手机 / 桌面客户端，在一个 App 里编排 Claude、Codex 与 Grok，复用你已有的订阅，可随时随地遥控本机会话 |
| KinetAios | [GitHub](https://github.com/phinn/KinetAios) ・[下载](https://github.com/phinn/KinetAios/releases) | 开源（GPL-3.0）Windows / macOS 桌面仪表盘：Claude Code 与 Codex 会话作为独立对话共存一窗，各自保留 CLI 会话续接（底层走官方 CLI），支持按会话切换模型、MCP 客户端与服务端、Skills、SQLite 本地历史全文检索，另含内置 ReAct 引擎可直连 API |
| CloudCLI（Claude Code UI） | [GitHub](https://github.com/siteboon/claudecodeui) | 在手机与网页上使用 Claude Code、OpenCode、Cursor CLI 与 Codex，远程管理会话和项目 |
| opcode（原 Claudia） | [GitHub](https://github.com/winfunc/opcode) | Claude Code 的桌面 GUI 与工具箱：自定义 agent、管理交互会话、运行后台 agent |
| Orca | [GitHub](https://github.com/stablyai/orca) | 管理一整队编码 Agent 的工作台，用自己的订阅运行任意编码 Agent，桌面与移动端可用（约 11 万 star） |
| claude-squad | [GitHub](https://github.com/smtg-ai/claude-squad) | 基于 tmux + git worktree 并行管理多个 Claude Code / Codex / OpenCode / Amp 终端会话 |
| ccmanager | [GitHub](https://github.com/kbwo/ccmanager) | 编码 Agent 会话管理器，支持 Claude Code、Gemini CLI、Codex CLI、Cursor Agent 等 |
| CodexMonitor | [GitHub](https://github.com/Dimillian/CodexMonitor) | 监控 Codex 任务运行状态的桌面小工具 |
| cc-connect | [GitHub](https://github.com/chenhg5/cc-connect) | 把 Claude Code / Codex 等接入微信、飞书、钉钉、Telegram 等聊天软件 |

## 工作流框架与方法论

| 名称 | 链接 | 简介 |
|------|------|------|
| **Superpowers** | [GitHub](https://github.com/obra/superpowers) | 2026 年最火的 Agent 技能框架与软件开发方法论（约 31 万 star）：头脑风暴 → 计划 → TDD → 子代理执行 → 评审 |
| **ECC** | [GitHub](https://github.com/affaan-m/ECC) | Agent harness 性能优化系统（约 29 万 star）：技能、本能、记忆、安全与研究优先开发，覆盖 Claude Code、Codex、OpenCode、Cursor |
| andrej-karpathy-skills | [GitHub](https://github.com/multica-ai/andrej-karpathy-skills) | 一份 CLAUDE.md，根据 Karpathy 对 LLM 编码常见坑的观察约束 Claude Code 的行为（约 23 万 star） |
| mattpocock/skills | [GitHub](https://github.com/mattpocock/skills) | TypeScript 名师 Matt Pocock 公开的个人 `.agents` 技能集（约 31 万 star） |
| Spec Kit | [GitHub](https://github.com/github/spec-kit) | GitHub 官方的规格驱动开发（SDD）工具包，先写 spec 再让 Agent 实现，支持 Claude Code、Codex、Copilot 等 |
| BMAD-METHOD | [GitHub](https://github.com/bmad-code-org/BMAD-METHOD) | 敏捷 AI 驱动开发方法：用分析师、PM、架构师、开发等多角色 Agent 走完整研发流程 |
| oh-my-claudecode | [GitHub](https://github.com/Yeachan-Heo/oh-my-claudecode) | 面向团队的 Claude Code 多智能体编排 |
| wshobson/agents | [GitHub](https://github.com/wshobson/agents) | 跨 harness 的 Agent 插件市场，适用于 Claude Code、Codex、Cursor、OpenCode、Copilot 等 |
| SuperClaude | [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 为 Claude Code 增加专用命令、认知角色与开发方法论的配置框架 |
| Archon | [GitHub](https://github.com/coleam00/Archon) | 开源 AI 编码 harness 构建器，让 AI 编码过程确定、可重复 |
| Claude Code Game Studios | [GitHub](https://github.com/Donchitos/Claude-Code-Game-Studios) | 把 Claude Code 变成游戏工作室：49 个 Agent、72 个工作流技能，模拟真实团队层级 |

## 热门技能与增强（2026 下半年）

| 名称 | 链接 | 简介 |
|------|------|------|
| claude-mem | [GitHub](https://github.com/thedotmack/claude-mem) | 跨会话持久记忆：自动记录 Agent 的操作并在新会话中注入相关上下文（约 11 万 star） |
| graphify | [GitHub](https://github.com/Graphify-Labs/graphify) | 把代码库连同文档、SQL schema、配置、PDF 变成可查询的知识图谱，以 `/graphify` 技能形式提供 |
| impeccable | [GitHub](https://github.com/pbakaus/impeccable) | 给编码 Agent 的设计词汇表：polish / bolder 调整、critique / audit 评审，拦住「AI 味」界面 |
| taste-skill | [GitHub](https://github.com/Leonxlnx/taste-skill) | 让编码 Agent 有「审美」：艺术指导、参考图与浏览器自检，告别千篇一律的 AI 页面 |
| hallmark | [GitHub](https://github.com/Nutlope/hallmark) | 反 AI slop 的设计技能，适用于 Claude Code、Cursor、Codex |
| security-audit-skill | [GitHub](https://github.com/cloudflare/security-audit-skill) | Cloudflare 开源的多阶段安全审计技能，输出经独立验证、机器可读的发现 |
| SkillSpector | [GitHub](https://github.com/NVIDIA/SkillSpector) | NVIDIA 开源的 Agent 技能安全扫描器：检测恶意模式、提示注入、数据外泄与供应链风险 |
| claude-seo | [GitHub](https://github.com/AgriciDaniel/claude-seo) | Claude Code 的 SEO 全家桶技能，含 26 个子技能与 19 个子代理 |

> 安装第三方技能 / 插件前，建议先用 SkillSpector 之类的工具扫描，或至少通读其脚本——技能可以执行任意命令。

## 学习资源

| 名称 | 链接 | 简介 |
|------|------|------|
| Claude Code Best Practices | [链接](https://www.anthropic.com/engineering/claude-code-best-practices) | Anthropic 官方最佳实践 |
| awesome-claude-code | [GitHub](https://github.com/hesreallyhim/awesome-claude-code) | 高人气 Claude Code 资源合集 |
| Codex 橙皮书 | [GitHub](https://github.com/bozhouDev/codex-orange-book) | 非官方 Codex 中文使用指南 |
| ai-guide | [GitHub](https://github.com/liyupi/ai-guide) | 鱼皮的中文 Vibe Coding 零基础教程，涵盖 Claude Code / Codex / Cursor |
