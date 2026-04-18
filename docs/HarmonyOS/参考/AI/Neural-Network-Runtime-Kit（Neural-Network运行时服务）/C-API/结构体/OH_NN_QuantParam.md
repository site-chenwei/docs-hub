---
title: "OH_NN_QuantParam"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-oh-nn-quantparam"
menu_path:
  - "参考"
  - "AI"
  - "Neural Network Runtime Kit（Neural Network运行时服务）"
  - "C API"
  - "结构体"
  - "OH_NN_QuantParam"
captured_at: "2026-04-17T01:49:05.768Z"
---

# OH\_NN\_QuantParam

```c
typedef struct OH_NN_QuantParam {...} OH_NN_QuantParam
```

#### 概述

量化信息。

在量化的场景中，32位浮点型数据根据以下公式量化为定点数据：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/U2LkVldhTCuPeeyTRsxiJA/zh-cn_image_0000002569021575.png?HW-CC-KV=V1&HW-CC-Date=20260417T014906Z&HW-CC-Expire=86400&HW-CC-Sign=CED9719F3E8EC3AE80A360E2C107A81D9A96B8CB1AD76BA63568AD0AE48EAC32)

其中s和z是量化参数，在OH\_NN\_QuantParam中通过scale和zeroPoint保存，r是浮点数，q是量化后的结果，q\_min是量化后下界，q\_max是量化后的上界，计算方式如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/6burhtk0TUK751mPyR1WQQ/zh-cn_image_0000002568901565.png?HW-CC-KV=V1&HW-CC-Date=20260417T014906Z&HW-CC-Expire=86400&HW-CC-Sign=A16A04204BAF311BB80037794419D556099B5C575F41CA03A3ACEE35DFB2617C)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/CebN11XZQmiStAVIMaUozQ/zh-cn_image_0000002538021864.png?HW-CC-KV=V1&HW-CC-Date=20260417T014906Z&HW-CC-Expire=86400&HW-CC-Sign=235A1770EBA7452A376253CB2F4ECC83CCA2494174939E07218994D95C1B8C58)

clamp函数定义如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/HJR536AZTNS2JV1Q5jERNQ/zh-cn_image_0000002538181790.png?HW-CC-KV=V1&HW-CC-Date=20260417T014906Z&HW-CC-Expire=86400&HW-CC-Sign=89D0556E9CFD3E1AA8706EEB986B23E437A840F7E199C0F45FC6CA5B56CB7977)

**起始版本：** 9

**废弃版本：** 11

**替代接口：** [NN\_QuantParam](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime-nn-quantparam)

**相关模块：** [NeuralNetworkRuntime](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neuralnetworkruntime)

**所在头文件：** [neural\_network\_runtime\_type.h](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-runtime-type-h)

#### 汇总

#### \[h2\]成员变量

| 名称 | 描述 |
| :-- | :-- |
| uint32\_t quantCount | 指定numBits、scale和zeroPoint数组的长度。在per-layer量化的场景下，quantCount通常指定为1，即一个张量所有通道共享一套量化参数；在per-channel量化场景下，quantCount通常和张量通道数一致，每个通道使用自己的量化参数。 |
| const uint32\_t \*numBits | 量化位数。 |
| const double \*scale | 指向量化公式中scale数据的指针。 |
| const int32\_t \*zeroPoint | 指向量化公式中zero point数据的指针。 |
