---
title: "GetOutputHandleShapesAndTypes"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputhandleshapesandtypes"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferenceContext"
  - "GetOutputHandleShapesAndTypes"
captured_at: "2026-04-17T01:36:31.749Z"
---

# GetOutputHandleShapesAndTypes

#### 函数功能

在推理上下文中，获取算子输出句柄的[ShapeAndType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shapeandtype-construction-and-destructor)。

#### 函数原型

```cpp
const std::vector<std::vector<ShapeAndType>> &GetOutputHandleShapesAndTypes() const
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| const std::vector<std::vector<ShapeAndType>> | 算子输出句柄的[ShapeAndType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shapeandtype-construction-and-destructor)。 |

#### 异常处理

无

#### 约束说明

无
