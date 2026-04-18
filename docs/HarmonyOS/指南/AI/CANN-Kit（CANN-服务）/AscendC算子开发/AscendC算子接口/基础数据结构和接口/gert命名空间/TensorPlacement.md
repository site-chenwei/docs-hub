---
title: "TensorPlacement"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensorplacement"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TensorPlacement"
captured_at: "2026-04-17T01:36:31.357Z"
---

# TensorPlacement

```cpp
enum TensorPlacement {
    kOnDeviceHbm,  // < Tensor位于Device上的HBM内存
    kOnHost,       // < Tensor位于Host
    kFollowing,    // < Tensor位于Host，且数据紧跟在结构体后面
    kOnDeviceP2p,  // < Tensor位于Device上的P2p内存, 指的是HBM透到PCIE BAR空间上,可以让NPU跨PCIE能访问的地址空间
    kTensorPlacementEnd
};
```
