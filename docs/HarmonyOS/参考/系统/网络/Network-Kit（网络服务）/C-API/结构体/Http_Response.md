---
title: "Http_Response"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-response"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "结构体"
  - "Http_Response"
captured_at: "2026-04-17T01:48:23.626Z"
---

# Http\_Response

```c
typedef struct Http_Response {...} Http_Response
```

#### 概述

定义HTTP响应的结构体。

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

**所在头文件：** [net\_http\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Http\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer) body | HTTP请求响应的数据，参考[Http\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-buffer)。 |
| [Http\_ResponseCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_responsecode) responseCode | HTTP请求响应码，参考[Http\_ResponseCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_responsecode)。 |
| [Http\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers) \*headers | HTTP响应的头，指向Http\_Headers的指针，参考[Http\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers)。 |
| char \*cookies | HTTP响应Cookies。 |
| [Http\_PerformanceTiming](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-performancetiming) \*performanceTiming | HTTP响应时间信息，指向Http\_PerformanceTiming的指针，参考[Http\_PerformanceTiming](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-performancetiming)。 |

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [void (\*destroyResponse)(struct Http\_Response \*\*response)](#destroyresponse) | 销毁HTTP响应的回调函数 |

#### 成员函数说明

#### \[h2\]destroyResponse()

```c
void (*destroyResponse)(struct Http_Response **response)
```

**描述**

销毁HTTP响应的回调函数

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| struct [Http\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-response) \*\*response | 要销毁的HTTP响应，指向Http\_Response的指针，参考[Http\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-response)。 |
