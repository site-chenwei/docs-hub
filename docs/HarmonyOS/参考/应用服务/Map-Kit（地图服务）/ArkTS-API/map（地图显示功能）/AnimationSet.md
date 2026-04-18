---
title: "AnimationSet"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animationset"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "AnimationSet"
captured_at: "2026-04-17T01:48:59.608Z"
---

# AnimationSet

#### 导入模块

```typescript
import { map } from '@kit.MapKit';
```

#### AnimationSet

动画类的集合，继承[Animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

#### \[h2\]constructor

constructor(shareInterpolator: boolean)

构造器，构造动画类的集合实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/M-gWYUrOQsCbrBOS_Uj1jA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014859Z&HW-CC-Expire=86400&HW-CC-Sign=AC2E2A91DDDAE9FA597625F58C872E15249714461D00F4E309B56AB2C533FA72)

动画类集合继承[Animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation)方法，仅shareInterpolator为true时共享插值器，其他属性不共享，不支持设置。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| shareInterpolator | boolean | 是 | 
定义是否共享插值器。

\- true：共享

\- false：不共享

 |

**示例：**

```typescript
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.setInterpolator(Curve.Linear);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
animation.clearAnimation();
```

#### \[h2\]addAnimation

addAnimation(animation: Animation): void

动画类集合增加动画。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| animation | [Animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation) | 是 | 动画类集合增加动画。 |

**示例：**

```typescript
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
```

#### \[h2\]clearAnimation

clearAnimation(): void

清空动画类集合。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**示例：**

```typescript
let animation1: map.AlphaAnimation = new map.AlphaAnimation(0.2, 1);
let animation2: map.RotateAnimation = new map.RotateAnimation(15, 150);
let animation3: map.ScaleAnimation = new map.ScaleAnimation(1, 3, 1, 3);
let animation = new map.AnimationSet(true);
animation.addAnimation(animation1);
animation.addAnimation(animation2);
animation.addAnimation(animation3);
animation.clearAnimation();
```
