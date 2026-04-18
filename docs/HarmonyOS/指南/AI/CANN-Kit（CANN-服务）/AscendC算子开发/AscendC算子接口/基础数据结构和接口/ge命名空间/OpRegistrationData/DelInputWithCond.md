---
title: "DelInputWithCond"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-delinputwithcond"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpRegistrationData"
  - "DelInputWithCond"
captured_at: "2026-04-17T01:36:35.480Z"
---

# DelInputWithCond

#### 函数功能

根据算子属性，删除算子指定输入边。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/i7rrzhukTqirlnt8udcCEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=CD551ACAB97AA56A5AA8B6CB0E984C81B457A7D926BC90E6A622707C593C2691)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
OpRegistrationData &DelInputWithCond(int32_t inputIdx, const std::string &attrName, bool attrValue);
OpRegistrationData &DelInputWithCond(int32_t input_idx, const char_t *attr_name, bool attr_value);
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| inputIdx | 输入 | 需要删除的输入边编号。 |
| attrName | 输入 | 属性名字。 |
| attrValue | 输入 | 属性的值。 |

#### 约束说明

无
