---
title: "INFER_FUNC_REG"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-infer-func-reg"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "INFER_FUNC_REG"
captured_at: "2026-04-17T01:36:38.467Z"
---

# INFER\_FUNC\_REG

#### 函数功能

注册算子的InferShape函数。

#### 函数原型

```cpp
INFER_FUNC_REG(op_name, x)
```

该函数内部会自动调用INFER\_VERIFY\_FUNC(op\_name, x)，INFER\_VERIFY\_FUNC函数中的op\_name为算子的类型，x为指向INFER\_FUNC\_REG（op\_name,x）中“x”的指针。

#### 约束说明

无

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| op\_name | 输入 | 算子类型。 |
| x | 输入 | InferShape函数名，和[IMPLEMT\_INFERFUNC](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-implemt-inferfunc)的InferShape函数名保持一致。 |

#### 返回值

无
