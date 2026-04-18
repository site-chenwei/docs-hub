---
title: "Print_StringList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-stringlist"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Print_StringList"
captured_at: "2026-04-17T01:48:29.467Z"
---

# Print\_StringList

```c
typedef struct {...} Print_StringList
```

#### 概述

表示字符串列表。

**起始版本：** 12

**相关模块：** [OH\_Print](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print)

**所在头文件：** [ohprint.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohprint-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t count | 字符串数量。 |
| char \*\*list | 字符串指针数组。 |
