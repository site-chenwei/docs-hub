---
title: "GetSize"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvectorvector-getsize"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ContinuousVectorVector"
  - "GetSize"
captured_at: "2026-04-17T01:36:28.588Z"
---

# GetSize

#### 函数功能

获取当前存放的实际元素数量。

#### 函数原型

```cpp
size_t GetSize() const
```

#### 参数说明

无

#### 返回值

当前存放的实际元素数量。

#### 约束说明

无

#### 调用示例

```cpp
// 创建ContinuousVectorVector对象cvv
// ...
// 增加元素
// ...
auto cv = cvv->add(inner_vector_capacity);
// ...
// 获取当前存放的实际元素数量
auto size = cvv->GetSize();
```
