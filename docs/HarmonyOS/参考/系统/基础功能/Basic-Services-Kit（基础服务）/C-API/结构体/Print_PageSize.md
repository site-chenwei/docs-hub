---
title: "Print_PageSize"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-pagesize"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Print_PageSize"
captured_at: "2026-04-17T01:48:29.127Z"
---

# Print\_PageSize

```c
typedef struct {...} Print_PageSize
```

#### 概述

表示纸张尺寸信息。

**起始版本：** 12

**相关模块：** [OH\_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)

**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \*id | 纸张 ID。 |
| char \*name | 纸张名称。 |
| uint32\_t width | 纸张宽度，单位：毫米。 |
| uint32\_t height | 纸张高度，单位：毫米。 |
