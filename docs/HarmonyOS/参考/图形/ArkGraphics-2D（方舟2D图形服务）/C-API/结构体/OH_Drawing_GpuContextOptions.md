---
title: "OH_Drawing_GpuContextOptions"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-oh-drawing-gpucontextoptions"
menu_path:
  - "参考"
  - "图形"
  - "ArkGraphics 2D（方舟2D图形服务）"
  - "C API"
  - "结构体"
  - "OH_Drawing_GpuContextOptions"
captured_at: "2026-04-17T01:48:49.982Z"
---

# OH\_Drawing\_GpuContextOptions

```c
typedef struct {...} OH_Drawing_GpuContextOptions
```

#### 概述

定义有关图形处理器上下文的选项。

**起始版本：** 12

**废弃版本：** 18

**相关模块：** [Drawing](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing)

**所在头文件：** [drawing\_gpu\_context.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-drawing-gpu-context-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| bool allowPathMaskCaching | 用于控制是否启用路径蒙版缓存，如果为true，则允许缓存路径蒙版纹理，如果为false，则不允许。 |
