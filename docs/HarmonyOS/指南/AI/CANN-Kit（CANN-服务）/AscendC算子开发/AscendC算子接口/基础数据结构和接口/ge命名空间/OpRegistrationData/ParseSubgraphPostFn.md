---
title: "ParseSubgraphPostFn"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-parsesubgraphpostfn"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpRegistrationData"
  - "ParseSubgraphPostFn"
captured_at: "2026-04-17T01:36:35.456Z"
---

# ParseSubgraphPostFn

#### 函数功能

根据算子类型，注册算子的子图中输入输出节点跟算子的输入输出的对应关系函数实现。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/ZSTf74goQAuVYywhF51WDQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=51EFAA01044186BC47F6A237B8CBD07FDED4335B9DC8A5CBB1F0FA659C0738C0)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OpRegistrationData &ParseSubgraphPostFn(const ParseSubgraphFunc &subgraph_post_fn)
OpRegistrationData &ParseSubgraphPostFn(const ParseSubgraphFuncV2 &subgraph_post_fn);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| subgraph\_post\_fn | 输入 | 
子图中输入输出节点跟算子的输入输出的对应关系函数对象。

详见[回调函数ParseSubgraphFuncV2](#回调函数parsesubgraphfuncv2) **。**

 |

#### 约束说明

无

#### 回调函数ParseSubgraphFuncV2

开发者自定义并实现ParseSubgraphFuncV2函数，完成解析子图中输入输出节点跟算子的输入输出的对应关系功能，回调函数原型定义如下。

```cpp
Status ParseSubgraphFuncV2(const ge::AscendString &subgraph_name, const ge::Graph &graph)
```

**表1** 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| subgraph\_name | 输入 | 子图名字。 |
| graph | 输出 | 构造的子图。 |
