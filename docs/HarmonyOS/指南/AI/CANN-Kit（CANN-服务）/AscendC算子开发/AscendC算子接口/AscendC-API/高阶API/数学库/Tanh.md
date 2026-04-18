---
title: "Tanh"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-math-tanh"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "高阶API"
  - "数学库"
  - "Tanh"
captured_at: "2026-04-17T01:36:27.361Z"
---

# Tanh

#### 功能说明

按元素做逻辑回归Tanh，计算公式如下，其中PAR表示矢量计算单元一个迭代能够处理的元素个数 ：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/EvE8FCcYS7SIKe5ZabE0og/zh-cn_image_0000002569019945.png?HW-CC-KV=V1&HW-CC-Date=20260417T013629Z&HW-CC-Expire=86400&HW-CC-Sign=B28351536AC1EB3147062AC49644BAA727E01737D2E459E86A9B9DDBA3D577A4)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/QsbZFqtIRWeKUbxr7979TA/zh-cn_image_0000002568899937.png?HW-CC-KV=V1&HW-CC-Date=20260417T013629Z&HW-CC-Expire=86400&HW-CC-Sign=6212BD59A5D3018E73F258B023533A9B9A3A48D18CB2300ACE0494FE93E5F1FF)

#### 函数原型

```cpp
template <typename T, bool isReuseSource = false>
__aicore__ inline void Tanh(const LocalTensor<T>& dstTensor, const LocalTensor<T>& srcTensor, const uint32_t calCount)
```

#### 参数说明

**表1** 模板参数说明

| 参数名 | 描述 |
| :-- | :-- |
| T | 操作数的数据类型。支持的数据类型为：half/float。 |
| isReuseSource | 是否允许修改源操作数。该参数预留，传入默认值false即可。 |

**表2** 接口参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| dstTensor | 输出 | 
目的操作数。

类型为[LocalTensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-localtensor)，支持的TPosition为VECIN/VECCALC/VECOUT。

 |
| srcTensor | 输入 | 

源操作数。

类型为[LocalTensor](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-localtensor)，支持的TPosition为VECIN/VECCALC/VECOUT。

 |
| calCount | 输入 | 实际计算数据元素个数。 |

#### 返回值

无

#### 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

#### 约束说明

-   操作数地址偏移对齐要求请参见[通用约束](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-general-constraints)。
    
-   输入输出操作数参与计算的数据长度要求32B对齐。
    

#### 调用示例

```cpp
AscendC::TPipe pipe;
// calCount为实际计算数据元素个数
// 其它处理省略
AscendC::Tanh<T, false>(yLocal, xLocal, calCount);
```
