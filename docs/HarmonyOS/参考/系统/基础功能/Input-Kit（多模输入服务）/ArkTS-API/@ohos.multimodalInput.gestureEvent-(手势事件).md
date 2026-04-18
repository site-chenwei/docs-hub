---
title: "@ohos.multimodalInput.gestureEvent (手势事件)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-multimodalinput-gestureevent"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "ArkTS API"
  - "@ohos.multimodalInput.gestureEvent (手势事件)"
captured_at: "2026-04-17T01:48:30.596Z"
---

# @ohos.multimodalInput.gestureEvent (手势事件)

设备上报的手势事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/moMIfHISQVSxwlkR4gIwEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=5447D43B63A0A73548FC9464B03D25B4B3813FE01DF0834EB528E99C7D3280EF)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import { Rotate, Pinch, ThreeFingersSwipe, FourFingersSwipe, ActionType } from '@kit.InputKit';
```

#### Pinch

捏合手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| scale | number | 否 | 否 | 捏合度，取值范围大于等于0。 |

#### Rotate11+

旋转手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| angle | number | 否 | 否 | 旋转角度。 |

#### ThreeFingersSwipe

三指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| x | number | 否 | 否 | 坐标x。 |
| y | number | 否 | 否 | 坐标y。 |

#### FourFingersSwipe

四指滑动手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |
| x | number | 否 | 否 | 坐标x。 |
| y | number | 否 | 否 | 坐标y。 |

#### ThreeFingersTap11+

三指轻点手势事件。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [ActionType](#actiontype) | 否 | 否 | 手势事件类型。如：手势开始、手势更新、手势结束等。 |

#### ActionType

手势事件类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| CANCEL | 0 | 取消。 |
| BEGIN | 1 | 手势开始。 |
| UPDATE | 2 | 手势更新。 |
| END | 3 | 手势结束。 |
