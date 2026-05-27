---
source_url: "https://github.com/chatboxai/chatbox/blob/b45fc528e6f6682656166d5d068f2f1b4907c405/docs/storage.md"
---

# 存储迁移与新会话机制

来源：

- `upstream-source/docs/storage.md`
- `upstream-source/docs/new-session-mechanism.md`

## 跨平台存储类型

| 类型 | 说明 |
| --- | --- |
| `DESKTOP_FILE` | 桌面端文件存储，通过 IPC |
| `INDEXEDDB` | IndexedDB，通过 localforage |
| `LOCAL_STORAGE` | localStorage，已弃用 |
| `MOBILE_SQLITE` | SQLite，通过 Capacitor |

## 当前存储方案

上游 `v1.17.0` 文档记录的方案：

| 平台 | Settings / Configs | Sessions | 原因 |
| --- | --- | --- | --- |
| Desktop | 文件存储 | IndexedDB | 配置便于备份，会话需要大容量 |
| Mobile | SQLite | SQLite | 统一存储，性能更好 |
| Web | IndexedDB | IndexedDB | 大容量、异步访问 |

关键历史事实：

- Desktop 的 `configVersion`、`settings`、`configs` 从未存储在 IndexedDB。
- Desktop 从 `v1.16.1` 开始只把 sessions 迁到 IndexedDB。
- `v1.16.1 -> v1.17.0` Desktop 存储策略未变。
- Mobile 演进为 `localStorage -> SQLite -> IndexedDB -> SQLite`。

## 迁移机制

迁移核心流程：

```typescript
const [oldConfigVersion, oldStorage] = await findNewestStorage(getOldVersionStorages())

if (
  (oldConfigVersion > configVersion || platform.type === 'desktop') &&
  oldStorage &&
  oldStorage.getStorageType() !== storage.getStorageType()
) {
  await doMigrateStorage(oldStorage)
}

for (; configVersion < CurrentVersion; configVersion++) {
  await migrateFunctions[configVersion]?.(dataStore)
  await setConfigVersion(configVersion + 1)
}
```

策略差异：

| 平台 | 策略 |
| --- | --- |
| Mobile | 复制所有 key |
| Desktop | 只复制会话数据，settings / configs 保留在文件 |

## 迁移设计决策

同类型存储共享数据源：

- 旧存储和当前存储类型一致时，无需复制数据。
- 例：Mobile SQLite v7 到 SQLite v13，只需升级数据格式。

多个旧存储选最新：

- 按 `configVersion` 最大值选择旧存储，避免迁移过时数据。

桌面端混合存储：

- 配置文件便于备份。
- 会话数据放 IndexedDB。
- 迁移时只复制会话 key，例如 `chat-sessions-list`、`session:*`。

增量数据格式升级：

- 按版本逐步执行迁移函数。
- 从任意旧版本升级都能覆盖。
- 中断后可继续。

## 存储测试要点

测试场景：

- 首次运行无旧数据。
- 已是最新版本时跳过迁移。
- 同类型存储数据已可访问。
- 跨存储迁移，例如 File 到 IndexedDB、localStorage 到 SQLite。
- 多旧存储共存时选最新版本。
- 从历史版本直接升级。

关键洞察：

- mock 同类型存储要共享同一数据容器。
- 桌面迁移只迁 sessions。
- 测试应尽量使用真实 Platform 实例，避免 mock 掩盖平台差异。

## 首页新会话机制

Chatbox 首页 `/` 是新对话入口。用户真正发送第一条消息前，页面使用特殊会话 ID：

```typescript
id: 'new'
```

这个 ID 表示尚未创建真实持久会话。

## newSessionStateAtom

首页临时状态通过 `newSessionStateAtom` 保存：

```typescript
export const newSessionStateAtom = atom<{
  knowledgeBase?: Pick<KnowledgeBase, 'id' | 'name'>
  webBrowsing?: boolean
}>({})
```

用途：

- 发送第一条消息前的知识库选择。
- 联网模式等临时开关。
- 避免把临时状态写入真实 `sessionKnowledgeBaseMap`。

## 新会话状态流转

用户交互阶段：

- 知识库选择进入 `newSessionStateAtom.knowledgeBase`。
- 模型和 Copilot 等进入首页组件的临时 session state。

输入框逻辑：

- `currentSessionId === 'new'` 时从 `newSessionState` 读写。
- 真实会话时从 `sessionKnowledgeBaseMap[currentSessionId]` 读写。

发送第一条消息：

1. `createSession()` 创建真实 session。
2. 把临时状态转移到真实 session，例如 `sessionKnowledgeBaseMap[newSession.id]`。
3. 清空 `newSessionStateAtom`。
4. 切换到真实 session。
5. 发送消息。

## 设计约束

- `"new"` 简单且不应与 UUID 冲突。
- 临时状态和持久状态必须分离。
- 状态转移应发生在会话创建成功后、切换会话前。
- 创建失败时不要清空临时状态，否则用户选择会丢失。
- 清理 `newSessionStateAtom` 是必要的内存与状态一致性步骤。
