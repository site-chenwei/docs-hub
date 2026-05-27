---
source_url: "https://github.com/chatboxai/chatbox-docs/blob/e1052931c02d4686c93f7c6b4ece4df229b83e9e/chatbox-ai-premium/openai-compatible-api.md"
---

# Chatbox AI OpenAI 兼容 API

来源：`upstream-docs/chatbox-ai-premium/openai-compatible-api.md`

Chatbox AI 提供 OpenAI 兼容接口，第三方客户端只要支持 OpenAI API 或自定义 base URL，就可以接入 Chatbox AI。

## 基本配置

| 配置项 | 值 |
| --- | --- |
| API Host | `https://ai.chatboxai.app` |
| OpenAI Base URL | `https://ai.chatboxai.app/v1` |
| API Key | Chatbox AI License Key |

获取 key 的官方流程：

1. 登录 Chatbox AI 账户。
2. 进入 Dashboard。
3. 复制 License Key。

## 常见第三方客户端配置

| 客户端 | 关键配置 |
| --- | --- |
| Cursor | OpenAI API Key 填 License Key，Override OpenAI Base URL 填 `https://ai.chatboxai.app/v1` |
| Continue | `provider: "openai"`，`apiBase: "https://ai.chatboxai.app/v1"`，`apiKey` 填 License Key |
| Cherry Studio | 新增 OpenAI API 类型服务商，API 地址填 `https://ai.chatboxai.app/v1` |
| Open WebUI | Connections / OpenAI API 中配置 API Base URL 和 API Key |
| 其他 OpenAI API 兼容应用 | 找 OpenAI API 或自定义 API 配置项，填 base URL、key、模型名 |

Continue 配置示例：

```json
{
  "models": [
    {
      "title": "Chatbox AI",
      "provider": "openai",
      "model": "gemini-3-pro",
      "apiKey": "your-chatbox-license-key",
      "apiBase": "https://ai.chatboxai.app/v1"
    }
  ]
}
```

## 官方快照中的模型名

高级模型，Pro / Pro+：

- `gpt-5`
- `claude-4.5-sonnet`
- `gemini-3-pro`

标准模型，所有付费方案：

- `deepseek-chat`
- `deepseek-reasoner`
- `deepseek-v3.2`
- `kimi-k2`
- `gpt-5-mini`
- `gemini-2.5-flash`

模型名称可能随官网更新。使用本地快照做工程设计时可以参考这些字段，但上线前应以当前 Chatbox AI 官网为准。

## 排错

| 问题 | 检查项 |
| --- | --- |
| API 请求失败 | API Key 是否正确、base URL 是否为 `https://ai.chatboxai.app/v1`、订阅是否有效 |
| 模型不可用 | 当前订阅是否支持该模型、模型名称是否拼写正确 |
| 点数消耗异常 | API 接入与 Chatbox 客户端使用同一账户点数，排查账户计费和调用频率 |

## 工程参考

- 若要把 Chatbox AI 作为内置 Provider，优先把 License Key 与普通 API Key 分层处理。
- UI 上应明确区分 API Host `https://ai.chatboxai.app` 与 OpenAI Base URL `https://ai.chatboxai.app/v1`。
- 对 OpenAI 兼容客户端，常见失败多来自 base URL 少 `/v1`、key 复制错误、订阅权限不足。
