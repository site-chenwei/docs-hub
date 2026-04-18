---
title: "HiDebug_SystemMemInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-systemmeminfo"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "C API"
  - "结构体"
  - "HiDebug_SystemMemInfo"
captured_at: "2026-04-17T01:48:35.100Z"
---

# HiDebug\_SystemMemInfo

```c
typedef struct HiDebug_SystemMemInfo {...} HiDebug_SystemMemInfo
```

#### 概述

系统内存信息结构类型定义。

**起始版本：** 12

**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)

**所在头文件：** [hidebug\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t totalMem | 系统总的内存，以KB为单位。 |
| uint32\_t freeMem | 系统空闲的内存，以KB为单位。 |
| uint32\_t availableMem | 系统可用的内存，以KB为单位。 |
