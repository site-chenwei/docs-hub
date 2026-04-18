---
title: "VerifyFuncRegister"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-verifyfuncregister"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "VerifyFuncRegister"
captured_at: "2026-04-17T01:36:38.078Z"
---

# VerifyFuncRegister

#### 函数功能

VerifyFuncRegister构造函数和析构函数。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/7JcD4VMsSrK89KZ_aLrNwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013638Z&HW-CC-Expire=86400&HW-CC-Sign=11C6FD2FFC91BB99C2A8815CCA842BF8B6F30B7E46D5CA004C16A58A82D801D1)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
VerifyFuncRegister(const std::string &operator_type, const VerifyFunc &verify_func);
VerifyFuncRegister(const char_t *const operator_type, const VerifyFunc &verify_func);
~VerifyFuncRegister() = default;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| operator\_type | 输入 | 算子类型。 |
| verify\_func | 输入 | 算子verify函数。 |

#### 返回值

VerifyFuncRegister构造函数返回VerifyFuncRegister类型的对象。

#### 约束说明

算子verifyFunc函数注册接口，此接口被其他头文件引用，一般不用由算子开发者直接调用。
