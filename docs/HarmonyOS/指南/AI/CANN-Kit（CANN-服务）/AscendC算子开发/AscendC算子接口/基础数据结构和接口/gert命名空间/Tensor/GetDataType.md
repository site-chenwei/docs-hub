---
title: "GetDataType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdatatype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Tensor"
  - "GetDataType"
captured_at: "2026-04-17T01:36:30.597Z"
---

# GetDataType

#### 函数功能

获取Tensor的数据类型。

#### 函数原型

```cpp
ge::DataType GetDataType() const
```

#### 参数说明

无

#### 返回值

返回Tensor中的数据类型。

关于ge::DataType的定义，请参见[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。

#### 约束说明

无

#### 调用示例

```cpp
StorageShape sh({1, 2, 3}, {1, 2, 3});
Tensor t = {sh, {}, {}, ge::DT_FLOAT, nullptr};
// ge::DT_FLOAT
auto dt = t.GetDataType();
```
