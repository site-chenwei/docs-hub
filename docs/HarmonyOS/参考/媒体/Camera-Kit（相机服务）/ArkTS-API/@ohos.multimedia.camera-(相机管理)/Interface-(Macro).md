---
title: "Interface (Macro)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macro"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Interface (Macro)"
captured_at: "2026-04-17T01:48:38.964Z"
---

# Interface (Macro)

Macro 继承自 [MacroQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macroquery)。

提供使能微距能力的接口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/iPtOsNQVR0ar1gwp5dmLBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014840Z&HW-CC-Expire=86400&HW-CC-Sign=616FC49BE82F7CA37388506AC48D6621086503EC184AEEC24ECBBB1BB764783C)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 19开始支持。

#### 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

#### enableMacro19+

enableMacro(enabled: boolean): void

使能当前的微距能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/xjrSayKDSRaE55p4wuHTRg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014840Z&HW-CC-Expire=86400&HW-CC-Sign=0E2E439DFE1CE8B26538B8BAD3664698A2255257B60A1FE6200B6126B5A3A959)

使用该接口前，需要先通过[isMacroSupported](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-macroquery#ismacrosupported19)接口查询当前设备是否支持微距能力。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enabled | boolean | 是 | 是否开启微距能力。true表示开启微距能力，false表示关闭微距能力。 |

**错误码：**

以下错误码的详细介绍请参见[Camera错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-camera)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |

**示例：**

```ts
function enableMacro(photoSession: camera.PhotoSession): void {
  let isSupported: boolean = photoSession.isMacroSupported();
  if (isSupported) {
    photoSession.enableMacro(true);
  }
}
```
