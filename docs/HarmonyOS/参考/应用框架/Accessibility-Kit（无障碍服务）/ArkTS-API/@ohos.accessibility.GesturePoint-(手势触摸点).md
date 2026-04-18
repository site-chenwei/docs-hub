---
title: "@ohos.accessibility.GesturePoint (手势触摸点)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepoint"
menu_path:
  - "参考"
  - "应用框架"
  - "Accessibility Kit（无障碍服务）"
  - "ArkTS API"
  - "@ohos.accessibility.GesturePoint (手势触摸点)"
captured_at: "2026-04-17T01:47:49.059Z"
---

# @ohos.accessibility.GesturePoint (手势触摸点)

GesturePoint表示手势触摸点。

本模块用于创建辅助功能注入手势所需的手势路径的触摸点信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/ah77PoMsSfSjfk8Zlb_E1A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=910E882FDFC7C7F67847A0B05234BF6693E1432D04CACBB4AA73DD7A19C30E3A)

-   本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { GesturePoint } from '@kit.AccessibilityKit';
```

#### GesturePoint

表示手势触摸点。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| positionX | number | 否 | 否 | 触摸点X坐标。 |
| positionY | number | 否 | 否 | 触摸点Y坐标。 |

#### \[h2\]constructor(deprecated)

constructor(positionX: number, positionY: number);

构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/3YZ0A6uoSceBuF9_3opHqw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=AEA4B5BE7CAEB5DA23688EF97BB9B4005A56AB00D2DAE1029707D7BED527491C)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| positionX | number | 是 | 触摸点X坐标。 |
| positionY | number | 是 | 触摸点Y坐标。 |

**示例：**

```ts
import { GesturePoint } from '@kit.AccessibilityKit';

let gesturePoint = new GesturePoint(1, 2);
```
