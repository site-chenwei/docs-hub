---
title: "XEG_ExtensionProperties"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-extensionproperties"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "XEG_ExtensionProperties"
captured_at: "2026-04-17T01:48:55.347Z"
---

# XEG\_ExtensionProperties

#### 概述

此结构体描述通过[HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties)接口查询到的XEngine扩展特性集合。

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

**所在头文件：** [xeg\_vulkan\_extension.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-vulkan-extension-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char [extensionName](#extensionname) \[[XEG\_MAX\_EXTENSION\_NAME\_SIZE](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_max_extension_name_size)\] | XEngine支持的扩展特性名称。 |
| uint32\_t [version](#version) | XEngine支持的扩展特性版本号。 |

#### 结构体成员变量说明

#### \[h2\]extensionName

```cpp
char XEG_ExtensionProperties::extensionName[XEG_MAX_EXTENSION_NAME_SIZE]
```

**描述**

XEngine支持的扩展特性名称。

#### \[h2\]version

```cpp
uint32_t XEG_ExtensionProperties::version
```

**描述**

XEngine支持的扩展特性版本号。
