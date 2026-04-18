---
title: "GetSubgraphNames"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getsubgraphnames"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetSubgraphNames"
captured_at: "2026-04-17T01:36:35.005Z"
---

# GetSubgraphNames

#### 函数功能

获取一个算子的子图名称列表。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/aTd8iYqTS6msuTjX7WBBRA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=368CA3B004458504FF7EFBD38671BD716CE300EF17345E1AC2DBEF0A6FE8297F)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::vector<std::string> GetSubgraphNames() const;
graphStatus GetSubgraphNames(std::vector<AscendString> &names) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| names | 输出 | 获取一个算子的子图名称列表。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 
GRAPH\_FAILED：失败。

GRAPH\_SUCCESS：成功。

 |

#### 异常处理

无

#### 约束说明

无
