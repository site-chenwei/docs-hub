---
title: "SetDataType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setdatatype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "SetDataType"
captured_at: "2026-04-17T01:36:37.366Z"
---

# SetDataType

#### 函数功能

设置Tensor的Datatype。

#### 函数原型

```cpp
graphStatus SetDataType(const ge::DataType &dtype);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| dtype | 输入 | 
需设置的DataType值。

关于DataType类型，请参见[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。

 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
