---
title: "JSVM_ExtendedErrorInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-extendederrorinfo"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_ExtendedErrorInfo"
captured_at: "2026-04-17T01:49:06.549Z"
---

# JSVM\_ExtendedErrorInfo

```c
typedef struct {...} JSVM_ExtendedErrorInfo
```

#### 概述

扩展的异常信息。

**起始版本：** 11

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char\* errorMessage | UTF-8编码的字符串，包含异常信息。 |
| void\* engineReserved | 特定于VM的详细异常信息。目前尚未为任何VM实现此功能。 |
| uint32\_t engineErrorCode | 特定于VM的异常代码。目前尚未为任何VM实现此功能。 |
| JSVM\_Status errorCode | 源自最后一个异常的JSVM-API状态码。 |
