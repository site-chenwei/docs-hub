---
title: "MediaLibrary_RequestId"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager-medialibrary-requestid"
menu_path:
  - "参考"
  - "媒体"
  - "Media Library Kit（媒体文件管理服务）"
  - "C API"
  - "结构体"
  - "MediaLibrary_RequestId"
captured_at: "2026-04-17T01:48:45.665Z"
---

# MediaLibrary\_RequestId

```c
typedef struct MediaLibrary_RequestId {...} MediaLibrary_RequestId
```

#### 概述

定义请求ID。

当请求媒体库资源时，会返回此类型。

请求ID可用于取消请求。

如果请求失败，值将全为零，如 "00000000-0000-0000-0000-000000000000"。

**起始版本：** 12

**相关模块：** [MediaAssetManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mediaassetmanager)

**所在头文件：** [media\_asset\_base\_capi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-media-asset-base-capi-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char requestId\[UUID\_STR\_MAX\_LENGTH\] | 请求ID。 |
