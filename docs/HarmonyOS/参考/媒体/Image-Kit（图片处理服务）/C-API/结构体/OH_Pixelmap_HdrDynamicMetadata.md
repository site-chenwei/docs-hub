---
title: "OH_Pixelmap_HdrDynamicMetadata"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-image-nativemodule-oh-pixelmap-hdrdynamicmetadata"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OH_Pixelmap_HdrDynamicMetadata"
captured_at: "2026-04-17T01:48:42.102Z"
---

# OH\_Pixelmap\_HdrDynamicMetadata

```c
typedef struct OH_Pixelmap_HdrDynamicMetadata {...} OH_Pixelmap_HdrDynamicMetadata
```

#### 概述

DR\_DYNAMIC\_METADATA关键字对应的动态元数据值。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)

**所在头文件：** [pixelmap\_native.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-pixelmap-native-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint8\_t\* data | 动态元数据的值。 |
| uint32\_t length | 动态元数据值的长度。 |
