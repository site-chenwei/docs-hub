---
title: "GetOriginFormat"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getoriginformat"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "GetOriginFormat"
captured_at: "2026-04-17T01:36:36.902Z"
---

# GetOriginFormat

#### 函数功能

获取Tensor的原始Format。

该Format是指原始网络模型的Format。

#### 函数原型

```cpp
ge::Format GetOriginFormat() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| ge::Format | 返回tensor的原始Format值，默认值为FORMAT\_RESERVED。 |

#### 异常处理

无

#### 约束说明

无
