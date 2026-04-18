---
title: "Print_Range"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-range"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Print_Range"
captured_at: "2026-04-17T01:48:29.122Z"
---

# Print\_Range

```c
typedef struct {...} Print_Range
```

#### 概述

表示打印范围结构体。

**起始版本：** 13

**相关模块：** [OH\_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)

**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t startPage | 打印起始页。 |
| uint32\_t endPage | 打印结束页。 |
| uint32\_t pagesArrayLen | 打印页数组长度。 |
| uint32\_t\* pagesArray | 打印页数组。 |
