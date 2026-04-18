---
title: "AREngine_ClipPlaneDistance"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-struct-clipplanedistance"
menu_path:
  - "参考"
  - "图形"
  - "AR Engine（AR引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "AREngine_ClipPlaneDistance"
captured_at: "2026-04-17T01:48:46.205Z"
---

# AREngine\_ClipPlaneDistance

#### 概述

裁剪平面距离数据。

作为[HMS\_AREngine\_ARCamera\_GetProjectionMatrix](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine#hms_arengine_arcamera_getprojectionmatrix)接口输入。

**起始版本：** 5.0.0(12)

**相关模块：** [AR Engine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-capi-arengine)

**所在头文件：** [ar\_engine\_core.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arengine-header-file)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| float [near](#near) | OpenGL近裁剪平面距离，以m为单位。 |
| float [far](#far) | OpenGL远裁剪平面距离，以m为单位。 |

#### 结构体成员变量说明

#### \[h2\]far

```cpp
float AREngine_ClipPlaneDistance::far
```

**描述**

OpenGL远裁剪平面距离，以m为单位。

#### \[h2\]near

```cpp
float AREngine_ClipPlaneDistance::near
```

**描述**

OpenGL近裁剪平面距离，以m为单位。
