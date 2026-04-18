---
title: "DRM_MediaKeySystemDescription"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeysystemdescription"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "DRM_MediaKeySystemDescription"
captured_at: "2026-04-17T01:48:40.641Z"
---

# DRM\_MediaKeySystemDescription

```c
typedef struct DRM_MediaKeySystemDescription {...} DRM_MediaKeySystemDescription
```

#### 概述

DRM解决方案名称及其UUID的列表。

**起始版本：** 12

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_drm\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char name\[MAX\_MEDIA\_KEY\_SYSTEM\_NAME\_LEN\] | DRM插件的名称。 |
| uint8\_t uuid\[DRM\_UUID\_LEN\] | UUID。 |
