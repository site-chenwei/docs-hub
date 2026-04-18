---
title: "HMS_GCP_PickedColorInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-colorinfo"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Pen Kit（手写笔服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "HMS_GCP_PickedColorInfo"
captured_at: "2026-04-17T01:48:33.726Z"
---

# HMS\_GCP\_PickedColorInfo

#### 概述

定义取色颜色信息的结构体。

**系统能力：** SystemCapability.Stylus.ColorPicker

**起始版本：** 5.0.0(12)

**相关模块：** [GlobalColorPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-c)

**所在头文件：** [native\_gcp\_api.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-headerfile-declare)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [HMS\_GCP\_Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-struct-color) color | 提取的颜色值。 |
| [HMS\_GCP\_ColorSpace](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pen-imagefeaturepicker-c#hms_gcp_colorspace) colorSpace | 颜色所属的颜色空间。 |
| int64\_t [timestamp](#timestamp) | 提取颜色的时间戳。 |

#### 结构体成员变量说明

#### \[h2\]color

```c
HMS_GCP_Color HMS_GCP_PickedColorInfo::color
```

**描述**

提取的颜色值。

#### \[h2\]colorSpace

```c
HMS_GCP_ColorSpace HMS_GCP_PickedColorInfo::colorSpace
```

**描述**

颜色所属的颜色空间。

#### \[h2\]timestamp

```c
int64_t HMS_GCP_PickedColorInfo::timestamp
```

**描述**

提取颜色的时间戳。
