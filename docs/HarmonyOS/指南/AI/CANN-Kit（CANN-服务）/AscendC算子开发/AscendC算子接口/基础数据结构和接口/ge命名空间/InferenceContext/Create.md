---
title: "Create"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-create"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "InferenceContext"
  - "Create"
captured_at: "2026-04-17T01:36:31.761Z"
---

# Create

#### 函数功能

在资源类算子推理的上下文中，创建资源算子的上下文对象。

#### 函数原型

```cpp
static std::unique_ptr<InferenceContext> Create(
void *resource_context_mgr = nullptr
)
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| resource\_context\_mgr | 输入 | 
Resource Context管理器指针。

Session创建时候会初始化此指针，由InferShape框架自动传入，生命周期同session。

 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| std::unique\_ptr<InferenceContext> | 资源类算子间传递的上下文对象。 |

#### 异常处理

无

#### 约束说明

无
