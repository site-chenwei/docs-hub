---
title: "Rcp_ContentOrPathOrCallback"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___content_or_path_or_callback"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_ContentOrPathOrCallback"
captured_at: "2026-04-17T01:48:26.033Z"
---

# Rcp\_ContentOrPathOrCallback

#### 概述

[Rcp\_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value)中使用的简单表单数据字段值。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_ContentOrPathOrCallbackType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_contentorpathorcallbacktype)[type](#type) | 表示union中使用的数据类型。 |
| 
union {

[Rcp\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer) [content](#content)

char [path](#path) \[[RCP\_MAX\_PATH\_LEN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_max_path_len)\]

[Rcp\_GetDataCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_getdatacallback) [callback](#callback)

}

 | 

content: 文本数据。

path: 文件路径。

callback: 获取数据的回调函数。

 |

#### 结构体成员变量说明

#### \[h2\]callback

```cpp
Rcp_GetDataCallback Rcp_ContentOrPathOrCallback::callback
```

**描述**

获取数据的回调。

#### \[h2\]content

```cpp
Rcp_Buffer Rcp_ContentOrPathOrCallback::content
```

**描述**

文本数据。

#### \[h2\]path

```cpp
char Rcp_ContentOrPathOrCallback::path[RCP_MAX_PATH_LEN]
```

**描述**

文件路径。

#### \[h2\]type

```cpp
Rcp_ContentOrPathOrCallbackType Rcp_ContentOrPathOrCallback::type
```

**描述**

union中使用的数据类型。
