---
title: "NetConn_Route"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-route"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetConn_Route"
captured_at: "2026-04-17T01:48:23.232Z"
---

# NetConn\_Route

```c
typedef struct NetConn_Route {...} NetConn_Route
```

#### 概述

路由配置信息。

**起始版本：** 11

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net\_connection\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char iface[\[NETCONN\_MAX\_STR\_LEN\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 网络接口 |
| [NetConn\_NetAddr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr) destination | 目标地址 |
| [NetConn\_NetAddr](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr) gateway | 网关地址 |
| int32\_t hasGateway | 是否存在网关 |
| int32\_t isDefaultRoute | 是否是默认路由 |
