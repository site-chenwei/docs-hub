---
source_url: "https://github.com/chatboxai/chatbox/blob/b45fc528e6f6682656166d5d068f2f1b4907c405/docs/rag.md"
---

# RAG 与知识库实现线索

来源：

- `upstream-source/docs/rag.md`
- `upstream-docs/guides/knowledge-base.md`
- `upstream-source/src/main/knowledge-base/`
- `upstream-source/docs/technical/tools-and-integrations.md`

## 数据流

Chatbox 知识库的核心流程：

```text
用户导入文件
-> 文件解析
-> 文本切块
-> embedding
-> 向量存储
-> 会话关联知识库
-> AI 调用 query_knowledge_base / read_file_chunks
-> 结合检索结果回答
```

官方功能侧要求：

- 用户在设置里创建知识库。
- 创建时选择 embedding 模型。
- 可选重排模型，用于提升检索结果准确度。
- 可选视觉模型，用于图片文字提取入库。
- 会话输入框可以选择知识库。

## 文件解析

上游快照的 main 进程知识库路径：

| 文件 | 用途 |
| --- | --- |
| `src/main/knowledge-base/index.ts` | 知识库入口 |
| `src/main/knowledge-base/db.ts` | 本地数据库 |
| `src/main/knowledge-base/file-loaders.ts` | 文件加载 |
| `src/main/knowledge-base/remote-file-parser.ts` | 远程文件解析 |
| `src/main/knowledge-base/ipc-handlers.ts` | IPC handlers |
| `src/main/knowledge-base/model-providers.ts` | 模型提供方 |
| `src/main/knowledge-base/parsers/` | 本地 / Chatbox / MinerU parser |

官方 FAQ 明确复杂 PDF 可能因为本地解析限制失败。工程上应把解析失败作为可见错误处理，不应静默跳过。

## Embedding 与 rerank

文档中把模型角色拆成：

- embedding：把文本 chunk 转向量，是必需项。
- rerank：对召回结果重排，可选但能提高答案质量。
- vision：图片 OCR / 视觉抽取，可选。

工程启示：

- Provider 模型列表中 `type: 'embedding'` 和 `type: 'rerank'` 不应走聊天模型路径。
- 导入 Provider 配置时要保留 `ModelInfo.type`。
- 知识库设置页应按模型类型筛选候选模型。

## 向量存储

上游 `rag.md` 把 vector store 作为独立阶段。与 Chatbox 本地知识库结合时，关键是：

- 文档元数据和 chunk 内容要能按文件分页读取。
- 检索结果需要能追溯到文件和 chunk。
- 如果支持重排，需要保留初次召回集合和 rerank 后分数。

## AI 工具调用

知识库工具集位于 `src/renderer/packages/model-calls/toolsets/knowledge-base.ts`。向模型暴露：

| 工具 | 用途 |
| --- | --- |
| `query_knowledge_base` | 语义搜索 |
| `get_files_meta` | 获取文件元数据 |
| `read_file_chunks` | 按 chunk 读取文档 |
| `list_files` | 分页列文件 |

工具集 description 会动态包含知识库名称和文件列表，让模型理解可查询范围。

注入条件：

- 会话已经关联知识库。
- 模型支持 knowledge-base 能力。
- 工具构建阶段会合并知识库工具和对应 instructions。

## 与新会话机制的关系

首页新会话发送第一条消息前，知识库选择存储在 `newSessionStateAtom.knowledgeBase`。发送后需要转移到真实 session 的 `sessionKnowledgeBaseMap[newSession.id]`。

设计要点：

- 不要用 `"new"` 作为真实 session key 持久化知识库选择。
- 创建真实 session 成功后再转移临时知识库状态。
- 转移后清空临时状态，避免污染下一次新会话。

## 实现风险

- PDF / 图片解析失败要暴露给用户。
- embedding / rerank / vision 模型类型必须与 chat 模型隔离。
- 工具调用失败应进入统一 tool error UI，不要吞错。
- 知识库检索结果要有来源锚点，否则很难解释回答依据。
- 大文件读取需要分页或 chunk，避免一次性注入超长上下文。
