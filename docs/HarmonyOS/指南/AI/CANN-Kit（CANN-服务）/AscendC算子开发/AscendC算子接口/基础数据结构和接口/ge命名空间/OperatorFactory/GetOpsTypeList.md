---
title: "GetOpsTypeList"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getopstypelist"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OperatorFactory"
  - "GetOpsTypeList"
captured_at: "2026-04-17T01:36:34.615Z"
---

# GetOpsTypeList

#### 函数功能

获取系统支持的所有算子类型列表。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/X3VKSQNkT2C1PaU4ieKHug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=B1CCCB88C7C65F87A89123EB7227675E661CB16C7F98442F1E2A72ECE7E4A0B8)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
static graphStatus GetOpsTypeList(std::vector<std::string> &all_ops);
static graphStatus GetOpsTypeList(std::vector<AscendString> &all_ops);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| all\_ops | 输出 | 算子类型列表。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 
\- SUCCESS：执行成功。

\- FAILED：执行失败。

 |

#### 约束说明

无
