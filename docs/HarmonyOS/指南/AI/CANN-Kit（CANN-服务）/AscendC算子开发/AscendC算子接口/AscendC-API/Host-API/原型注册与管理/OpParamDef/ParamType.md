---
title: "ParamType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-paramtype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "AscendC API"
  - "Host API"
  - "原型注册与管理"
  - "OpParamDef"
  - "ParamType"
captured_at: "2026-04-17T01:36:27.539Z"
---

# ParamType

#### 函数功能

定义算子参数类型。

#### 函数原型

```cpp
OpParamDef &ParamType(Option param_type);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| param\_type | 输入 | 参数类型，Option取值为：OPTIONAL（可选）、REQUIRED（必选）。 |

#### 返回值

[OpParamDef](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-paramtype)算子定义。

#### 约束说明

无
