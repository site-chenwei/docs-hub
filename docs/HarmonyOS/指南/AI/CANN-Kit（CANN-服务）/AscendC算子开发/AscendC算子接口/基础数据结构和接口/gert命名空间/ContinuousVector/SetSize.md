---
title: "SetSize"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-setsize"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ContinuousVector"
  - "SetSize"
captured_at: "2026-04-17T01:36:28.712Z"
---

# SetSize

#### 函数功能

设置当前保存的元素个数。

#### 函数原型

```cpp
ge::graphStatus SetSize(const size_t size)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| size | 输入 | 当前保存的元素个数。 |

#### 返回值

成功时返回ge::GRAPH\_SUCCESS。

设置的size>capacity时，返回失败ge::GRAPH\_FAILED。

#### 约束说明

无

#### 调用示例

```cpp
size_t capacity = 100U;
auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
auto ret = cv->SetSize(10U); // ge::GRAPH_SUCCESS
ret = cv->GetSize(101U); // ge::GRAPH_FAILED
```
