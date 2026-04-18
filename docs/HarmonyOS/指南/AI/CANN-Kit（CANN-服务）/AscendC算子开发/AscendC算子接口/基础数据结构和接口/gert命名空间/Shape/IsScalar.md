---
title: "IsScalar"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isscalar"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Shape"
  - "IsScalar"
captured_at: "2026-04-17T01:36:29.936Z"
---

# IsScalar

#### 函数功能

判断本shape是否为标量，所谓标量，是指GetDimNum()为0的张量。

#### 函数原型

```cpp
bool IsScalar() const
```

#### 参数说明

无

#### 返回值

true为标量，false为非标量。

#### 约束说明

无

#### 调用示例

```cpp
Shape shape0({3, 256, 256});
Shape shape2;
shape0.IsScalar(); // false
shape2.IsScalar(); // true
```
