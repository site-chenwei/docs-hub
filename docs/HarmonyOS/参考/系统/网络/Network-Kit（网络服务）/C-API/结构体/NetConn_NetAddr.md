---
title: "NetConn_NetAddr"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netaddr"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetConn_NetAddr"
captured_at: "2026-04-17T01:48:23.211Z"
---

# NetConn\_NetAddr

```c
typedef struct NetConn_NetAddr {...} NetConn_NetAddr
```

#### 概述

网络地址。

**起始版本：** 11

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net\_connection\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t family | 网络地址族。 |
| uint8\_t prefixlen | 前缀长度。 |
| uint8\_t port | 端口号。 |
| char address[\[NETCONN\_MAX\_STR\_LEN\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 地址。 |
