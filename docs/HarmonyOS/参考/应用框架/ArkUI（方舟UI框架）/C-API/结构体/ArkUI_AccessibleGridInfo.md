---
title: "ArkUI_AccessibleGridInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility-arkui-accessiblegridinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ArkUI_AccessibleGridInfo"
captured_at: "2026-04-17T01:48:08.985Z"
---

# ArkUI\_AccessibleGridInfo

```c
typedef struct {...} ArkUI_AccessibleGridInfo
```

#### 概述

用于配置特定组件（如[List](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-list)、[Flex](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-flex)、[Select](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-select)、[Swiper](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-swiper)组件）的网格布局属性。

**起始版本：** 13

**相关模块：** [ArkUI\_Accessibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-accessibility)

**所在头文件：** [native\_interface\_accessibility.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-interface-accessibility-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t rowCount | 组件的行数。取值范围为大于0的整数。 |
| int32\_t columnCount | 组件的列数。取值范围为大于0的整数。 |
| int32\_t selectionMode | 值为0时表示仅选中网格的一行，非0值时表示选中网格的多行。 |
