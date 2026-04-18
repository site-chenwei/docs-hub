---
title: "DRM_MediaKeyStatus"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeystatus"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "DRM_MediaKeyStatus"
captured_at: "2026-04-17T01:48:40.597Z"
---

# DRM\_MediaKeyStatus

```c
typedef struct DRM_MediaKeyStatus {...} DRM_MediaKeyStatus
```

#### 概述

媒体密钥状态。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_drm\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t statusCount | 状态计数。 |
| char statusName\[MAX\_MEDIA\_KEY\_STATUS\_COUNT\]\[MAX\_MEDIA\_KEY\_STATUS\_NAME\_LEN\] | 状态名数组。 |
| char statusValue\[MAX\_MEDIA\_KEY\_STATUS\_COUNT\]\[MAX\_MEDIA\_KEY\_STATUS\_VALUE\_LEN\] | 状态值数组。 |
