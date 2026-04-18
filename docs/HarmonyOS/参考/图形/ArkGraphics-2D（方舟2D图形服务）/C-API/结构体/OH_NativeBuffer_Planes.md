---
title: "OH_NativeBuffer_Planes"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-planes"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_NativeBuffer_Planes"
captured_at: "2026-04-17T01:48:49.888Z"
---

# OH\_NativeBuffer\_Planes

```c
typedef struct OH_NativeBuffer_Planes {...} OH_NativeBuffer_Planes
```

#### 概述

OH\_NativeBuffer的图像平面格式信息。

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)

**所在头文件：** [native\_buffer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t planeCount | 不同平面的数量。 |
| [OH\_NativeBuffer\_Plane](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-plane) planes\[4\] | 图像平面格式信息数组。 |
