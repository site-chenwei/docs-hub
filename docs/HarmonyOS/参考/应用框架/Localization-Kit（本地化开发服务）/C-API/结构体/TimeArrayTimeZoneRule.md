---
title: "TimeArrayTimeZoneRule"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "结构体"
  - "TimeArrayTimeZoneRule"
captured_at: "2026-04-17T01:48:16.784Z"
---

# TimeArrayTimeZoneRule

```c
typedef struct TimeArrayTimeZoneRule {...} TimeArrayTimeZoneRule
```

#### 概述

起始时间戳数组定义的时区规则。

**起始版本：** 22

**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)

**所在头文件：** [timezone.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* name | 时区规则的名称。 |
| int32\_t rawOffset | 时区的原始偏移量。 |
| int32\_t dstSavings | 夏令时的偏移量。 |
| double\* startTimes | 规则生效的起始时间戳数组。 |
| int32\_t numStartTimes | 规则生效的起始时间戳数组的大小。 |
| [TimeRuleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h#timeruletype) timeRuleType | 时间规则类型。 |
