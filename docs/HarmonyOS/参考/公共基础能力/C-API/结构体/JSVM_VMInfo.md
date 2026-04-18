---
title: "JSVM_VMInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-vminfo"
menu_path:
  - "参考"
  - "公共基础能力"
  - "C API"
  - "结构体"
  - "JSVM_VMInfo"
captured_at: "2026-04-17T01:49:06.472Z"
---

# JSVM\_VMInfo

```c
typedef struct {...} JSVM_VMInfo
```

#### 概述

JavaScript虚拟机信息。

**起始版本：** 11

**相关模块：** [JSVM](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm)

**所在头文件：** [jsvm\_types.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-types-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t apiVersion | 此虚拟机支持的最高API版本。 |
| const char\* engine | 实现虚拟机的引擎名称。 |
| const char\* version | 虚拟机的版本。 |
| uint32\_t cachedDataVersionTag | 缓存数据版本标签。 |
