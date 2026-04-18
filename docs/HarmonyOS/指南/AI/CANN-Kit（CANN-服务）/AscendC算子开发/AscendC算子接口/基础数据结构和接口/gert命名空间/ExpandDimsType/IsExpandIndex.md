---
title: "IsExpandIndex"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isexpandindex"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ExpandDimsType"
  - "IsExpandIndex"
captured_at: "2026-04-17T01:36:28.810Z"
---

# IsExpandIndex

#### 函数功能

基于补维后的shape，判断指定的index轴是否为补维轴。

#### 函数原型

```cpp
bool IsExpandIndex(const AxisIndex index) const
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| index | 输入 | 指定轴的索引。 |

#### 返回值

-   true代表指定的轴为补维轴。
    
-   false代表指定的轴为原始轴。
    

#### 约束说明

无

#### 调用示例

```cpp
ExpandDimsType type1("1001");
bool is_expand_index0 = type1.IsExpandIndex(0); // true
bool is_expand_index1 = type1.IsExpandIndex(1); // false
```
