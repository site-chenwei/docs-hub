---
title: "@ohos.accessibility.GesturePath (手势路径)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepath"
menu_path:
  - "参考"
  - "应用框架"
  - "Accessibility Kit（无障碍服务）"
  - "ArkTS API"
  - "@ohos.accessibility.GesturePath (手势路径)"
captured_at: "2026-04-17T01:47:48.951Z"
---

# @ohos.accessibility.GesturePath (手势路径)

GesturePath表示手势路径信息。

本模块用于创建辅助功能注入手势所需的手势路径信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/pQ9QIYNPR6ilLz08NU2m5g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=09734DD6ECBA86AB8143E608D2BCF8F1D83C9516B76D6212950596084D39B9E9)

-   本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { GesturePath } from '@kit.AccessibilityKit';
```

#### GesturePath

表示手势路径信息。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| points | Array<[GesturePoint](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepoint#gesturepoint)\> | 否 | 否 | 手势触摸点。 |
| durationTime | number | 否 | 否 | 手势总耗时，单位为毫秒。 |

#### \[h2\]constructor(deprecated)

constructor(durationTime: number);

构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/NYnCm06OSOuL9VHIg-BuCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=242B5E26BC89C2D2D4F446C165A06B895B4CBFB021907BB8DB13CE0F079C7B9B)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| durationTime | number | 是 | 手势总耗时，单位为毫秒。 |

**示例：**

```ts
import { GesturePath } from '@kit.AccessibilityKit';

let gesturePath = new GesturePath(20);
```
