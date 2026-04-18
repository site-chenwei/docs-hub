---
title: "XEG_HPSRadixSortDescription"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsortdescription"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_HPSRadixSortDescription"
captured_at: "2026-04-17T01:48:55.446Z"
---

# XEG\_HPSRadixSortDescription

#### 概述

此结构体描述使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_hps_radix_sort_extension_name)扩展进行排序时所需的信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_hps.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-hps-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| XEG\_StructureType [sType](#stype) | 识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION。 |
| const void \* [pNext](#pnext) | 指向扩展结构的指针。 |
| VkBuffer [sortCount](#sortcount) | 存储要排序的索引数量的缓冲区，数量值从缓冲区第0位读取。 |
| VkBuffer [keyBuffer](#keybuffer) | 存储排序使用的key值的缓冲区，数据格式为32位无符号整数。 |
| VkBuffer [indexBuffer](#indexbuffer) | 存储待排序value值的缓冲区，数据格式为32位无符号整数。 |

#### 结构体成员变量说明

#### \[h2\]indexBuffer

```cpp
VkBuffer XEG_HPSRadixSortDescription::indexBuffer
```

**描述**

存储待排序value值的缓冲区，数据格式为32位无符号整数。

#### \[h2\]keyBuffer

```cpp
VkBuffer XEG_HPSRadixSortDescription::keyBuffer
```

**描述**

存储排序使用的key值的缓冲区，数据格式为32位无符号整数。

#### \[h2\]pNext

```cpp
const void* XEG_HPSRadixSortDescription::pNext
```

**描述**

指向扩展结构的指针。

#### \[h2\]sortCount

```cpp
VkBuffer XEG_HPSRadixSortDescription::sortCount
```

**描述**

存储要排序的索引数量的缓冲区，数量值从缓冲区第0位读取。

#### \[h2\]sType

```cpp
XEG_StructureType XEG_HPSRadixSortDescription::sType
```

**描述**

识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_RADIX\_SORT\_DESCRIPTION。
