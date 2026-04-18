---
title: "Interface (ControlCenterQuery)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenterquery"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Interface (ControlCenterQuery)"
captured_at: "2026-04-17T01:48:38.887Z"
---

# Interface (ControlCenterQuery)

控制中心类，用于查询是否支持相机控制器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/7_jRj6D9TNKwoo2ySIW3uA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014840Z&HW-CC-Expire=86400&HW-CC-Sign=A1B0060C241F2520B734BF197DF19F91716936EFFC0F78CCBC52CBBD04D45248)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 20开始支持。

#### 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

#### isControlCenterSupported20+

isControlCenterSupported(): boolean

查询是否支持相机控制器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回是否支持相机控制器。true表示支持，false表示不支持。 |

**示例：**

```ts
function isControlCenterSupported(videoSession: camera.VideoSession): boolean {
    let isSupported: boolean = videoSession.isControlCenterSupported();
    return isSupported;
}
```

#### getSupportedEffectTypes20+

getSupportedEffectTypes(): Array<ControlCenterEffectType>

查询相机控制器支持的效果类型。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<[ControlCenterEffectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-e#controlcentereffecttype20)\> | 支持的效果类型。 |

**示例：**

```ts
function getSupportedEffectTypes(videoSession: camera.VideoSession): Array<camera.ControlCenterEffectType> {
    let effectTypes: Array<camera.ControlCenterEffectType> = [];
    effectTypes = videoSession.getSupportedEffectTypes();
    return effectTypes;
}
```
