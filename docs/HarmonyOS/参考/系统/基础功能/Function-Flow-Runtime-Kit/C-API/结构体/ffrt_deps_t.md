---
title: "ffrt_deps_t"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-deps-t"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Function Flow Runtime Kit"
  - "C API"
  - "结构体"
  - "ffrt_deps_t"
captured_at: "2026-04-17T01:48:30.277Z"
---

# ffrt\_deps\_t

```c
typedef struct {...} ffrt_deps_t
```

#### 概述

依赖结构定义。

**起始版本：** 10

**相关模块：** [FFRT](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt)

**所在头文件：** [type\_def.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-type-def-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t len | 依赖数量 |
| const [ffrt\_dependence\_t\*](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ffrt-ffrt-dependence-t) items | 依赖数据 |
