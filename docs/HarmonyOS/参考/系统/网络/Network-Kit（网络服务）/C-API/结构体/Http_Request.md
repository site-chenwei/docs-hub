---
title: "Http_Request"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "Http_Request"
captured_at: "2026-04-17T01:48:23.628Z"
---

# Http\_Request

```c
typedef struct Http_Request {...} Http_Request
```

#### 概述

HTTP请求结构体。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_http\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t requestId | HTTP请求的ID。 |
| char \*url | HTTP请求的URL。 |
| [Http\_RequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-requestoptions) \*options | HTTP请求配置，指向Http\_RequestOptions的指针，参考[Http\_RequestOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-requestoptions)。 |
