---
title: "SetPlacement"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-tensor-setplacement"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Tensor"
  - "SetPlacement"
captured_at: "2026-04-17T01:36:30.807Z"
---

# SetPlacement

#### 函数功能

设置tensor的placement。

#### 函数原型

```cpp
void SetPlacement(const TensorPlacement placement)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| placement | 输入 | 
需要设置的tensor的placement。

关于TensorPlacement类型的定义，请参见[TensorPlacement](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacement)。

 |

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
Tensor tensor{{{8, 3, 224, 224}, {16, 3, 224, 224}},       // shape
              {ge::FORMAT_ND, ge::FORMAT_FRACTAL_NZ, {}},  // format
              kFollowing,                                  // placement
              ge::DT_FLOAT16,                              // dt
              nullptr};
tensor.SetPlacement(TensorPlacement::kOnDeviceHbm);
auto placement = tensor.GetPlacement(); // kOnDeviceHbm
```
