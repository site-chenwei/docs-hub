---
title: "VkMemoryGetNativeBufferInfoOHOS"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkmemorygetnativebufferinfoohos"
menu_path:
  - "参考"
  - "标准库"
  - "Vulkan"
  - "Vulkan扩展能力"
  - "VkMemoryGetNativeBufferInfoOHOS"
captured_at: "2026-04-17T01:49:07.393Z"
---

# VkMemoryGetNativeBufferInfoOHOS

```c
typedef struct VkMemoryGetNativeBufferInfoOHOS {...} VkMemoryGetNativeBufferInfoOHOS
```

#### 概述

用于从Vulkan内存中获取OH\_NativeBuffer。

**起始版本：** 10

**相关模块：** [Vulkan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan)

**所在头文件：** [vulkan\_ohos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| VkStructureType sType | 结构体类型，值必须为VK\_STRUCTURE\_TYPE\_MEMORY\_GET\_NATIVE\_BUFFER\_INFO\_OHOS。 |
| const void\* pNext | 下一级结构体指针，值必须为空。 |
| VkDeviceMemory memory | VkDeviceMemory对象，值必须为一个有效的VkDeviceMemory对象。 |
