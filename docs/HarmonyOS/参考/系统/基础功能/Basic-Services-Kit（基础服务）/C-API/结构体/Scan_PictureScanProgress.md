---
title: "Scan_PictureScanProgress"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan-scan-picturescanprogress"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "C API"
  - "结构体"
  - "Scan_PictureScanProgress"
captured_at: "2026-04-17T01:48:29.550Z"
---

# Scan\_PictureScanProgress

```c
typedef struct {...} Scan_PictureScanProgress
```

#### 概述

表示扫描仪扫描图片的进度

**起始版本：** 12

**相关模块：** [OH\_Scan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-scan)

**所在头文件：** [ohscan.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-ohscan-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t progress | 图片的扫描进度，从0到100，单位：百分比。 |
| int32\_t fd | 扫描仪文件句柄 |
| bool isFinal | 指示该图像是否为最后扫描的图像。true表示该图像是最后扫描的图像，false表示该图像不是最后扫描的图像。 |
