---
title: "Rcp_DnsOverHttps"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___dns_over_https"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_DnsOverHttps"
captured_at: "2026-04-17T01:48:26.287Z"
---

# Rcp\_DnsOverHttps

#### 概述

HTTPS上的DNS配置如果设置，则首选由DOH dns服务器解析的地址。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char \* [url](#url) | DOH服务器的URL。 |
| bool [skipCertificatesValidation](#skipcertificatesvalidation) | 判断是否跳过证书验证。默认值为false。 |

#### 结构体成员变量说明

#### \[h2\]skipCertificatesValidation

```cpp
bool Rcp_DnsOverHttps::skipCertificatesValidation
```

**描述**

判断是否跳过证书验证。默认值为false。

#### \[h2\]url

```cpp
const char* Rcp_DnsOverHttps::url
```

**描述**

DOH服务器的URL。
