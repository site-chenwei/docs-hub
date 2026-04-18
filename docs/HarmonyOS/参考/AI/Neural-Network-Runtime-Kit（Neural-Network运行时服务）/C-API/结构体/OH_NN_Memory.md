---
title: "OH_NN_Memory"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-memory"
menu_path:
  - "参考"
  - "AI"
  - "Neural Network Runtime Kit（Neural Network运行时服务）"
  - "C API"
  - "结构体"
  - "OH_NN_Memory"
captured_at: "2026-04-17T01:49:05.768Z"
---

# OH\_NN\_Memory

```c
typedef struct OH_NN_Memory {...} OH_NN_Memory
```

#### 概述

内存结构体。

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN\_Tensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-nn-tensor)

**相关模块：** [NeuralNetworkRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime)

**所在头文件：** [neural\_network\_runtime\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| void \* const data | 指向共享内存的指针，该共享内存通常由底层硬件驱动申请。 |
| const size\_t length | 记录共享内存的字节长度。 |
