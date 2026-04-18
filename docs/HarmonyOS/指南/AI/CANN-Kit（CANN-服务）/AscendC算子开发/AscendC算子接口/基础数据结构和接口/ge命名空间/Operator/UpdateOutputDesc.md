---
title: "UpdateOutputDesc"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-updateoutputdesc"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "UpdateOutputDesc"
captured_at: "2026-04-17T01:36:35.156Z"
---

# UpdateOutputDesc

#### 函数功能

根据算子Output名称更新Output的TensorDesc。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/cep-14INS_KCF8a1DsLlDg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013635Z&HW-CC-Expire=86400&HW-CC-Sign=BCC7900D35B2D09142566CE3AEEF61359010559C9307B66DAD7D551984416287)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
graphStatus UpdateOutputDesc(const std::string &name, const TensorDesc &tensor_desc);
graphStatus UpdateOutputDesc(const char_t *name, const TensorDesc &tensor_desc);
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 算子Output名称。 |
| tensor\_desc | 输入 | TensorDesc对象。 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| graphStatus | 更新TensorDesc成功，返回GRAPH\_SUCCESS， 否则，返回GRAPH\_FAILED。 |

#### 异常处理

无

#### 约束说明

无
