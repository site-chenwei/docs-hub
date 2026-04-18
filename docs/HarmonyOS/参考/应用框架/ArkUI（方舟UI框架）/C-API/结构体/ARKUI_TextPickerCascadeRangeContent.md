---
title: "ARKUI_TextPickerCascadeRangeContent"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/i-nativemodule-arkui-textpickercascaderangecontent"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "C API"
  - "结构体"
  - "ARKUI_TextPickerCascadeRangeContent"
captured_at: "2026-04-17T01:48:09.414Z"
---

# ARKUI\_TextPickerCascadeRangeContent

```c
typedef struct {...} ARKUI_TextPickerCascadeRangeContent
```

#### 概述

定义多列联动滑动数据选择器的结构体。

**起始版本：** 12

**相关模块：** [ArkUI\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-arkui-nativemodule)

**所在头文件：** [native\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char\* text | 文本信息。 |
| const [ARKUI\_TextPickerRangeContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pi-arkui-nativemodule-arkui-textpickerrangecontent)\* children | 联动数据。 |
| int32\_t size | 联动数据数组大小。 |
