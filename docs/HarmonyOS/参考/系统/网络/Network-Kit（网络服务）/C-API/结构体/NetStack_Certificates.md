---
title: "NetStack_Certificates"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-netstack-certificates"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "NetStack_Certificates"
captured_at: "2026-04-17T01:48:23.341Z"
---

# NetStack\_Certificates

```c
typedef struct NetStack_Certificates {...} NetStack_Certificates
```

#### 概述

定义证书信息。

**起始版本：** 12

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_ssl\_c\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \*\*content | 证书的PEM内容。 |
| size\_t length | 证书数量。 |
