---
title: "VkImportNativeBufferInfoOHOS"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkimportnativebufferinfoohos"
menu_path:
  - "参考"
  - "标准库"
  - "Vulkan"
  - "Vulkan扩展能力"
  - "VkImportNativeBufferInfoOHOS"
captured_at: "2026-04-17T01:49:07.354Z"
---

# VkImportNativeBufferInfoOHOS

```c
typedef struct VkImportNativeBufferInfoOHOS {...} VkImportNativeBufferInfoOHOS
```

#### 概述

包含了OH\_NativeBuffer结构体的指针。

**起始版本：** 10

**相关模块：** [Vulkan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan)

**所在头文件：** [vulkan\_ohos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| VkStructureType sType | 结构体类型。 |
| const void\* pNext | 下一级结构体指针。 |
| struct [OH\_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-oh-nativebuffer)\* buffer | OH\_NativeBuffer结构体的指针。 |
