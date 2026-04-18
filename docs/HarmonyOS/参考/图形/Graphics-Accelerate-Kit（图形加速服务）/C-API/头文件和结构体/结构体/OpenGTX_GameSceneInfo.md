---
title: "OpenGTX_GameSceneInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___game_scene_info"
menu_path:
  - "参考"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "OpenGTX_GameSceneInfo"
captured_at: "2026-04-17T01:48:51.935Z"
---

# OpenGTX\_GameSceneInfo

#### 概述

此结构体描述游戏场景信息，游戏应用获取到场景后传递此参数。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

**所在头文件：** [opengtx\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengtx__base_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OpenGTX\_SceneID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#opengtx_sceneid-1) [sceneID](#sceneid) | 游戏场景类型。 |
| char\* [description](#description) | 对游戏场景的描述，字节长度范围\[0,256\]。 |
| int32\_t [recommendFPS](#recommendfps) | 当前场景的建议帧率。取值范围0、\[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)\]，若设置0则该值不生效。 |
| int32\_t [minFPS](#minfps) | 当前场景预期的最小帧率。取值范围0、\[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)\]，若设置0则该值不生效。 |
| int32\_t [maxFPS](#maxfps) | 当前场景预期的最大帧率。取值范围0、\[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)\]，若设置0则该值不生效。 |
| [OpenGTX\_ResolutionValue](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___resolution_value) [resolutionCurValue](#resolutioncurvalue) | 当前场景的分辨率，取值范围360p-8k。 |

#### 结构体成员变量说明

#### \[h2\]description

```c
char* OpenGTX_GameSceneInfo::description
```

**描述**

对游戏场景的描述，字节长度范围\[0,256\]。

#### \[h2\]maxFPS

```c
int32_t OpenGTX_GameSceneInfo::maxFPS
```

**描述**

当前场景预期的最大帧率。取值范围0、\[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)\]，若设置0则该值不生效。

#### \[h2\]minFPS

```c
int32_t OpenGTX_GameSceneInfo::minFPS
```

**描述**

当前场景预期的最小帧率。取值范围0、\[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)\]，若设置0则该值不生效。

#### \[h2\]recommendFPS

```c
int32_t OpenGTX_GameSceneInfo::recommendFPS
```

**描述**

当前场景的建议帧率。取值范围0、\[30,[targetFPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___config_description#targetfps)\]，若设置0则该值不生效。

#### \[h2\]resolutionCurValue

```c
OpenGTX_ResolutionValue OpenGTX_GameSceneInfo::resolutionCurValue
```

**描述**

当前场景的分辨率，取值范围360p-8k。

#### \[h2\]sceneID

```c
OpenGTX_SceneID OpenGTX_GameSceneInfo::sceneID
```

**描述**

游戏场景类型。
