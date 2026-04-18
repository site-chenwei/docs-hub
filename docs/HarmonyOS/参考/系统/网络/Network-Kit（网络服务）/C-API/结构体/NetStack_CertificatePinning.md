---
title: "NetStack_CertificatePinning"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificatepinning"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetStack_CertificatePinning"
captured_at: "2026-04-17T01:48:23.343Z"
---

# NetStack\_CertificatePinning

```c
typedef struct NetStack_CertificatePinning {...} NetStack_CertificatePinning
```

#### 概述

定义证书锁定信息。

**起始版本：** 12

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_ssl\_c\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [NetStack\_CertificatePinningKind](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h#netstack_certificatepinningkind) kind | 证书锁定类型。 |
| [NetStack\_HashAlgorithm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h#netstack_hashalgorithm) hashAlgorithm | 哈希算法。 |
| char \*publicKeyHash | 哈希值。 |
