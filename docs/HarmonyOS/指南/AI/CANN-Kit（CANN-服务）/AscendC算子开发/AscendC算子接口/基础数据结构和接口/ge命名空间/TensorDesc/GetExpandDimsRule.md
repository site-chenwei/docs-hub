---
title: "GetExpandDimsRule"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getexpanddimsrule"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "GetExpandDimsRule"
captured_at: "2026-04-17T01:36:36.017Z"
---

# GetExpandDimsRule

#### 函数功能

获取Tensor的补维规则。

#### 函数原型

```cpp
graphStatus GetExpandDimsRule(AscendString &expand_dims_rule) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| expand\_dims\_rule | 引用输入 | 获取到的补维规则，作为出参。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 获取成功返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
