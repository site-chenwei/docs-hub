---
title: "TileOverlay"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-tileoverlay"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "TileOverlay"
captured_at: "2026-04-17T01:48:59.733Z"
---

# TileOverlay

#### 导入模块

```typescript
import { map, mapCommon } from '@kit.MapKit';
```

#### TileOverlay

瓦片图层，继承[BaseOverlay](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-baseoverlay)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/IVrSeT8RQwuHQ7Ym4AKSAg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=2753CE03A5978BD395D9D1D9FA2E12191F4BFE07E93AAFC4B1BC776AE84A22F7)

建议最多添加10个TileOverlay，且提供的图层瓦片分辨率是256\*256。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**示例：**

```typescript
let params: mapCommon.TileOverlayParams = {
  // 设置地图瓦片图层的地址,必须是以http或者https开头的URL且包含占位符{x}、{y}和{z}
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  transparency: 0,
  fadeIn: false
};
let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);
```

#### \[h2\]clearTileCache

clearTileCache(): void

清除瓦片图层的缓存。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**示例：**

```typescript
tileOverlay.clearTileCache();
```

#### \[h2\]setFadeIn

setFadeIn(fadeIn: boolean): void

是否开启瓦片图层淡入。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| fadeIn | boolean | 是 | 
是否开启瓦片图层淡入。

\- true：开启瓦片图层淡入。

\- false：不开启瓦片图层淡入。

 |

**示例：**

```typescript
tileOverlay.setFadeIn(false);
```

#### \[h2\]setTransparency

setTransparency(transparency: number): void

设置瓦片图层的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| transparency | number | 是 | 瓦片图层的透明度。取值范围：\[0, 1\]。0表示不透明，1表示全透明。 |

**示例：**

```typescript
tileOverlay.setTransparency(0.5);
```

#### \[h2\]getFadeIn

getFadeIn(): boolean

返回是否开启瓦片图层淡入。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 
返回是否开启瓦片图层淡入。

\- true：已开启瓦片图层淡入。

\- false：未开启瓦片图层淡入。

 |

**示例：**

```typescript
let isFadeIn: boolean = tileOverlay.getFadeIn();
```

#### \[h2\]getTransparency

getTransparency(): number

返回瓦片图层的透明度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.3(15)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.3(15)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回瓦片图层的透明度。 |

**示例：**

```typescript
let transparency: number = tileOverlay.getTransparency();
```

#### \[h2\]clearDiskCache

clearDiskCache(): Promise<void>

清除磁盘缓存，内存缓存也会被清除。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本6.0.0(20)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```typescript
tileOverlay.clearDiskCache();
```
