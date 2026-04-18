---
title: "GetStr"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getstr"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "RuntimeAttrs"
  - "GetStr"
captured_at: "2026-04-17T01:36:29.788Z"
---

# GetStr

#### 函数功能

获取string类型的属性值。

#### 函数原型

```cpp
const char *GetStr(const size_t index) const
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| index | 输入 | 属性在IR原型定义中以及在OP\_IMPL注册中的索引。 |

#### 返回值

指向属性值的指针。

#### 约束说明

无

#### 调用示例

```cpp
const RuntimeAttrs * runtime_attrs = kernel_context->GetAttrs();
const char *attr0 = runtime_attrs->GetStr(0);
```
