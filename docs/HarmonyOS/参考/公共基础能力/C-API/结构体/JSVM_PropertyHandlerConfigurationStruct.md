---
title: "JSVM_PropertyHandlerConfigurationStruct"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-propertyhandlerconfigurationstruct"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_PropertyHandlerConfigurationStruct"
captured_at: "2026-04-17T01:49:06.572Z"
---

# JSVM\_PropertyHandlerConfigurationStruct

```c
typedef struct {...} JSVM_PropertyHandlerConfigurationStruct
```

#### 概述

当执行对象的getter、setter、deleter和enumerator操作时，该结构体中对应的函数回调将会触发。

**起始版本：** 12

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [JSVM\_Value](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-value--8h) namedPropertyData | 命名属性回调使用的数据。 |
| [JSVM\_Value](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-value--8h) indexedPropertyData | 索引属性回调使用的数据。 |

#### \[h2\]成员函数

| 名称 | 描述 |
| :-- | :-- |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyGetterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](#genericnamedpropertygettercallback) | 通过获取实例对象的命名属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertySetterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value property,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](#genericnamedpropertysettercallback) | 通过设置实例对象的命名属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyDeleterCallback)(JSVM\_Env env,JSVM\_Value name,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](#genericnamedpropertydeletercallback) | 通过删除实例对象的命名属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericNamedPropertyEnumeratorCallback)(JSVM\_Env env,JSVM\_Value thisArg,JSVM\_Value namedPropertyData)](#genericnamedpropertyenumeratorcallback) | 通过获取对象上的所有命名属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyGetterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](#genericindexedpropertygettercallback) | 通过获取实例对象的索引属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertySetterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value property,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](#genericindexedpropertysettercallback) | 通过设置实例对象的索引属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyDeleterCallback)(JSVM\_Env env,JSVM\_Value index,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](#genericindexedpropertydeletercallback) | 通过删除实例对象的索引属性而触发的回调函数。 |
| [JSVM\_Value (JSVM\_CDECL\* genericIndexedPropertyEnumeratorCallback)(JSVM\_Env env,JSVM\_Value thisArg,JSVM\_Value indexedPropertyData)](#genericindexedpropertyenumeratorcallback) | 通过获取对象上的所有索引属性而触发的回调函数。 |

#### 成员函数说明

#### \[h2\]genericNamedPropertyGetterCallback()

```c
JSVM_Value (JSVM_CDECL* genericNamedPropertyGetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过获取实例对象的命名属性而触发的回调函数。

#### \[h2\]genericNamedPropertySetterCallback()

```c
JSVM_Value (JSVM_CDECL* genericNamedPropertySetterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value property,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过设置实例对象的命名属性而触发的回调函数。

#### \[h2\]genericNamedPropertyDeleterCallback()

```c
JSVM_Value (JSVM_CDECL* genericNamedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value name,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过删除实例对象的命名属性而触发的回调函数。

#### \[h2\]genericNamedPropertyEnumeratorCallback()

```c
JSVM_Value (JSVM_CDECL* genericNamedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value namedPropertyData)
```

**描述**

通过获取对象上的所有命名属性而触发的回调函数。

#### \[h2\]genericIndexedPropertyGetterCallback()

```c
JSVM_Value (JSVM_CDECL* genericIndexedPropertyGetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过获取实例对象的索引属性而触发的回调函数。

#### \[h2\]genericIndexedPropertySetterCallback()

```c
JSVM_Value (JSVM_CDECL* genericIndexedPropertySetterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value property,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过设置实例对象的索引属性而触发的回调函数。

#### \[h2\]genericIndexedPropertyDeleterCallback()

```c
JSVM_Value (JSVM_CDECL* genericIndexedPropertyDeleterCallback)(JSVM_Env env,JSVM_Value index,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过删除实例对象的索引属性而触发的回调函数。

#### \[h2\]genericIndexedPropertyEnumeratorCallback()

```c
JSVM_Value (JSVM_CDECL* genericIndexedPropertyEnumeratorCallback)(JSVM_Env env,JSVM_Value thisArg,JSVM_Value indexedPropertyData)
```

**描述**

通过获取对象上的所有索引属性而触发的回调函数。
