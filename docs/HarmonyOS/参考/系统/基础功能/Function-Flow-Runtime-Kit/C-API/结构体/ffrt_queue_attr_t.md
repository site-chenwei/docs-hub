---
title: "ffrt_queue_attr_t"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-queue-attr-t"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Function Flow Runtime Kit"
  - "C API"
  - "结构体"
  - "ffrt_queue_attr_t"
captured_at: "2026-04-17T01:48:30.293Z"
---

# ffrt\_queue\_attr\_t

```c
typedef struct {...} ffrt_queue_attr_t
```

#### 概述

串行队列属性结构。

**起始版本：** 10

**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)

**所在头文件：** [type\_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t storage\[(ffrt\_queue\_attr\_storage\_size + sizeof(uint32\_t) - 1) / sizeof(uint32\_t)\] | 串行队列属性占用空间 |
