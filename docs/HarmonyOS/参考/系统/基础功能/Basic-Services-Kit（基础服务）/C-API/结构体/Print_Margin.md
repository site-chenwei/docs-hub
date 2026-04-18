---
title: "Print_Margin"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-margin"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Print_Margin"
captured_at: "2026-04-17T01:48:29.103Z"
---

# Print\_Margin

```c
typedef struct {...} Print_Margin
```

#### 概述

表示打印边距。

**起始版本：** 12

**相关模块：** [OH\_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)

**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t leftMargin | 左边距，单位：毫米。 |
| uint32\_t topMargin | 上边距，单位：毫米。 |
| uint32\_t rightMargin | 右边距，单位：毫米。 |
| uint32\_t bottomMargin | 下边距，单位：毫米。 |
