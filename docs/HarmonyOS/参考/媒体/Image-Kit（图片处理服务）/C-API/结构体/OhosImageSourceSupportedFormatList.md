---
title: "OhosImageSourceSupportedFormatList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformatlist"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OhosImageSourceSupportedFormatList"
captured_at: "2026-04-17T01:48:42.654Z"
---

# OhosImageSourceSupportedFormatList

```c
struct OhosImageSourceSupportedFormatList {...}
```

#### 概述

定义图像源支持的格式字符串列表。由[OH\_ImageSource\_GetSupportedFormats](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_getsupportedformats)获取。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image\_source\_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| struct [OhosImageSourceSupportedFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcesupportedformat)\*\* supportedFormatList = nullptr | 图像源支持的格式字符串列表头地址。 |
| size\_t size = 0 | 图像源支持的格式字符串列表大小。 |
