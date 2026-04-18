---
title: "GetInferenceContext"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinferencecontext"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetInferenceContext"
captured_at: "2026-04-17T01:36:34.878Z"
---

# GetInferenceContext

#### 函数功能

获取当前算子传递InferShape推导所需要的关联信息，比如前面算子的shape和DataType信息。

#### 函数原型

```cpp
InferenceContextPtr GetInferenceContext() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| InferenceContextPtr | 
返回当前operator的推理上下文。

InferenceContextPtr是指向InferenceContext类的指针的别名：

using InferenceContextPtr = std::shared\_ptr<InferenceContext>

 |

#### 异常处理

无

#### 约束说明

无
