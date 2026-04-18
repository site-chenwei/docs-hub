---
title: "GetComputeNodeInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcomputenodeinfo"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ExtendedKernelContext"
  - "GetComputeNodeInfo"
captured_at: "2026-04-17T01:36:29.035Z"
---

# GetComputeNodeInfo

#### 函数功能

获取本kernel对应的计算节点的信息。

图执行时本质上是执行图上的一个个结点的kernel在执行。本方法能够从KernelContext中获取保存的ComputeNodeInfo，而ComputeNodeInfo中包含InputDesc等信息。

#### 函数原型

```cpp
const ComputeNodeInfo *GetComputeNodeInfo() const
```

#### 参数说明

无

#### 返回值

计算节点的信息。

关于ComputeNodeInfo的定义，请参见[ComputeNodeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computenodeinfo-introduction)。

#### 约束说明

无

#### 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto compute_node_info = extend_context->GetComputeNodeInfo();
```
