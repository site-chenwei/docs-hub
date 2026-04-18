---
title: "IsValid"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isvalid"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "IsValid"
captured_at: "2026-04-17T01:36:36.729Z"
---

# IsValid

#### 函数功能

判断Tensor对象是否有效。

若实际Tensor数据的大小与TensorDesc所描述的Tensor数据大小一致，则有效。

#### 函数原型

```cpp
graphStatus IsValid()
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 如果Tensor对象有效，则返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
