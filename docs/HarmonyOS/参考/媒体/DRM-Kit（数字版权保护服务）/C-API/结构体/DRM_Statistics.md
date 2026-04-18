---
title: "DRM_Statistics"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-statistics"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "DRM_Statistics"
captured_at: "2026-04-17T01:48:40.537Z"
---

# DRM\_Statistics

```c
typedef struct DRM_Statistics {...} DRM_Statistics
```

#### 概述

MediaKeySystem的度量信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_drm\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t statisticsCount | 度量计数。 |
| char statisticsName\[MAX\_STATISTICS\_COUNT\]\[MAX\_STATISTICS\_NAME\_LEN\] | 度量信息名称集合。 |
| char statisticsDescription\[MAX\_STATISTICS\_COUNT\]\[MAX\_STATISTICS\_BUFFER\_LEN\] | 度量信息描述集合。 |
