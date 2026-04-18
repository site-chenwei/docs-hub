---
title: "OH_AI_CallBackParam"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-callbackparam"
menu_path:
  - "参考"
  - "AI"
  - "MindSpore Lite Kit（昇思推理框架服务）"
  - "C API"
  - "结构体"
  - "OH_AI_CallBackParam"
captured_at: "2026-04-17T01:49:05.416Z"
---

# OH\_AI\_CallBackParam

```c
typedef struct OH_AI_CallBackParam {...} OH_AI_CallBackParam
```

#### 概述

回调函数中传入的算子信息。

**起始版本：** 9

**相关模块：** [MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)

**所在头文件：** [model.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-model-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| char\* node\_name | 算子名称。 |
| char\* node\_type | 算子类型。 |
