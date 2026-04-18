---
title: "Rcp_ConnectionConfiguration"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___connection_configuration"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_ConnectionConfiguration"
captured_at: "2026-04-17T01:48:26.030Z"
---

# Rcp\_ConnectionConfiguration

#### 概述

连接配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| long [maxConnectionsPerHost](#maxconnectionsperhost) | 每台主机的最大连接数。 |
| long [maxTotalConnections](#maxtotalconnections) | 最大总连接数。 |
| long [maxCacheConnections](#maxcacheconnections) | 最大缓存连接数。 |

#### 结构体成员变量说明

#### \[h2\]maxCacheConnections

```cpp
long Rcp_ConnectionConfiguration::maxCacheConnections
```

**描述**

最大缓存连接数。

#### \[h2\]maxConnectionsPerHost

```cpp
long Rcp_ConnectionConfiguration::maxConnectionsPerHost
```

**描述**

每台主机的最大连接数。

#### \[h2\]maxTotalConnections

```cpp
long Rcp_ConnectionConfiguration::maxTotalConnections
```

**描述**

最大总连接数。范围由long决定。
