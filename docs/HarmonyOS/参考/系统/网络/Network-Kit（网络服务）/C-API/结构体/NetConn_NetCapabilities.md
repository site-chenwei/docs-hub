---
title: "NetConn_NetCapabilities"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-netcapabilities"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetConn_NetCapabilities"
captured_at: "2026-04-17T01:48:23.144Z"
---

# NetConn\_NetCapabilities

```c
typedef struct NetConn_NetCapabilities {...} NetConn_NetCapabilities
```

#### 概述

网络能力集。

**起始版本：** 11

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net\_connection\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t linkUpBandwidthKbps | 上行带宽。 |
| uint32\_t linkDownBandwidthKbps | 下行带宽。 |
| [NetConn\_NetCap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#netconn_netcap) netCaps[\[NETCONN\_MAX\_CAP\_SIZE\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 网络能力列表。 |
| int32\_t netCapsSize | 网络能力列表的实际size。 |
| [NetConn\_NetBearerType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#netconn_netbearertype) bearerTypes[\[NETCONN\_MAX\_BEARER\_TYPE\_SIZE\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 承载类型列表 |
| int32\_t bearerTypesSize | 承载类型列表的实际size |
