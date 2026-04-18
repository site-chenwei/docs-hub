---
title: "Rcp_ResponseCallbackObject"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_ResponseCallbackObject"
captured_at: "2026-04-17T01:48:26.626Z"
---

# Rcp\_ResponseCallbackObject

#### 概述

响应回调结构体。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_ResponseCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_responsecallback)[callback](#callback) | 响应回调函数。 |
| void \* [usrCtx](#usrctx) | 用户上下文。 |

#### 结构体成员变量说明

#### \[h2\]callback

```cpp
Rcp_ResponseCallback Rcp_ResponseCallbackObject::callback
```

**描述**

响应回调函数。

#### \[h2\]usrCtx

```cpp
void* Rcp_ResponseCallbackObject::usrCtx
```

**描述**

用户上下文。
