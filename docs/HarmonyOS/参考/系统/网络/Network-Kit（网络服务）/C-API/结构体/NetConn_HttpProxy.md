---
title: "NetConn_HttpProxy"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection-netconn-httpproxy"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetConn_HttpProxy"
captured_at: "2026-04-17T01:48:23.233Z"
---

# NetConn\_HttpProxy

```c
typedef struct NetConn_HttpProxy {...} NetConn_HttpProxy
```

#### 概述

代理配置信息。

**起始版本：** 11

**相关模块：** [NetConnection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netconnection)

**所在头文件：** [net\_connection\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char host[\[NETCONN\_MAX\_STR\_LEN\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 主机名。 |
| char exclusionList[\[NETCONN\_MAX\_EXCLUSION\_SIZE\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义)[\[NETCONN\_MAX\_STR\_LEN\]](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-connection-type-h#宏定义) | 代理服务器的排除列表。 |
| int32\_t exclusionListSize | 排除列表的实际大小。 |
| uint16\_t port | 端口号。 |
