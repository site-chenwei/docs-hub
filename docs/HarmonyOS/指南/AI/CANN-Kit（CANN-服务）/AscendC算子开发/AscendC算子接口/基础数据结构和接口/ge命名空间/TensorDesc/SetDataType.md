---
title: "SetDataType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-setdatatype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "SetDataType"
captured_at: "2026-04-17T01:36:36.144Z"
---

# SetDataType

#### 函数功能

向TensorDesc中设置Tensor的数据类型。

#### 函数原型

```cpp
void SetDataType(DataType dt);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| dt | 输入 | 
需设置的TensorDesc所描述的Tensor的数据类型信息。

关于DataType类型，请参见[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。

 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

无
