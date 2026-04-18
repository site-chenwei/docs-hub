---
title: "operator[]"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatorc"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Shape"
  - "operator[]"
captured_at: "2026-04-17T01:36:29.935Z"
---

# operator\[\]

#### 函数功能

获取指定index轴的dim值。

#### 函数原型

```cpp
const int64_t &operator[](size_t idx) const
int64_t &operator[](size_t idx)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| idx | 输入 | dim的index，调用者需要保证index合法。 |

#### 返回值

-   const int64\_t &operator\[\](size\_t idx) const：dim值，在idx>=kMaxDimNum时，行为未定义。
    
-   int64\_t &operator\[\](size\_t idx)：dim值，在idx>=kMaxDimNum时，行为未定义。
    

#### 约束说明

调用者需要保证index合法，即idx<kMaxDimNum。

#### 调用示例

```cpp
Shape shape0({3, 256, 256});
auto dim0 = shape0[0]; // 3
auto dim5 = shape0[5]; // 5
auto invalid_dim = shape0[kMaxDimNum]; // 行为未定义
```
