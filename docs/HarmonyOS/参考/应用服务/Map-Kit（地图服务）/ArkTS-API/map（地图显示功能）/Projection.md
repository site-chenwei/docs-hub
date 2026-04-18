---
title: "Projection"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-projection"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "Projection"
captured_at: "2026-04-17T01:48:59.511Z"
---

# Projection

#### 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

#### Projection

用于在屏幕坐标和经纬度之间进行转换，在调用map.[MapComponentController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller)类的[getProjection](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-mapcomponentcontroller#getprojection)方法时会返回该类型的实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
let projection: map.Projection = this.mapController?.getProjection();
```

#### \[h2\]fromScreenLocation

fromScreenLocation(point: mapCommon.MapPoint): mapCommon.LatLng

将屏幕像素点坐标转换成经纬度。屏幕位置是以相对于地图左上角（而不是整个屏幕的左上角）的屏幕像素（而非显示像素）指定的。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| point | [mapCommon.MapPoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#mappoint) | 是 | 屏幕上的坐标点，单位：px。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng) | 经纬度坐标。 |

**示例：**

```typescript
let point: mapCommon.MapPoint = {
  positionX: 10,
  positionY: 10
};
let latLng: mapCommon.LatLng = projection.fromScreenLocation(point);
```

#### \[h2\]toScreenLocation

toScreenLocation(position: mapCommon.LatLng): mapCommon.MapPoint

将经纬度转换为对应的屏幕上的点的坐标。屏幕上的点的坐标是以相对于地图左上角（而不是整个屏幕的左上角）的屏幕像素（而非显示像素）指定的。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| position | [mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng) | 是 | 经纬度坐标。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [mapCommon.MapPoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#mappoint) | 屏幕上的坐标点，单位：px。 |

**示例：**

```typescript
let position: mapCommon.MapPoint = projection.toScreenLocation({ latitude: 31.984, longitude: 118.766 });
```

#### \[h2\]getVisibleRegion

getVisibleRegion(): mapCommon.VisibleRegion

获取可视区域的坐标信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [mapCommon.VisibleRegion](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#visibleregion) | 可见区域。 |

**示例：**

```typescript
let visibleRegion: mapCommon.VisibleRegion = projection.getVisibleRegion();
```

#### \[h2\]getMapBounds

getMapBounds(center: mapCommon.LatLng, zoom: number): mapCommon.LatLngBounds

根据中心点和缩放级别获取地图控件对应的目标区域。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| center | [mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng) | 是 | 中心点经纬度坐标。 |
| zoom | number | 是 | 缩放级别，取值范围：\[2, 20\]。传入的值大于最大层级，会取最大层级，传入的值小于最小层级，会取最小层级。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [mapCommon.LatLngBounds](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlngbounds) | 目标区域。 |

**示例：**

```typescript
let position: mapCommon.LatLng = {
  latitude: 31.98, longitude: 118.766
};
let result: mapCommon.LatLngBounds = projection.getMapBounds(position, 10);
```
