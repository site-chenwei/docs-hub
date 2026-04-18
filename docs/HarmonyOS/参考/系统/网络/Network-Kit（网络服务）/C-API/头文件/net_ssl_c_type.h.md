---
title: "net_ssl_c_type.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "头文件"
  - "net_ssl_c_type.h"
captured_at: "2026-04-17T01:48:23.121Z"
---

# net\_ssl\_c\_type.h

#### 概述

定义SSL/TLS证书链校验模块的C接口需要的数据结构。

**引用文件：** <network/netstack/net\_ssl/net\_ssl\_c\_type.h>

**库：** libnet\_ssl.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [NetStack\_CertBlob](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certblob) | \- | 证书数据结构体。 |
| [NetStack\_CertificatePinning](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificatepinning) | NetStack\_CertificatePinning | 定义证书锁定信息。 |
| [NetStack\_Certificates](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificates) | NetStack\_Certificates | 定义证书信息。 |

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [NetStack\_CertType](#netstack_certtype) | \- | 证书类型枚举。 |
| [NetStack\_CertificatePinningKind](#netstack_certificatepinningkind) | NetStack\_CertificatePinningKind | 定义证书锁定类型枚举。 |
| [NetStack\_HashAlgorithm](#netstack_hashalgorithm) | NetStack\_HashAlgorithm | 定义哈希算法。 |

#### 枚举类型说明

#### \[h2\]NetStack\_CertType

```c
enum NetStack_CertType
```

**描述**

证书类型枚举。

**起始版本：** 11

| 枚举项 | 描述 |
| :-- | :-- |
| NETSTACK\_CERT\_TYPE\_PEM = 0 | PEM证书类型 |
| NETSTACK\_CERT\_TYPE\_DER = 1 | DER证书类型 |
| NETSTACK\_CERT\_TYPE\_INVALID | 错误证书类型 |

#### \[h2\]NetStack\_CertificatePinningKind

```c
enum NetStack_CertificatePinningKind
```

**描述**

定义证书锁定类型枚举。

**起始版本：** 12

| 枚举项 | 描述 |
| :-- | :-- |
| PUBLIC\_KEY | 公钥锁定类型 |

#### \[h2\]NetStack\_HashAlgorithm

```c
enum NetStack_HashAlgorithm
```

**描述**

定义哈希算法。

**起始版本：** 12

| 枚举项 | 描述 |
| :-- | :-- |
| SHA\_256 | Sha256 |
