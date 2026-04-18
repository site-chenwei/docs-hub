---
title: "OhosImageSourceSupportedFormat"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformat"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OhosImageSourceSupportedFormat"
captured_at: "2026-04-17T01:48:42.658Z"
---

# OhosImageSourceSupportedFormat

```c
struct OhosImageSourceSupportedFormat {...}
```

#### 概述

定义图像源支持的格式字符串。此选项给[OhosImageSourceSupportedFormatList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformatlist)和[OH\_ImageSource\_GetSupportedFormats](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_getsupportedformats)接口使用。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image\_source\_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* format = nullptr | 图像源支持的格式字符串头地址。 |
| size\_t size = 0 | 图像源支持的格式字符串大小。 |
