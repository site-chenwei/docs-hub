---
title: "NetConn_NetHandleList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandlelist"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetConn_NetHandleList"
captured_at: "2026-04-17T01:48:23.237Z"
---

# NetConn\_NetHandleList

```c
typedef struct NetConn_NetHandleList {...} NetConn_NetHandleList
```

#### 概述

网络列表。

**起始版本：** 11

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net\_connection\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [NetConn\_NetHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-nethandle) netHandles[\[NETCONN\_MAX\_NET\_SIZE\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | netHandle列表。 |
| int32\_t netHandleListSize | netHandleList的实际大小。 |
