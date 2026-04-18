---
title: "SetUnknownDimNumShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setunknowndimnumshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "SetUnknownDimNumShape"
captured_at: "2026-04-17T01:36:36.452Z"
---

# SetUnknownDimNumShape

#### 函数功能

设置tensor的shape为{-2}，用来表示tensor是完全未知的。

#### 函数原型

```cpp
graphStatus SetUnknownDimNumShape();
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 函数执行结果。执行成功，则该值为GRAPH\_SUCCESS(即0)，其他值则为执行失败。 |

#### 异常处理

无

#### 约束说明

无
