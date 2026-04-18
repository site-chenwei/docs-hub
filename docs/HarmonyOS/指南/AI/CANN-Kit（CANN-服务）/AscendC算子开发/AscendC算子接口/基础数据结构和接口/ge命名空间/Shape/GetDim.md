---
title: "GetDim"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-shape-getdim"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Shape"
  - "GetDim"
captured_at: "2026-04-17T01:36:35.816Z"
---

# GetDim

#### 函数功能

获取Shape第idx维的长度。

#### 函数原型

```cpp
int64_t GetDim(size_t idx) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| idx | 输入 | 维度索引，索引从0开始。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| int64\_t | 第idx维的长度。 |

#### 异常处理

无

#### 约束说明

无
