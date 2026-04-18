---
title: "OH_NativeBuffer_Plane"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer-oh-nativebuffer-plane"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_NativeBuffer_Plane"
captured_at: "2026-04-17T01:48:49.874Z"
---

# OH\_NativeBuffer\_Plane

```c
typedef struct {...} OH_NativeBuffer_Plane
```

#### 概述

单个图像平面格式信息。

**起始版本：** 12

**相关模块：** [OH\_NativeBuffer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-nativebuffer)

**所在头文件：** [native\_buffer.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-native-buffer-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint64\_t offset | 图像平面的偏移量，单位为Byte。 |
| uint32\_t rowStride | 从图像一行的第一个值到下一行的第一个值的距离，单位为Byte。 |
| uint32\_t columnStride | 从图像一列的第一个值到下一列的第一个值的距离，单位为Byte。 |
