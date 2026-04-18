---
title: "GetPlacement"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensor-getplacement"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "GetPlacement"
captured_at: "2026-04-17T01:36:37.077Z"
---

# GetPlacement

#### 函数功能

获取Tensor的placement。

#### 函数原型

```cpp
ge::Placement GetPlacement() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| ge::Placement | 返回tensor的Placement值，默认值为kPlacementEnd。 |

#### 异常处理

无

#### 约束说明

无
