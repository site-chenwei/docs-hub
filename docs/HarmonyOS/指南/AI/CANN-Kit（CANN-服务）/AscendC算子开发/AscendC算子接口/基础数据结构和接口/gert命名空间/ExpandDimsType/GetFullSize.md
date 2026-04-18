---
title: "GetFullSize"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getfullsize"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ExpandDimsType"
  - "GetFullSize"
captured_at: "2026-04-17T01:36:28.795Z"
---

# GetFullSize

#### 函数功能

获取补维后的dim数。

#### 函数原型

```cpp
AxisIndex GetFullSize() const
```

#### 参数说明

无

#### 返回值

返回补维规则的长度，或者说是补维规则描述的维度。

#### 约束说明

无

#### 调用示例

```cpp
ExpandDimsType type1("1001");
auto dim_num = type1.GetFullSize(); // dim_num=4
```
