---
title: "SetDataType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdatatype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Tensor"
  - "SetDataType"
captured_at: "2026-04-17T01:36:30.583Z"
---

# SetDataType

#### 函数功能

设置Tensor的数据类型。

#### 函数原型

```cpp
void SetDataType(const ge::DataType data_type)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| data\_type | 输入 | 
需要设置的Tensor的数据类型。

关于ge::DataType的定义，请参见[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。

 |

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
StorageShape sh({1, 2, 3}, {1, 2, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
t.SetDataType(ge::DT_DOUBLE);
```
