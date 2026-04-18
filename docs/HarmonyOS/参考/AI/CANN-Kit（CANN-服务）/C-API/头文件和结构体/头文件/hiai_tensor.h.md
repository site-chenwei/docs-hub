---
title: "hiai_tensor.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit-hiai-tensor-8h"
menu_path:
  - "参考"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "C API"
  - "头文件和结构体"
  - "头文件"
  - "hiai_tensor.h"
captured_at: "2026-04-17T01:49:04.612Z"
---

# hiai\_tensor.h

#### 概述

模型推理时使用的输入输出内存相关的辅助接口。

通过以下接口，可以关联AippParam到tensor中，也可计算图片格式需要申请的tensor内存大小。

**引用文件：** <CANNKit/hiai\_tensor.h>

**库：** libhiai\_foundation.so

**系统能力：** SystemCapability.AI.HiAIFoundation

**起始版本：** 4.1.0(11)

**相关模块：** [CANN](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit)

#### 汇总

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| size\_t [HMS\_HiAITensor\_GetSizeWithImageFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hms_hiaitensor_getsizewithimageformat) (NN\_TensorDesc \*desc, [HiAI\_ImageFormat](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_imageformat) format) | 根据NN\_TensorDesc和HiAI\_ImageFormat计算申请tensor的大小。 |
| OH\_NN\_ReturnCode [HMS\_HiAITensor\_SetAippParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hms_hiaitensor_setaippparams) (NN\_Tensor \*tensor, [HiAI\_AippParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/cannkit#hiai_aippparam) \*aippParams\[\], size\_t aippNum) | 给NN\_Tensor设置AippParams。 |
