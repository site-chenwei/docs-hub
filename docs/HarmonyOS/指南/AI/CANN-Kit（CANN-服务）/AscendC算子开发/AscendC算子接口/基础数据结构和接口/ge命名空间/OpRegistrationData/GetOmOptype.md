---
title: "GetOmOptype"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getomoptype"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpRegistrationData"
  - "GetOmOptype"
captured_at: "2026-04-17T01:36:35.501Z"
---

# GetOmOptype

#### 函数功能

获取模型的算子类型。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/K3el5cuRT6yVcBK5i9umIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=911AB5559F40918F38C4F1D29EC28691B4F0EF0D483EE19B490793AC9EA772C5)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::string GetOmOptype () const;
Status GetOmOptype(ge::AscendString &om_op_type) const;
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| om\_op\_type | 输出 | 模型的算子类型。 |

#### 约束说明

无
