---
title: "Interface (CapturePhoto)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-capturephoto"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Interface (CapturePhoto)"
captured_at: "2026-04-17T01:48:38.855Z"
---

# Interface (CapturePhoto)

获取全质量图和未压缩图的对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/uv8sjTrCRriV5VM2CCtIiw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014840Z&HW-CC-Expire=86400&HW-CC-Sign=AC4AEC676582BE5D8D5BB199D510EDD828B89A38C74B2E8D9D1758A06EE2B6B0)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

#### 属性

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| main | [ImageType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-t#imagetype) | 否 | 否 | 全质量图和未压缩图的对象。 |

#### release

release(): Promise<void>

释放输出资源。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```ts
import { camera } from '@kit.CameraKit';

async function releaseCapturePhoto(capturePhoto: camera.CapturePhoto): Promise<void> {
  await capturePhoto.release();
}
```
