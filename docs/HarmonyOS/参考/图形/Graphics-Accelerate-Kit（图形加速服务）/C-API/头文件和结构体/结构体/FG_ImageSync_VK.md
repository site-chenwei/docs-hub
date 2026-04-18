---
title: "FG_ImageSync_VK"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_sync___v_k"
menu_path:
  - "参考"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "FG_ImageSync_VK"
captured_at: "2026-04-17T01:48:51.821Z"
---

# FG\_ImageSync\_VK

#### 概述

此结构体描述超帧输入输出图像同步状态信息，用于创建超帧图像内存屏障。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

**所在头文件：** [frame\_generation\_vk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__vk_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| VkAccessFlagBits [accessMask](#accessmask) | 内存访问类型的位掩码。 |
| VkImageLayout [layout](#layout) | 图像和图像子资源的内存布局。 |
| VkPipelineStageFlagBits [stages](#stages) | 管线阶段的位掩码。 |

#### 结构体成员变量说明

#### \[h2\]accessMask

```c
VkAccessFlagBits FG_ImageSync_VK::accessMask
```

**描述**

内存访问类型的位掩码。

#### \[h2\]layout

```c
VkImageLayout FG_ImageSync_VK::layout
```

**描述**

图像和图像子资源的内存布局。

#### \[h2\]stages

```c
VkPipelineStageFlagBits FG_ImageSync_VK::stages
```

**描述**

管线阶段的位掩码。
