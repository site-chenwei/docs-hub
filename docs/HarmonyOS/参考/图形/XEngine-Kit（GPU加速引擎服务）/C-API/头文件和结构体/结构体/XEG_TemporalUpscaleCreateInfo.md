---
title: "XEG_TemporalUpscaleCreateInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-temporalupscalecreateinfo"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_TemporalUpscaleCreateInfo"
captured_at: "2026-04-17T01:48:55.561Z"
---

# XEG\_TemporalUpscaleCreateInfo

#### 概述

此结构体描述创建[XEG\_TemporalUpscale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_temporalupscale)对象的信息。当结构体中的信息变化时，需要创建新的[XEG\_TemporalUpscale](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_temporalupscale)对象。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_temporal\_upscale.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-temporal-upscale-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| VkExtent2D [inputSize](#inputsize) | 输入图像的尺寸。支持的最大尺寸为2048 \* 1024。 |
| VkExtent2D [outputSize](#outputsize) | 输出图像的尺寸。 |
| VkRect2D [outputRegion](#outputregion) | 超分输出图像区域。 |
| VkFormat [outputFormat](#outputformat) | 输出图像的格式。 |
| int [jitterNum](#jitternum) | 相机抖动的周期数，取值范围为\[4, 16\]，推荐8。 |
| bool [isDepthReversed](#isdepthreversed) | 是否存在深度反转，如果使用0.0表示最远深度则需要设置此参数值为true，否则设置为false。 |

#### 结构体成员变量说明

#### \[h2\]inputSize

```cpp
VkExtent2D XEG_TemporalUpscaleCreateInfo::inputSize
```

**描述**

输入图像的尺寸。支持的最大尺寸为2048 \* 1024。

#### \[h2\]isDepthReversed

```cpp
bool XEG_TemporalUpscaleCreateInfo::isDepthReversed
```

**描述**

是否存在深度反转，如果使用0.0表示最远深度则需要设置此参数值为true，否则设置为false。

#### \[h2\]jitterNum

```cpp
int XEG_TemporalUpscaleCreateInfo::jitterNum
```

**描述**

相机抖动的周期数，取值范围为\[4, 16\]，推荐8。

#### \[h2\]outputFormat

```cpp
VkFormat XEG_TemporalUpscaleCreateInfo::outputFormat
```

**描述**

输出图像的格式。

#### \[h2\]outputRegion

```cpp
VkRect2D XEG_TemporalUpscaleCreateInfo::outputRegion
```

**描述**

超分输出图像区域。

#### \[h2\]outputSize

```cpp
VkExtent2D XEG_TemporalUpscaleCreateInfo::outputSize
```

**描述**

输出图像的尺寸。
