---
title: "RotateAnimation"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-rotateanimation"
menu_path:
  - "参考"
  - "应用服务"
  - "Map Kit（地图服务）"
  - "ArkTS API"
  - "map（地图显示功能）"
  - "RotateAnimation"
captured_at: "2026-04-17T01:48:59.513Z"
---

# RotateAnimation

#### 导入模块

```typescript
import { map } from '@kit.MapKit';
```

#### RotateAnimation

控制旋转的动画类，继承[Animation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-animation)。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

#### \[h2\]constructor

constructor(fromDegree: number, toDegree: number)

构造器，构造控制旋转的动画实例。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本4.1.0(11)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 4.1.0(11)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| fromDegree | number | 是 | 起始角度。角度的范围为\[0, 360\]。 |
| toDegree | number | 是 | 目标角度。角度的范围为\[0, 360\]。 |

**示例：**

```typescript
let animation: map.RotateAnimation = new map.RotateAnimation(15, 150);
```
