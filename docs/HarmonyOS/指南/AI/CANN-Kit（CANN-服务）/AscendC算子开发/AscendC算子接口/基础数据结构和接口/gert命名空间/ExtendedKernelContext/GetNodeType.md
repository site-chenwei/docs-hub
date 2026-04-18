---
title: "GetNodeType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getnodetype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ExtendedKernelContext"
  - "GetNodeType"
captured_at: "2026-04-17T01:36:29.000Z"
---

# GetNodeType

#### 函数功能

获取算子的类型。

#### 函数原型

```cpp
const char *GetNodeType() const
```

#### 参数说明

无

#### 返回值

算子的类型。

#### 约束说明

无

#### 调用示例

```cpp
// 假设已存在KernelContext *context
auto extend_context = reinterpret_cast<ExtendedKernelContext *>(context);
auto node_type = extend_context->GetNodeType();
```
