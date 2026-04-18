---
title: "OpenGTX_FrameRenderInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___frame_render_info"
menu_path:
  - "参考"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "OpenGTX_FrameRenderInfo"
captured_at: "2026-04-17T01:48:51.953Z"
---

# OpenGTX\_FrameRenderInfo

#### 概述

此结构体描述帧渲染信息，游戏应用获取到帧属性后传递此参数。该参数中的相机矩阵通常用于优化渲染层降负载方案的画质效果。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

**所在头文件：** [opengtx\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengtx__base_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [OpenGTX\_Vector3](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___vector3) [mainCameraPosition](#maincameraposition) | 主摄像头的位置。x, y, z的取值范围\[-360,360\]。 |
| [OpenGTX\_Vector3](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_open_g_t_x___vector3) [mainCameraRotate](#maincamerarotate) | 主摄像头的转动，包括偏航、俯仰、侧滚。 x, y, z的取值范围\[-360,360\]。 |

#### 结构体成员变量说明

#### \[h2\]mainCameraPosition

```c
OpenGTX_Vector3 OpenGTX_FrameRenderInfo::mainCameraPosition
```

**描述**

主摄像头的位置。

#### \[h2\]mainCameraRotate

```c
OpenGTX_Vector3 OpenGTX_FrameRenderInfo::mainCameraRotate
```

**描述**

主摄像头的转动，包括偏航、俯仰、侧滚。 x, y, z的取值范围\[-360,360\]。
