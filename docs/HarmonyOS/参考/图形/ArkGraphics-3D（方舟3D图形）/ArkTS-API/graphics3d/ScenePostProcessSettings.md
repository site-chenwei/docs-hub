---
title: "ScenePostProcessSettings"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-post-process-settings"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 3D（方舟3D图形）"
  - "ArkTS API"
  - "graphics3d"
  - "ScenePostProcessSettings"
captured_at: "2026-04-17T01:48:51.376Z"
---

# ScenePostProcessSettings

本模块提供3D图形中的色调映射等图像后处理方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/LMlcRDJFS-GtHpwzo13wCA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014854Z&HW-CC-Expire=86400&HW-CC-Sign=63CA616D4DA8BFD2D0ED772D60F951C66F506650A85D15231012DFEF35DF53D4)

-   本模块首批接口从API version 12开始支持，后续版本的新增接口，采用上角标标记接口的起始版本。

#### 导入模块

```ts
import { ToneMappingType, ToneMappingSettings, BloomSettings, PostProcessSettings } from '@kit.ArkGraphics3D';
```

#### ToneMappingType

色调映射类型枚举。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ACES | 0 | ACES类型。 |
| ACES\_2020 | 1 | ACES\_2020类型。 |
| FILMIC | 2 | FILMIC类型。 |

#### ToneMappingSettings

色调映射设置。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [ToneMappingType](#tonemappingtype) | 否 | 是 | 色调映射类型，默认值为undefined。 |
| exposure | number | 否 | 是 | 曝光度，取值大于0，默认值为undefined。 |

#### BloomSettings18+

泛光设置。当[RenderingPipelineType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#renderingpipelinetype21)为FORWARD\_LIGHTWEIGHT时，此功能不可用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| thresholdHard | number | 否 | 是 | 硬阈值，取值范围是非负数，默认值为1.0。 |
| thresholdSoft | number | 否 | 是 | 软阈值，取值范围是非负数，默认值为2.0。 |
| scaleFactor | number | 否 | 是 | 缩放因子，取值范围大于0，默认值为1.0。 |
| scatter | number | 否 | 是 | 扩散量，取值范围大于0，默认值为1.0。 |

#### VignetteSettings22+

边缘暗角设置。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| roundness | number | 否 | 是 | 作用范围，取值范围为\[0, 1\]，取值为0时作用范围收缩至最小，取值为1时作用范围为全局，默认值为sqrt(0.5)。 |
| intensity | number | 否 | 是 | 作用强度，取值范围为\[0, 1\]，取值为0时无暗角效果，取值为1时为最大暗角强度，默认值为0.4。 |

#### ColorFringeSettings22+

色晕设置。当[RenderingPipelineType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-types#renderingpipelinetype21)为FORWARD\_LIGHTWEIGHT时，此功能不可用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| intensity | number | 否 | 是 | 作用强度，取值范围为0到1之间，默认值为0.2。 |

#### PostProcessSettings

后处理设置，用于配置相机渲染后的图像处理效果，包括色调映射、泛光、边缘暗角和色晕等，作为[Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-scene-nodes#camera)的postProcess属性来使用。

**系统能力：** SystemCapability.ArkUi.Graphics3D

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| toneMapping | [ToneMappingSettings](#tonemappingsettings) | 否 | 是 | 色调映射，默认值为undefined。 |
| bloom18+ | [BloomSettings](#bloomsettings18) | 否 | 是 | 泛光，默认值为undefined。 |
| vignette22+ | [VignetteSettings](#vignettesettings22) | 否 | 是 | 边缘暗角，默认值为undefined。 |
| colorFringe22+ | [ColorFringeSettings](#colorfringesettings22) | 否 | 是 | 色晕，默认值为undefined。 |
