---
title: "calculateDistance"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-calculatedistance"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "calculateDistance"
captured_at: "2026-04-17T01:49:00.015Z"
---

# calculateDistance

#### 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

#### calculateDistance

calculateDistance(from: mapCommon.LatLng, to: mapCommon.LatLng): number

计算坐标点之间的距离。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| from | [mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng) | 是 | 起点坐标。 |
| to | [mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng) | 是 | 终点坐标。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 
两个坐标点之间的距离，单位：米。

入参为空返回0。

 |

**示例：**

```typescript
let fromLatLng: mapCommon.LatLng = {
  latitude: 38,
  longitude: 118
};
let toLatLng: mapCommon.LatLng = {
  latitude: 39,
  longitude: 119
};

let distance = map.calculateDistance(fromLatLng, toLatLng);
```
