---
title: "Rcp_WebProxy"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___web_proxy"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_WebProxy"
captured_at: "2026-04-17T01:48:26.864Z"
---

# Rcp\_WebProxy

#### 概述

自定义代理配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char \* [url](#url) | 代理服务器的URL。如果您没有明确设置端口，则端口将为1080。 |
| [Rcp\_ProxyTunnelMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_proxytunnelmode)[createTunnel](#createtunnel) | 用于控制何时创建代理隧道。 |
| [Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)[exclusions](#exclusions) | 如果[Rcp\_Request.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#url)匹配[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)规则，则[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)将不使用代理。 |
| [Rcp\_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)[securityConfiguration](#securityconfiguration) | 代理中的[Rcp\_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)。 |

#### 结构体成员变量说明

#### \[h2\]createTunnel

```cpp
Rcp_ProxyTunnelMode Rcp_WebProxy::createTunnel
```

**描述**

用于控制何时创建代理隧道。

#### \[h2\]exclusions

```cpp
Rcp_Exclusions Rcp_WebProxy::exclusions
```

**描述**

如果[Rcp\_Request.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#url)匹配[Rcp\_Exclusions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___exclusions)规则，则[Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request)将不使用代理。

#### \[h2\]securityConfiguration

```cpp
Rcp_SecurityConfiguration Rcp_WebProxy::securityConfiguration
```

**描述**

代理中的[Rcp\_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)。

#### \[h2\]url

```cpp
const char* Rcp_WebProxy::url
```

**描述**

代理服务器的URL。如果您没有明确设置端口，则端口将为1080。
