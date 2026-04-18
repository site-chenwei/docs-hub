---
title: "GetExpandDimsType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getexpanddimstype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "StorageFormat"
  - "GetExpandDimsType"
captured_at: "2026-04-17T01:36:30.131Z"
---

# GetExpandDimsType

#### 函数功能

获取补维规则。

#### 函数原型

```cpp
ExpandDimsType GetExpandDimsType() const
```

#### 参数说明

无

#### 返回值

补维规则。

#### 约束说明

无

#### 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
auto fmt_dim_type = format.GetExpandDimsType();
```
