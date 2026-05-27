---
source_url: "https://github.com/chatboxai/chatbox/blob/b45fc528e6f6682656166d5d068f2f1b4907c405/docs/token-estimation.md"
---

# Token 预估系统

来源：`upstream-source/docs/token-estimation.md`

Token 预估系统用于异步计算聊天消息和附件的 token 数量，在不阻塞 UI 的情况下显示实时 token 统计。

## 架构

```text
React UI: InputBox, TokenCountMenu
-> useTokenEstimation hook
-> analyzer.ts
-> computation-queue.ts
-> task-executor.ts
-> result-persister.ts
-> chatStore.ts
-> storage / React Query cache
```

文件结构：

```text
src/renderer/packages/token-estimation/
├── index.ts
├── types.ts
├── hooks/useTokenEstimation.ts
├── analyzer.ts
├── computation-queue.ts
├── task-executor.ts
├── result-persister.ts
├── tokenizer.ts
├── cache-keys.ts
└── __tests__/
```

## useTokenEstimation

UI 入口 Hook 返回：

- `totalTokens`
- `contextTokens`
- `currentInputTokens`
- `isCalculating`
- `pendingTasks`
- `breakdown`

职责：

- 分析当前输入和历史消息。
- 将待计算任务加入队列。
- 订阅队列状态。
- session 切换时取消旧 session 任务。

## Analyzer

`analyzer.ts` 检查消息和附件是否已有 token 缓存：

- 已缓存：直接累加结果。
- 未缓存：生成 `ComputationTask`。

缓存位于消息或附件的 `tokenCountMap`，并记录 `tokenCalculatedAt`。

示例字段：

```typescript
type TokenCountMap = {
  tiktoken?: number
  tiktoken_preview?: number
  deepseek?: number
  deepseek_preview?: number
}
```

## Computation Queue

队列特性：

- 优先级调度。
- `taskId` 去重。
- 并发控制，`maxConcurrency = 1`。
- session 级取消。

优先级：

| 任务 | 优先级 |
| --- | --- |
| 当前输入文本 | `0` |
| 当前输入附件 | `1` |
| 历史消息文本 | `10` |
| 历史消息附件 | `11` |

这样可以先保证用户当前正在看的输入统计更新。

## Task Executor

`task-executor.ts` 负责：

- 读取消息文本。
- 读取附件内容。
- 调用 tokenizer 计算。
- 将结果交给 `resultPersister`。

Tokenizer 支持：

- tiktoken：OpenAI 模型，例如 `cl100k_base`、`o200k_base`。
- DeepSeek tokenizer：DeepSeek 模型专用。

## Result Persister

结果持久化使用 throttle，而不是 debounce。

原因：

- 大量任务连续完成时，debounce 会不断重置计时器，可能长时间不 flush。
- throttle 保证每秒至少 flush 一次，让用户持续看到中间进度。

关键参数：

```typescript
private throttleMs = 1000
```

`result-persister.ts` 批量调用 `chatStore.updateMessages(sessionId, updater)`，把 token 结果写回消息或附件。

## React Query 集成

`chatStore.updateMessages()` 内部直接更新 React Query 缓存：

```typescript
queryClient.setQueryData(QueryKeys.ChatSession(sessionId), updated)
```

这里不使用 `invalidateQueries`，避免不必要的重新获取。

## 初始化

应用启动时初始化：

```typescript
setResultPersister(resultPersister)
initializeExecutor()
computationQueue.startCleanup()
```

## 调试

开发环境可通过 `window.__tokenEstimation` 访问调试工具。

## 常见问题

| 问题 | 排查方向 |
| --- | --- |
| token 数显示为 0 | 是否未初始化 executor / persister、是否没有可用 tokenizer、缓存 key 是否不匹配 |
| 计算很慢 | 检查附件大小、队列堆积、当前模型 tokenizer |
| 新 tokenizer 接入 | 更新 tokenizer 选择逻辑、cache key、测试 |
| 切换 session 后状态错乱 | 检查 session cancel、队列订阅和 pending task 清理 |

## 工程约束

- 当前输入优先级必须高于历史消息。
- session 切换要取消旧任务，避免跨 session 写回。
- 持久化应节流，不要每个 task 完成后立即写存储。
- token 缓存 key 必须区分 tokenizer 和 preview 模式。
- 附件 token 与消息 token 都要可缓存，否则大文件会反复计算。
