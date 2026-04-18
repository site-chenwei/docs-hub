---
title: "MutableStorageShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-mutablestorageshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Tensor"
  - "MutableStorageShape"
captured_at: "2026-04-17T01:36:30.670Z"
---

# MutableStorageShape

#### 函数功能

获取运行时Tensor的shape，此shape对象是可变的。

#### 函数原型

```cpp
Shape &MutableStorageShape()
```

#### 参数说明

无

#### 返回值

运行时shape的引用。

#### 约束说明

无

#### 调用示例

```cpp
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.MutableStorageShape(); // 2,1,3
```
