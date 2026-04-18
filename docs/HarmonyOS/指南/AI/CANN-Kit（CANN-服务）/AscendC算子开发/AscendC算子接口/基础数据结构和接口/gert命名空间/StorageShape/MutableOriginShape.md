---
title: "MutableOriginShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-mutableoriginshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "StorageShape"
  - "MutableOriginShape"
captured_at: "2026-04-17T01:36:30.282Z"
---

# MutableOriginShape

#### 函数功能

获取可写的原始shape。

#### 函数原型

```cpp
Shape &MutableOriginShape()
```

#### 参数说明

无

#### 返回值

可写的原始shape。

#### 约束说明

无

#### 调用示例

```cpp
StorageShape shape({3, 256, 256}, {256, 256, 3});
auto origin_shape = shape.MutableOriginShape(); // 3,256,256
```
