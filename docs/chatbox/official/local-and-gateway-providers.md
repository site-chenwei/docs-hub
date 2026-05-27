---
source_url: "https://github.com/chatboxai/chatbox-docs/blob/e1052931c02d4686c93f7c6b4ece4df229b83e9e/guides/providers/ollama.md"
---

# 本地与聚合模型 Provider 配置

来源：

- `upstream-docs/guides/providers/openrouter.md`
- `upstream-docs/guides/providers/ollama.md`
- `upstream-docs/guides/providers/lm-studio.md`

## OpenRouter

OpenRouter 是统一模型网关，使用单一 API Key 访问多家模型提供商。

配置步骤：

1. 到 OpenRouter 创建 API Key，常见格式为 `sk-or-v1-...`。
2. 在 Chatbox 设置页选择 `OpenRouter` Provider。
3. 填入 API Key。
4. 点击检查验证 key。
5. 点击获取刷新模型列表。
6. 回到主界面选择 OpenRouter 模型对话。

工程要点：

- OpenRouter 模型 ID 通常带供应商前缀，例如 `anthropic/...`、`openai/...`、`google/...`。
- 上游源码中 OpenRouter 是 `ModelProviderType.OpenAI`，并设置 `modelsDevProviderId: 'openrouter'`，可使用 models.dev 元数据富化。
- 免费模型通常带 `:free` 后缀，UI 与计费提示需要保留完整模型 ID。

## Ollama

Ollama 用于本地或局域网运行开源模型。

本地连接：

1. 安装 Ollama。
2. 用命令下载并运行模型，例如 `ollama run llama3.2` 或 `ollama run deepseek-r1:8b`。
3. 在 Chatbox 设置页选择 Ollama。
4. 模型下拉框应能看到本地运行的模型。

远程连接需要让 Ollama 对局域网开放：

```bash
OLLAMA_HOST=0.0.0.0
OLLAMA_ORIGINS=*
```

macOS 示例：

```bash
launchctl setenv OLLAMA_HOST "0.0.0.0"
launchctl setenv OLLAMA_ORIGINS "*"
```

远程 API Host 形式：

```text
http://192.168.xx.xx:11434
```

工程要点：

- 不要默认把 Ollama 暴露到公网；官方文档只建议家庭 Wi-Fi 等受信网络。
- 远程连接常见问题是防火墙、端口 `11434`、CORS 和局域网绑定。
- Ollama 在上游 provider registry 中不参与 models.dev 富化。

## LM Studio

LM Studio 可作为本地 OpenAI 兼容服务。

配置步骤：

1. 打开 LM Studio。
2. 进入 Developer 模式和 Developer 面板。
3. 启动 Server，等待 Status 显示 running。
4. 如需局域网访问，开启 Enable CORS 和 Serve on Local Network。
5. 复制 LM Studio 显示的 API Host。
6. 在 Chatbox 设置页选择 LM Studio 并填入 API Host。

工程要点：

- LM Studio 更接近用户自托管 OpenAI 兼容 endpoint，重点校验 API Host。
- 局域网使用时 CORS 和 local network 开关直接影响 Web / 移动端访问。
- 上游源码中 LM Studio 也不参与 models.dev 富化。
