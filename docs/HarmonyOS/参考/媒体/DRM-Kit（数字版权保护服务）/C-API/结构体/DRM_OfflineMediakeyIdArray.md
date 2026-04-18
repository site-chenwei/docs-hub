---
title: "DRM_OfflineMediakeyIdArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-offlinemediakeyidarray"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "DRM_OfflineMediakeyIdArray"
captured_at: "2026-04-17T01:48:40.567Z"
---

# DRM\_OfflineMediakeyIdArray

```c
typedef struct DRM_OfflineMediakeyIdArray {...} DRM_OfflineMediakeyIdArray
```

#### 概述

离线媒体密钥ID数组。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_drm\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t idsCount | ID计数。 |
| int32\_t idsLen\[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT\] | ID长度集合。 |
| uint8\_t ids\[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT\]\[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_LEN\] | ID数据集合。 |
