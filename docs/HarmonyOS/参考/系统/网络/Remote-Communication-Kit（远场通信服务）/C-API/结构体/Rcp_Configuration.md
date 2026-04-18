---
title: "Rcp_Configuration"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_Configuration"
captured_at: "2026-04-17T01:48:26.008Z"
---

# Rcp\_Configuration

#### 概述

请求配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_TransferConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_configuration)[transferConfiguration](#transferconfiguration) | 传输配置。 |
| [Rcp\_TracingConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration)[tracingConfiguration](#tracingconfiguration) | 请求追踪配置。 |
| [Rcp\_ProxyConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___proxy_configuration)[proxyConfiguration](#proxyconfiguration) | 代理配置。 |
| [Rcp\_DnsConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration)[dnsConfiguration](#dnsconfiguration) | DNS配置。 |
| [Rcp\_SecurityConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___security_configuration)[securityConfiguration](#securityconfiguration) | 安全配置。 |
| void \* [configurationPrivate](#configurationprivate) | 可扩展字段。 |

#### 结构体成员变量说明

#### \[h2\]configurationPrivate

```cpp
void* Rcp_Configuration::configurationPrivate
```

**描述**

可扩展字段。

#### \[h2\]dnsConfiguration

```cpp
Rcp_DnsConfiguration Rcp_Configuration::dnsConfiguration
```

**描述**

DNS配置。

#### \[h2\]proxyConfiguration

```cpp
Rcp_ProxyConfiguration Rcp_Configuration::proxyConfiguration
```

**描述**

代理配置。

#### \[h2\]securityConfiguration

```cpp
Rcp_SecurityConfiguration Rcp_Configuration::securityConfiguration
```

**描述**

安全配置。

#### \[h2\]tracingConfiguration

```cpp
Rcp_TracingConfiguration Rcp_Configuration::tracingConfiguration
```

**描述**

请求追踪配置。

#### \[h2\]transferConfiguration

```cpp
Rcp_TransferConfiguration Rcp_Configuration::transferConfiguration
```

**描述**

传输配置。
