---
title: "net_http.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-h"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Network Kit（网络服务）"
  - "C API"
  - "头文件"
  - "net_http.h"
captured_at: "2026-04-17T01:48:23.130Z"
---

# net\_http.h

#### 概述

定义HTTP请求模块的接口。

**引用文件：** <network/netstack/net\_http.h>

**库：** libnet\_http.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**相关模块：** [netstack](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [Http\_Headers \*OH\_Http\_CreateHeaders(void)](#oh_http_createheaders) | 创建HTTP请求或者响应的头。 |
| [void OH\_Http\_DestroyHeaders(Http\_Headers \*\*headers)](#oh_http_destroyheaders) | 销毁HTTP请求或者响应的头。 |
| [uint32\_t OH\_Http\_SetHeaderValue(struct Http\_Headers \*headers, const char \*name, const char \*value)](#oh_http_setheadervalue) | 设置HTTP请求或者响应的头的键值对。 |
| [Http\_HeaderValue \*OH\_Http\_GetHeaderValue(Http\_Headers \*headers, const char \*name)](#oh_http_getheadervalue) | 通过键获取请求或响应头的值。 |
| [Http\_HeaderEntry \*OH\_Http\_GetHeaderEntries(Http\_Headers \*headers)](#oh_http_getheaderentries) | 获取请求或响应头的所有键值对。 |
| [void OH\_Http\_DestroyHeaderEntries(Http\_HeaderEntry \*\*headerEntry)](#oh_http_destroyheaderentries) | 销毁OH\_Http\_GetHeaderEntries中获取的所有键值对。 |
| [Http\_Request \*OH\_Http\_CreateRequest(const char \*url)](#oh_http_createrequest) | 创建HTTP请求。 |
| [int OH\_Http\_Request(Http\_Request \*request, Http\_ResponseCallback callback, Http\_EventsHandler handler)](#oh_http_request) | 发起HTTP请求。 |
| [void OH\_Http\_Destroy(struct Http\_Request \*\*request)](#oh_http_destroy) | 销毁HTTP请求。 |

#### 函数说明

#### \[h2\]OH\_Http\_CreateHeaders()

```c
Http_Headers *OH_Http_CreateHeaders(void)
```

**描述**

创建HTTP请求或者响应的头。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/v_gjjcErTaeTGL0SsY-yOA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014824Z&HW-CC-Expire=86400&HW-CC-Sign=42EBA225AE074295B6A4C622E3ABA7E8C502EC3D6B745AB06B6B1C234463A701)

建议在本次HTTP请求结束后，及时调用[OH\_Http\_DestroyHeaders](#oh_http_destroyheaders)销毁HTTP请求或者响应的头，执行资源清理等操作。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Http\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers) \* | Http\_Headers 返回HTTP请求或者响应的头，指向Http\_Headers。 |

#### \[h2\]OH\_Http\_DestroyHeaders()

```c
void OH_Http_DestroyHeaders(Http_Headers **headers)
```

**描述**

销毁HTTP请求或者响应的头。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Http\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers) \*\*headers | 要被销毁的HTTP请求或响应的头，是通过OH\_Http\_CreateHeaders生成的数据。 |

#### \[h2\]OH\_Http\_SetHeaderValue()

```c
uint32_t OH_Http_SetHeaderValue(struct Http_Headers *headers, const char *name, const char *value)
```

**描述**

设置HTTP请求或者响应的头的键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [struct Http\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers) \*headers | 指向要设置的Http\_Headers的指针。 |
| const char \*name | 键值。 |
| const char \*value | 键值对应的值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| uint32\_t | uint32\_t 0 - 成功。 401 - 参数错误。 2300027 - 内存不足。 |

#### \[h2\]OH\_Http\_GetHeaderValue()

```c
Http_HeaderValue *OH_Http_GetHeaderValue(Http_Headers *headers, const char *name)
```

**描述**

通过键获取请求或响应头的值。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Http\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers) \*headers | 指向要获取值的Http\_Headers的指针。 |
| const char \*name | 键值。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Http\_HeaderValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headervalue) \* | Http\_HeaderValue 指向获取的Http\_HeaderValue的指针。 |

#### \[h2\]OH\_Http\_GetHeaderEntries()

```c
Http_HeaderEntry *OH_Http_GetHeaderEntries(Http_Headers *headers)
```

**描述**

获取请求或响应头的所有键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Http\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headers) \*headers | 指向要获取值的Http\_Headers的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Http\_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headerentry) \* | Http\_HeaderEntry 指向获取的Http\_HeaderEntry的指针。 |

#### \[h2\]OH\_Http\_DestroyHeaderEntries()

```c
void OH_Http_DestroyHeaderEntries(Http_HeaderEntry **headerEntry)
```

**描述**

销毁OH\_Http\_GetHeaderEntries中获取的所有键值对。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Http\_HeaderEntry](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-headerentry) \*\*headerEntry | 指向要销毁的Http\_HeaderEntry的指针，是通过OH\_Http\_GetHeaderEntries获取的数据。 |

#### \[h2\]OH\_Http\_CreateRequest()

```c
Http_Request *OH_Http_CreateRequest(const char *url)
```

**描述**

创建HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const char \*url | 请求URL。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [Http\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request) \* | 返回创建的请求，指向Http\_Request的指针。 |

#### \[h2\]OH\_Http\_Request()

```c
int OH_Http_Request(Http_Request *request, Http_ResponseCallback callback, Http_EventsHandler handler)
```

**描述**

发起HTTP请求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/xLliSUmZTy6FaH7Pb3ZC5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014824Z&HW-CC-Expire=86400&HW-CC-Sign=4CCBEEDEBA3EA9D0CA9911B7CBE1102E8CD55AF42346FC3FD54B22F468A10EA0)

建议在本次HTTP请求收到响应并处理完毕后，及时调用[OH\_Http\_Destroy](#oh_http_destroy)中断HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**需要权限：** ohos.permission.INTERNET

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [Http\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request) \*request | 发送的请求，指向Http\_Request的指针。 |
| [Http\_ResponseCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-http-type-h#http_responsecallback) callback | 请求的响应，指向Http\_ResponseCallback。 |
| [Http\_EventsHandler](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-eventshandler) handler | 监听不同HTTP事件的回调函数，指向Http\_EventsHandler。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
请求发起成功返回0，非0表示请求发起失败，错误码的具体描述，可以参考Http\_ErrCode。

在Http\_ResponseCallback中也会携带errCode信息，表示请求发起成功，但是因为一些原因，和服务器的交互异常，具体异常原因，同步参考Http\_ErrCode。

 |

#### \[h2\]OH\_Http\_Destroy()

```c
void OH_Http_Destroy(struct Http_Request **request)
```

**描述**

中断HTTP请求。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [struct Http\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request) \*\*request | 要中断的请求，指向Http\_Request的指针，参考[Http\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-netstack-http-request)。 |
