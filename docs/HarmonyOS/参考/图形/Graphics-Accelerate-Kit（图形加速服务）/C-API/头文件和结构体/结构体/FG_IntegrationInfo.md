---
title: "FG_IntegrationInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___intergration_info"
menu_path:
  - "参考"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "FG_IntegrationInfo"
captured_at: "2026-04-17T01:48:51.929Z"
---

# FG\_IntegrationInfo

#### 概述

此结构体描述超帧集成的信息。包括显示模式，是否需要额外缓存深度和颜色纹理，以及是否需要翻转颜色纹理。仅在[FG\_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。

**起始版本**：5.1.0(18)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

**所在头文件：** [frame\_generation\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__base_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [FG\_PresentMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_presentmode) [presentMode](#presentmode) | 预测帧展示模式。取值为FG\_PRESENT\_BY\_SYSTEM时，仅在[FG\_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_predictionmode)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。 |
| bool [textureCachedByGame](#texturecachedbygame) | 
深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。取值为True时，仅在[FG\_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_predictionmode)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。

取值范围：\[true, false\]。

 |
| bool [needFlipInputColor](#needflipinputcolor) | 

输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。取值为True时，仅在[FG\_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_predictionmode)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。

取值范围：\[true, false\]。

 |
| bool [needFlipOutputColor](#needflipoutputcolor) | 

预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。取值为True时，仅在[FG\_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_predictionmode)为FG\_PREDICTION\_MODE\_INTERPOLATION时生效。

取值范围：\[true, false\]。

 |

#### 结构体成员变量说明

#### \[h2\]presentMode

```c
FG_PresentMode FG_IntegrationInfo::presentMode
```

**描述**

展示模式。

#### \[h2\]textureCachedByGame

```c
bool FG_IntegrationInfo::textureCachedByGame
```

**描述**

深度纹理和颜色纹理是否被游戏单独缓存来用于超帧。缓存情况下算法将直接使用不再额外缓存。取值为True时，仅在[FG\_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION生效。

#### \[h2\]needFlipInputColor

```c
bool FG_IntegrationInfo::needFlipInputColor
```

**描述**

输入的颜色纹理是否需要翻转。需要翻转情况下，算法映射Y轴坐标读取颜色纹理。取值为True时，仅在[FG\_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION生效。

#### \[h2\]needFlipOutputColor

```c
bool FG_IntegrationInfo::needFlipOutputColor
```

**描述**

预测帧是否需要翻转。需要翻转情况下，算法映射Y轴坐标进行翻转输出。取值为True时，仅在[FG\_PredictionMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_predictionmode-1)为FG\_PREDICTION\_MODE\_INTERPOLATION生效。
