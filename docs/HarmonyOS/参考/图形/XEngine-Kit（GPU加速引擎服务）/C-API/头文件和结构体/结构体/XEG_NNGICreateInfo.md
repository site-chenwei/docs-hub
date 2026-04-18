---
title: "XEG_NNGICreateInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngicreateinfo"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_NNGICreateInfo"
captured_at: "2026-04-17T01:48:55.451Z"
---

# XEG\_NNGICreateInfo

#### 概述

此结构体描述创建具有NNGI特性的[XEG\_RTGI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_RTGI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgi)对象。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_rtgi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rtgi-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| XEG\_StructureType [sType](#stype) | 识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO。 |
| const void \* [pNext](#pnext) | 指向扩展结构的指针。 |
| XEG\_RTGIQualityMode [qualityMode](#qualitymode) | 输出图像的质量模式，必须为[XEG\_RTGIQualityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgiqualitymode)中的枚举值。 |
| VkExtent2D [inferenceInputSize](#inferenceinputsize) | 推理输入图像的分辨率，必须与[XEG\_NNGIDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription)中的推理输入图像的分辨率保持一致。 |
| VkExtent2D [inferenceOutputSize](#inferenceoutputsize) | 推理输出图像的分辨率，必须与[XEG\_NNGIDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription)中的推理输出图像的分辨率保持一致，推荐使用（640，368）。 |
| VkExtent2D [trainingSize](#trainingsize) | 训练图像的分辨率，必须与[XEG\_NNGIDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription)中的训练输入和输出图像的分辨率保持一致，推荐使用（64，32）。 |

#### 结构体成员变量说明

#### \[h2\]inferenceInputSize

```cpp
VkExtent2D XEG_NNGICreateInfo::inferenceInputSize
```

**描述**

推理输入图像的分辨率，必须与[XEG\_NNGIDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription)中的推理输入图像的分辨率保持一致。

#### \[h2\]inferenceOutputSize

```cpp
VkExtent2D XEG_NNGICreateInfo::inferenceOutputSize
```

**描述**

推理输出图像的分辨率，必须与[XEG\_NNGIDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription)中的推理输出图像的分辨率保持一致，推荐使用（640，368）。

#### \[h2\]pNext

```cpp
const void* XEG_NNGICreateInfo::pNext
```

**描述**

指向扩展结构的指针。

#### \[h2\]qualityMode

```cpp
XEG_RTGIQualityMode XEG_NNGICreateInfo::qualityMode
```

**描述**

输出图像的质量模式，必须为[XEG\_RTGIQualityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgiqualitymode)中的枚举值。

#### \[h2\]sType

```cpp
XEG_StructureType XEG_NNGICreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_NNGI\_CREATE\_INFO。

#### \[h2\]trainingSize

```cpp
VkExtent2D XEG_NNGICreateInfo::trainingSize
```

**描述**

训练图像的分辨率，必须与[XEG\_NNGIDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-nngidescription)中的训练输入和输出图像的分辨率保持一致，推荐使用（64，32）。
