---
title: "DRM_MediaKeyRequest"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm-drm-mediakeyrequest"
menu_path:
  - "参考"
  - "媒体"
  - "DRM Kit（数字版权保护服务）"
  - "C API"
  - "结构体"
  - "DRM_MediaKeyRequest"
captured_at: "2026-04-17T01:48:40.528Z"
---

# DRM\_MediaKeyRequest

```c
typedef struct DRM_MediaKeyRequest {...} DRM_MediaKeyRequest
```

#### 概述

媒体密钥请求。

**起始版本：** 11

**相关模块：** [Drm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drm)

**所在头文件：** [native\_drm\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [DRM\_MediaKeyRequestType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-drm-common-h#drm_mediakeyrequesttype) type | 媒体密钥请求类型。 |
| int32\_t dataLen | 媒体密钥请求数据长度。 |
| uint8\_t data\[MAX\_MEDIA\_KEY\_REQUEST\_DATA\_LEN\] | 发送到媒体密钥服务器的媒体密钥请求数据。 |
| char defaultUrl\[MAX\_DEFAULT\_URL\_LEN\] | 媒体密钥服务器URL。 |
