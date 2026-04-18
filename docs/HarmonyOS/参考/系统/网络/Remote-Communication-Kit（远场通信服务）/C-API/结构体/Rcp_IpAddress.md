---
title: "Rcp_IpAddress"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_IpAddress"
captured_at: "2026-04-17T01:48:26.413Z"
---

# Rcp\_IpAddress

#### 概述

指定静态DNS规则使用的IP地址组。用于[Rcp\_StaticDnsRuleItem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___static_dns_rule_item)。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char [ipAddress](#ipaddress) \[[RCP\_IP\_MAX\_LEN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_ip_max_len)\] | IP地址。 |
| struct [Rcp\_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address) \* [next](#next) | 链式存储。指向下一个[Rcp\_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address)。 |

#### 结构体成员变量说明

#### \[h2\]ipAddress

```cpp
char Rcp_IpAddress::ipAddress[RCP_IP_MAX_LEN]
```

**描述**

ip地址。

#### \[h2\]next

```cpp
struct Rcp_IpAddress* Rcp_IpAddress::next
```

**描述**

链式存储。指向下一个[Rcp\_IpAddress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___ip_address)。
