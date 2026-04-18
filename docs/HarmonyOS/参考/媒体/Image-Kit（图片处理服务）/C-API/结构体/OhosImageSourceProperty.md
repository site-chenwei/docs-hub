---
title: "OhosImageSourceProperty"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourceproperty"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OhosImageSourceProperty"
captured_at: "2026-04-17T01:48:42.713Z"
---

# OhosImageSourceProperty

```c
struct OhosImageSourceProperty {...}
```

#### 概述

定义图像源属性键值字符串。此选项给[OH\_ImageSource\_GetImageProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_getimageproperty)和[OH\_ImageSource\_ModifyImageProperty](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_modifyimageproperty)接口使用。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image\_source\_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* value = nullptr | 定义图像源属性键值字符串头地址。 |
| size\_t size = 0 | 定义图像源属性键值字符串大小。 |
