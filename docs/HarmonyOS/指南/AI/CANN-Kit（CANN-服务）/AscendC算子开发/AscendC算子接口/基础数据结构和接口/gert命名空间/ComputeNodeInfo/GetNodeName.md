---
title: "GetNodeName"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-computenodeinfo-getnodename"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ComputeNodeInfo"
  - "GetNodeName"
captured_at: "2026-04-17T01:36:28.254Z"
---

# GetNodeName

#### 函数功能

获取算子的名称。

#### 函数原型

```cpp
const char *GetNodeName() const
```

#### 参数说明

无

#### 返回值

返回算子的名称。

#### 约束说明

无

#### 调用示例

```cpp
auto node_name = compute_node_info.GetNodeName();
```
