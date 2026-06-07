# 浏览器与计算机自动化（Browser / Computer Use）

让 AI Agent 像人一样操作浏览器与电脑，是 agentic 时代最关键的能力之一。**Browser Use** 指让 agent 自主操控浏览器完成网页任务；**Computer Use** 更进一步，让 agent 通过截图 + 鼠标键盘直接操作整台电脑。本章收录相关框架、为 agent 打造的浏览器基础设施、自动化 MCP、反检测方案、桌面操作 Agent 与评测基准。

> 相关：浏览器类 MCP Server 见 [MCP 指南](MCP.md)，理念见 [Agent-First](Agent_First.md)。

## Browser Use 浏览器操作 Agent（框架）

| 名称 | 链接 | 简介 |
|------|------|------|
| browser-use | [GitHub](https://github.com/browser-use/browser-use) | 当前最热门的浏览器 Agent 框架（Python，MIT），让 AI 直接操控浏览器完成网页任务 |
| Stagehand | [GitHub](https://github.com/browserbase/stagehand) | Browserbase 出品的"浏览器 Agent SDK"（TypeScript），融合自然语言与代码控制，带自愈与缓存 |
| Skyvern | [GitHub](https://github.com/Skyvern-AI/skyvern) | 用 LLM + 计算机视觉自动化网页工作流，提供 Playwright 兼容 SDK 与无代码流程编排 |
| Nanobrowser | [GitHub](https://github.com/nanobrowser/nanobrowser) | 开源 Chrome 扩展，定位 OpenAI Operator 的免费替代，多 Agent、本地运行、自带 API Key |
| LaVague | [GitHub](https://github.com/lavague-ai/LaVague) | 由 World Model + Action Engine 组成，将目标翻译为 Selenium/Playwright 可执行代码 |
| Agent-E | [GitHub](https://github.com/EmergenceAI/Agent-E) | EmergenceAI 出品，基于多 Agent 框架，用自然语言驱动浏览器自动化 |
| browser-use WebUI | [GitHub](https://github.com/browser-use/web-ui) | browser-use 官方的 Gradio 网页界面，支持多家 LLM、自定义浏览器与持久会话 |
| Notte | [GitHub](https://github.com/nottelabs/notte) | 主打速度、成本与可扩展性的网页 Agent 框架，支持结构化抽取 |
| Index (Laminar) | [GitHub](https://github.com/lmnr-ai/index) | 结合视觉推理 LLM 自主执行复杂网页任务的开源浏览器 Agent，提供 CLI 与 serverless API |
| Playwright（底层） | [GitHub](https://github.com/microsoft/playwright) | 微软出品，跨 Chromium/Firefox/WebKit 的统一自动化 API，常作为上层 Agent 的底层驱动 |
| Puppeteer（底层） | [GitHub](https://github.com/puppeteer/puppeteer) | Chrome 团队出品，通过 DevTools 协议控制浏览器的经典底层库 |

## Agent 浏览器基础设施（开源 / 云）

为 agent 提供开箱即用、可扩展、带反检测与会话管理的浏览器运行环境。

| 名称 | 链接 | 简介 |
|------|------|------|
| Steel / steel-browser | [GitHub](https://github.com/steel-dev/steel-browser) | 开源"为 Agent 打造的浏览器 API"，开箱即用浏览器沙箱，封装会话/代理/扩展/反检测，支持 Puppeteer/Playwright/Selenium |
| Browserbase | [官网](https://www.browserbase.com/) | 为 AI Agent 而生的云端浏览器基础设施（Stagehand 出品方） |
| Browserless | [官网](https://www.browserless.io/) | 远程 Chrome 服务，支持 Playwright/Puppeteer/Selenium，可自托管 |
| Hyperbrowser | [官网](https://www.hyperbrowser.ai/) | "Web Infra for AI Agents"，AI-first 的 serverless 浏览器，含 HyperAgent |
| Anchor Browser | [官网](https://anchorbrowser.io/) | 面向 Computer-Use Agent 的安全浏览器基础设施，fork Chromium 强化行为级反检测 |
| BrowserCat | [官网](https://www.browsercat.com/) | Headless 浏览器 API，"浏览器界的 OpenRouter"，一份脚本路由到托管后端 |

## 浏览器自动化 MCP

| 名称 | 链接 | 简介 |
|------|------|------|
| Chrome DevTools MCP（Google 官方） | [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp) | 官方 MCP，让编码 Agent 控制并检视真实 Chrome（性能分析、网络调试、自动化、截图），可对接 Claude/Copilot/Cursor/Gemini |
| Playwright MCP（微软官方） | [GitHub](https://github.com/microsoft/playwright-mcp) | 微软官方 Playwright MCP，基于可访问性树驱动真实浏览器，比截图方案更快更可靠 |
| Stagehand | [GitHub](https://github.com/browserbase/stagehand) | "浏览器 Agent SDK"，可与 MCP 生态集成 |

## 反检测 / 隐身浏览器（anti-bot / stealth）

| 名称 | 链接 | 简介 |
|------|------|------|
| CloakBrowser（官方） | [GitHub](https://github.com/CloakHQ/cloakbrowser) ・[官网](https://cloakbrowser.dev/) | 在 Chromium C++ 源码层打入多处指纹补丁的 Stealth Chromium，Playwright drop-in 替代品 |
| Camoufox | [GitHub](https://github.com/daijro/camoufox) | Firefox fork 的反检测浏览器，在实现层拦改指纹（navigator/WebGL/屏幕等），面向爬取与 Agent |

> ⚠️ **安全提醒**：GitHub 上存在多个冒名 "CloakBrowser" 的李鬼仓库（如 `SpikySituations/CloakBrowser` 等），盗用官方描述、README 实为诱导下载 exe 安装包的页面，疑似分发恶意软件。**请认准官方 `CloakHQ/CloakBrowser` 与官网 cloakbrowser.dev，切勿下载来路不明的 zip/exe。**

## Computer Use 计算机 / 桌面操作 Agent

让 Agent 通过"看屏幕 + 操作鼠标键盘"直接控制整台电脑。

| 名称 | 链接 | 简介 |
|------|------|------|
| Anthropic Computer Use（官方文档） | [文档](https://platform.claude.com/docs/en/docs/build-with-claude/computer-use) | Anthropic 官方 Computer Use 工具，让 Claude 通过截图 + 鼠标键盘控制桌面 |
| Anthropic 参考实现 | [GitHub](https://github.com/anthropics/claude-quickstarts) | 官方 quickstarts 仓库，含 `computer-use-demo` 让 Claude 控制桌面环境的参考实现 |
| OpenAI Operator / CUA | [公告](https://openai.com/index/computer-using-agent/) | OpenAI 的 Computer-Using Agent，结合视觉与强化学习像人一样操作 GUI；产品 Operator 已并入 ChatGPT Agent |
| UI-TARS | [GitHub](https://github.com/bytedance/UI-TARS) | 字节跳动开源的多模态 GUI Agent 视觉语言模型，覆盖桌面/移动/浏览器，在 OSWorld 等取得 SOTA |
| UI-TARS Desktop | [GitHub](https://github.com/bytedance/UI-TARS-desktop) | 字节出品，含 Agent TARS 框架与原生桌面应用，自然语言控制电脑 |
| Agent S | [GitHub](https://github.com/simular-ai/Agent-S) | simular-ai 开源 GUI Agent 框架，"像人一样使用电脑"，Agent S3 在 OSWorld 上表现突出 |
| cua | [GitHub](https://github.com/trycua/cua) | Computer-Use Agent 开源基础设施，提供沙箱、SDK 与基准，可操控 macOS/Linux/Windows 桌面 |
| OmniParser | [GitHub](https://github.com/microsoft/OmniParser) | 微软出品的屏幕解析工具，将 UI 截图解析为结构化元素，为纯视觉 GUI Agent 提供精准定位 |
| Self-Operating Computer | [GitHub](https://github.com/OthersideAI/self-operating-computer) | 早期框架，让多模态模型看屏幕并执行鼠标键盘操作 |
| Open Interpreter | [GitHub](https://github.com/OpenInterpreter/open-interpreter) | "计算机的自然语言接口"，让 LLM 在本地执行代码与操作电脑（执行前需确认） |

## AI 浏览器产品（消费级）

| 名称 | 链接 | 简介 |
|------|------|------|
| ChatGPT Atlas | [链接](https://openai.com/index/introducing-chatgpt-atlas/) | OpenAI 浏览器，含 Agent Mode 多步自主任务（先 macOS） |
| Perplexity Comet | [链接](https://www.perplexity.ai/comet) | Perplexity 的浏览器，每个标签页内嵌多模型助手 |
| Dia | [链接](https://www.diabrowser.com/) | The Browser Company（Arc 团队）的新一代 AI 浏览器，AI 作为浏览器底层 |
| Gemini in Chrome | [链接](https://www.google.com/chrome/) | Google 在 Chrome 内集成 Gemini，提供侧边栏与自主浏览能力 |

> 注：AI 浏览器产品的功能、定价与上线时间变动较快，请以官方为准。

## 评测基准

| 名称 | 链接 | 简介 |
|------|------|------|
| WebArena | [GitHub](https://github.com/web-arena-x/webarena) | 可自托管的真实网站仿真环境，评测自主网页 Agent（含多模态扩展 VisualWebArena） |
| WebVoyager | [GitHub](https://github.com/MinorJerry/WebVoyager) | 基于多模态大模型的网页 Agent 与基准，含 15 个真实网站、600+ 任务 |
| Mind2Web | [GitHub](https://github.com/OSU-NLP-Group/Mind2Web) | 首个通用网页 Agent 基准，覆盖 137 个网站、31 个领域、2000+ 任务 |
| OSWorld | [GitHub](https://github.com/xlang-ai/OSWorld) | 真实计算机环境中评测多模态 Agent 的开放式桌面任务基准 |
| AndroidWorld | [GitHub](https://github.com/google-research/android_world) | 运行在真实 Android 模拟器上的移动端 Agent 基准 |
| GAIA | [链接](https://huggingface.co/datasets/gaia-benchmark/GAIA) | 通用 AI 助手基准（含网页浏览任务），466 题分 3 个难度等级 |
