---
title: "OhosImageSource"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesource"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OhosImageSource"
captured_at: "2026-04-17T01:48:42.644Z"
---

# OhosImageSource

```c
struct OhosImageSource {...}
```

#### 概述

定义图像源输入资源，每次仅接收一种类型。由[OH\_ImageSource\_CreateFromUri](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createfromuri)、[OH\_ImageSource\_CreateFromFd](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createfromfd)和[OH\_ImageSource\_CreateFromData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_createfromdata)获取。

**起始版本：** 10

**废弃版本：** 11

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image\_source\_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* uri = nullptr | 图像源资源标识符，接受文件资源或者base64资源。 |
| size\_t uriSize = 0 | 图像源资源长度。 |
| int32\_t fd = - 1 | 图像源文件资源描述符。 |
| uint8\_t\* buffer = nullptr | 图像源缓冲区资源，接受格式化包缓冲区或者base64缓冲区。 |
| size\_t bufferSize = 0 | 图像源缓冲区资源大小。 |
