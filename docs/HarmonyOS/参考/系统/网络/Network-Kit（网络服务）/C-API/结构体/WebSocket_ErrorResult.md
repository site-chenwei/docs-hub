---
title: "WebSocket_ErrorResult"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-websocket-errorresult"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "WebSocket_ErrorResult"
captured_at: "2026-04-17T01:48:23.427Z"
---

# WebSocket\_ErrorResult

```c
struct WebSocket_ErrorResult {...}
```

#### 概述

websocket客户端来自服务端连接错误的参数。

**起始版本：** 11

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_websocket\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-websocket-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t errorCode | 错误码。 |
| const char \*errorMessage | 错误的消息。 |
