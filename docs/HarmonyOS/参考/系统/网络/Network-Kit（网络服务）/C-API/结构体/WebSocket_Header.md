---
title: "WebSocket_Header"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-header"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "WebSocket_Header"
captured_at: "2026-04-17T01:48:23.441Z"
---

# WebSocket\_Header

```c
struct WebSocket_Header {...}
```

#### 概述

websocket客户端增加header的链表节点。

**起始版本：** 11

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_websocket\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char \*fieldName | header的字段名。 |
| const char \*fieldValue | header的字段内容。 |
| struct [WebSocket\_Header](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-header) \*next | header链表的next指针。 |
