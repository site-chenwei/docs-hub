---
title: "OH_AI_ShapeInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-shapeinfo"
menu_path:
  - "参考"
  - "AI"
  - "MindSpore Lite Kit（昇思推理框架服务）"
  - "C API"
  - "结构体"
  - "OH_AI_ShapeInfo"
captured_at: "2026-04-17T01:49:05.410Z"
---

# OH\_AI\_ShapeInfo

```c
typedef struct OH_AI_ShapeInfo {...} OH_AI_ShapeInfo
```

#### 概述

形状维度大小，预留最大维度是32，当前实际支持的最大维度是8。

**起始版本：** 9

**相关模块：** [MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)

**所在头文件：** [model.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-model-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| size\_t shape\_num | 维度数组长度。 |
| int64\_t shape\[OH\_AI\_MAX\_SHAPE\_NUM\] | 维度数组。 |
