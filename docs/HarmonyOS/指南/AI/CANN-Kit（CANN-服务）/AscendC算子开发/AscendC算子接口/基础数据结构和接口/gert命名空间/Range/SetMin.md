---
title: "SetMin"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setmin"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "Range"
  - "SetMin"
captured_at: "2026-04-17T01:36:29.656Z"
---

# SetMin

#### 函数功能

设置最小的T对象指针。

#### 函数原型

```cpp
void SetMin(T *min)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| min | 输入 | 最小的T对象指针。 |

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
Range<int> range;
int min = -1;
range.SetMin(&min);
```
