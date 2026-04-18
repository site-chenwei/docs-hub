---
title: "ArkUI_AccessibleRangeInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblerangeinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_AccessibleRangeInfo"
captured_at: "2026-04-17T01:48:08.906Z"
---

# ArkUI\_AccessibleRangeInfo

```c
typedef struct {...} ArkUI_AccessibleRangeInfo
```

#### 概述

用于为特定组件（如[Slider](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-slider)、[Rating](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-rating)、[Progress](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-progress)组件）设置和获取其当前值、最大值和最小值。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility)

**所在头文件：** [native\_interface\_accessibility.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-accessibility-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| double min | 组件的最小值。 |
| double max | 组件的最大值。 |
| double current | 组件的当前值。 |
