---
title: "GetName"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getname"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetName"
captured_at: "2026-04-17T01:36:34.931Z"
---

# GetName

#### 函数功能

获取算子名称。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/4q2GplrnS5m8C-Qf2IQwyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=8A6117816EBC60A9F1FCD3E2C59FFC737404FC3E1FF8FD48A84D13A547E92633)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::string GetName() const;
graphStatus GetName(AscendString &name) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输出 | 算子名称。 |

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
