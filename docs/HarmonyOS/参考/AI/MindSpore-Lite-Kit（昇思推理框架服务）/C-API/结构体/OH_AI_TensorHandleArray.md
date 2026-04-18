---
title: "OH_AI_TensorHandleArray"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-tensorhandlearray"
menu_path:
  - "参考"
  - "AI"
  - "MindSpore Lite Kit（昇思推理框架服务）"
  - "C API"
  - "结构体"
  - "OH_AI_TensorHandleArray"
captured_at: "2026-04-17T01:49:05.397Z"
---

# OH\_AI\_TensorHandleArray

```c
typedef struct OH_AI_TensorHandleArray {...} OH_AI_TensorHandleArray
```

#### 概述

张量数组结构体，用于存储张量数组指针和张量数组长度。

**起始版本：** 9

**相关模块：** [MindSpore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore)

**所在头文件：** [model.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-model-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| size\_t handle\_num | 张量数组长度。 |
| [OH\_AI\_TensorHandle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-mindspore-oh-ai-tensorhandle)\* handle\_list | 指向张量数组的指针。 |
