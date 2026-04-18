---
title: "SetDimNum"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdimnum"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Shape"
  - "SetDimNum"
captured_at: "2026-04-17T01:36:30.026Z"
---

# SetDimNum

#### 函数功能

设置dim num。

#### 函数原型

```cpp
void SetDimNum(const size_t dim_num)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| dim\_num | 输入 | 将Shape对象的dim\_num\_设置为dim\_num。 |

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
Shape shape0({3, 256, 256});
shape0.SetDimNum(1);
auto dim_num = shape0.GetDimNum(); // 1
```
