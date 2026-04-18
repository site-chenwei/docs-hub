---
title: "CameraUpdate"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-cameraupdate"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "CameraUpdate"
captured_at: "2026-04-17T01:48:59.489Z"
---

# CameraUpdate

#### 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

#### CameraUpdate

CameraUpdate定义了相机移动参数。CameraUpdate的创建方法参见[newCameraPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-newcameraposition)等function。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
let target: mapCommon.LatLng = {
  latitude: 39.9,
  longitude: 116.4
};
let cameraPosition: mapCommon.CameraPosition = {
  target: target,
  zoom: 10
};
// 新建CameraUpdate对象
let cameraUpdate: map.CameraUpdate = map.newCameraPosition(cameraPosition);
// 移动相机
this.mapController.moveCamera(cameraUpdate);
```
