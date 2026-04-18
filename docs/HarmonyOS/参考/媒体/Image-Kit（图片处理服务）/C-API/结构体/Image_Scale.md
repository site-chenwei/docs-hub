---
title: "Image_Scale"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-scale"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "Image_Scale"
captured_at: "2026-04-17T01:48:42.934Z"
---

# Image\_Scale

```c
typedef struct Image_Scale {...} Image_Scale
```

#### 概述

图像缩放倍数。

**起始版本：** 22

**相关模块：** [Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)

**所在头文件：** [image\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| float x | 宽度的缩放倍数。不能为0。 |
| float y | 高度的缩放倍数。不能为0。 |
