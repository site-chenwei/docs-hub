---
title: "Rcp_Response"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_Response"
captured_at: "2026-04-17T01:48:26.631Z"
---

# Rcp\_Response

#### 概述

网络请求的响应。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const [Rcp\_Request](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request) \* [request](#request) | 表示生成响应的请求。 |
| char \* [effectiveUrl](#effectiveurl) | 上次使用的有效URL。 |
| [Rcp\_StatusCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_statuscode)[statusCode](#statuscode) | 响应状态码。 |
| [Rcp\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_headers) \* [headers](#headers) | 响应标头。 |
| [Rcp\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer)[body](#body) | 响应消息体。 |
| [Rcp\_DebugInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___debug_info) \* [debugInfo](#debuginfo) | 请求/响应处理调试信息。 |
| [Rcp\_TimeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___time_info) \* [timeInfo](#timeinfo) | 响应时间信息。 |
| [Rcp\_ResponseCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_cookies) \* [cookies](#cookies) | 响应Cookies。 |
| const [Rcp\_ResponseCallbackObject](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response_callback_object) \* [responseCallback](#responsecallback) | 使用的响应回调。 |
| void(\* [destroyResponse](#destroyresponse) )(struct [Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response) \*response) | 用于销毁响应的方法。 |
| void \* [responsePrivate](#responseprivate) | 可扩展字段。 |

#### 结构体成员变量说明

#### \[h2\]body

```cpp
Rcp_Buffer Rcp_Response::body
```

**描述**

响应消息体。

#### \[h2\]cookies

```cpp
Rcp_ResponseCookies* Rcp_Response::cookies
```

**描述**

响应Cookies。

#### \[h2\]debugInfo

```cpp
Rcp_DebugInfo* Rcp_Response::debugInfo
```

**描述**

请求/响应处理调试信息。

收集的事件取决于[Rcp\_TracingConfiguration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration)配置信息。

#### \[h2\]destroyResponse

```cpp
void(* Rcp_Response::destroyResponse) (struct Rcp_Response *response)
```

**描述**

用于销毁响应的方法。

**起始版本：** 5.0.0(12)

**参数:**

| 名称 | 描述 |
| :-- | :-- |
| response | 指示要销毁的响应。它是一个指向[Rcp\_Response](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___response)的指针。 |

#### \[h2\]effectiveUrl

```cpp
char* Rcp_Response::effectiveUrl
```

**描述**

上次使用的有效URL。

如果重定向，或设置了[Rcp\_SessionConfiguration.baseUrl](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___session_configuration#baseurl)，则有效URL可能不等于[Rcp\_Request.url](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request#url)。

#### \[h2\]headers

```cpp
Rcp_Headers* Rcp_Response::headers
```

**描述**

响应标头。

#### \[h2\]request

```cpp
const Rcp_Request* Rcp_Response::request
```

**描述**

表示生成响应的请求。

#### \[h2\]responseCallback

```cpp
const Rcp_ResponseCallbackObject* Rcp_Response::responseCallback
```

**描述**

使用的响应回调。

#### \[h2\]responsePrivate

```cpp
void* Rcp_Response::responsePrivate
```

**描述**

可扩展字段。

#### \[h2\]statusCode

```cpp
Rcp_StatusCode Rcp_Response::statusCode
```

**描述**

响应状态码。

#### \[h2\]timeInfo

```cpp
Rcp_TimeInfo* Rcp_Response::timeInfo
```

**描述**

响应时间信息。

是否收集该信息取决于[Rcp\_TracingConfiguration.collectTimeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___tracing_configuration#collecttimeinfo)文件中的配置信息。
