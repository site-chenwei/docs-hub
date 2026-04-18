---
title: "TimeZoneRuleQuery"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n-timezonerulequery"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "C API"
  - "结构体"
  - "TimeZoneRuleQuery"
captured_at: "2026-04-17T01:48:16.804Z"
---

# TimeZoneRuleQuery

```c
typedef struct TimeZoneRuleQuery {...} TimeZoneRuleQuery
```

#### 概述

用于传入查询的信息，并接收查询的结果。

**起始版本：** 22

**相关模块：** [i18n](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-i18n)

**所在头文件：** [timezone.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-timezone-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| double base | 查询的基准时间。 |
| int32\_t prevRawOffset | 上一次的时区原始偏移量。 |
| int32\_t prevDSTSavings | 上一次的夏令时偏移量。 |
| bool inclusive | 查询结果是否包含基准时间。true：查询结果包含基准时间；false：查询结果不包含基准时间。 |
| double result | 查询结果。 |
