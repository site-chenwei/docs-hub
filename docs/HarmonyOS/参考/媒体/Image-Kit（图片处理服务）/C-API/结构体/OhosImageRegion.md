---
title: "OhosImageRegion"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimageregion"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OhosImageRegion"
captured_at: "2026-04-17T01:48:42.567Z"
---

# OhosImageRegion

```c
struct OhosImageRegion {...}
```

#### 概述

定义图像源解码的范围选项。是[OhosImageDecodingOps](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagedecodingops)的成员变量。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image\_source\_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t x | 起始x坐标，用pixels表示。 |
| int32\_t y | 起始y坐标，用pixels表示。 |
| int32\_t width | 宽度范围，用pixels表示。 |
| int32\_t height | 高度范围，用pixels表示。 |
