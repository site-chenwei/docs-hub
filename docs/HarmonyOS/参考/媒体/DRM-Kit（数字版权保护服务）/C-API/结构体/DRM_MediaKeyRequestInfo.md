---
title: "DRM_MediaKeyRequestInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequestinfo"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "DRM_MediaKeyRequestInfo"
captured_at: "2026-04-17T01:48:40.527Z"
---

# DRM\_MediaKeyRequestInfo

```c
typedef struct DRM_MediaKeyRequestInfo {...} DRM_MediaKeyRequestInfo
```

#### 概述

媒体密钥请求信息。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_drm\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [DRM\_MediaKeyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h#drm_mediakeytype) type | 密钥类型。 |
| int32\_t initDataLen | 初始数据长度。 |
| uint8\_t initData\[MAX\_INIT\_DATA\_LEN\] | base64解码后格式为PSSH的初始数据。 |
| char mimeType\[MAX\_MIMETYPE\_LEN\] | 媒体上下文的MIME类型。 |
| uint32\_t optionsCount | 选项数据计数。 |
| char optionName\[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT\]\[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_NAME\_LEN\] | 选项名称集合。 |
| char optionData\[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT\]\[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_DATA\_LEN\] | 选项数据集合。 |
