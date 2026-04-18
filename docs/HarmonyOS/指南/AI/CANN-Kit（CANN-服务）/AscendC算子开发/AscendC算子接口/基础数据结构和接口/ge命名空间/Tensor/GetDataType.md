---
title: "GetDataType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getdatatype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "GetDataType"
captured_at: "2026-04-17T01:36:36.817Z"
---

# GetDataType

#### 函数功能

获取Tensor的DataType。

#### 函数原型

```cpp
ge::DataType GetDataType() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| ge:: [DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype) | 返回tensor的DataType值，默认值为DT\_UNDEFINED。 |

#### 异常处理

无

#### 约束说明

无
