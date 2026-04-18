---
title: "Camera_MetadataObject"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-metadataobject"
menu_path:
  - "参考"
  - "媒体"
  - "Camera Kit（相机服务）"
  - "C API"
  - "结构体"
  - "Camera_MetadataObject"
captured_at: "2026-04-17T01:48:39.845Z"
---

# Camera\_MetadataObject

```c
typedef struct Camera_MetadataObject {...} Camera_MetadataObject
```

#### 概述

元数据对象基础。

**起始版本：** 11

**相关模块：** [OH\_Camera](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera)

**所在头文件：** [camera.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [Camera\_MetadataObjectType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-camera-h#camera_metadataobjecttype) type | 元数据对象类型。 |
| int64\_t timestamp | 元数据对象时间戳，单位为纳秒（ns）。 |
| [Camera\_Rect](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-camera-camera-rect)\* boundingBox | 检测到的元数据对象的轴对齐边界框。 |
