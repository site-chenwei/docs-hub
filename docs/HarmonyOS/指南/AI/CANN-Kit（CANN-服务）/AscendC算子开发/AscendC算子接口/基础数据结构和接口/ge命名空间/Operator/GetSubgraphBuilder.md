---
title: "GetSubgraphBuilder"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphbuilder"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetSubgraphBuilder"
captured_at: "2026-04-17T01:36:34.977Z"
---

# GetSubgraphBuilder

#### 函数功能

根据子图名称获取算子对应的子图构建的函数对象。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/PlfyXV7EQ1WJ536kEn1P6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=2D9F96B92ACC6A92D9F3EE4B3ABE6EFE3CD1B26E9DCC3EBF60FC3691BDDBF736)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
SubgraphBuilder GetSubgraphBuilder(const std::string &name) const;
SubgraphBuilder GetSubgraphBuilder(const char_t *name) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 子图名称。 |

#### 返回值

SubgraphBuilder对象。

#### 异常处理

无

#### 约束说明

无
