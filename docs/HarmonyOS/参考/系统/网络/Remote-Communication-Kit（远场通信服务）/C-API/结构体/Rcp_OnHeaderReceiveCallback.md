---
title: "Rcp_OnHeaderReceiveCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_header_receive_callback"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_OnHeaderReceiveCallback"
captured_at: "2026-04-17T01:48:26.491Z"
---

# Rcp\_OnHeaderReceiveCallback

#### 概述

[Rcp\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___events_handler)中配置的接收到的header的回调配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_OnHeaderReceiveCallbackFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_onheaderreceivecallbackfunc)[callback](#callback) | 接收到的headers的回调函数。 |
| void \* [usrObject](#usrobject) | 用户定义的对象，在回调函数中使用。 |

#### 结构体成员变量说明

#### \[h2\]callback

```cpp
Rcp_OnHeaderReceiveCallbackFunc Rcp_OnHeaderReceiveCallback::callback
```

**描述**

接收到的headers的回调函数。

#### \[h2\]usrObject

```cpp
void* Rcp_OnHeaderReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
