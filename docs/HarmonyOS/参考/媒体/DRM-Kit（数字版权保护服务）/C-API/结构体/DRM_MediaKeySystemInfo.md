---
title: "DRM_MediaKeySystemInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysysteminfo"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "DRM_MediaKeySystemInfo"
captured_at: "2026-04-17T01:48:40.637Z"
---

# DRM\_MediaKeySystemInfo

```c
typedef struct DRM_MediaKeySystemInfo {...} DRM_MediaKeySystemInfo
```

#### 概述

加密媒体内容的DRM信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_drm\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t psshCount | PSSH计数。 |
| [DRM\_PsshInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-psshinfo) psshInfo\[MAX\_PSSH\_INFO\_COUNT\] | PSSH信息。 |
