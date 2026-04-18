---
title: "GetTensorData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettensordata"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Tensor"
  - "GetTensorData"
captured_at: "2026-04-17T01:36:30.815Z"
---

# GetTensorData

#### 函数功能

获取tensor中的数据，返回只读的TensorData类型对象。

#### 函数原型

```cpp
const TensorData &GetTensorData() const
```

#### 参数说明

无

#### 返回值

只读的tensor data引用。

关于TensorData类型的定义，请参见[TensorData](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-construction-and-destructor-functions)。

#### 约束说明

无

#### 调用示例

```cpp
Tensor t = {{}, {}, {}, {}, nullptr};
const Tensor &ct = t;
std::vector<int> a = {10};
t.MutableTensorData() = TensorData{reinterpret_cast<void *>(a.data()), nullptr}; // 设置新tensordata
auto td = t.GetTensorData(); // TensorData{a, nullptr}
```
