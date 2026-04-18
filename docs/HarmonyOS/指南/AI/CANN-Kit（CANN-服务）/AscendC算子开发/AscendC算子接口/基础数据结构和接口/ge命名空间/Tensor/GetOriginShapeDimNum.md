---
title: "GetOriginShapeDimNum"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginshapedimnum"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Tensor"
  - "GetOriginShapeDimNum"
captured_at: "2026-04-17T01:36:36.951Z"
---

# GetOriginShapeDimNum

#### 函数功能

获取原始shape的维度大小，即rank大小。

#### 函数原型

```cpp
size_t GetOriginShapeDimNum() const;
```

#### 参数说明

无

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| size\_t | 返回原始shape的维度大小，即原始shape的rank，如果是unknown的rank，返回0。 |

#### 异常处理

无

#### 约束说明

无
