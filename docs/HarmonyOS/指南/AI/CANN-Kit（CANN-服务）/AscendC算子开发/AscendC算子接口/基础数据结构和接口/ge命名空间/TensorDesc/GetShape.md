---
title: "GetShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getshape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "GetShape"
captured_at: "2026-04-17T01:36:36.105Z"
---

# GetShape

#### 函数功能

获取TensorDesc所描述Tensor的Shape。

#### 函数原型

```cpp
Shape GetShape() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| [Shape](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shape-construction-and-destructor) | TensorDesc描述的shape。 |

#### 异常处理

无

#### 约束说明

由于返回的Shape信息为值拷贝，因此修改返回的Shape信息，不影响TensorDesc中已有的Shape信息。
