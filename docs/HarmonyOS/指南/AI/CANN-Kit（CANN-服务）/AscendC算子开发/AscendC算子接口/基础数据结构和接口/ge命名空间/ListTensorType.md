---
title: "ListTensorType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-listtensortype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "ListTensorType"
captured_at: "2026-04-17T01:36:34.433Z"
---

# ListTensorType

#### 函数功能

ListTensorType类用以定义输入或者输出支持的数据类型，是TensorType的封装，用于标识支持多个数据类型的情况。

#### 函数原型

```cpp
explicit ListTensorType(const TensorType &type)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| type | 输入 | 数据类型，具体参见[TensorType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensortype)。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无
