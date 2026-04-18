---
title: "GetShapeDimNum"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getshapedimnum"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "GetShapeDimNum"
captured_at: "2026-04-17T01:36:37.191Z"
---

# GetShapeDimNum

#### 函数功能

获取shape的维度大小，即rank大小。

#### 函数原型

```cpp
size_t GetShapeDimNum() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| size\_t | 返回shape的维度大小，即shape的rank，如果是unknown的rank，返回0。 |

#### 异常处理

无

#### 约束说明

无
