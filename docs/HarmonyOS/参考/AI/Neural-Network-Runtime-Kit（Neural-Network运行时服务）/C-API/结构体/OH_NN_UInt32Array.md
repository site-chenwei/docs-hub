---
title: "OH_NN_UInt32Array"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-uint32array"
menu_path:
  - "参考"
  - "AI"
  - "Neural Network Runtime Kit（Neural Network运行时服务）"
  - "C API"
  - "结构体"
  - "OH_NN_UInt32Array"
captured_at: "2026-04-17T01:49:05.730Z"
---

# OH\_NN\_UInt32Array

```c
typedef struct OH_NN_UInt32Array {...} OH_NN_UInt32Array
```

#### 概述

该结构体用于存储32位无符号整型数组。

**起始版本：** 9

**相关模块：** [NeuralNetworkRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime)

**所在头文件：** [neural\_network\_runtime\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t \*data | 无符号整型数组的指针。 |
| uint32\_t size | 数组长度。 |
