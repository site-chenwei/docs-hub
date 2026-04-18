---
title: "Print_DefaultValue"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-defaultvalue"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Print_DefaultValue"
captured_at: "2026-04-17T01:48:29.137Z"
---

# Print\_DefaultValue

```c
typedef struct {...} Print_DefaultValue
```

#### 概述

表示当前属性。

**起始版本：** 12

**相关模块：** [OH\_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)

**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Print\_ColorMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h#print_colormode) defaultColorMode | 默认色彩模式。 |
| [Print\_DuplexMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h#print_duplexmode) defaultDuplexMode | 默认双面模式。 |
| char \*defaultMediaType | 默认介质类型。 |
| char \*defaultPageSizeId | 默认纸张尺寸 ID。 |
| [Print\_Margin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-margin) defaultMargin | 默认边距。 |
| char \*defaultPaperSource | 默认纸张来源。 |
| [Print\_Quality](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h#print_quality) defaultPrintQuality | 默认打印质量。 |
| uint32\_t defaultCopies | 默认份数。 |
| [Print\_Resolution](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-resolution) defaultResolution | 默认打印机分辨率。 |
| [Print\_OrientationMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h#print_orientationmode) defaultOrientation | 默认方向。 |
| char \*otherDefaultValues | JSON 格式的其他默认值。 |
