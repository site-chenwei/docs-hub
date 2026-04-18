---
title: "Rcp_ProxyConfiguration"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_ProxyConfiguration"
captured_at: "2026-04-17T01:48:26.520Z"
---

# Rcp\_ProxyConfiguration

#### 概述

代理配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_ProxyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_proxytype)[proxyType](#proxytype) | 区分请求使用的代理类型。 |
| [Rcp\_WebProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy)[customProxy](#customproxy) | 自定义代理配置，参见[Rcp\_WebProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy)。 |

#### 结构体成员变量说明

#### \[h2\]customProxy

```cpp
Rcp_WebProxy Rcp_ProxyConfiguration::customProxy
```

**描述**

自定义代理配置，参见[Rcp\_WebProxy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy)。

#### \[h2\]proxyType

```cpp
Rcp_ProxyType Rcp_ProxyConfiguration::proxyType
```

**描述**

区分请求使用的代理类型。
