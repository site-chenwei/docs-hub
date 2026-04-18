---
title: "HiDebug_GraphicsMemorySummary"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-hidebug-graphicsmemorysummary"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Performance Analysis Kit（性能分析服务）"
  - "C API"
  - "结构体"
  - "HiDebug_GraphicsMemorySummary"
captured_at: "2026-04-17T01:48:35.234Z"
---

# HiDebug\_GraphicsMemorySummary

```c
typedef struct HiDebug_GraphicsMemorySummary {...} HiDebug_GraphicsMemorySummary
```

#### 概述

应用图形显存占用详情的结构定义。

**起始版本：** 21

**相关模块：** [HiDebug](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug)

**所在头文件：** [hidebug\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidebug-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t gl | gl内存大小，RenderService渲染进程加载所需资源占用的内存，例如图片、纹理等，以KB为单位。 |
| uint32\_t graph | graph内存大小，进程统计的DMA内存占用，包括直接通过接口申请的DMA buffer和通过allocator\_host申请的DMA buffer，以KB为单位。 |
