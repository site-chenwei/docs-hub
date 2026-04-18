---
title: "GetSize"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-getsize"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ContinuousVector"
  - "GetSize"
captured_at: "2026-04-17T01:36:28.697Z"
---

# GetSize

#### 函数功能

获取当前保存的元素个数。

#### 函数原型

```cpp
size_t GetSize() const
```

#### 参数说明

无

#### 返回值

当前保存的元素个数。

#### 约束说明

无

#### 调用示例

```cpp
size_t capacity = 100U;
auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
auto size = cv->GetSize(); // 0U
```
