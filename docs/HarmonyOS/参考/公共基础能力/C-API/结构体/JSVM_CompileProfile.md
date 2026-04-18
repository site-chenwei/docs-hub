---
title: "JSVM_CompileProfile"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-compileprofile"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_CompileProfile"
captured_at: "2026-04-17T01:49:06.952Z"
---

# JSVM\_CompileProfile

```c
typedef const struct {...} JSVM_CompileProfile
```

#### 概述

与JSVM\_COMPILE\_COMPILE\_PROFILE一起传递的编译采样文件。

**起始版本：** 12

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int \*profile | 编译采样文件的指针。 |
| size\_t length | 编译采样文件的大小。 |
