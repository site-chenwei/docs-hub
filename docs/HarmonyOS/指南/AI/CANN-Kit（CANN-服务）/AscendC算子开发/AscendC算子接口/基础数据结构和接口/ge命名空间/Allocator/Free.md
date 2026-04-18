---
title: "Free"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-allocator-free"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Allocator"
  - "Free"
captured_at: "2026-04-17T01:36:31.447Z"
---

# Free

#### 函数功能

根据指定的MemBlock释放内存到内存池。

#### 函数原型

```cpp
virtual void Free(MemBlock *block) = 0;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| block | 输入 | 内存block指针。 |

#### 返回值

无

#### 异常处理

无

#### 约束说明

虚函数开发者必须实现。
