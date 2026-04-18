---
title: "Interface (ControlCenter)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenter"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Interface (ControlCenter)"
captured_at: "2026-04-17T01:48:38.859Z"
---

# Interface (ControlCenter)

ControlCenter 继承自 [ControlCenterQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-controlcenterquery)。

控制中心类，用于使能相机控制器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/3B51f24IQC-G3iIFrPDugQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014840Z&HW-CC-Expire=86400&HW-CC-Sign=4B02201231A702FD29A063543E1F5FE465EE54E6385F9AB8852C0112BD5647E8)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 20开始支持。

#### 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

#### enableControlCenter20+

enableControlCenter(enabled: boolean): void

使能相机控制器。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enabled | boolean | 是 | 开启或关闭相机控制器。true表示开启，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 7400103 | Session not config. |

**示例：**

```ts
function enableControlCenter(videoSession: camera.VideoSession, enable: boolean): void {
    let isSupported: boolean = videoSession.isControlCenterSupported();
    if (isSupported) {
        videoSession.enableControlCenter(enable);
    }
}
```
