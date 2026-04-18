---
title: "IsExistOp"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-isexistop"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OperatorFactory"
  - "IsExistOp"
captured_at: "2026-04-17T01:36:34.635Z"
---

# IsExistOp

#### 函数功能

查询指定的算子类型是否支持。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/wnS0GmcWTSWBLGd5krczLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=3F004D63AE1723EFA6EF240D21F53917D8A5BAB36C5BC2BF028D7418875BAA1B)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
static bool IsExistOp(const std::string &operator_type)
static bool IsExistOp(const char_t *const operator_type)
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| operator\_type | 输入 | 算子类型。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| bool | 
\- true：支持此算子。

\- false：不支持此算子。

 |

#### 约束说明

无
