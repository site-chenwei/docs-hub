---
source_url: "https://github.com/chatboxai/chatbox"
---

# Chatbox 资料源索引

## 快照基线

本资料包清洗自 AnyChat 项目内的 `docs/chatbox-reference` 快照。

| 来源 | 快照版本 |
| --- | --- |
| `chatboxai/chatbox` 源码仓库 | `main` at `b45fc528e6f6682656166d5d068f2f1b4907c405` |
| `chatboxai/chatbox-docs` 官方文档仓库 | `main` at `e1052931c02d4686c93f7c6b4ece4df229b83e9e` |
| GitHub Release 元数据 | `v1.20.1`, published at `2026-04-09T03:25:01Z` |
| 抓取时间 | `2026-05-04T13:03:45Z` |

## 官方来源

- 源码仓库：<https://github.com/chatboxai/chatbox>
- 官方文档仓库：<https://github.com/chatboxai/chatbox-docs>
- 官网：<https://chatboxai.app/en/>
- 官方文档站点：<https://docs.chatboxai.app>

## 本地原始快照入口

- AnyChat 快照说明：`/Users/bill/WorkSpace/AnyChat/docs/chatbox-reference/README.md`
- 来源清单：`/Users/bill/WorkSpace/AnyChat/docs/chatbox-reference/SOURCE-MANIFEST.md`
- 官方文档 Markdown：`/Users/bill/WorkSpace/AnyChat/docs/chatbox-reference/upstream-docs/`
- 源码仓库文档：`/Users/bill/WorkSpace/AnyChat/docs/chatbox-reference/upstream-source/docs/`
- 源码 README / FAQ：`/Users/bill/WorkSpace/AnyChat/docs/chatbox-reference/upstream-source/doc/`
- Provider 导入手工用例：`/Users/bill/WorkSpace/AnyChat/docs/chatbox-reference/upstream-source/test/cases/provider-config-import-manual-test.md`

## 清洗原则

- 保留 Markdown 中对架构、协议、配置、运行边界、排错和测试有复用价值的内容。
- 优先保留中文官方文档；英文重复文档不再单独迁入。
- HTML 快照、图片资源、完整源码、lockfile、构建配置不进入 docs-hub。
- 文档内容是快照摘要，不是在线最新版。需要判断当前上游状态时，重新查官方仓库或刷新快照。

## 重点源码锚点

| 主题 | 上游快照路径 |
| --- | --- |
| Provider registry | `upstream-source/src/shared/providers/registry.ts` |
| Provider 入口 side-effect import | `upstream-source/src/shared/providers/index.ts` |
| Provider definition | `upstream-source/src/shared/providers/definitions/*.ts` |
| Provider model class | `upstream-source/src/shared/providers/definitions/models/*.ts` |
| 自建 Provider model | `upstream-source/src/shared/providers/custom.ts` 和 `definitions/models/custom-*.ts` |
| models.dev 映射 | `upstream-source/src/shared/model-registry/provider-mapping.ts` |
| models.dev 富化 | `upstream-source/src/shared/model-registry/enrich.ts` |
| Web Search | `upstream-source/src/renderer/packages/web-search/` |
| Toolsets | `upstream-source/src/renderer/packages/model-calls/toolsets/` |
| 会话工具构建 | `upstream-source/src/renderer/stores/session/tools-builder.ts` |
| 知识库 main 进程 | `upstream-source/src/main/knowledge-base/` |
| Token 预估 | `upstream-source/src/renderer/packages/token-estimation/` |
| 存储迁移 | `upstream-source/src/renderer/stores/migration.ts` |

## 查询建议

- Provider 架构：`defineProvider ProviderDefinition ModelProviderEnum createModel modelsDevProviderId curatedModelIds`
- 自建 Provider：`custom provider id unique apiHost apiPath ProviderConfig chatbox provider import`
- 模型富化：`models.dev registry contextWindow maxOutput capabilities prefix match`
- 工具调用：`web_search parse_link MCP toolsets buildToolsForSession ChatboxAIAPIError`
- 知识库：`knowledge base embedding rerank vector store query_knowledge_base`
- 会话与存储：`newSessionStateAtom sessionKnowledgeBaseMap DESKTOP_FILE INDEXEDDB MOBILE_SQLITE migration`
- Token 预估：`useTokenEstimation computationQueue ResultPersister tokenCountMap throttle`
