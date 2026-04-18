---
title: "Interface (MacroQuery)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macroquery"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Interface (MacroQuery)"
captured_at: "2026-04-17T01:48:39.003Z"
---

# Interface (MacroQuery)

提供查询设备是否支持相机微距拍摄的方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/DrFV6o9qR4exmkMnEiUZSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014841Z&HW-CC-Expire=86400&HW-CC-Sign=F786ED208B37507F00CB0E909B50ACFD46F3A51112644CF7502B4CAD18FF7F0D)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 19开始支持。

#### 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

#### isMacroSupported19+

isMacroSupported(): boolean

检测当前状态下是否支持微距能力，需要在CaptureSession调用[commitConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-session#commitconfig11)之后进行调用。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回是否支持微距能力。true表示支持，false表示不支持。 |

**示例：**

```ts
function isMacroSupported(photoSession: camera.PhotoSession): boolean {
  let isSupported: boolean = photoSession.isMacroSupported();
  return isSupported;
}
```
