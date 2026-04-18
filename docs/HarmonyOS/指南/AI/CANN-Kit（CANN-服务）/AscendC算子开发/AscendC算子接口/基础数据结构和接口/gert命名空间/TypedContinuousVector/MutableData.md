---
title: "MutableData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutabledata"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "TypedContinuousVector"
  - "MutableData"
captured_at: "2026-04-17T01:36:31.344Z"
---

# MutableData

#### 函数功能

获取首个元素的指针地址，\[GetData(), reinterpret\_cast<T \*>(GetData()) + GetSize())\]中的数据即为当前容器中保存的数据。

#### 函数原型

```cpp
T *MutableData()
```

#### 参数说明

无

#### 返回值

首个元素的指针地址。

#### 约束说明

无

#### 调用示例

```cpp
size_t capacity = 100U;
auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
auto cv = reinterpret_cast<TypedContinuousVector *>(cv_holder.get());
auto cap = cv->MutableData();
```
