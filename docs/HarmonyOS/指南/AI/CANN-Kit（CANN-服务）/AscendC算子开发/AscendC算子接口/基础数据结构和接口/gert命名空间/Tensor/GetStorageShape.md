---
title: "GetStorageShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getstorageshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Tensor"
  - "GetStorageShape"
captured_at: "2026-04-17T01:36:30.653Z"
---

# GetStorageShape

#### 函数功能

获取运行时Tensor的StorageShape，此shape对象为只读。StorageShape和[GetOriginShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getoriginshape)的区别如下。OriginShape是Tensor最初创建时的形状，StorageShape是保存Tensor数据的底层存储的形状。运行时为了适配底层硬件，Tensor的StorageShape和其OriginShape可能会有所不同。

#### 函数原型

```cpp
const Shape &GetStorageShape() const
```

#### 参数说明

无

#### 返回值

只读的运行时shape引用。

#### 约束说明

无

#### 调用示例

```cpp
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.GetStorageShape(); // 2,1,3
```
