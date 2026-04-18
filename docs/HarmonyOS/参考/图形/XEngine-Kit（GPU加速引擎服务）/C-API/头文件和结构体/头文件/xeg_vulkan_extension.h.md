---
title: "xeg_vulkan_extension.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-extension-8h"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "头文件"
  - "xeg_vulkan_extension.h"
captured_at: "2026-04-17T01:48:52.410Z"
---

# xeg\_vulkan\_extension.h

#### 概述

XEngine扩展特性查询接口（Vulkan）。

**引用文件**：<xengine/xeg\_vulkan\_extension.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

#### 汇总

#### \[h2\]结构体

| 名称 | 描述 |
| :-- | :-- |
| struct [XEG\_ExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties) | 此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。 |

#### \[h2\]宏定义

| 名称 | 描述 |
| :-- | :-- |
| [XEG\_MAX\_EXTENSION\_NAME\_SIZE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_max_extension_name_size) 256 | XEngine扩展特性名称支持的最大长度。 |

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef struct [XEG\_ExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties) XEG\_ExtensionProperties | 此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。 |
| typedef VkResult(VKAPI\_PTR \* [PFN\_HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#pfn_hms_xeg_enumeratedeviceextensionproperties)) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties) \*pProperties) | XEngine Vulkan扩展特性查询接口函数指针定义。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| VKAPI\_ATTR VkResult VKAPI\_CALL [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) (VkPhysicalDevice physicalDevice, uint32\_t \*pPropertyCount, [XEG\_ExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties) \*pProperties) | XEngine Vulkan扩展特性查询接口。 |
