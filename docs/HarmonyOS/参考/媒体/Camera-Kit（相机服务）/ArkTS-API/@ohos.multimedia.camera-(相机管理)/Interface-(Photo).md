---
title: "Interface (Photo)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-photo"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Interface (Photo)"
captured_at: "2026-04-17T01:48:39.087Z"
---

# Interface (Photo)

全质量图对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/7hxaO9t-Rzi8Goq3KAHvsA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014841Z&HW-CC-Expire=86400&HW-CC-Sign=B7040DA7AB7130E9C11FE8CC257B22AF1A90585E9AC1D0ACFEECCCF868045887)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 11开始支持。

#### 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

#### 属性

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| main11+ | [image.Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-image) | 否 | 否 | 全质量图Image。 |

#### release11+

release(): Promise<void>

释放输出资源。使用Promise异步回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
async function releasePhoto(photo: camera.Photo): Promise<void> {
  await photo.release();
}
```
