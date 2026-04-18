---
title: "GetIrInputsNum"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getirinputsnum"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ComputeNodeInfo"
  - "GetIrInputsNum"
captured_at: "2026-04-17T01:36:28.254Z"
---

# GetIrInputsNum

#### 函数功能

获取算子IR原型定义中的输入个数。

#### 函数原型

```cpp
size_t GetIrInputsNum() const
```

#### 参数说明

无

#### 返回值

IR原型中定义的输入个数，size\_t类型。

#### 约束说明

无

#### 调用示例

```cpp
size_t index = compute_node_info->GetIrInputsNum();
```
