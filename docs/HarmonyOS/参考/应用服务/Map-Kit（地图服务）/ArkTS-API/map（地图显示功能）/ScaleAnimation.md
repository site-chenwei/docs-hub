---
title: "ScaleAnimation"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-scaleanimation"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "ScaleAnimation"
captured_at: "2026-04-17T01:48:59.557Z"
---

# ScaleAnimation

#### 导入模块

```typescript
import { map } from '@kit.MapKit';
```

#### ScaleAnimation

控制缩放的动画类，继承[Animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

#### \[h2\]constructor

constructor(fromX: number, toX: number, fromY: number, toY: number)

构造器，构造控制缩放的动画实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/ymtMzrB_TcuGcwV8FDeA8A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=232673AC77FE164FDADB55B40E8FD790C8E1CF66CCB2ACFB1844BE60BD95C390)

0表示缩小消失。

1表示不缩放。

小于1的值表示缩小。

大于1的值表示放大。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| fromX | number | 是 | 指动画开始时应用的水平缩放倍数。 |
| toX | number | 是 | 指动画结束时应用的水平缩放倍数。 |
| fromY | number | 是 | 指动画开始时应用的垂直缩放倍数。 |
| toY | number | 是 | 指动画结束时应用的垂直缩放倍数。 |

**示例：**

```typescript
let animation: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
```
