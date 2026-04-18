---
title: "GetOverHeadLength"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoverheadlength"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ContinuousVectorVector"
  - "GetOverHeadLength"
captured_at: "2026-04-17T01:36:28.612Z"
---

# GetOverHeadLength

#### 函数功能

获取数据描述信息的长度。

#### 函数原型

```cpp
static size_t GetOverHeadLength(const size_t capacity)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| capacity | 输入 | 实例的最大容量。 |

#### 返回值

数据描述信息的长度。

#### 约束说明

无

#### 调用示例

```cpp
size_t capacity = 100U;
auto length = ContinuousVectorVector::GetOverHeadLength(capacity);
```
