---
source_url: "https://github.com/chatboxai/chatbox-docs/blob/e1052931c02d4686c93f7c6b4ece4df229b83e9e/guides/knowledge-base.md"
---

# 知识库、联网、MCP 与 FAQ

来源：

- `upstream-docs/guides/knowledge-base.md`
- `upstream-docs/guides/lian-wang-mo-shi.md`
- `upstream-docs/guides/mcp.md`
- `upstream-docs/guides/shortcuts.md`
- `upstream-docs/faq/faq/*.md`

## 本地知识库

Chatbox `1.15` 推出本地知识库。用户在设置中创建知识库、导入文档，处理完成后可在对话输入框选择知识库进行问答。

创建知识库时需要选择模型：

| 模型 | 用途 |
| --- | --- |
| 嵌入模型 | 将文档转换为向量 |
| 重排模型 | 可选，提高搜索结果准确度 |
| 视觉模型 | 可选，用于图片文字提取入库 |

导入文档时，复杂 PDF 可能因本地解析限制失败。官方建议用专业工具先提取文本，或跳过失败文件继续导入其他文件。

## 联网模式

联网搜索在「拓展」中配置服务商。

| 服务商 | 说明 |
| --- | --- |
| Chatbox | 供 Chatbox AI 订阅用户使用。使用其他模型服务提供商时，不应选择该项。 |
| Bing | 用 Bing 作为联网问答信息来源 |
| Tavily | 需要用户自行配置 Tavily API Key |

## MCP

Chatbox `1.14` 推出 MCP 支持。入口是设置页的 MCP 页面，用户可以手动添加服务器，也可以从内置列表选择。

MCP deep link 格式：

```text
chatbox://mcp/install?server=$BASE64_ENCODED_CONFIG
```

Stdio 配置示例：

```json
{
  "name": "fetch",
  "command": "npx",
  "args": ["fetch-mcp"],
  "env": {}
}
```

HTTP 配置示例：

```json
{
  "name": "deepwiki",
  "url": "https://mcp.deepwiki.com/mcp"
}
```

生成一键安装链接时，先 `JSON.stringify` MCP server 配置，再 base64 编码，最后拼到 `chatbox://mcp/install?server=` 后面。

## 快捷键

| 操作 | macOS | Windows / Linux |
| --- | --- | --- |
| 显示或隐藏应用窗口 | `Option + \`` | `Alt + \`` |
| 下一条对话 | `Command + Tab` | `Ctrl + Tab` |
| 上一条对话 | `Command + Shift + Tab` | `Ctrl + Shift + Tab` |
| 指定对话 | `Command + 1/2/3...` | `Ctrl + 1/2/3...` |
| 新建对话 | `Command + N` | `Ctrl + N` |
| 新建图像创造者对话 | `Command + Shift + N` | `Ctrl + Shift + N` |
| 聚焦输入框 | `Command + I` | `Ctrl + I` |
| 发送 | `Enter` | `Enter` |
| 输入框换行 | `Shift + Enter` | `Shift + Enter` |
| 发送但不生成回复 | `Command + Enter` | `Ctrl + Enter` |
| 刷新上下文，新线程 | `Option + R` | `Alt + R` |
| 搜索对话框 | `Command + K` | `Ctrl + K` |

## 常见错误代码

| 错误码 | 常见含义 | 排查方向 |
| --- | --- | --- |
| 400 | 请求语法、参数或格式错误 | 检查请求参数 |
| 401 | 未授权，鉴权或认证失败 | 检查登录凭证和 API Key |
| 403 | 权限不足 | 检查账户权限 |
| 404 | 资源不存在 | 检查请求路径 |
| 429 | 访问次数或限流问题 | 检查实名、额度、调用频率 |
| 500 | 服务端内部错误 | 检查服务端日志 |
| 502 | 网关收到无效上游响应 | 检查上游服务 |
| 503 | 服务过载或维护 | 等待恢复或扩容 |

## 数据存储与隐私口径

- 聊天消息和设置数据默认存储在用户设备上。
- 使用 Chatbox AI 模型服务时，消息、上下文、上传图片或文件会发送到 Chatbox AI 服务用于生成回复。
- 官方 FAQ 表述为 Chatbox AI 不会永久存储这些数据，也不会用于广告、模型训练或其他商业用途。
- 使用第三方 API 服务时，数据隐私和安全取决于第三方服务条款。

## 模型身份 FAQ

直接问模型「你是什么模型」不是可靠验证方式。模型可能基于训练语料猜测身份，系统提示词也可能影响回答。

更可靠的验证方式：

- 使用标准化 benchmark 或第三方评测工具。
- 对比模型实际能力表现。
- 观察模型在推理、代码、格式偏好等方面的特征性行为。
