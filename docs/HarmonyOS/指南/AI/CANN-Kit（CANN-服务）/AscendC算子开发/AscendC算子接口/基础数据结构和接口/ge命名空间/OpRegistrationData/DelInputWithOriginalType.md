---
title: "DelInputWithOriginalType"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-delinputwithoriginaltype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpRegistrationData"
  - "DelInputWithOriginalType"
captured_at: "2026-04-17T01:36:35.475Z"
---

# DelInputWithOriginalType

#### 函数功能

根据算子类型，删除算子指定输入边。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/Wd0vum9fTua31zZxUh2j4Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=9BA6E7734EF5C2244E0615F694356E466B81C80DDF2184D0A485F8639E3E3CB4)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OpRegistrationData &DelInputWithOriginalType(int32_t input_idx, const std::string &ori_type)
OpRegistrationData &DelInputWithOriginalType(int32_t input_idx, const char_t *ori_type)
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| input\_idx | 输入 | 需要删除的输入边编号。 |
| ori\_type | 输入 | 删除节点的原始算子类型。 |

#### 约束说明

无
