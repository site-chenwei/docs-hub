---
title: "HiAI_SingleOpExecutorConvolutionParam"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-sopexec-convparam"
menu_path:
  - "参考"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "C API"
  - "头文件和结构体"
  - "结构体"
  - "HiAI_SingleOpExecutorConvolutionParam"
captured_at: "2026-04-17T01:49:04.705Z"
---

# HiAI\_SingleOpExecutorConvolutionParam

#### 概述

[HMS\_HiAISingleOpExecutor\_CreateConvolution](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_createconvolution)输入参数。

**起始版本：** 5.0.0(12)

**相关模块：** [CANN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit)

**所在头文件：** [hiai\_single\_op.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-single-op-8h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| [HiAI\_SingleOpOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopoptions) \* [options](#options) | 指向[HiAI\_SingleOpOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopdescriptor) \* [opDesc](#opdesc) | 指向卷积算子对应的[HiAI\_SingleOpDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensorDesc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleoptensordesc) \* [input](#input) | 指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensorDesc](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleoptensordesc) \* [output](#output) | 指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleoptensor) \* [filter](#filter) | 指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。 |
| [HiAI\_SingleOpTensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleoptensor) \* [bias](#bias) | 指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。 |

#### 结构体成员变量说明

#### \[h2\]bias

```cpp
HiAI_SingleOpTensor* HiAI_SingleOpExecutorConvolutionParam::bias
```

**描述**

指向偏置Tensor的指针。如果卷积没有偏置，则该值可以是空指针。

#### \[h2\]filter

```cpp
HiAI_SingleOpTensor* HiAI_SingleOpExecutorConvolutionParam::filter
```

**描述**

指向卷积核Tensor的指针。该值不能为空指针，否则接口调用失败。

#### \[h2\]input

```cpp
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorConvolutionParam::input
```

**描述**

指向输入Tensor描述的指针。该值不能为空指针，否则接口调用失败。

#### \[h2\]opDesc

```cpp
HiAI_SingleOpDescriptor* HiAI_SingleOpExecutorConvolutionParam::opDesc
```

**描述**

指向卷积算子对应的[HiAI\_SingleOpDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopdescriptor)对象的指针。该值不能为空指针，否则接口调用失败。

#### \[h2\]options

```cpp
HiAI_SingleOpOptions* HiAI_SingleOpExecutorConvolutionParam::options
```

**描述**

指向[HiAI\_SingleOpOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_singleopoptions)对象的指针。该值不能为空指针，否则接口调用失败。

#### \[h2\]output

```cpp
HiAI_SingleOpTensorDesc* HiAI_SingleOpExecutorConvolutionParam::output
```

**描述**

指向输出Tensor描述的指针。该值不能为空指针，否则接口调用失败。
