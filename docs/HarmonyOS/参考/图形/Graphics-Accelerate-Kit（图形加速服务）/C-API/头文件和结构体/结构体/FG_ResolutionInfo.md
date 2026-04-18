---
title: "FG_ResolutionInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___resolution_info"
menu_path:
  - "参考"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "FG_ResolutionInfo"
captured_at: "2026-04-17T01:48:51.828Z"
---

# FG\_ResolutionInfo

#### 概述

此结构体描述超帧输入输出图像的分辨率。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

**所在头文件：** [frame\_generation\_base.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__base_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [FG\_Dimension2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dimension2_d) [inputColorResolution](#inputcolorresolution) | 真实渲染帧颜色缓冲区分辨率。 |
| [FG\_Dimension2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dimension2_d) [inputDepthStencilResolution](#inputdepthstencilresolution) | 真实渲染帧深度模板缓冲区分辨率。当设置成0时, 系统中会默认使用[inputColorResolution](#inputcolorresolution)作为真实帧深度模板缓冲区分辨率。 |
| [FG\_Dimension2D](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___dimension2_d) [outputColorResolution](#outputcolorresolution) | 预测帧缓冲区分辨率。当设置成0时, 系统中会默认使用[inputColorResolution](#inputcolorresolution)作为预测帧缓冲区分辨率。 |

#### 结构体成员变量说明

#### \[h2\]inputColorResolution

```c
FG_Dimension2D FG_ResolutionInfo::inputColorResolution
```

**描述**

真实渲染帧颜色缓冲区分辨率。

#### \[h2\]inputDepthStencilResolution

```c
FG_Dimension2D FG_ResolutionInfo::inputDepthStencilResolution
```

**描述**

真实渲染帧深度模板缓冲区分辨率。当设置成0时, 系统中会默认使用[inputColorResolution](#inputcolorresolution)作为真实帧深度模板缓冲区分辨率。

#### \[h2\]outputColorResolution

```c
FG_Dimension2D FG_ResolutionInfo::outputColorResolution
```

**描述**

预测帧缓冲区分辨率。当设置成0时, 系统中会默认使用[inputColorResolution](#inputcolorresolution)作为预测帧缓冲区分辨率。
