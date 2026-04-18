---
title: "Rcp_OnBinaryReceiveCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___on_binary_receive_callback"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_OnBinaryReceiveCallback"
captured_at: "2026-04-17T01:48:26.887Z"
---

# Rcp\_OnBinaryReceiveCallback

#### 概述

响应的二进制数据接收回调函数。可以通过[HMS\_Rcp\_SetRequestOnBinaryDataRecvCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#hms_rcp_setrequestonbinarydatarecvcallback)为请求设置相应回调函数。

**起始版本：** 5.0.1(13)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_OnBinaryReceiveCallbackFunc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_onbinaryreceivecallbackfunc)[callback](#callback) | 请求过程中接收二进制数据的回调函数。 |
| void \*[usrObject](#usrobject) | 用户定义的对象，在回调函数中使用。 |

#### 结构体成员变量说明

#### \[h2\]callback

```cpp
Rcp_OnBinaryReceiveCallbackFunc Rcp_OnBinaryReceiveCallback::callback
```

**描述**

二进制数据接收回调函数。

#### \[h2\]usrObject

```cpp
void* Rcp_OnBinaryReceiveCallback::usrObject
```

**描述**

用户定义的对象，在回调函数中使用。
