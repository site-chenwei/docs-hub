---
title: "NetStack_CertBlob"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certblob"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetStack_CertBlob"
captured_at: "2026-04-17T01:48:23.341Z"
---

# NetStack\_CertBlob

```c
struct NetStack_CertBlob {...}
```

#### 概述

证书数据结构体。

**起始版本：** 11

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_ssl\_c\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| enum [NetStack\_CertType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h#netstack_certtype) type | 证书类型。 |
| uint32\_t size | 证书内容长度。 |
| uint8\_t \*data | 证书内容。 |
