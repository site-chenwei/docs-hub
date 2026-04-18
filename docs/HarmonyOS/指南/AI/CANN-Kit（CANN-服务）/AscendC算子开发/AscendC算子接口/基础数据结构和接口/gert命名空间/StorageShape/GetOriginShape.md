---
title: "GetOriginShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "StorageShape"
  - "GetOriginShape"
captured_at: "2026-04-17T01:36:30.230Z"
---

# GetOriginShape

#### 函数功能

获取原始shape。

#### 函数原型

```cpp
const Shape &GetOriginShape() const
```

#### 参数说明

无

#### 返回值

原始shape

#### 约束说明

无

#### 调用示例

```cpp
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto origin_shape = shape.GetOriginShape(); // 3,256,256
```
