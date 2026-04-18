---
title: "operator=="
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-storageformat-operatora"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "StorageFormat"
  - "operator=="
captured_at: "2026-04-17T01:36:30.175Z"
---

# operator==

#### 函数功能

判断格式是否相等。

#### 函数原型

```cpp
bool operator==(const StorageFormat &other) const
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| other | 输入 | 另一种格式。 |

#### 返回值

true代表相等。

false代表不等。

#### 约束说明

无

#### 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
StorageFormat another_format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_NC, dim_type);
bool is_same_fmt = format == another_format; // false
```
