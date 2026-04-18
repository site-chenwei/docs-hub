---
title: "Rcp_FormFieldValue"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value"
menu_path:
  - "参考"
  - "系统"
  - "网络"
  - "Remote Communication Kit（远场通信服务）"
  - "C API"
  - "结构体"
  - "Rcp_FormFieldValue"
captured_at: "2026-04-17T01:48:26.316Z"
---

# Rcp\_FormFieldValue

#### 概述

简单表单数据字段值，参见[Rcp\_Form](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_form)和[Rcp\_MultipartFormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___multipart_form_field_value)。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview)

**所在头文件：** [rcp.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/rcp_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Rcp\_FormValueType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/remote-communication-overview#rcp_formvaluetype)[type](#type) | 表示union中使用的数据类型。 |
| 
union {

uint8\_t [varBool](#varbool)

int32\_t [varInt32](#varint32)

int64\_t [varInt64](#varint64)

double [varDouble](#vardouble)

[Rcp\_Buffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___buffer) [varStr](#varstr)

}

 | 

bool类型。

int32类型。

int64类型。

double类型。

string类型。

 |
| struct [Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value) \* [next](#next) | 指向下一个[Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value)。链式存储。 |

#### 结构体成员变量说明

#### \[h2\]next

```cpp
struct Rcp_FormFieldValue* Rcp_FormFieldValue::next
```

**描述**

指向下一个[Rcp\_FormFieldValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___form_field_value)。链式存储。

#### \[h2\]type

```cpp
Rcp_FormValueType Rcp_FormFieldValue::type
```

**描述**

表示union中使用的数据类型。

#### \[h2\]varBool

```cpp
uint8_t Rcp_FormFieldValue::varBool
```

**描述**

bool类型。

#### \[h2\]varDouble

```cpp
double Rcp_FormFieldValue::varDouble
```

**描述**

double类型。

#### \[h2\]varInt32

```cpp
int32_t Rcp_FormFieldValue::varInt32
```

**描述**

int32类型。

#### \[h2\]varInt64

```cpp
int64_t Rcp_FormFieldValue::varInt64
```

**描述**

int64类型。

#### \[h2\]varStr

```cpp
Rcp_Buffer Rcp_FormFieldValue::varStr
```

**描述**

string类型。
