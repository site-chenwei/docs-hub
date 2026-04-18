---
title: "XEG_DDGICreateInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-ddgicreateinfo"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_DDGICreateInfo"
captured_at: "2026-04-17T01:48:55.338Z"
---

# XEG\_DDGICreateInfo

#### 概述

此结构体描述创建具有DDGI特性的[XEG\_RTGI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgi)对象的信息，当结构体中的信息变化时，需要创建新的[XEG\_RTGI](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgi)对象。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_rtgi.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-rtgi-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| XEG\_StructureType [sType](#stype) | 识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO。 |
| const void \* [pNext](#pnext) | 指向扩展结构的指针。 |
| XEG\_RTGIQualityMode [qualityMode](#qualitymode) | 输出图像的质量模式，必须为[XEG\_RTGIQualityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgiqualitymode)中的枚举值。 |
| uint32\_t [numberVolume](#numbervolume) | 需要同时渲染的最大体积数量，范围为\[1, 9\]。 |
| VkExtent2D [scaledView](#scaledview) | 渲染宽高缩小倍率，建议范围为\[1, 4\]，必须不小于1。 |
| VkExtent2D [viewSize](#viewsize) | 输出GI图像的渲染宽高。 |
| bool [enableCloud](#enablecloud) | 是否开启端云模式，true为开启，false为关闭。 |

#### 结构体成员变量说明

#### \[h2\]enableCloud

```cpp
bool XEG_DDGICreateInfo::enableCloud
```

**描述**

是否开启端云模式，true为开启，false为关闭。

#### \[h2\]numberVolume

```cpp
uint32_t XEG_DDGICreateInfo::numberVolume
```

**描述**

需要同时渲染的最大体积数量，范围为\[1, 9\]。

#### \[h2\]pNext

```cpp
const void* XEG_DDGICreateInfo::pNext
```

**描述**

指向扩展结构的指针。

#### \[h2\]qualityMode

```cpp
XEG_RTGIQualityMode XEG_DDGICreateInfo::qualityMode
```

**描述**

输出图像的质量模式，必须为[XEG\_RTGIQualityMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_rtgiqualitymode)中的枚举值。

#### \[h2\]scaledView

```cpp
VkExtent2D XEG_DDGICreateInfo::scaledView
```

**描述**

渲染宽高缩小倍率，建议范围为\[1, 4\]，必须不小于1。

#### \[h2\]sType

```cpp
XEG_StructureType XEG_DDGICreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_DDGI\_CREATE\_INFO。

#### \[h2\]viewSize

```cpp
VkExtent2D XEG_DDGICreateInfo::viewSize
```

**描述**

输出GI图像的渲染宽高。
