---
title: "SetInferShape"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setinfershape"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "Host API"
  - "原型注册与管理"
  - "OpDef"
  - "SetInferShape"
captured_at: "2026-04-17T01:36:27.469Z"
---

# SetInferShape

#### 函数功能

注册Shape推导函数。

#### 函数原型

```cpp
OpDef &SetInferShape(gert::OpImplRegisterV2::InferShapeKernelFunc func);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| func | 输入 | 
Shape推导函数。InferShapeKernelFunc类型定义如下。

using InferShapeKernelFunc = UINT32 (\*)(InferShapeContext \*);

 |

#### 返回值

[OpDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-input)算子定义。

#### 约束说明

无
