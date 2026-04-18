---
title: "Scan_ScannerDevice"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-scannerdevice"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Scan_ScannerDevice"
captured_at: "2026-04-17T01:48:29.545Z"
---

# Scan\_ScannerDevice

```c
typedef struct {...} Scan_ScannerDevice
```

#### 概述

表示扫描仪设备信息

**起始版本：** 12

**相关模块：** [OH\_Scan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan)

**所在头文件：** [ohscan.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohscan-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| const char\* scannerId | 扫描仪ID |
| const char\* manufacturer | 扫描仪制造商 |
| const char\* model | 扫描仪型号 |
| const char\* discoverMode | 扫描仪发现模式 |
| const char\* serialNumber | 扫描仪序列号 |
