---
title: "OhosImageSourceDelayTimeList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-ohosimagesourcedelaytimelist"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "C API"
  - "结构体"
  - "OhosImageSourceDelayTimeList"
captured_at: "2026-04-17T01:48:42.647Z"
---

# OhosImageSourceDelayTimeList

```c
struct OhosImageSourceDelayTimeList {...}
```

#### 概述

定义图像源延迟时间列表。由[OH\_ImageSource\_GetDelayTime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h#oh_imagesource_getdelaytime)获取。

**起始版本：** 10

**相关模块：** [Image](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image)

**所在头文件：** [image\_source\_mdk.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-image-source-mdk-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| int32\_t\* delayTimeList | 图像源延迟时间列表头地址。 |
| size\_t size = 0 | 图像源延迟时间列表大小。 |
