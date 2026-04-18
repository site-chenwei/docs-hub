---
title: "SetOriginFormat"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setoriginformat"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "StorageFormat"
  - "SetOriginFormat"
captured_at: "2026-04-17T01:36:30.104Z"
---

# SetOriginFormat

#### 函数功能

设置原始format。

#### 函数原型

```cpp
void SetOriginFormat(const ge::Format origin_format)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| origin\_format | 输入 | 原始format。 |

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
ExpandDimsType dim_type("1100");
StorageFormat format(ge::Format::FORMAT_NCHW, ge::Format::FORMAT_C1HWNC0, dim_type);
format.SetOriginFormat(ge::Format::FORMAT_NC);
```
