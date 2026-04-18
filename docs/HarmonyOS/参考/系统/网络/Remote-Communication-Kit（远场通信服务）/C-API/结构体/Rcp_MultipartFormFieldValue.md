---
title: "Rcp_MultipartFormFieldValue"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_MultipartFormFieldValue"
captured_at: "2026-04-17T01:48:26.476Z"
---

# Rcp\_MultipartFormFieldValue

#### 概述

多部分表单域值，在[Rcp\_MultipartForm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_multipartform)中使用。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_MultipartValueType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_multipartvaluetype) [type](#type) | 表示union中使用的数据类型。 |
| 
union {

[Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value) [formValue](#formvalue)

[Rcp\_FormFieldFileValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_file_value) [formFileValue](#formfilevalue)

}

 | 

formValue：简单表单数据字段值。

formFileValue：简单表单数据字段文件值。

 |
| struct [Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value) \* [next](#next) | 指向下一个[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。链式存储。 |

#### 结构体成员变量说明

#### \[h2\]formFileValue

```cpp
Rcp_FormFieldFileValue Rcp_MultipartFormFieldValue::formFileValue
```

**描述**

简单表单数据字段文件值。

#### \[h2\]formValue

```cpp
Rcp_FormFieldValue Rcp_MultipartFormFieldValue::formValue
```

**描述**

简单表单数据字段值。

#### \[h2\]next

```cpp
struct Rcp_MultipartFormFieldValue* Rcp_MultipartFormFieldValue::next
```

**描述**

指向下一个[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。链式存储。

#### \[h2\]type

```cpp
Rcp_MultipartValueType Rcp_MultipartFormFieldValue::type
```

**描述**

表示union中使用的数据类型。
