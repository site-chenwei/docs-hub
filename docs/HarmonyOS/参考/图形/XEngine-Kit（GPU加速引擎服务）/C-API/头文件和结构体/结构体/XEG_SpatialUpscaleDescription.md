---
title: "XEG_SpatialUpscaleDescription"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-spatialupscaledescription"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_SpatialUpscaleDescription"
captured_at: "2026-04-17T01:48:55.566Z"
---

# XEG\_SpatialUpscaleDescription

#### 概述

此结构体描述下发空域GPU超分渲染命令时需要的图像信息。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_spatial\_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-spatial-upscale-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| VkImageView [inputImage](#inputimage) | 超分输入图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。 |
| VkImageView [outputImage](#outputimage) | 超分输出图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/I5gEofneS7WT-QxlfQ8khA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014855Z&HW-CC-Expire=86400&HW-CC-Sign=534A8C10DD5CE6A0BBA0CAA9D05DB193EA4425716DBAF55FEFDC6B4BF1860018)

对创建VkImageView的VkImage对象有以下约束：

imageType = VK\_IMAGE\_TYPE\_2D, extent.depth = 1, mipLevels = 1, arrayLayers = 1。

#### 结构体成员变量说明

#### \[h2\]inputImage

```cpp
VkImageView XEG_SpatialUpscaleDescription::inputImage
```

**描述**

超分输入图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。

#### \[h2\]outputImage

```cpp
VkImageView XEG_SpatialUpscaleDescription::outputImage
```

**描述**

超分输出图像的VkImageView，需要是有效的VkImageView，否则会出现未定义行为，如渲染失败或程序崩溃。
