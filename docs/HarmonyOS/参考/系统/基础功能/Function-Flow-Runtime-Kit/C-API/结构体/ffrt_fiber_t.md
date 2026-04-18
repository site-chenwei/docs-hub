---
title: "ffrt_fiber_t"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-fiber-t"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Function Flow Runtime Kit"
  - "C API"
  - "结构体"
  - "ffrt_fiber_t"
captured_at: "2026-04-17T01:48:30.456Z"
---

# ffrt\_fiber\_t

```c
typedef struct {...} ffrt_fiber_t
```

#### 概述

纤程结构。

**起始版本：** 20

**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)

**所在头文件：** [type\_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uintptr\_t storage\[ffrt\_fiber\_storage\_size\] | 纤程上下文占用空间。 |
