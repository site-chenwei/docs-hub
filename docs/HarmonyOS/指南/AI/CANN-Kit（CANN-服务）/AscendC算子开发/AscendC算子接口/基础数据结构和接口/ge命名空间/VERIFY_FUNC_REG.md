---
title: "VERIFY_FUNC_REG"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-verify-func-reg"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "VERIFY_FUNC_REG"
captured_at: "2026-04-17T01:36:38.473Z"
---

# VERIFY\_FUNC\_REG

#### 函数功能

注册算子的Verify函数。

#### 函数原型

```cpp
VERIFY_FUNC_REG(op_name, x)
```

#### 约束说明

无

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| op\_name | 输入 | 算子类型。 |
| x | 输入 | Verify函数名，和[IMPLEMT\_VERIFIER](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-implemt-verifier)的Verify函数名保持一致。 |

#### 返回值

无
