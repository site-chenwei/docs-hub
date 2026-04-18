---
title: "Add"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvectorvector-add"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ContinuousVectorVector"
  - "Add"
captured_at: "2026-04-17T01:36:28.588Z"
---

# Add

#### 函数功能

新增一个ContinuousVector元素，其中新增ContinuousVector元素的容量为inner\_vector\_capacity。

#### 函数原型

```cpp
template<typename T> ContinuousVector *Add(size_t inner_vector_capacity)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| inner\_vector\_capacity | 输入 | 新增ContinuousVector元素的容量。 |

#### 返回值

新增ContinuousVector元素的首地址。

#### 约束说明

无

#### 调用示例

```cpp
// 创建ContinuousVectorVector对象cvv
// ...
// 增加元素
size_t inner_vector_capacity = 2;
auto cv = cvv->Add(inner_vector_capacity);
```
