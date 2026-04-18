---
title: "XEG_DDGIDescription"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgidescription"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_DDGIDescription"
captured_at: "2026-04-17T01:48:55.329Z"
---

# XEG\_DDGIDescription

#### 概述

此结构体描述更新DDGI探针辐照度及渲染输出GI图像所需的信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_rtgi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rtgi-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| XEG\_StructureType [sType](#stype) | 识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION。 |
| const void \* [pNext](#pnext) | 指向扩展结构的指针。 |
| float [viewMatrix](#viewmatrix) \[16\] | 相机观察矩阵，必须是4\*4列主序矩阵。 |
| float [projectionMatrix](#projectionmatrix) \[16\] | 相机投影矩阵，必须是4\*4列主序矩阵。 |
| VkImageView [inputNormalImage](#inputnormalimage) | 输入Gbuffer法向量图像，其宽高必须和[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。 |
| VkImageView [inputDepthImage](#inputdepthimage) | 输入Gbuffer深度图像，其宽高必须和[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。 |
| VkImageView [inputBasecolorMetallicImage](#inputbasecolormetallicimage) | 输入Gbuffer基础颜色和金属度图像，其宽高必须和[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。 |
| VkImageView [inputDirectionImage](#inputdirectionimage) | 输入探针发射光线方向图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkImageView [inputRayRadianceDistanceImage](#inputrayradiancedistanceimage) | 输入探针发射光线交点的辐射率及距离图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkImageView [inputRayHitNormalAndMetallicImage](#inputrayhitnormalandmetallicimage) | 输入探针发射光线交点的法向量及金属度图像，其宽高分别为：探针发射光线数量，输入探针数量。 |
| VkBuffer [inputVolumeIndexAndProbeIndex](#inputvolumeindexandprobeindex) | 输入探针的索引信息，对应于探针发射光线的信息，每个数据为两个uint值（探针索引/体积索引）。 |
| uint32\_t [inputProbeCount](#inputprobecount) | 输入探针数量，对应于inputVolumeIndexAndProbeIndex中的有效数据个数。 |
| VkBuffer [outputVolumeIndexAndProbeIndex](#outputvolumeindexandprobeindex) | 输出探针的索引信息，指示用户下一帧如何发射光线，每个数据为两个uint值（探针索引/体积索引）。 |
| VkBuffer [outputProbeCount](#outputprobecount) | 输出探针数量，对应于outputVolumeIndexAndProbeIndex中的有效数据个数。 |
| VkImageView [outputGIImage](#outputgiimage) | 输出GI 2D图像，其宽高必须和[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致，VkFormat为VK\_FORMAT\_R8G8B8A8\_UNORM。 |
| uint32\_t [enableVolumeNumber](#enablevolumenumber) | 使用的体积数量，必须不大于[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中的numberVolume值。 |
| const struct [XEG\_DDGIVolumeEntryParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgivolumeentryparameters) \* [pVolumeEntryParameters](#pvolumeentryparameters) | 输入体积参数信息，对应于[XEG\_DDGIVolumeEntryParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgivolumeentryparameters)。该结构体数组的大小必须等于enableVolumeNumber的值。 |

#### 结构体成员变量说明

#### \[h2\]enableVolumeNumber

```cpp
uint32_t XEG_DDGIDescription::enableVolumeNumber
```

**描述**

使用的体积数量，必须不大于[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中的numberVolume值。

#### \[h2\]inputBasecolorMetallicImage

```cpp
VkImageView XEG_DDGIDescription::inputBasecolorMetallicImage
```

**描述**

输入Gbuffer基础颜色和金属度图像，其宽高必须和[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。

#### \[h2\]inputDepthImage

```cpp
VkImageView XEG_DDGIDescription::inputDepthImage
```

**描述**

输入Gbuffer深度图像，其宽高必须和[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。

#### \[h2\]inputDirectionImage

```cpp
VkImageView XEG_DDGIDescription::inputDirectionImage
```

**描述**

输入探针发射光线方向图像，其宽高分别为：探针发射光线数量，输入探针数量。

#### \[h2\]inputNormalImage

```cpp
VkImageView XEG_DDGIDescription::inputNormalImage
```

**描述**

输入Gbuffer法向量图像，其宽高必须和[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致。

#### \[h2\]inputProbeCount

```cpp
uint32_t XEG_DDGIDescription::inputProbeCount
```

**描述**

输入探针数量，对应于inputVolumeIndexAndProbeIndex中的有效数据个数。

#### \[h2\]inputRayHitNormalAndMetallicImage

```cpp
VkImageView XEG_DDGIDescription::inputRayHitNormalAndMetallicImage
```

**描述**

输入探针发射光线交点的法向量及金属度图像，其宽高分别为：探针发射光线数量，输入探针数量。

#### \[h2\]inputRayRadianceDistanceImage

```cpp
VkImageView XEG_DDGIDescription::inputRayRadianceDistanceImage
```

**描述**

输入探针发射光线交点的辐射率及距离图像，其宽高分别为：探针发射光线数量，输入探针数量。

#### \[h2\]inputVolumeIndexAndProbeIndex

```cpp
VkBuffer XEG_DDGIDescription::inputVolumeIndexAndProbeIndex
```

**描述**

输入探针的索引信息，对应于探针发射光线的信息，每个数据为两个uint值（探针索引/体积索引）。

#### \[h2\]outputGIImage

```cpp
VkImageView XEG_DDGIDescription::outputGIImage
```

**描述**

输出GI 2D图像，其宽高必须和[XEG\_DDGICreateInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo)中viewSize的宽高保持一致，VkFormat为VK\_FORMAT\_R8G8B8A8\_UNORM。

#### \[h2\]outputProbeCount

```cpp
VkBuffer XEG_DDGIDescription::outputProbeCount
```

**描述**

输出探针数量，对应于outputVolumeIndexAndProbeIndex中的有效数据个数。

#### \[h2\]outputVolumeIndexAndProbeIndex

```cpp
VkBuffer XEG_DDGIDescription::outputVolumeIndexAndProbeIndex
```

**描述**

输出探针的索引信息，指示用户下一帧如何发射光线，每个数据为两个uint值（探针索引/体积索引）。

#### \[h2\]pNext

```cpp
const void* XEG_DDGIDescription::pNext
```

**描述**

指向扩展结构的指针。

#### \[h2\]projectionMatrix

```cpp
float XEG_DDGIDescription::projectionMatrix[16]
```

**描述**

相机投影矩阵，必须是4\*4列主序矩阵。

#### \[h2\]pVolumeEntryParameters

```cpp
const struct XEG_DDGIVolumeEntryParameters* XEG_DDGIDescription::pVolumeEntryParameters
```

**描述**

输入体积参数信息，对应于[XEG\_DDGIVolumeEntryParameters](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgivolumeentryparameters)。该结构体数组的大小必须等于enableVolumeNumber的值。

#### \[h2\]sType

```cpp
XEG_StructureType XEG_DDGIDescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_DDGI\_DESCRIPTION。

#### \[h2\]viewMatrix

```cpp
float XEG_DDGIDescription::viewMatrix[16]
```

**描述**

相机观察矩阵，必须是4\*4列主序矩阵。
