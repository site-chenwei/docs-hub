---
title: "DRM_KeysInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-keysinfo"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "DRM_KeysInfo"
captured_at: "2026-04-17T01:48:40.568Z"
---

# DRM\_KeysInfo

```c
typedef struct DRM_KeysInfo {...} DRM_KeysInfo
```

#### 概述

媒体密钥信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_drm\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t keysInfoCount | 钥匙计数。 |
| uint8\_t keyId\[MAX\_KEY\_INFO\_COUNT\]\[MAX\_KEY\_ID\_LEN\] | 密钥ID集合。 |
| char statusValue\[MAX\_KEY\_INFO\_COUNT\]\[MAX\_KEY\_STATUS\_VALUE\_LEN\] | 密钥状态值。 |
