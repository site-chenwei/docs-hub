---
title: "Image_String"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule-image-string"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "Image_String"
captured_at: "2026-04-17T01:48:42.267Z"
---

# Image\_String

```c
struct Image_String {...}
typedef struct Image_String Image_MimeType
typedef struct Image_String Image_String
```

#### 概述

字符串结构。

**起始版本：** 12

**相关模块：** [Image\_NativeModule](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-nativemodule)

**所在头文件：** [image\_common.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-common-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char \*data = nullptr | 字符类型数据。 |
| size\_t size = 0 | 数据长度。 |
