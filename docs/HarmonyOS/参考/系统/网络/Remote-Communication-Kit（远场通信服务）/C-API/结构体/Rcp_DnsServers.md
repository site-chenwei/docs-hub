---
title: "Rcp_DnsServers"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_DnsServers"
captured_at: "2026-04-17T01:48:26.293Z"
---

# Rcp\_DnsServers

#### 概述

DNS服务器。[Rcp\_DnsConfiguration.dnsRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_configuration#dnsrules)中的类型之一。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_IpAndPort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_and_port)[ipAndPort](#ipandport) | IP和端口。 |
| struct [Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers) \* [next](#next) | 链式存储。指向下一个[Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)的指针。 |

#### 结构体成员变量说明

#### \[h2\]ipAndPort

```cpp
Rcp_IpAndPort Rcp_DnsServers::ipAndPort
```

**描述**

IP和端口。

#### \[h2\]next

```cpp
struct Rcp_DnsServers* Rcp_DnsServers::next
```

**描述**

链式存储。指向下一个[Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers)的指针。
