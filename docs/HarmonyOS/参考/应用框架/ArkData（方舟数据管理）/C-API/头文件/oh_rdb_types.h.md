---
title: "oh_rdb_types.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-types-h"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "头文件"
  - "oh_rdb_types.h"
captured_at: "2026-04-17T01:47:50.211Z"
---

# oh\_rdb\_types.h

#### 概述

提供与数据值相关的类型定义。

**引用文件：** <database/rdb/oh\_rdb\_types.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 18

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext) | OH\_RDB\_ReturningContext | returning相关接口的上下文。 |

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [Rdb\_ConflictResolution](#rdb_conflictresolution) | Rdb\_ConflictResolution | 表示冲突解决策略的枚举。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_RDB\_ReturningContext \*OH\_RDB\_CreateReturningContext(void)](#oh_rdb_createreturningcontext) | 创建[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)的实例对象。 |
| [void OH\_RDB\_DestroyReturningContext(OH\_RDB\_ReturningContext \*context)](#oh_rdb_destroyreturningcontext) | 销毁[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)实例对象。 |
| [int OH\_RDB\_SetReturningFields(OH\_RDB\_ReturningContext \*context, const char \*const fields\[\], int32\_t len)](#oh_rdb_setreturningfields) | 设置结果集中返回的字段。 |
| [int OH\_RDB\_SetMaxReturningCount(OH\_RDB\_ReturningContext \*context, int32\_t count)](#oh_rdb_setmaxreturningcount) | 设置返回结果集的最大行数量。 |
| [OH\_Cursor \*OH\_RDB\_GetReturningValues(OH\_RDB\_ReturningContext \*context)](#oh_rdb_getreturningvalues) | 获取数据变化的游标，默认包含1024条。 |
| [int64\_t OH\_RDB\_GetChangedCount(OH\_RDB\_ReturningContext \*context)](#oh_rdb_getchangedcount) | 获取受此操作影响的数据行的数量。 |

#### 枚举类型说明

#### \[h2\]Rdb\_ConflictResolution

```c
enum Rdb_ConflictResolution
```

**描述**

表示冲突解决策略的枚举。

**起始版本：** 18

| 枚举项 | 描述 |
| :-- | :-- |
| RDB\_CONFLICT\_NONE = 1 | 发生冲突时不执行任何操作。 |
| RDB\_CONFLICT\_ROLLBACK | 发生冲突时抛错误码，同时回滚本次事务。 |
| RDB\_CONFLICT\_ABORT | 发生冲突时抛错误码，同时回滚本次修改。 |
| RDB\_CONFLICT\_FAIL | 发生冲突时抛错误码，不回滚冲突前的修改同时终止本次修改。 |
| RDB\_CONFLICT\_IGNORE | 发生冲突时忽略冲突的数据，继续执行后续修改。 |
| RDB\_CONFLICT\_REPLACE | 发生冲突时，尝试删除后插入，如果还是冲突则等同于RDB\_CONFLICT\_ABORT。 |

#### 函数说明

#### \[h2\]OH\_RDB\_CreateReturningContext()

```c
OH_RDB_ReturningContext *OH_RDB_CreateReturningContext(void)
```

**描述**

创建[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)的实例对象。

**起始版本：** 23

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_RDB\_ReturningContext \*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext) | 
执行成功时返回指向[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)实例的指针。

否则返回nullptr。使用完成后必须通过[OH\_RDB\_DestroyReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-types-h#oh_rdb_destroyreturningcontext)接口释放内存。

 |

#### \[h2\]OH\_RDB\_DestroyReturningContext()

```c
void OH_RDB_DestroyReturningContext(OH_RDB_ReturningContext *context)
```

**描述**

销毁[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)实例对象。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext) \*context | 指向[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)实例的指针。 |

#### \[h2\]OH\_RDB\_SetReturningFields()

```c
int OH_RDB_SetReturningFields(OH_RDB_ReturningContext *context, const char *const fields[], int32_t len)
```

**描述**

设置结果集中返回的字段。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext) \*context | 指向[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)实例的指针。 |
| const char \*const fields\[\] | 要返回的列名。 |
| int32\_t len | 字段长度。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行结果。

执行成功返回RDB\_OK。

输入参数无效返回RDB\_E\_INVALID\_ARGS。

 |

#### \[h2\]OH\_RDB\_SetMaxReturningCount()

```c
int OH_RDB_SetMaxReturningCount(OH_RDB_ReturningContext *context, int32_t count)
```

**描述**

设置返回结果集的最大行数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext) \*context | 指向[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)实例的指针。 |
| int32\_t count | 表示返回结果集的最大条目数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回执行结果。

执行成功返回RDB\_OK。

输入参数无效返回RDB\_E\_INVALID\_ARGS。

 |

#### \[h2\]OH\_RDB\_GetReturningValues()

```c
OH_Cursor *OH_RDB_GetReturningValues(OH_RDB_ReturningContext *context)
```

**描述**

获取数据变化的游标，默认包含1024条。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext) \*context | 指向[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| OH\_Cursor \* | 
返回指向[OH\_Cursor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-cursor)结构体实例的指针。

如果获取游标失败，则返回nullptr。使用[OH\_RDB\_DestroyReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-rdb-types-h#oh_rdb_destroyreturningcontext)接口释放内存时会销毁游标，无需单独释放。

 |

#### \[h2\]OH\_RDB\_GetChangedCount()

```c
int64_t OH_RDB_GetChangedCount(OH_RDB_ReturningContext *context)
```

**描述**

获取受此操作影响的数据行的数量。

**起始版本：** 23

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext) \*context | 指向[OH\_RDB\_ReturningContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-rdb-returningcontext)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int64\_t | 返回已更改的条目数，如果获取变更失败则返回-1。 |
