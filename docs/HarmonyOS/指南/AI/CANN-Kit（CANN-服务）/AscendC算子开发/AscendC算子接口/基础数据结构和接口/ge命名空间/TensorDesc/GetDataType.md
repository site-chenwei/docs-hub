---
title: "GetDataType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getdatatype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "GetDataType"
captured_at: "2026-04-17T01:36:35.981Z"
---

# GetDataType

#### 函数功能

获取TensorDesc所描述Tensor的数据类型。

#### 函数原型

```cpp
DataType GetDataType() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| [DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype) | TensorDesc所描述的Tensor的数据类型。 |

#### 异常处理

无

#### 约束说明

由于返回的DataType信息为值拷贝，因此修改返回的DataType信息，不影响TensorDesc中已有的DataType信息。
