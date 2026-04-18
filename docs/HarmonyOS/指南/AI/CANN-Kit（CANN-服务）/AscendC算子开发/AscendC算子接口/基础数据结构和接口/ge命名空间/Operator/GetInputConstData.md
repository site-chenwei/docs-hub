---
title: "GetInputConstData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getinputconstdata"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetInputConstData"
captured_at: "2026-04-17T01:36:34.885Z"
---

# GetInputConstData

#### 函数功能

如果指定算子Input对应的节点为Const节点，可调用该接口获取Const节点的数据。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/6U0ffcbAQ1SI3aucBHqPvQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=CE3312A560E84DA33E7617A67207808E8C652D0095ACA435BB3C74578A9E430F)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus GetInputConstData(const std::string &dst_name, Tensor &data) const;
graphStatus GetInputConstData(const char_t *dst_name, Tensor &data) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| dst\_name | 输入 | 输入名称。 |
| data | 输出 | 返回Const节点的数据Tensor。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 如果指定算子Input对应的节点为Const节点且获取数据成功，返回GRAPH\_SUCCESS，否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
