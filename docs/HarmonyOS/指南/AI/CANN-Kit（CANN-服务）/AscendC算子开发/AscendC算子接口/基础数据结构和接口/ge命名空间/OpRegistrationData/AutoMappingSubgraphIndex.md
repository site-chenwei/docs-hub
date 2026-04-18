---
title: "AutoMappingSubgraphIndex"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-automappingsubgraphindex"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpRegistrationData"
  - "AutoMappingSubgraphIndex"
captured_at: "2026-04-17T01:36:35.699Z"
---

# AutoMappingSubgraphIndex

#### 函数功能

设置子图的输入输出和主图对应父节点输入输出的对应关系。

#### 函数原型

```cpp
Status AutoMappingSubgraphIndex(const ge::Graph &graph,
const std::function<int32_t(int32_t data_index)> &input,
const std::function<int32_t(int32_t netoutput_index)> &output)
Status AutoMappingSubgraphIndex(const ge::Graph &graph,
const std::function<Status(int32_t data_index, int32_t &parent_input_index)> &input,
const std::function<Status(int32_t netoutput_index, int32_t &parent_output_index)> &output)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| graph | 输入 | 子图对象 |
| input | 输入 | 输入对应关系函数 |
| output | 输入 | 输出对应关系函数 |

#### 约束说明

无
