---
title: "xeg_gles_extension.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xeg-gles-extension-8h"
menu_path:
  - "参考"
  - "图形"
  - "XEngine Kit（GPU加速引擎服务）"
  - "C API"
  - "头文件和结构体"
  - "头文件"
  - "xeg_gles_extension.h"
captured_at: "2026-04-17T01:48:52.362Z"
---

# xeg\_gles\_extension.h

#### 概述

XEngine扩展特性查询接口（OpenGL ES）。

**引用文件**：<xengine/xeg\_gles\_extension.h>

**库：** libxengine.so

**系统能力：** SystemCapability.Graphic.XEngine

**起始版本：** 5.0.0(12)

**相关模块：** [XEngine](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine)

#### 汇总

#### \[h2\]宏定义

| 名称 | 描述 |
| :-- | :-- |
| [XEG\_EXTENSIONS](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#xeg_extensions) 0x01U | 作为[HMS\_XEG\_GetString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring)接口的入参，以获取XEngine支持的OpenGL ES扩展特性。 |

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef const GLubyte \*(GL\_APIENTRYP [PFN\_HMS\_XEG\_GETSTRING](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#pfn_hms_xeg_getstring)) (GLenum name) | XEngine OpenGL ES扩展特性查询接口函数指针定义。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| const GLubyte \* [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring) (GLenum name) | XEngine OpenGL ES扩展特性查询接口。 |
