---
source_url: "https://github.com/chatboxai/chatbox/blob/b45fc528e6f6682656166d5d068f2f1b4907c405/docs/testing.md"
---

# 测试策略与 Provider 导入用例

来源：

- `upstream-source/docs/testing.md`
- `upstream-source/test/cases/provider-config-import-manual-test.md`

## 测试基础设施

上游快照使用：

| 工具 | 用途 |
| --- | --- |
| Vitest | ESM 优先的 TypeScript test runner |
| `@ai-sdk/provider-utils/test` | AI Provider mock server |
| Testing Library | React 组件测试 |

Vitest 配置要点：

```typescript
test: {
  globals: true,
  environment: 'node',
  env: { NODE_ENV: 'test' },
  include: ['src/**/*.{test,spec}.{ts,tsx}'],
  exclude: ['node_modules', 'dist', 'release', '.erb'],
}
```

命令：

- `npm run test`
- `npm run test:watch`
- `npm run test:ui`
- `npm run test:coverage`

## 已有覆盖

| 模块 | 覆盖点 |
| --- | --- |
| AI Provider adapters | OpenAI streaming、tool calls、rate limit、network errors、消息格式转换 |
| shared utils | API URL normalize、消息排序合并、content parts |
| renderer content | base64 image、LaTeX、Provider config parsing |
| message utils | role 顺序、空消息过滤、多 part 合并、图片内容 |

待补高优先级：

- Data storage layer。
- Session management。
- Settings management。

## Mock Server 模式

AI Provider 测试使用真实 fetch + mock server，不优先 mock 内部模块。

```typescript
import { createTestServer } from '@ai-sdk/provider-utils/test'

const server = createTestServer({
  'https://api.openai.com/v1/chat/completions': {
    headers: { 'Content-Type': 'text/event-stream' },
    chunks: [
      'data: {"id":"1","object":"chat.completion.chunk","choices":[{"delta":{"content":"Hello"}}]}\n\n',
      'data: [DONE]\n\n'
    ]
  }
})
```

需要多次请求不同响应时使用 `callNumber`。

测试规范：

- test 文件与源码相邻，命名 `.test.ts`。
- 测试名描述预期行为。
- async 操作必须 await。
- `afterEach` 做清理。
- 测试代码避免 `any`。
- 测试环境下可抑制 console 噪声。

## Provider 导入有效用例

上游手工用例建议覆盖：

| 用例 | 重点 |
| --- | --- |
| 完整自定义 Provider | `id/name/type/iconUrl/urls/settings/models` 全字段 |
| 最小自定义 Provider | 只保留必需字段 |
| 内置 Provider 配置 | 导入内置 ID 时的覆盖和冲突语义 |
| OpenRouter 实例 | 聚合 Provider 的模型 ID、host、key 格式 |
| embedding / rerank 模型 | `ModelInfo.type` 非 chat |
| base64 deep link | `chatbox://provider/import?config=` 解码 |

## Provider 导入失败用例

必须 fail：

- 缺少 `name`。
- 缺少 `type`。
- `type` 不是支持值。
- capability 不在允许列表。
- JSON 格式错误。

边界：

- 重复 Provider ID。
- Anthropic 或其他非 OpenAI 类型配置。

## Provider JSON 验证建议

导入时至少验证：

- 顶层是 object，不是 array / null / primitive。
- `id`、`name`、`type`、`settings.apiHost` 是非空字符串。
- `type` 当前只接受明确支持的协议。
- `settings.models` 是非空数组。
- 每个 model 有非空 `modelId`。
- `model.type` 只能是 `chat`、`embedding`、`rerank` 或缺省。
- `capabilities[]` 只能是 `vision`、`reasoning`、`tool_use`。
- URL 字段如果存在，应是可解析 URL。

## 回归重点

Provider 导入功能很容易影响设置页、模型选择、运行时调用、deep link 路由。回归至少覆盖：

- 导入成功后 Provider 出现在设置页。
- API Key / host 可以编辑和持久化。
- chat、embedding、rerank 模型不会互相污染。
- 无效配置给出可见错误。
- deep link 解码失败和 JSON 验证失败路径清晰。
- 不允许 builtin / custom ID 冲突静默通过。
