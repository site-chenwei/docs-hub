---
title: "GetDynamicSubgraph"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getdynamicsubgraph"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetDynamicSubgraph"
captured_at: "2026-04-17T01:36:34.855Z"
---

# GetDynamicSubgraph

#### 函数功能

根据子图名称和子图索引获取算子对应的动态输入子图。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/xdS_LX2iSMeDeZNKoB8ovQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=CE3C9903A341B2A30BE4B986797B61352CC2BA7F13A7056AE5370F69876DEE27)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
Graph GetDynamicSubgraph(const std::string &name, uint32_t index) const;
Graph GetDynamicSubgraph(const char_t *name, uint32_t index) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 子图名。 |
| index | 输入 | 同名子图的索引。 |

#### 返回值

Graph对象。

#### 异常处理

无

#### 约束说明

无
