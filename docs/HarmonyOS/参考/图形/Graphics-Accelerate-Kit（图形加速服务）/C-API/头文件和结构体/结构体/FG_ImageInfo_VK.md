---
title: "FG_ImageInfo_VK"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_info___v_k"
menu_path:
  - "参考"
  - "图形"
  - "Graphics Accelerate Kit（图形加速服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "FG_ImageInfo_VK"
captured_at: "2026-04-17T01:48:51.823Z"
---

# FG\_ImageInfo\_VK

#### 概述

此结构体描述超帧输入输出图像信息。

**起始版本：** 5.0.0(12)

**相关模块：** [GraphicsAccelerate](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate)

**所在头文件：** [frame\_generation\_vk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/frame__generation__vk_8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [FG\_Image\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_image_vk)\* [image](#image) | 超帧输入输出图像结构体[FG\_Image\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_image_vk)对象的指针，该图像实例需要通过[HMS\_FG\_CreateImage\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_createimage_vk)进行创建，通过[HMS\_FG\_DestroyImage\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_destroyimage_vk)进行销毁。 |
| [FG\_ImageSync\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_sync___v_k) [initialSync](#initialsync) | [HMS\_FG\_Dispatch\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_dispatch_vk)执行前，该图像的同步状态。 |
| [FG\_ImageSync\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_f_g___image_sync___v_k) [finalSync](#finalsync) | [HMS\_FG\_Dispatch\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_dispatch_vk)执行后，该图像的同步状态。 |

#### 结构体成员变量说明

#### \[h2\]finalSync

```c
FG_ImageSync_VK FG_ImageInfo_VK::finalSync
```

**描述**

[HMS\_FG\_Dispatch\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_dispatch_vk)执行后，该图像的同步状态。

#### \[h2\]image

```c
FG_Image_VK* FG_ImageInfo_VK::image
```

**描述**

超帧输入输出图像结构体[FG\_Image\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#fg_image_vk)对象的指针，该图像实例需要通过[HMS\_FG\_CreateImage\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_createimage_vk)进行创建，通过[HMS\_FG\_DestroyImage\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_destroyimage_vk)进行销毁。

#### \[h2\]initialSync

```c
FG_ImageSync_VK FG_ImageInfo_VK::initialSync
```

**描述**

[HMS\_FG\_Dispatch\_VK](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_graphics_accelerate#hms_fg_dispatch_vk)执行前，该图像的同步状态。
