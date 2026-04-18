---
title: "Interface (AutoDeviceSwitchQuery)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autodeviceswitchquery"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Interface (AutoDeviceSwitchQuery)"
captured_at: "2026-04-17T01:48:38.746Z"
---

# Interface (AutoDeviceSwitchQuery)

自动切换镜头查询类，用于查询设备是否支持自动切换镜头。

[自动切换镜头能力](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/camera-auto-switch)仅支持折叠屏设备使用，如需使能该能力请参考[enableAutoDeviceSwitch](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-autodeviceswitch#enableautodeviceswitch13)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/gzN2PXW5Rp6qjl-mJ726Dw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014840Z&HW-CC-Expire=86400&HW-CC-Sign=E29143ACDEB5D3E017B11F25906029779B5722BEDFF3DB21CAE5E6ECC1A736FC)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 13开始支持。

#### 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

#### isAutoDeviceSwitchSupported13+

isAutoDeviceSwitchSupported(): boolean

查询设备是否支持自动切换镜头能力。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 是否支持自动切换镜头，true为支持，false为不支持。 |

**示例：**

```ts
// 本示例用于查询折叠屏设备是否支持自动切换相机镜头。
// 当示例代码返回true时，可继续使用enableAutoDeviceSwitch使能自动切换摄像头能力。
function isAutoDeviceSwitchSupported(session: camera.PhotoSession): boolean {
  let isSupported = false;
  isSupported = session.isAutoDeviceSwitchSupported();
  return isSupported;
}
```
