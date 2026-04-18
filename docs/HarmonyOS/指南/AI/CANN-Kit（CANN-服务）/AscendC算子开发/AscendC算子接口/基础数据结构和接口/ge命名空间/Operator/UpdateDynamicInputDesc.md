---
title: "UpdateDynamicInputDesc"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updatedynamicinputdesc"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "UpdateDynamicInputDesc"
captured_at: "2026-04-17T01:36:35.160Z"
---

# UpdateDynamicInputDesc

#### 函数功能

根据name和index的组合更新算子动态Input的TensorDesc。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/NUYgWEQ1QP2l3W71qIGYJQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=F28A85270C60F4002D6CBBF53E87E63381EC8B64AC678B0DF5379864CDF8D222)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus UpdateDynamicInputDesc(const std::string &name, uint32_t index, const TensorDesc &tensor_desc);
graphStatus UpdateDynamicInputDesc(const char_t *name, uint32_t index, const TensorDesc &tensor_desc);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 算子动态Input的名称。 |
| index | 输入 | 算子动态Input编号，编号起始值从1开始。 |
| tensor\_desc | 输入 | TensorDesc对象。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 更新动态Input成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
