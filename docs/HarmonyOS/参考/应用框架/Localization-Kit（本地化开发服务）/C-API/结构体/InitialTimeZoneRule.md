---
title: "InitialTimeZoneRule"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-initialtimezonerule"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "结构体"
  - "InitialTimeZoneRule"
captured_at: "2026-04-17T01:48:16.782Z"
---

# InitialTimeZoneRule

```c
typedef struct InitialTimeZoneRule {...} InitialTimeZoneRule
```

#### 概述

起始时区规则。

**起始版本：** 22

**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)

**所在头文件：** [timezone.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t rawOffset | 时区的原始偏移量。 |
| int32\_t dstSavings | 夏令时的偏移量。 |
