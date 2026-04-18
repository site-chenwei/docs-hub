---
title: "OriginOpType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-originoptype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpRegistrationData"
  - "OriginOpType"
captured_at: "2026-04-17T01:36:35.381Z"
---

# OriginOpType

#### 函数功能

设置原始模型的算子类型或算子类型列表。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/r2rfbDHxQo6yTG4LJBcP3Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=CACBE8669A58E4E83E12D915D18582AB804516DB317B3E56DE4C1355A8FE29D5)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OpRegistrationData &OriginOpType(const std::vector<ge::AscendString> &ori_op_type_list);
OpRegistrationData &OriginOpType(const char_t *ori_op_type);
OpRegistrationData &OriginOpType(const std::initializer_list<std::string> &ori_optype_list);
OpRegistrationData &OriginOpType(const std::string &ori_optype);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| ori\_op\_type\_list/ori\_optype\_list | 输入 | 原始模型算子类型列表 |
| ori\_op\_type/ori\_optype | 输入 | 原始模型算子类型 |
