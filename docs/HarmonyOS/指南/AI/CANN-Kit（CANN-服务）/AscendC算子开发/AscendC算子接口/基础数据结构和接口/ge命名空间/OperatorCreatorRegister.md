---
title: "OperatorCreatorRegister"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operatorcreatorregister"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OperatorCreatorRegister"
captured_at: "2026-04-17T01:36:34.594Z"
---

# OperatorCreatorRegister

#### 函数功能

OperatorCreatorRegister构造函数和析构函数。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/grtYsIfTRXquT5--CFx9Sw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=67A15E65FF99E8673CD36A9EFC3581BE48C3C1E8802659DB58372285C8CE0580)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OperatorCreatorRegister(const std::string &operator_type, OpCreator const &op_creator);
OperatorCreatorRegister(const char_t *const operator_type, OpCreatorV2 const &op_creator);
~OperatorCreatorRegister() = default;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| operator\_type | 输入 | 算子类型。 |
| op\_creator | 输入 | 算子构造函数。 |

#### 返回值

OperatorCreatorRegister构造函数返回OperatorCreatorRegister类型的对象。

#### 约束说明

算子注册接口，注册一个算子原型，此接口被其他头文件引用，一般不用由算子开发者直接调用。
