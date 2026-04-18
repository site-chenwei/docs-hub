---
title: "operator!="
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatorb"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Shape"
  - "operator!="
captured_at: "2026-04-17T01:36:29.976Z"
---

# operator!=

#### 函数功能

判断与另一个Shape对象是否不等。

#### 函数原型

```cpp
bool operator!=(const Shape &rht) const
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| rht | 输入 | 另一个Shape对象。 |

#### 返回值

true：不相等。

false：相等。

#### 约束说明

无

#### 调用示例

```cpp
Shape shape0({3, 256, 256});
Shape shape1({1, 3, 256, 256});
auto is_diff_shape = shape0 != shape1; // 返回值为true，不相等
```
