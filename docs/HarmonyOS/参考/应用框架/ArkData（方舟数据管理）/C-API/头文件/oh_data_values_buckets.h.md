---
title: "oh_data_values_buckets.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-data-values-buckets-h"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkData（方舟数据管理）"
  - "C API"
  - "头文件"
  - "oh_data_values_buckets.h"
captured_at: "2026-04-17T01:47:50.115Z"
---

# oh\_data\_values\_buckets.h

#### 概述

提供与存储数据值相关的结构定义、函数和枚举。

**引用文件：** <database/data/oh\_data\_values\_buckets.h>

**库：** libnative\_rdb\_ndk.z.so

**系统能力：** SystemCapability.DistributedDataManager.RelationalStore.Core

**起始版本：** 18

**相关模块：** [RDB](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets) | OH\_Data\_VBuckets | 定义OH\_Data\_VBuckets结构类型。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Data\_VBuckets \*OH\_VBuckets\_Create(void)](#oh_vbuckets_create) | 创建OH\_Data\_VBuckets实例。 |
| [int OH\_VBuckets\_Destroy(OH\_Data\_VBuckets \*buckets)](#oh_vbuckets_destroy) | 销毁OH\_Data\_VBuckets对象。 |
| [int OH\_VBuckets\_PutRow(OH\_Data\_VBuckets \*buckets, const OH\_VBucket \*row)](#oh_vbuckets_putrow) | 添加OH\_VBucket类型数据。 |
| [int OH\_VBuckets\_PutRows(OH\_Data\_VBuckets \*buckets, const OH\_Data\_VBuckets \*rows)](#oh_vbuckets_putrows) | 添加OH\_Data\_VBuckets类型数据。 |
| [int OH\_VBuckets\_RowCount(OH\_Data\_VBuckets \*buckets, size\_t \*count)](#oh_vbuckets_rowcount) | 获取OH\_Data\_VBuckets中OH\_VBucket的行数。 |

#### 函数说明

#### \[h2\]OH\_VBuckets\_Create()

```c
OH_Data_VBuckets *OH_VBuckets_Create(void)
```

**描述**

创建OH\_Data\_VBuckets实例。

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets) | 
执行成功时返回指向[OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets)实例的指针。否则返回nullptr。

使用完成后，必须通过[OH\_VBuckets\_Destroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-data-values-buckets-h#oh_vbuckets_destroy)接口释放内存。

 |

#### \[h2\]OH\_VBuckets\_Destroy()

```c
int OH_VBuckets_Destroy(OH_Data_VBuckets *buckets)
```

**描述**

销毁OH\_Data\_VBuckets对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets) \*buckets | 表示指向[OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回错误码。

返回RDB\_OK表示成功。

返回RDB\_E\_INVALID\_ARGS表示无效参数。

 |

#### \[h2\]OH\_VBuckets\_PutRow()

```c
int OH_VBuckets_PutRow(OH_Data_VBuckets *buckets, const OH_VBucket *row)
```

**描述**

添加OH\_VBucket类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets) \*buckets | 表示指向[OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets)实例的指针。 |
| const [OH\_VBucket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-vbucket) \*row | 表示指向[OH\_VBucket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-vbucket)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回错误码。

返回RDB\_OK表示成功。

返回RDB\_E\_INVALID\_ARGS表示无效参数。

 |

#### \[h2\]OH\_VBuckets\_PutRows()

```c
int OH_VBuckets_PutRows(OH_Data_VBuckets *buckets, const OH_Data_VBuckets *rows)
```

**描述**

添加OH\_Data\_VBuckets类型数据。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets) \*buckets | 表示指向[OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets)实例的指针。 |
| const [OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets) \*rows | 表示指向[OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets)实例的指针。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回错误码。

返回RDB\_OK表示成功。

返回RDB\_E\_INVALID\_ARGS表示无效参数。

 |

#### \[h2\]OH\_VBuckets\_RowCount()

```c
int OH_VBuckets_RowCount(OH_Data_VBuckets *buckets, size_t *count)
```

**描述**

获取OH\_Data\_VBuckets中OH\_VBucket的行数。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets) \*buckets | 表示指向[OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets)实例的指针。 |
| size\_t \*count | 一个输出参数，表示[OH\_Data\_VBuckets](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-data-vbuckets)中[OH\_VBucket](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-rdb-oh-vbucket)的个数。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| int | 
返回错误码。

返回RDB\_OK表示成功。

返回RDB\_E\_INVALID\_ARGS表示无效参数。

 |
