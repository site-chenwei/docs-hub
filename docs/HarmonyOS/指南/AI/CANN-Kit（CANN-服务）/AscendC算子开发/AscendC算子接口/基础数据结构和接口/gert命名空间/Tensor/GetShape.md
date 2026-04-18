---
title: "GetShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Tensor"
  - "GetShape"
captured_at: "2026-04-17T01:36:30.685Z"
---

# GetShape

#### 函数功能

获取Tensor的shape，包含运行时和原始shape。

#### 函数原型

```cpp
const StorageShape &GetShape() const
StorageShape &GetShape()
```

#### 参数说明

无

#### 返回值

-   const StorageShape &GetShape() const：返回只读的shape引用。
    
-   StorageShape &GetShape()：返回shape引用。
    

关于StorageShape类型的定义，请参见[StorageShape](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageshape-introduction)。

#### 约束说明

无

#### 调用示例

```cpp
StorageShape sh({1, 2, 3}, {2, 1, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
auto shape = t.GetShape(); // sh
```
