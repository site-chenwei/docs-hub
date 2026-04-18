---
title: "zoomOut"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-zoomout"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "zoomOut"
captured_at: "2026-04-17T01:48:59.962Z"
---

# zoomOut

#### 导入模块

```typescript
import { map } from '@kit.MapKit';
```

#### zoomOut

zoomOut(): CameraUpdate

缩小地图缩放级别，在当前地图显示的级别基础上减1。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [CameraUpdate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate) | 描述地图状态将要发生的变化。 |

**示例：**

```typescript
let cameraUpdate: map.CameraUpdate = map.zoomOut();
```
