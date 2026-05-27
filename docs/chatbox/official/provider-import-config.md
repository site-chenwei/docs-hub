---
source_url: "https://github.com/chatboxai/chatbox-docs/blob/e1052931c02d4686c93f7c6b4ece4df229b83e9e/guides/providers/import-config.md"
---

# 第三方 Provider 配置导入

来源：

- `upstream-docs/guides/providers/import-config.md`
- `upstream-source/test/cases/provider-config-import-manual-test.md`

Chatbox 从 `1.15.1` 开始支持导入 JSON 格式的模型提供方配置。配置可以手动复制导入，也可以通过 deep link 一键导入客户端。

## ProviderConfig schema

```typescript
type ProviderConfig = {
  id: string
  name: string
  type: 'openai'
  iconUrl: string
  urls: {
    website: string
    getApiKey?: string
    docs?: string
    models?: string
  }
  settings: {
    apiHost: string
    apiPath?: string
    apiKey?: string
    models: ModelInfo[]
  }
}

type ModelInfo = {
  modelId: string
  nickname?: string
  type?: 'chat' | 'embedding' | 'rerank'
  capabilities?: ('vision' | 'reasoning' | 'tool_use')[]
  contextWindow?: number
  maxOutput?: number
}
```

字段含义：

| 字段 | 说明 |
| --- | --- |
| `id` | Provider 唯一 ID，建议使用域名或稳定短名 |
| `name` | UI 展示名称 |
| `type` | 官方文档快照中仅支持 `openai` |
| `iconUrl` | Provider 图标 URL |
| `urls.website` | 官网 |
| `urls.getApiKey` | 获取 API Key 的页面 |
| `urls.docs` | 文档页面 |
| `urls.models` | 模型列表页面 |
| `settings.apiHost` | API host，例如 `https://api.openai.com` |
| `settings.apiPath` | 可选 API path，默认 `/v1/chat/completions` |
| `settings.apiKey` | 可选，用户也可以导入后在界面填写 |
| `settings.models` | 默认展示模型列表 |

## 示例

```json
{
  "id": "openai",
  "name": "OpenAI",
  "type": "openai",
  "iconUrl": "https://openai.com/favicon.ico",
  "urls": { "website": "https://openai.com" },
  "settings": {
    "apiHost": "https://api.openai.com/",
    "models": [
      {
        "modelId": "gpt-4o",
        "nickname": "GPT 4o",
        "type": "chat",
        "capabilities": ["vision", "tool_use"],
        "contextWindow": 128000,
        "maxOutput": 16384
      },
      {
        "modelId": "text-embedding-3-small",
        "type": "embedding"
      }
    ]
  }
}
```

## Deep Link

```text
chatbox://provider/import?config=$BASE64_ENCODED_CONFIG
```

`BASE64_ENCODED_CONFIG` 是 Provider JSON 配置经过 base64 编码后的字符串。

## 手工测试覆盖

上游测试样例覆盖以下路径：

| 类别 | 覆盖点 |
| --- | --- |
| 有效配置 | 完整自定义 Provider、最小有效配置、内置 Provider 配置、OpenRouter 实例、embedding / rerank 模型、base64 deep link |
| 无效配置 | 缺少 `name`、缺少 `type`、非法 `type`、非法 capability、JSON 格式错误 |
| 边界配置 | 重复 Provider ID、Anthropic 类型 Provider |

## 工程约束

- 导入必须 fail-loud，不能把非法 JSON 或缺字段配置静默吞掉。
- `customProviders[].id` 不能与内置 Provider ID 冲突，否则运行时路由、设置主键和 OAuth 共享键会产生歧义。
- capability 只能接受明确枚举：`vision`、`reasoning`、`tool_use`。
- `embedding`、`rerank` 模型应与 chat 模型分开展示和调用，不要默认走聊天补全路径。
- deep link 只解决配置传递，实际 API Key、host、model 仍需要导入后校验。
