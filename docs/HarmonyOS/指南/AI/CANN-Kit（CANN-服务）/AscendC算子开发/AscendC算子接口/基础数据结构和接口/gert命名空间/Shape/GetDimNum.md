---
title: "GetDimNum"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdimnum"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Shape"
  - "GetDimNum"
captured_at: "2026-04-17T01:36:29.997Z"
---

# GetDimNum

#### 函数功能

获取dim\_num。

#### 函数原型

```cpp
size_t GetDimNum() const
```

#### 参数说明

无

#### 返回值

获取dim\_num，即Shape的长度。

#### 约束说明

无

#### 调用示例

```cpp
Shape shape0({3, 256, 256});
auto dim_num = shape0.GetDimNum(); // 3
```
