---
title: "Print_PropertyList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-propertylist"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Print_PropertyList"
captured_at: "2026-04-17T01:48:29.450Z"
---

# Print\_PropertyList

```c
typedef struct {...} Print_PropertyList
```

#### 概述

打印机属性列表。

**起始版本：** 12

**相关模块：** [OH\_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)

**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t count | 属性数量。 |
| [Print\_Property](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-property) \*list | 属性指针数组。 |
