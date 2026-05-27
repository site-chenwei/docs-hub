---
source_url: "https://github.com/chatboxai/chatbox/blob/b45fc528e6f6682656166d5d068f2f1b4907c405/docs/technical/ai-providers.md"
---

# Provider 注册表与模型系统

来源：

- `upstream-source/docs/technical/ai-providers.md`
- `upstream-source/docs/adding-new-provider.md`
- `upstream-source/docs/adding-provider.md`
- `upstream-source/src/shared/providers/definitions/*.ts`

## 总览

Chatbox 的 AI Provider 系统负责对接 OpenAI、Claude、Gemini、DeepSeek、Groq、Ollama、OpenRouter 等模型服务商。当前上游文档描述的是注册表模式，核心是 `defineProvider()`。

设计目标：

- 单一数据源：Provider 的 ID、名称、API 类型、默认配置、模型工厂集中到一个 definition。
- 可扩展：新增内置 Provider 主要改 enum、model class、definition、side-effect import。
- 关注点分离：Provider definition 与具体模型实现解耦。

## 注册表机制

注册表位于 `src/shared/providers/registry.ts`，维护 `Map<string, ProviderDefinition>`。

| API | 用途 |
| --- | --- |
| `defineProvider(def)` | 注册 Provider definition |
| `getProviderDefinition(id)` | 按 ID 获取 Provider definition |
| `getAllProviders()` | 获取所有 Provider |
| `getSystemProviders()` | 获取 UI 使用的 Provider 基础信息 |

注册依赖 side-effect import。`src/shared/providers/index.ts` 导入每个 `definitions/*.ts`，模块加载时执行 `defineProvider()`。导入顺序决定 UI 展示顺序，ChatboxAI 保持首位。

## ProviderDefinition 字段

| 字段 | 必填 | 说明 |
| --- | --- | --- |
| `id` | 是 | Provider 唯一 ID，对应 `ModelProviderEnum` |
| `name` | 是 | UI 展示名称 |
| `type` | 是 | API 类型，如 `OpenAI`、`Claude`、`Gemini`、`OpenAIResponses`、`ChatboxAI` |
| `urls` | 否 | 官网、API Key、文档、模型列表等链接 |
| `defaultSettings` | 否 | 默认 API host、模型列表、模型能力 |
| `modelsDevProviderId` | 否 | models.dev 中的 Provider ID，用于模型元数据富化 |
| `curatedModelIds` | 否 | 默认策展模型列表，通常与 `modelsDevProviderId` 配套 |
| `createModel` | 是 | 由 settings、providerSetting、model、dependencies 创建模型实例 |
| `getDisplayName` | 否 | 自定义消息头展示名称 |

`createModel(config)` 可读取：

- `settings`：会话级 temperature、topP、maxTokens、stream 等。
- `globalSettings`：全局设置，如 Chatbox AI license。
- `providerSetting`：Provider API Key、apiHost、models 等。
- `formattedApiHost`：格式化后的 host。
- `model`：选中的模型信息。
- `dependencies`：平台依赖，如 fetch。

## 模型实例化流程

`getModel()` 是统一入口：

1. 根据 session setting 中的 `provider` ID 查找 Provider registry。
2. 找到内置 Provider 时，调用 `providerDefinition.createModel(config)`。
3. 未找到时，检查是否为用户自建 Provider，通过 custom provider model 创建。
4. 都未匹配时抛错。

## 控制面优先级

| 决策 | 优先级 |
| --- | --- |
| Provider 路由 | session setting 的 `provider` 是唯一来源 |
| Provider definition | 内置 registry 优先，其次 custom provider |
| 自定义 Provider ID | 必须全局唯一，不允许与 builtin 同 ID |
| OAuth 凭证 | provider-local settings 优先，其次 shared OAuth settings |
| `activeAuthMode` | provider-local settings 优先，其次 defaults |
| `apiHost` / `apiPath` | provider settings 优先，其次 provider defaults |
| effective API key | desktop OAuth token 优先，其次 provider settings `apiKey` |
| model list | user-saved models、后端 manifest / provider API、curated registry fallback |
| capability / context / maxOutput | models.dev registry 覆写本地数据 |

关键约束：

- builtin 与 custom Provider 不能同 ID。
- OAuth 可以共享凭证，但不共享认证模式，例如 `openai-responses -> openai` 只复用 token。
- Provider definition 不直接决定消息流或 UI 交互细节，只提供 contract、默认配置和实例工厂。

## models.dev 模型注册表

Chatbox 使用 `models.dev` 为内置 Provider 的模型提供能力、上下文窗口、最大输出、新模型发现等元数据。

| 层 | 路径 | 职责 |
| --- | --- | --- |
| shared | `src/shared/model-registry/` | Provider ID 映射、模型匹配、富化、类型转换 |
| renderer | `src/renderer/packages/model-registry/` | 网络请求、多级缓存、订阅、兼容 API |

缓存优先级：

```text
内存缓存 -> 平台 Blob 存储 -> 构建时快照
```

关键 API：

| API | 用途 |
| --- | --- |
| `getRegistrySync()` | 同步读取内存或构建时快照 |
| `getRegistry()` | 异步读取缓存或网络 |
| `prefetchModelRegistry()` | 启动后台预加载 |
| `forceRefreshRegistry()` | 用户点击获取模型时强制刷新 |
| `fetchAndUpdateRegistry()` | 从 `https://models.dev/api.json` 获取数据，15s 超时，并发去重 |

模型匹配规则：

1. 大小写不敏感的精确匹配。
2. 边界感知前缀匹配，取最长 key，要求后续字符是 `-`、`:`、`.` 或字符串结束。

富化策略：

| 字段 | 策略 |
| --- | --- |
| `capabilities` | registry 覆写 |
| `contextWindow` | registry 覆写 |
| `maxOutput` | registry 覆写 |
| `nickname` | 仅缺失时填充 |
| `type` | 仅缺失时填充 |

## 新增 Provider 当前推荐路径

注册表架构下新增内置 Provider：

1. 在 `src/shared/types.ts` 的 `ModelProviderEnum` 增加 Provider ID。
2. 新建 model class，例如 `src/shared/providers/definitions/models/your-provider.ts`。
3. 新建 definition，例如 `src/shared/providers/definitions/your-provider.ts`。
4. 在 `src/shared/providers/index.ts` 增加 side-effect import。
5. 可选：在 `ProviderIcon.tsx` 增加 Provider 图标。

OpenAI 兼容 Provider 通常继承 `OpenAICompatible`；非兼容 API 继承 `AbstractAISDKModel` 并实现 `streamText()`、`callChatCompletion()`，必要时实现模型能力检测。

## 内置 Provider 快照

快照中 `src/shared/providers/definitions/` 包含：

`azure`, `bedrock`, `chatboxai`, `chatglm`, `claude`, `deepseek`, `gemini`, `groq`, `lmstudio`, `minimax`, `mistral-ai`, `moonshot`, `ollama`, `openai`, `openai-responses`, `openrouter`, `perplexity`, `qwen`, `qwen-portal`, `siliconflow`, `volcengine`, `xai`。

## 契约测试

Provider / model registry 相关不变量由测试锁定：

- Provider ID 全局唯一。
- models.dev 映射一致。
- 策展模型覆盖。
- 按 Provider 隔离模型查找。
- 前缀匹配行为。
- fetch 失败时保留已有缓存。
- 并发请求去重。

## 迁移注意

上游同时保留过旧版 `adding-provider.md`。旧路径依赖 switch / factory / setting-util 分散改动；当前应优先参考注册表架构，不要在新实现中恢复分散 switch 逻辑。
