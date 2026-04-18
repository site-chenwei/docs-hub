---
title: "JSVM_CodeCache"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-codecache"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_CodeCache"
captured_at: "2026-04-17T01:49:06.590Z"
---

# JSVM\_CodeCache

```c
typedef struct {...} JSVM_CodeCache
```

#### 概述

表示当id为JSVM\_COMPILE\_CODE\_CACHE时，content的类型。

**起始版本：** 12

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t\* cache | 缓存地址。 |
| size\_t length | 缓存大小。 |
