---
title: "VkNativeBufferPropertiesOHOS"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferpropertiesohos"
menu_path:
  - "参考"
  - "标准库"
  - "Vulkan"
  - "Vulkan扩展能力"
  - "VkNativeBufferPropertiesOHOS"
captured_at: "2026-04-17T01:49:07.348Z"
---

# VkNativeBufferPropertiesOHOS

```c
typedef struct VkNativeBufferPropertiesOHOS {...} VkNativeBufferPropertiesOHOS
```

#### 概述

包含了NativeBuffer的属性。

**起始版本：** 10

**相关模块：** [Vulkan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan)

**所在头文件：** [vulkan\_ohos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| VkStructureType sType | 结构体类型。 |
| void\* pNext | 下一级结构体指针。 |
| VkDeviceSize allocationSize | 占用的内存大小。 |
| uint32\_t memoryTypeBits | 内存类型。 |
