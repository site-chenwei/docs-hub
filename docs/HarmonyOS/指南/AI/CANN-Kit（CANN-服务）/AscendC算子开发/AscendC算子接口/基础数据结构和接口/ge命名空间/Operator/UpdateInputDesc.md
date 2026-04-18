---
title: "UpdateInputDesc"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updateinputdesc"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "UpdateInputDesc"
captured_at: "2026-04-17T01:36:35.180Z"
---

# UpdateInputDesc

#### 函数功能

根据算子Input名称更新Input的TensorDesc。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/Iz8R6tmTQYOTwY5tpSZ0kg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=36F1B14AFBBB6564FA837ADEB7C319329F1DBFC0BDC5379203B7864795F05812)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus UpdateInputDesc(const std::string &name, const TensorDesc &tensor_desc);
graphStatus UpdateInputDesc(const char_t *name, const TensorDesc &tensor_desc);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 算子Input名称。 |
| tensor\_desc | 输入 | TensorDesc对象。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 更新TensorDesc成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

#### 异常处理

| 异常场景 | 说明 |
| :-- | :-- |
| 无对应name输入 | 函数提前结束，返回GRAPH\_FAILED。 |

#### 约束说明

无
