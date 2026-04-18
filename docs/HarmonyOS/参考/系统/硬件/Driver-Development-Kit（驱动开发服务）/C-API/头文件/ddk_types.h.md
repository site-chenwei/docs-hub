---
title: "ddk_types.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ddk-types-h"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Driver Development Kit（驱动开发服务）"
  - "C API"
  - "头文件"
  - "ddk_types.h"
captured_at: "2026-04-17T01:48:32.512Z"
---

# ddk\_types.h

#### 概述

提供基础DDK接口所使用的Base DDK类型，宏定义，枚举值和数据结构。

**引用文件：** <ddk/ddk\_types.h>

**库：** libddk\_base.z.so

**系统能力：** SystemCapability.Driver.DDK.Extension

**起始版本：** 12

**相关模块：** [Ddk](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [DDK\_Ashmem](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-baseddk-ddk-ashmem) | DDK\_Ashmem | 定义通过接口**OH\_DDK\_CreateAshmem**创建的共享内存，共享内存的缓冲区提供更好的性能。 |

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [DDK\_RetCode](#ddk_retcode) | DDK\_RetCode | 枚举基本DDK中使用的错误代码。 |

#### 枚举类型说明

#### \[h2\]DDK\_RetCode

```c
enum DDK_RetCode
```

**描述**

枚举基本DDK中使用的错误代码。

**起始版本：** 12

| 枚举项 | 描述 |
| :-- | :-- |
| DDK\_SUCCESS = 0 | 操作成功 |
| DDK\_FAILURE = 28600001 | 操作失败 |
| DDK\_INVALID\_PARAMETER = 28600002 | 无效参数 |
| DDK\_INVALID\_OPERATION = 28600003 | 无效操作 |
| DDK\_NULL\_PTR = 28600004 | 空指针异常 |
