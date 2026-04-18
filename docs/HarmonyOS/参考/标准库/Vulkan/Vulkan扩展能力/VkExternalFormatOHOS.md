---
title: "VkExternalFormatOHOS"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-vkexternalformatohos"
menu_path:
  - "参考"
  - "标准库"
  - "Vulkan"
  - "Vulkan扩展能力"
  - "VkExternalFormatOHOS"
captured_at: "2026-04-17T01:49:07.392Z"
---

# VkExternalFormatOHOS

```c
typedef struct VkExternalFormatOHOS {...} VkExternalFormatOHOS
```

#### 概述

表示外部定义的格式标识符。

**起始版本：** 10

**相关模块：** [Vulkan](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan)

**所在头文件：** [vulkan\_ohos.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-vulkan-ohos-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| VkStructureType sType | 结构体类型，值必须为VK\_STRUCTURE\_TYPE\_EXTERNAL\_FORMAT\_OHOS。 |
| void\* pNext | pNext为空或者下一级结构体指针。 |
| uint64\_t externalFormat | 外部定义的格式标识符。 |
