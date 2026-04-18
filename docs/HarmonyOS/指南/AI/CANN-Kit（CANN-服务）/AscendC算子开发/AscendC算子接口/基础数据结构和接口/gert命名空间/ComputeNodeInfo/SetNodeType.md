---
title: "SetNodeType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setnodetype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ComputeNodeInfo"
  - "SetNodeType"
captured_at: "2026-04-17T01:36:28.506Z"
---

# SetNodeType

#### 函数功能

设置算子的类型。

#### 函数原型

```cpp
void SetNodeType(const ge::char_t *node_type)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| node\_type | 输入 | 算子的类型。 |

#### 返回值

无

#### 约束说明

无

#### 调用示例

```cpp
compute_node_info.SetNodeType("Const");
```
