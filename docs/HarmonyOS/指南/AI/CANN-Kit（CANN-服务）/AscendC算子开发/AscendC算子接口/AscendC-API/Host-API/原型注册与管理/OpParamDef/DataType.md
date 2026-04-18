---
title: "DataType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-datatype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "Host API"
  - "原型注册与管理"
  - "OpParamDef"
  - "DataType"
captured_at: "2026-04-17T01:36:27.541Z"
---

# DataType

#### 函数功能

定义算子参数数据类型。

#### 函数原型

```cpp
OpParamDef &DataType(std::vector<ge::DataType> types);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| types | 输入 | 算子参数数据类型，ge::DataType请参考[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。 |

#### 返回值

[OpParamDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-paramtype)算子定义。

#### 约束说明

无
