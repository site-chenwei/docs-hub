---
title: "GetName"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-getname"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "TensorDesc"
  - "GetName"
captured_at: "2026-04-17T01:36:36.029Z"
---

# GetName

#### 函数功能

获取TensorDesc所描述Tensor的名称。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/w-fbR0h6QCyRX9K9dP2Lmw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013636Z&HW-CC-Expire=86400&HW-CC-Sign=4AC5F33CAE9770E1D8B598D176D2DA02900A83250819EA1994585B348785C925)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
std::string GetName() const;
graphStatus GetName(AscendString &name);
graphStatus GetName(AscendString &name) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输出 | 算子名称。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 获取name成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
