---
title: "GetOutputsNum"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputsnum"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ComputeNodeInfo"
  - "GetOutputsNum"
captured_at: "2026-04-17T01:36:28.323Z"
---

# GetOutputsNum

#### 函数功能

获取算子在网络中的实际输出个数。

#### 函数原型

```cpp
size_t GetOutputsNum() const
```

#### 参数说明

无

#### 返回值

算子的实际输出个数。

#### 约束说明

无

#### 调用示例

```cpp
size_t index = compute_node_info->GetOutputsNum();
```
