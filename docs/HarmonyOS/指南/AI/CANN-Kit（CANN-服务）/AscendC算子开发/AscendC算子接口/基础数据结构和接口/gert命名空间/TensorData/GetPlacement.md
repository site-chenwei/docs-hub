---
title: "GetPlacement"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getplacement"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TensorData"
  - "GetPlacement"
captured_at: "2026-04-17T01:36:30.369Z"
---

# GetPlacement

#### 函数功能

获取tensor的placement，tensor数据所在的设备位置。

```cpp
// tensor数据所在的设备位置
enum TensorPlacement {
  kOnDeviceHbm,  // < Tensor位于Device上的HBM内存
  kOnHost,       // < Tensor位于Host
  kFollowing,    // < Tensor位于Host，且数据紧跟在结构体后面
  kTensorPlacementEnd
};
```

#### 函数原型

```cpp
TensorPlacement GetPlacement() const
```

#### 参数说明

无

#### 返回值

tensor的placement。

关于TensorPlacement类型的定义，请参见[TensorPlacement](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacement)。

#### 约束说明

无

#### 调用示例

```cpp
std::vector<int> a = {10};
auto addr = reinterpret_cast<void *>(a.data());
TensorData td(addr, HostAddrManager, 100U, kOnHost);
auto td_place = td.GetPlacement(); // kOnHost
```
