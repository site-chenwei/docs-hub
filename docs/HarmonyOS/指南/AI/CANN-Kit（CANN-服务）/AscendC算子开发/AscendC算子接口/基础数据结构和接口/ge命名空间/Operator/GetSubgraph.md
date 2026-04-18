---
title: "GetSubgraph"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraph"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetSubgraph"
captured_at: "2026-04-17T01:36:34.948Z"
---

# GetSubgraph

#### 函数功能

根据子图名称获取算子对应的子图。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/9ooYRjP6RPmzrW3T3oU-xQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=251B89C24CA42BA3826C938E0AAD0F35E2A94F44E868DA14659D7C9B5ED00D6B)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
Graph GetSubgraph(const std::string &name) const;
Graph GetSubgraph(const char_t *name) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 子图名称。 |

#### 返回值

Graph对象。

#### 异常处理

无

#### 约束说明

无
