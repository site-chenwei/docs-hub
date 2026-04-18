---
title: "XEG_NNGIDescription"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_NNGIDescription"
captured_at: "2026-04-17T01:48:55.463Z"
---

# XEG\_NNGIDescription

#### 概述

此结构体描述更新NNGI用于计算光线追踪全局光照的所需的信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_rtgi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rtgi-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| XEG\_StructureType [sType](#stype) | 识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION。 |
| const void \* [pNext](#pnext) | 指向扩展结构的指针。 |
| float [inferenceCameraViewMatrix](#inferencecameraviewmatrix) \[16\] | 推理图像的相机观察矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4\*4列主序矩阵。 |
| float [inferenceCameraProjectionMatrix](#inferencecameraprojectionmatrix) \[16\] | 推理图像的相机投影矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4\*4列主序矩阵。 |
| VkImageView [inferenceInputDepthImage](#inferenceinputdepthimage) | 推理输入深度图像，不能为空，格式必须支持深度模板附件，存储Gbuffer的depth纹理。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中inferenceInputSize的分辨率保持一致。 |
| VkImageView [inferenceInputNormalImage](#inferenceinputnormalimage) | 推理输入法线向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中inferenceInputSize的分辨率保持一致。 |
| VkImageView [inferenceInputBaseColorMetallicImage](#inferenceinputbasecolormetallicimage) | 推理输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中inferenceInputSize的分辨率保持一致。 |
| VkImageView [inferenceOutputGIImage](#inferenceoutputgiimage) | 推理输出GI图像，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的间接光照值，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中inferenceOutputSize的分辨率保持一致。 |
| float [trainingCameraViewMatrix](#trainingcameraviewmatrix) \[16\] | 训练图像的相机观察矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4\*4列主序矩阵。 |
| float [trainingCameraProjectionMatrix](#trainingcameraprojectionmatrix) \[16\] | 训练图像的相机投影矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4\*4列主序矩阵。 |
| VkImageView [trainingInputPositionImage](#traininginputpositionimage) | 训练输入位置图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储每个像素的xyz轴坐标。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中trainingSize的分辨率保持一致。 |
| VkImageView [trainingInputNormalImage](#traininginputnormalimage) | 训练输入法向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中trainingSize的分辨率保持一致。 |
| VkImageView [trainingInputBaseColorMetallicImage](#traininginputbasecolormetallicimage) | 训练输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中trainingSize的分辨率保持一致。 |
| VkImageView [trainingInputGIImage](#traininginputgiimage) | 训练输入GI图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的辐射度值，忽略alpha通道信息。该训练图像的GI结果的质量越高，推理输出的GI结果的质量就越高。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中trainingSize的分辨率保持一致。 |
| VkAabbPositionsKHR [sceneAabb](#sceneaabb) | 渲染包围盒范围。 |
| bool [isSceneUnbounded](#issceneunbounded) = false | 渲染场景是否无界，当前只支持false。 |
| float [spatialScaleFactor](#spatialscalefactor) = 0 | 场景缩放因子，对于有界场景，无需设置，XEngine根据sceneAabb计算该值，对于无界场景，建议设置为平均深度。 |

#### 结构体成员变量说明

#### \[h2\]inferenceCameraProjectionMatrix

```cpp
float XEG_NNGIDescription::inferenceCameraProjectionMatrix[16]
```

**描述**

推理图像的相机投影矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4\*4列主序矩阵。

#### \[h2\]inferenceCameraViewMatrix

```cpp
float XEG_NNGIDescription::inferenceCameraViewMatrix[16]
```

**描述**

推理图像的相机观察矩阵，与用户生成Gbuffer使用的矩阵保持一致，必须是4\*4列主序矩阵。

#### \[h2\]inferenceInputBaseColorMetallicImage

```cpp
VkImageView XEG_NNGIDescription::inferenceInputBaseColorMetallicImage
```

**描述**

推理输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中inferenceInputSize的分辨率保持一致。

#### \[h2\]inferenceInputDepthImage

```cpp
VkImageView XEG_NNGIDescription::inferenceInputDepthImage
```

**描述**

推理输入深度图像，不能为空，格式必须支持深度模板附件，存储Gbuffer的depth纹理。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中inferenceInputSize的分辨率保持一致。

#### \[h2\]inferenceInputNormalImage

```cpp
VkImageView XEG_NNGIDescription::inferenceInputNormalImage
```

**描述**

推理输入法线向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中inferenceInputSize的分辨率保持一致。

#### \[h2\]inferenceOutputGIImage

```cpp
VkImageView XEG_NNGIDescription::inferenceOutputGIImage
```

**描述**

推理输出GI图像，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的间接光照值，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中inferenceOutputSize的分辨率保持一致。

#### \[h2\]isSceneUnbounded

```cpp
bool XEG_NNGIDescription::isSceneUnbounded = false
```

**描述**

渲染场景是否无界，当前只支持false。

#### \[h2\]pNext

```cpp
const void* XEG_NNGIDescription::pNext
```

**描述**

指向扩展结构的指针。

#### \[h2\]sceneAabb

```cpp
VkAabbPositionsKHR XEG_NNGIDescription::sceneAabb
```

**描述**

渲染包围盒范围。

#### \[h2\]spatialScaleFactor

```cpp
float XEG_NNGIDescription::spatialScaleFactor = 0
```

**描述**

场景缩放因子，对于有界场景，无需设置，XEngine根据sceneAabb计算该值，对于无界场景，建议设置为平均深度。

#### \[h2\]sType

```cpp
XEG_StructureType XEG_NNGIDescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NNGI\_DESCRIPTION。

#### \[h2\]trainingCameraProjectionMatrix

```cpp
float XEG_NNGIDescription::trainingCameraProjectionMatrix[16]
```

**描述**

训练图像的相机投影矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4\*4列主序矩阵。

#### \[h2\]trainingCameraViewMatrix

```cpp
float XEG_NNGIDescription::trainingCameraViewMatrix[16]
```

**描述**

训练图像的相机观察矩阵，该矩阵与用户生成PathTracing使用的矩阵保持一致，必须是4\*4列主序矩阵。

#### \[h2\]trainingInputBaseColorMetallicImage

```cpp
VkImageView XEG_NNGIDescription::trainingInputBaseColorMetallicImage
```

**描述**

训练输入基础颜色图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量，忽略alpha通道信息。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中trainingSize的分辨率保持一致。

#### \[h2\]trainingInputGIImage

```cpp
VkImageView XEG_NNGIDescription::trainingInputGIImage
```

**描述**

训练输入GI图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储红绿蓝分量的辐射度值，忽略alpha通道信息。该训练图像的GI结果的质量越高，推理输出的GI结果的质量就越高。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中trainingSize的分辨率保持一致。

#### \[h2\]trainingInputNormalImage

```cpp
VkImageView XEG_NNGIDescription::trainingInputNormalImage
```

**描述**

训练输入法向量图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储法线的xyz分量。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中trainingSize的分辨率保持一致。

#### \[h2\]trainingInputPositionImage

```cpp
VkImageView XEG_NNGIDescription::trainingInputPositionImage
```

**描述**

训练输入位置图像，不能为空，格式必须是至少3通道数据，RGB通道分别存储每个像素的xyz轴坐标。其分辨率和[XEG\_NNGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo)中trainingSize的分辨率保持一致。
