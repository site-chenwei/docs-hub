---
title: "Init"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvectorvector-init"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ContinuousVectorVector"
  - "Init"
captured_at: "2026-04-17T01:36:28.572Z"
---

# Init

#### 函数功能

初始化ContinuousVectorVector类。

#### 函数原型

```cpp
void Init(const size_t capacity)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| capacity | 输入 | 实例的最大容量。 |

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
size_t total_length = 1000U; // 需根据实际存放的数据量进行设置
size_t capacity = 100U;
std::vector<uint8_t> buf(total_length);
auto cvv = new (buf.data()) ContinuousVectorVector();
cvv->Init(capacity);
```
