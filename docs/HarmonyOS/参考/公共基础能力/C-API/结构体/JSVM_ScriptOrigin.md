---
title: "JSVM_ScriptOrigin"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-scriptorigin"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_ScriptOrigin"
captured_at: "2026-04-17T01:49:06.556Z"
---

# JSVM\_ScriptOrigin

```c
typedef struct {...} JSVM_ScriptOrigin
```

#### 概述

某段JavaScript代码的原始信息，如sourceMap路径、源文件名、源文件中的起始行/列号等。

**起始版本：** 12

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char\* sourceMapUrl | Sourcemap 路径。 |
| const char\* resourceName | 源文件名。 |
| size\_t resourceLineOffset | 这段代码在源文件中的起始行号。 |
| size\_t resourceColumnOffset | 这段代码在源文件中的起始列号。 |
