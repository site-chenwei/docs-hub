---
title: "VkNativeBufferUsageOHOS"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vknativebufferusageohos"
menu_path:
  - "参考"
  - "标准库"
  - "Vulkan"
  - "Vulkan扩展能力"
  - "VkNativeBufferUsageOHOS"
captured_at: "2026-04-17T01:49:07.350Z"
---

# VkNativeBufferUsageOHOS

```c
typedef struct VkNativeBufferUsageOHOS {...} VkNativeBufferUsageOHOS
```

#### 概述

提供HarmonyOS NativeBuffer用途的说明。

**起始版本：** 10

**相关模块：** [Vulkan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan)

**所在头文件：** [vulkan\_ohos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| VkStructureType sType | 结构体类型，值必须为VK\_STRUCTURE\_TYPE\_NATIVE\_BUFFER\_USAGE\_OHOS。 |
| void\* pNext | 下一级结构体指针。 |
| uint64\_t OHOSNativeBufferUsage | NativeBuffer的用途说明。 |
