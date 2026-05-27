---
source_url: "https://github.com/chatboxai/chatbox/blob/b45fc528e6f6682656166d5d068f2f1b4907c405/docs/technical/tools-and-integrations.md"
---

# 工具与集成系统

来源：

- `upstream-source/docs/technical/tools-and-integrations.md`
- `upstream-source/docs/product/tools-and-integrations.md`
- `upstream-docs/guides/mcp.md`
- `upstream-docs/guides/lian-wang-mo-shi.md`

## 系统概览

Chatbox Pro 工具系统为 AI 模型提供外部能力调用。模型不仅生成文本，还能搜索网页、读取网页和文件、查询知识库、调用第三方 MCP 服务。

工具体系由三层组成：

| 层 | 位置 | 职责 |
| --- | --- | --- |
| MCP 服务器 | Main 进程 + Renderer 控制器 | 管理外部 MCP server，提供第三方工具 |
| 内置 Toolsets | `src/renderer/packages/model-calls/toolsets/` | 文件读取、知识库、Web Search 等 |
| Web Search 引擎 | `src/renderer/packages/web-search/` | 多搜索供应商抽象与执行 |

这些工具最终被合并为 Vercel AI SDK 的 `ToolSet`，在模型生成前注入。

## MCP 集成

MCP 支持两种传输：

| 传输 | 实现 | 适用 |
| --- | --- | --- |
| Stdio | Renderer 通过 Electron IPC 代理到 Main 进程，Main 管理子进程生命周期、stderr、编码 | 桌面端本地进程 |
| HTTP | Renderer 直接请求，优先 Streamable HTTP，失败降级 SSE | Web、移动端、远程服务 |

`mcpController` 是运行时管理中心：

- 根据配置启动、停止、更新 server。
- 配置变更时自动重连。
- 通过事件系统发布 idle / starting / running / stopping 状态。
- `getAvailableTools()` 合并所有运行中 server 的工具。
- 工具名格式为 `mcp__<serverName>__<toolName>`，避免冲突。
- 单个 MCP 工具执行失败时返回错误信息，不中断整个对话流程。

内置云端 MCP server：

| 服务 | 能力 |
| --- | --- |
| Fetch | 网页抓取与 HTML 转 Markdown |
| Sequential Thinking | 结构化推理辅助 |
| EdgeOne Pages | HTML 部署与公开 URL |
| arXiv | 论文检索 |
| Context7 | 库文档与代码示例检索 |

内置 server 连接 `mcp.chatboxai.app`，通过 `x-chatbox-license` 请求头认证。

## Web Search

Web Search 统一抽象为 `search(query, signal)` 和可选 `parseLink(url, signal)`。

| Provider | 搜索 | 读取网页 | 说明 |
| --- | --- | --- | --- |
| Chatbox Search | 支持 | 支持 | 内置搜索，读取网页需要 license |
| Bing | 支持 | 不支持 | 免费，国际覆盖 |
| Bing News | 支持 | 不支持 | 新闻专项，非中文环境自动启用 |
| Tavily | 支持 | 支持 | 调用 `/extract`，需用户 API Key |
| BoCha | 支持 | 不支持 | 国内搜索 API |
| Querit | 支持 | 不支持 | 多源聚合 |

`supportsParseLink` 由 provider 实例声明。`PROVIDERS_WITH_PARSE_LINK` 是静态单一数据源，同时供工具注入和设置 UI 使用。测试会断言静态集合与 provider 实例标志一致。

搜索执行流程：

1. 根据设置中的 `extensionSettings.webSearch.provider` 选择 provider。
2. 多 provider 并行搜索。
3. round-robin 合并结果，避免单一来源垄断。
4. 5 分钟 TTL 缓存重复查询。
5. 最多返回 10 条结果，每条摘要截断到约 150 字符。

## 内置 Toolsets

工具集导出结构：

```typescript
{ description: string, tools: ToolSet }
```

`description` 会注入系统提示词，引导模型正确使用工具。

文件工具：

- `read_file`：按行号范围读取，默认 200 行。
- `search_file_content`：按关键词搜索，支持上下文行。
- 小文件直接内联，大文件超过阈值后启用工具调用。

知识库工具：

- `query_knowledge_base`：语义搜索。
- `get_files_meta`：文件元数据。
- `read_file_chunks`：按块读取。
- `list_files`：分页列文件。

Web Search 工具：

- `web_search`：执行搜索。
- `parse_link`：读取网页。只有选中 provider 支持读取网页时才注入。

`parse_link` 执行分派：

| Provider | 执行路径 | 失败模式 |
| --- | --- | --- |
| Chatbox AI | 检查 `licenseKey`，调用 `remote.parseUserLinkPro` | 缺 license 抛 `chatbox_search_license_key_required` |
| Tavily | `getParseLinkProvider().parseLink()`，调用 Tavily `/extract` | 缺 key 抛 `tavily_api_key_required`，空结果抛 `parse_link_failed` |
| Bing / BoCha / Querit | 不注入 `parse_link` | 模型不可见该工具 |

## 工具错误渲染

工具错误走 AI / 用户双层结构：

- `Error.message` 给 AI 或内部推理使用，包含技术原因。
- `detail.i18nKey` 给用户显示本地化友好提示。

UI 路径：

```text
tool execute throws ChatboxAIAPIError
-> AI SDK tool-error chunk
-> stream-chunk-processor.ts 保存 result.error / result.errorCode
-> ToolCallPartUI error state 自动展开
-> ChatboxAIErrorMessage 渲染本地化错误和跳转按钮
```

## 工具构建与注入

工具在 AI 调用前动态组装，主要规则：

1. 检查模型是否支持 Tool Use。
2. 从 `mcpController.getAvailableTools()` 获取 MCP 工具。
3. 有附件且模型支持 read-file 时启用文件工具。
4. 会话启用网页浏览且模型支持 web-browsing 时启用 Web Search 工具。
5. 会话关联知识库且模型支持 knowledge-base 时启用知识库工具。
6. 合并各工具集 description 并注入系统提示词。

`buildToolsForSession()` 已封装工具组装逻辑，返回 `{ tools, instructions }`，由会话编排层调用。

## Agent Skills

Skills 沿用渐进披露模式：

1. 在 `instructions` 注入 `<available_skills>` 元数据。
2. 当模型支持 Tool Use 时注册 `load_skill`。
3. 模型命中场景后再加载完整 skill 指令。

这样避免每次请求注入全部 skill 正文造成 token 膨胀。

## Sandbox 工具集

Task 模式引入 Sandbox toolset，通过 Electron IPC 调用 Main 进程沙箱管理器。包含：

`sandbox_bash`, `sandbox_read`, `sandbox_write`, `sandbox_edit`, `sandbox_grep`, `sandbox_ls`, `sandbox_find`。

通过 `stream-text.ts` 的 `sandboxEnabled` 控制，只在 Task 会话启用，不影响普通 Chat 会话。

## 未完成方向

上游文档提到统一 `ToolRegistry` 仍未实现。目标是把 MCP、toolsets、Web Search 分散注册收敛为 shared 层统一接口，参考 Provider Registry 的 `defineProvider()` 模式。
