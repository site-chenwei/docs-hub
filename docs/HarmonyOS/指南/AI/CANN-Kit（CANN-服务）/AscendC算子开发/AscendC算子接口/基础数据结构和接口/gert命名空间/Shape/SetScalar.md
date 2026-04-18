---
title: "SetScalar"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setscalar"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Shape"
  - "SetScalar"
captured_at: "2026-04-17T01:36:29.998Z"
---

# SetScalar

#### 函数功能

设置shape为标量。

#### 函数原型

```cpp
void SetScalar()
```

#### 参数说明

无

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
Shape shape0({3, 256, 256});
shape0.IsScalar(); // false
shape0.SetScalar();
shape0.IsScalar(); // true
```
