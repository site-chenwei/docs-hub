---
title: "SetPlacement"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-setplacement"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "SetPlacement"
captured_at: "2026-04-17T01:36:37.829Z"
---

# SetPlacement

#### 函数功能

设置Tensor的数据存放的位置。

#### 函数原型

```cpp
graphStatus SetPlacement(const ge::Placement &placement);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| placement | 输入 | 需设置的数据地址的值。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 设置成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
