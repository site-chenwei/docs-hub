---
title: "Scan_ScannerOptions"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scanneroptions"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Scan_ScannerOptions"
captured_at: "2026-04-17T01:48:29.557Z"
---

# Scan\_ScannerOptions

```c
typedef struct {...} Scan_ScannerOptions
```

#### 概述

表示一个扫描仪的所有参数选项

**起始版本：** 12

**相关模块：** [OH\_Scan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan)

**所在头文件：** [ohscan.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohscan-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\*\* titles | 选项标题 |
| char\*\* descriptions | 选项描述 |
| char\*\* ranges | 选项可设置的范围 |
| int32\_t optionCount | 可设置的参数选项数量 |
