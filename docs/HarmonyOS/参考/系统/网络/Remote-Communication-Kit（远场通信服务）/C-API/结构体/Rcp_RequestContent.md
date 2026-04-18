---
title: "Rcp_RequestContent"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___request_content"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_RequestContent"
captured_at: "2026-04-17T01:48:26.593Z"
---

# Rcp\_RequestContent

#### 概述

请求的内容。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_ContentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_contenttype)[type](#type) | 表示union中使用的数据类型。 |
| 
union {

[Rcp\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer) [contentStr](#contentstr)

[Rcp\_Form](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_form) \* [form](#form)

[Rcp\_MultipartForm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_multipartform) \* [multipartForm](#multipartform)

[Rcp\_GetDataCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_getdatacallback) [getDataCallback](#getdatacallback)

}

 | 

contentStr：文本。

form：表单。

multipartForm：多部分表单。

getDataCallback：使用回调函数获取数据。

 |

#### 结构体成员变量说明

#### \[h2\]contentStr

```cpp
Rcp_Buffer Rcp_RequestContent::contentStr
```

**描述**

字符串内容。

#### \[h2\]form

```cpp
Rcp_Form* Rcp_RequestContent::form
```

**描述**

表单内容。

#### \[h2\]getDataCallback

```cpp
Rcp_GetDataCallback Rcp_RequestContent::getDataCallback
```

**描述**

回调函数。

#### \[h2\]multipartForm

```cpp
Rcp_MultipartForm* Rcp_RequestContent::multipartForm
```

**描述**

多部分表单内容。

#### \[h2\]type

```cpp
Rcp_ContentType Rcp_RequestContent::type
```

**描述**

表示union中使用的数据类型。
