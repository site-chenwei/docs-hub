---
title: "Types"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-t"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Types"
captured_at: "2026-04-17T01:48:39.320Z"
---

# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/ZtjExIbHTJi1XK0VXUbaXQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014841Z&HW-CC-Expire=86400&HW-CC-Sign=DE3290454FA449EF3FAD6EA922D27CC1549F25CDF17065A69BA1A7F347E0C7B1)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### ImageType

type ImageType = image.Image | image.Picture

图片容器类型，用于获取全质量图和未压缩图(YUV)。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 类型 | 说明 |
| :-- | :-- |
| [image.Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image) | 图片容器类型，用于获取全质量图。 |
| [image.Picture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-picture) | 图片容器类型，用于获取未压缩图(YUV)。 |
