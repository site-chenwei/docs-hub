---
title: "CreateOperator"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-createoperator"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OperatorFactory"
  - "CreateOperator"
captured_at: "2026-04-17T01:36:34.601Z"
---

# CreateOperator

#### 函数功能

基于算子名称和算子类型获取算子对象实例。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/Pk3kvzCWRh-4mCNku1zY4Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=573CCBFD645923437F4DB86690741661922114E37673AD9B05A0C6C597D1003D)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
static Operator CreateOperator(const std::string &operator_name, const std::string &operator_type)
static Operator CreateOperator(const char_t *const operator_name, const char_t *const operator_type)
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| operator\_name | 输入 | 算子名称。 |
| operator\_type | 输入 | 算子类型。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| string | 算子对象实例。 |

#### 约束说明

无
