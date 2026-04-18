---
title: "SetRealDimCnt"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setrealdimcnt"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "SetRealDimCnt"
captured_at: "2026-04-17T01:36:36.300Z"
---

# SetRealDimCnt

#### 函数功能

向TensorDesc中设置Tensor的实际维度数目。

通过[GetShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getshape)接口返回的Shape的维度可能存在补1的场景，因此可以通过该接口设置Shape的实际维度个数。

#### 函数原型

```cpp
void SetRealDimCnt(const int64_t real_dim_cnt);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| real\_dim\_cnt | 输入 | 需设置的TensorDesc的实际数据维度数目信息。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无
