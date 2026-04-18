---
title: "Rcp_Request"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_Request"
captured_at: "2026-04-17T01:48:26.530Z"
---

# Rcp\_Request

#### 概述

网络请求。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char [id](#id) \[[RCP\_MAX\_REQUEST\_ID\_LEN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_max_request_id_len)\] | 每个请求的唯一ID。由系统生成。 |
| char \* [url](#url) | 请求URL。 |
| const char \* [method](#method) | 请求方法。默认值为GET。 |
| [Rcp\_Headers](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_headers) \* [headers](#headers) | 请求标头。 |
| [Rcp\_RequestContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content) \* [content](#content) | 请求体。 |
| [Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration) \* [configuration](#configuration) | 请求配置。请参见[Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)。 |
| [Rcp\_TransferRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___transfer_range) \* [transferRange](#transferrange) | HTTP传输范围。该设置将转换为HTTP Range标头。 |
| [Rcp\_RequestCookies](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_requestcookies) \* [cookies](#cookies) | 请求Cookie。该设置将转换为HTTP Cookie标头。 |
| void \* [requestPrivate](#requestprivate) | 可扩展字段。 |

#### 结构体成员变量说明

#### \[h2\]configuration

```cpp
Rcp_Configuration* Rcp_Request::configuration
```

**描述**

请求配置。请参见[Rcp\_Configuration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___configuration)。

#### \[h2\]content

```cpp
Rcp_RequestContent* Rcp_Request::content
```

**描述**

请求体。

#### \[h2\]cookies

```cpp
Rcp_RequestCookies* Rcp_Request::cookies
```

**描述**

请求Cookie。该设置将转换为HTTP Cookie标头。

#### \[h2\]headers

```cpp
Rcp_Headers* Rcp_Request::headers
```

**描述**

请求标头。

#### \[h2\]id

```cpp
char Rcp_Request::id[RCP_MAX_REQUEST_ID_LEN]
```

**描述**

每个请求的唯一ID。由系统生成。

#### \[h2\]method

```cpp
const char* Rcp_Request::method
```

**描述**

请求方法。默认值为GET。

#### \[h2\]requestPrivate

```cpp
void* Rcp_Request::requestPrivate
```

**描述**

可扩展字段。

#### \[h2\]transferRange

```cpp
Rcp_TransferRange* Rcp_Request::transferRange
```

**描述**

HTTP传输范围。该设置将转换为HTTP Range标头。

#### \[h2\]url

```cpp
char* Rcp_Request::url
```

**描述**

请求URL。
