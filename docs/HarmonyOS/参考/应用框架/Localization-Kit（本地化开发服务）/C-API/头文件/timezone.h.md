---
title: "timezone.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "头文件"
  - "timezone.h"
captured_at: "2026-04-17T01:48:16.616Z"
---

# timezone.h

#### 概述

提供获取时区信息的能力。

**引用文件：** <i18n/timezone.h>

**库：** libohi18n.so

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)

#### 汇总

#### \[h2\]结构体

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [DateTimeRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-datetimerule) | DateTimeRule | 时间日期规则。 |
| [InitialTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-initialtimezonerule) | InitialTimeZoneRule | 起始时区规则。 |
| [TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule) | TimeArrayTimeZoneRule | 起始时间戳数组定义的时区规则。 |
| [AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule) | AnnualTimeZoneRule | 每年生效的时区规则。 |
| [TimeZoneRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerules) | TimeZoneRules | 完整的时区规则。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery) | TimeZoneRuleQuery | 用于传入查询的信息，并接收查询的结果。 |

#### \[h2\]枚举

| 名称 | typedef关键字 | 描述 |
| :-- | :-- | :-- |
| [DateRuleType](#dateruletype) | DateRuleType | 日期规则类型的枚举。 |
| [TimeRuleType](#timeruletype) | TimeRuleType | 时间规则类型的枚举。 |

#### \[h2\]宏定义

| 名称 | 描述 |
| :-- | :-- |
| MAX\_YEAR\_IN\_ANNUAL\_TIMEZONE\_RULE 0x7fffffff | 
每年生效时区规则的年份最大值。

**起始版本：** 22

 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [I18n\_ErrorCode OH\_i18n\_GetTimeZoneRules(const char\* timeZoneID, TimeZoneRules\* rules)](#oh_i18n_gettimezonerules) | 通过时区ID，获取完整的时区规则。 |
| [I18n\_ErrorCode OH\_i18n\_GetFirstStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](#oh_i18n_getfirststartfromtimearraytimezonerule) | 根据TimeArrayTimeZoneRule，获取时区规则的首次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetFirstStartFromAnnualTimeZoneRule(AnnualTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](#oh_i18n_getfirststartfromannualtimezonerule) | 根据AnnualTimeZoneRule，获取时区规则的首次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetFinalStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](#oh_i18n_getfinalstartfromtimearraytimezonerule) | 根据TimeArrayTimeZoneRule，获取时区规则的最后一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetFinalStartFromAnnualTimeZoneRule(AnnualTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](#oh_i18n_getfinalstartfromannualtimezonerule) | 根据AnnualTimeZoneRule，获取时区规则的最后一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetNextStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](#oh_i18n_getnextstartfromtimearraytimezonerule) | 根据TimeArrayTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetNextStartFromAnnualTimeZoneRule(AnnualTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](#oh_i18n_getnextstartfromannualtimezonerule) | 根据AnnualTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetPrevStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](#oh_i18n_getprevstartfromtimearraytimezonerule) | 根据TimeArrayTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetPrevStartFromAnnualTimeZoneRule(AnnualTimeZoneRule\* rule, TimeZoneRuleQuery\* query)](#oh_i18n_getprevstartfromannualtimezonerule) | 根据AnnualTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetStartTimeAt(TimeArrayTimeZoneRule\* rule, int32\_t index, double\* result)](#oh_i18n_getstarttimeat) | 根据TimeArrayTimeZoneRule，获取时区规则指定索引的起始时间。 |
| [I18n\_ErrorCode OH\_i18n\_GetStartInYear(AnnualTimeZoneRule\* rule, int32\_t year, TimeZoneRuleQuery\* query)](#oh_i18n_getstartinyear) | 根据AnnualTimeZoneRule，获取时区规则在指定年份的生效时间。 |

#### 枚举类型说明

#### \[h2\]DateRuleType

```c
enum DateRuleType
```

**描述**

日期规则类型的枚举。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

| 枚举项 | 描述 |
| :-- | :-- |
| DOM = 0 | 当月的第几天，以2025年为例，十月十六日为：十月的第十六天。 |
| DOW = 1 | 当月的第几个星期几，以2025年为例，十月十六日为：十月的第三个星期四。 |
| DOW\_GEQ\_DOM = 2 | 当月第几天之后的第一个星期几，以2025年为例，十月十六日为：十月第十三天/十四天/十五天之后的第一个星期四。 |
| DOW\_LEQ\_DOM = 3 | 当月第几天之前的最后一个星期几，以2025年为例，十月十六日为：十月第二十天之前的最后一个星期四。 |

#### \[h2\]TimeRuleType

```c
enum TimeRuleType
```

**描述**

时间规则类型的枚举。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

| 枚举项 | 描述 |
| :-- | :-- |
| WALL\_TIME = 0 | 本地时钟时间（不考虑时区偏移）。 |
| STANDARD\_TIME = 1 | 本地标准时间（不考虑夏令时偏移）。 |
| UTC\_TIME = 2 | 世界标准时间（UTC时间）。 |

#### 函数说明

#### \[h2\]OH\_i18n\_GetTimeZoneRules()

```c
I18n_ErrorCode OH_i18n_GetTimeZoneRules(const char* timeZoneID, TimeZoneRules* rules)
```

**描述**

通过时区ID，获取完整的时区规则。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| const char\* timeZoneID | 时区ID，例如“Asia/Shanghai”。 |
| [TimeZoneRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerules)\* rules | 与时区ID对应的完整时区规则[TimeZoneRules](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerules)。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetFirstStartFromTimeArrayTimeZoneRule()

```c
I18n_ErrorCode OH_i18n_GetFirstStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则的首次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetFirstStartFromAnnualTimeZoneRule()

```c
I18n_ErrorCode OH_i18n_GetFirstStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则的首次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetFinalStartFromTimeArrayTimeZoneRule()

```c
I18n_ErrorCode OH_i18n_GetFinalStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则的最后一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetFinalStartFromAnnualTimeZoneRule()

```c
I18n_ErrorCode OH_i18n_GetFinalStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则的最后一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetNextStartFromTimeArrayTimeZoneRule()

```c
I18n_ErrorCode OH_i18n_GetNextStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetNextStartFromAnnualTimeZoneRule()

```c
I18n_ErrorCode OH_i18n_GetNextStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则在基准时间之后的下一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetPrevStartFromTimeArrayTimeZoneRule()

```c
I18n_ErrorCode OH_i18n_GetPrevStartFromTimeArrayTimeZoneRule(TimeArrayTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetPrevStartFromAnnualTimeZoneRule()

```c
I18n_ErrorCode OH_i18n_GetPrevStartFromAnnualTimeZoneRule(AnnualTimeZoneRule* rule, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则在基准时间之前的上一次生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetStartTimeAt()

```c
I18n_ErrorCode OH_i18n_GetStartTimeAt(TimeArrayTimeZoneRule* rule, int32_t index, double* result)
```

**描述**

根据TimeArrayTimeZoneRule，获取时区规则指定索引的起始时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)\* rule | 起始时间戳数组定义的时区规则[TimeArrayTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timearraytimezonerule)。 |
| int32\_t index | 起始时间的索引。 |
| double\* result | 规则生效的起始时间。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |

#### \[h2\]OH\_i18n\_GetStartInYear()

```c
I18n_ErrorCode OH_i18n_GetStartInYear(AnnualTimeZoneRule* rule, int32_t year, TimeZoneRuleQuery* query)
```

**描述**

根据AnnualTimeZoneRule，获取时区规则在指定年份的生效时间。

**系统能力：** SystemCapability.Global.I18n

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| :-- | :-- |
| [AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)\* rule | 每年生效的时区规则[AnnualTimeZoneRule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-annualtimezonerule)。 |
| int32\_t year | 查询的年份。 |
| [TimeZoneRuleQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery)\* query | 用于传入查询的信息，并接收查询的结果。 |

**返回：**

| 类型 | 说明 |
| :-- | :-- |
| [I18n\_ErrorCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-errorcode-h#i18n_errorcode) | 
0 - 成功。

8900001 - 传入参数无效。

8900050 - 预期之外的错误，例如内存错误。

 |
