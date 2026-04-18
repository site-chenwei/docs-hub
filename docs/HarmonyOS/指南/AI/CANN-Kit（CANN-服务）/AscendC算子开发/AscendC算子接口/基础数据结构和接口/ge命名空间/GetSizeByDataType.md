---
title: "GetSizeByDataType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsizebydatatype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "GetSizeByDataType"
captured_at: "2026-04-17T01:36:38.232Z"
---

# GetSizeByDataType

#### 函数功能

根据传入的data\_type，获取该data\_type所占用的内存大小。

#### 函数原型

```cpp
inline int GetSizeByDataType(DataType data_type)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| data\_type | 输入 | 数据类型，请参见[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)。 |

#### 返回值

该data\_type所占用的内存大小（单位为bytes），如果传入非法值或不支持的数据类型，返回-1。

#### 异常处理

无

#### 约束说明

无
