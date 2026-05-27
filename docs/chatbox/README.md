# Chatbox 资料包

生成日期：2026-05-04
来源快照：AnyChat `docs/chatbox-reference`
用途：为后续 Chatbox / BYOK AI 客户端 / Provider / RAG / MCP / 工具调用相关开发提供可检索参考。

## 清洗范围

已迁入：

- 官方文档仓库中对工程实现有长期参考价值的配置、功能、FAQ。
- Chatbox 源码仓库中已有的架构说明、Provider 注册、工具系统、存储迁移、RAG、Token 预估、测试策略。
- 少量由源码目录结构提炼的索引，便于后续按文件路径和关键字反查。

未迁入：

- `official-site/` 下的 HTML 页面快照和 sitemap，内容与 Markdown 文档高度重复。
- 图片、GIF、图标、安装包配置、lockfile、完整源码、测试样例文件。
- 隐私政策、用户协议、商务联系、价格订阅页等低工程复用价值内容。
- 上游源码全文。需要逐行对照时，回到 AnyChat 的 `docs/chatbox-reference/upstream-source/` 快照或上游仓库。

## 文档清单

- [资料源索引](source-index.md)：快照版本、来源、保留/剔除规则和查询词。
- [Chatbox AI OpenAI 兼容 API](official/openai-compatible-api.md)：第三方应用接入 Chatbox AI 的 host、key、模型与排错。
- [第三方 Provider 配置导入](official/provider-import-config.md)：JSON schema、Deep Link、校验边界。
- [本地与聚合模型 Provider 配置](official/local-and-gateway-providers.md)：OpenRouter、Ollama、LM Studio 配置要点。
- [知识库、联网、MCP 与快捷键](official/knowledge-web-mcp-faq.md)：官方能力入口、常见错误、数据存储说明。
- [Provider 注册表与模型系统](engineering/provider-registry-and-models.md)：`defineProvider()`、模型工厂、models.dev 富化、自建 Provider。
- [工具与集成系统](engineering/tools-and-integrations.md)：MCP、Web Search、文件读取、知识库工具、Agent Skills、工具注入。
- [存储迁移与新会话机制](engineering/storage-and-session.md)：跨平台存储、迁移策略、首页 `"new"` 临时会话。
- [RAG 与知识库实现线索](engineering/rag-and-knowledge-base.md)：文件解析、embedding、向量库、AI 工具调用。
- [Token 预估系统](engineering/token-estimation.md)：异步队列、缓存、throttle 持久化、React Query 集成。
- [测试策略与 Provider 导入用例](engineering/testing-and-provider-import-cases.md)：Vitest、mock server、Provider JSON 正反例。

## 推荐检索词

`Chatbox`, `ProviderDefinition`, `defineProvider`, `ModelProviderEnum`, `OpenAICompatible`, `models.dev`, `ProviderConfig`, `chatbox://provider/import`, `chatbox://mcp/install`, `MCP`, `web_search`, `parse_link`, `knowledge base`, `RAG`, `token estimation`, `newSessionStateAtom`, `DESKTOP_FILE`, `MOBILE_SQLITE`
