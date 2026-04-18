---
title: "InferShapeAndType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infershapeandtype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "InferShapeAndType"
captured_at: "2026-04-17T01:36:34.721Z"
---

# InferShapeAndType

#### 函数功能

推导Operator输出的shape和DataType。

关于DataType数据类型的定义，请参见[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。

#### 函数原型

```cpp
graphStatus InferShapeAndType();
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 推导成功，返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
