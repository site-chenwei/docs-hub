---
title: "Rcp_OnProgressCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_progress_callback"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_OnProgressCallback"
captured_at: "2026-04-17T01:48:26.521Z"
---

# Rcp\_OnProgressCallback

#### 概述

收发时回调配置，在[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_OnProgressCallbackFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_onprogresscallbackfunc)[callback](#callback) | 收发过程中的回调函数。 |
| void \* [usrObject](#usrobject) | 用户定义的对象，在回调函数中使用。 |

#### 结构体成员变量说明

#### \[h2\]callback

```cpp
Rcp_OnProgressCallbackFunc Rcp_OnProgressCallback::callback
```

**描述**

收发过程中的回调函数。

#### \[h2\]usrObject

```cpp
void* Rcp_OnProgressCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
