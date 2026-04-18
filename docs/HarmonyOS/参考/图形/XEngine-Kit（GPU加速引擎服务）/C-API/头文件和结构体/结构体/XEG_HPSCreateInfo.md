---
title: "XEG_HPSCreateInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpscreateinfo"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_HPSCreateInfo"
captured_at: "2026-04-17T01:48:55.379Z"
---

# XEG\_HPSCreateInfo

#### 概述

此结构体描述创建[XEG\_HPS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_hps)对象的信息。

**起始版本：** 6.0.0(20)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_hps.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-hps-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| XEG\_StructureType [sType](#stype) | 识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO。 |
| const void \* [pNext](#pnext) | 指向扩展结构的指针，不允许为空。表示启用的XEngine HPS扩展，如当使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_hps_radix_sort_extension_name)扩展时，必须指定为[XEG\_HPSRadixSort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsort)。 |

#### 结构体成员变量说明

#### \[h2\]pNext

```cpp
const void* XEG_HPSCreateInfo::pNext
```

**描述**

指向扩展结构的指针，不允许为空。表示启用的XEngine HPS扩展，如当使用[XEG\_HPS\_RADIX\_SORT\_EXTENSION\_NAME](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_hps_radix_sort_extension_name)扩展时，必须指定为[XEG\_HPSRadixSort](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-hpsradixsort)。

#### \[h2\]sType

```cpp
XEG_StructureType XEG_HPSCreateInfo::sType
```

**描述**

识别此结构的[XEG\_StructureType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_structuretype)值，必须是XEG\_STRUCTURE\_TYPE\_HPS\_CREATE\_INFO。
