---
title: "Interface (ColorManagementQuery)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-camera-colormanagementquery"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "ArkTS API"
  - "@ohos.multimedia.camera (相机管理)"
  - "Interface (ColorManagementQuery)"
captured_at: "2026-04-17T01:48:38.882Z"
---

# Interface (ColorManagementQuery)

色彩管理类，用于查询色彩空间参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/sydx7FY0SVaJcQLx11ujBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014840Z&HW-CC-Expire=86400&HW-CC-Sign=1E141DE752067EB1DF58C078595DFEAB43644915BC8BF9D1A1A3AF97462223C8)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 12开始支持。

#### 导入模块

```ts
import { camera } from '@kit.CameraKit';
```

#### getSupportedColorSpaces12+

getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>

获取支持的色彩空间列表。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Camera.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<[colorSpaceManager.ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager#colorspace)\> | 支持的色彩空间列表。若接口调用失败，返回undefined。 |

**示例：**

```ts
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function getSupportedColorSpaces(session: camera.PhotoSession): Array<colorSpaceManager.ColorSpace> {
  let colorSpaces: Array<colorSpaceManager.ColorSpace> = [];
  colorSpaces = session.getSupportedColorSpaces();
  return colorSpaces;
}
```
