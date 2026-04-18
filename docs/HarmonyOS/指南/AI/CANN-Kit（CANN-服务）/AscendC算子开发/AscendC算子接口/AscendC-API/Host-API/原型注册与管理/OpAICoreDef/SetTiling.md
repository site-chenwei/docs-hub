---
title: "SetTiling"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settiling"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "Host API"
  - "原型注册与管理"
  - "OpAICoreDef"
  - "SetTiling"
captured_at: "2026-04-17T01:36:27.586Z"
---

# SetTiling

#### 函数功能

注册Tiling函数。

#### 函数原型

```cpp
OpAICoreDef &SetTiling(gert::OpImplRegisterV2::TilingKernelFunc func);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| func | 输入 | 
Tiling函数。TilingKernelFunc类型定义如下。

using TilingKernelFunc = UINT32 (\*)(TilingContext \*);

 |

#### 返回值

[OpAICoreDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-settiling)算子定义。

#### 约束说明

无
