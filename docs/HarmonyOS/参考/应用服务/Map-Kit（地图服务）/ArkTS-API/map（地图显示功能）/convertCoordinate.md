---
title: "convertCoordinate"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-convertcoordinate"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "convertCoordinate"
captured_at: "2026-04-17T01:49:00.024Z"
---

# convertCoordinate

#### 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

#### convertCoordinate

convertCoordinate(fromType: mapCommon.CoordinateType, toType: mapCommon.CoordinateType, location: mapCommon.LatLng): Promise<mapCommon.LatLng>

坐标系转换。当前仅支持WGS84坐标系转GCJ02坐标系。使用Promise异步回调。

建议使用[convertCoordinateSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-convertcoordinatesync)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| fromType | [mapCommon.CoordinateType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#coordinatetype) | 是 | 转换前坐标类型，当前仅支持WGS84。 |
| toType | [mapCommon.CoordinateType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#coordinatetype) | 是 | 转换后坐标类型，当前仅支持GCJ02。 |
| location | [mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng) | 是 | 待转换坐标。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng)\> | Promise对象，返回[mapCommon.LatLng](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-common#latlng)。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-errorcode)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Invalid input parameter. |

**示例：**

```typescript
let wgs84Position: mapCommon.LatLng = {
  latitude: 30,
  longitude: 118
};
let gcj02Position: mapCommon.LatLng = await map.convertCoordinate(mapCommon.CoordinateType.WGS84, mapCommon.CoordinateType.GCJ02,wgs84Position);
```
