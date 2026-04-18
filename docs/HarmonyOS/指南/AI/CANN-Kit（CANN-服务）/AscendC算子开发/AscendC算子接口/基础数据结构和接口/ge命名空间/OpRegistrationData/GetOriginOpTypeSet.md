---
title: "GetOriginOpTypeSet"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getoriginoptypeset"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "OpRegistrationData"
  - "GetOriginOpTypeSet"
captured_at: "2026-04-17T01:36:35.523Z"
---

# GetOriginOpTypeSet

#### 函数功能

获取原始模型的算子类型集合。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/SzWjoWVBTcemm0ADMIfBew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=A782FD093EA036E9F462074F6EDAE981E7F510954A40C392F8608C324534151A)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::set<std::string> GetOriginOpTypeSet () const;
Status GetOriginOpTypeSet(std::set<ge::AscendString> &ori_op_type) const;
```

#### 参数说明

| 参数 | 输入/输出 | 说明 |
| :-- | :-- | :-- |
| ori\_op\_type | 输出 | 原始模型的算子类型集合。 |

#### 约束说明

无
