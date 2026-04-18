---
title: "DateTimeRule"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-datetimerule"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "结构体"
  - "DateTimeRule"
captured_at: "2026-04-17T01:48:16.768Z"
---

# DateTimeRule

```c
typedef struct DateTimeRule {...} DateTimeRule
```

#### 概述

时间日期规则。

**起始版本：** 22

**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)

**所在头文件：** [timezone.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t month | 月份。 |
| int32\_t dayOfMonth | 当月的第几天。 |
| int32\_t dayOfWeek | 当周的第几天。 |
| int32\_t weekInMonth | 当月的第几周。 |
| int32\_t millisInDay | 从当天凌晨0点开始到当前时间的毫秒值。 |
| [DateRuleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h#dateruletype) dateRuleType | 日期规则类型。 |
| [TimeRuleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h#timeruletype) timeRuleType | 时间规则类型。 |
