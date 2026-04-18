---
title: "JSVM_CallbackStruct"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-callbackstruct"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_CallbackStruct"
captured_at: "2026-04-17T01:49:06.437Z"
---

# JSVM\_CallbackStruct

```c
typedef struct {...} JSVM_CallbackStruct
```

#### 概述

用户提供的Native回调函数的指针和数据，这些函数通过JSVM-API接口暴露给JavaScript。

**起始版本：** 11

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| void\* data | 用户提供的Native回调函数的数据。 |

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [JSVM\_Value(JSVM\_CDECL\* callback)(JSVM\_Env env,JSVM\_CallbackInfo info)](#callback) | 用户提供的Native回调函数的指针。 |

#### 成员函数说明

#### \[h2\]callback()

```c
JSVM_Value(JSVM_CDECL* callback)(JSVM_Env env,JSVM_CallbackInfo info)
```

**描述**

用户提供的Native回调函数的指针。
