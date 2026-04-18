---
title: "GetOutputInstanceInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoutputinstanceinfo"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "gert命名空间"
  - "ComputeNodeInfo"
  - "GetOutputInstanceInfo"
captured_at: "2026-04-17T01:36:28.333Z"
---

# GetOutputInstanceInfo

#### 函数功能

根据算子IR原型中的输出索引，获取对应的实例化对象。

#### 函数原型

```cpp
const AnchorInstanceInfo *GetOutputInstanceInfo(const size_t ir_index) const
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| ir\_index | 输入 | 算子IR原型定义中的输出索引，从0开始计数。 |

#### 返回值

返回const类型的实例化对象的地址。

#### 约束说明

无

#### 调用示例

```cpp
for (size_t i = 0; i < ir_outputs.size(); ++i) {
  auto ins_info = compute_node_info.GetOutputInstanceInfo(i);
  // ...
}
```
