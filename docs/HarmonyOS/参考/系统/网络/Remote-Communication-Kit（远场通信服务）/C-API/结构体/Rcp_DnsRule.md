---
title: "Rcp_DnsRule"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_rule"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_DnsRule"
captured_at: "2026-04-17T01:48:26.289Z"
---

# Rcp\_DnsRule

#### 概述

DNS规则配置。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_DnsRuleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_dnsruletype)[type](#type) | 表示union中使用的数据类型。 |
| 
union {

[Rcp\_DnsServers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_servers) \* [dnsServers](#dnsservers)

[Rcp\_StaticDnsRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule) \* [staticDnsRule](#staticdnsrule)

[Rcp\_DynamicDnsRuleFunction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_dynamicdnsrulefunction) [dynamicDnsRule](#dynamicdnsrule)

}

 | 

dnsServers：DNS服务器。

staticDnsRule：静态DNS规则。

dynamicDnsRule：动态DNS规则。

 |

#### 结构体成员变量说明

#### \[h2\]dnsServers

```cpp
Rcp_DnsServers* Rcp_DnsRule::dnsServers
```

**描述**

DNS服务器。

#### \[h2\]dynamicDnsRule

```cpp
Rcp_DynamicDnsRuleFunction Rcp_DnsRule::dynamicDnsRule
```

**描述**

动态DNS规则。

#### \[h2\]staticDnsRule

```cpp
Rcp_StaticDnsRule* Rcp_DnsRule::staticDnsRule
```

**描述**

静态DNS规则。

#### \[h2\]type

```cpp
Rcp_DnsRuleType Rcp_DnsRule::type
```

**描述**

表示union中使用的数据类型。
