---
title: "GetInputDesc"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-operator-getinputdesc"
menu_path:
  - "指南"
  - "AI"
  - "CANN Kit（CANN 服务）"
  - "AscendC算子开发"
  - "AscendC算子接口"
  - "基础数据结构和接口"
  - "ge命名空间"
  - "Operator"
  - "GetInputDesc"
captured_at: "2026-04-17T01:36:34.916Z"
---

# GetInputDesc

#### 函数功能

根据算子Input名称或Input索引获取算子Input的TensorDesc。

#### 函数原型

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/cb8ci5rqQVSUM0qmSdgIew/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013634Z&HW-CC-Expire=86400&HW-CC-Sign=C9AEDB0B5133907560E8C5CDAEAA4B42E66333426982D89083EF1D54E0A85CEF)

数据类型为string的接口后续版本会废弃，建议使用数据类型为非string的接口。

```cpp
TensorDesc GetInputDesc(const std::string &name) const;
TensorDesc GetInputDescByName(const char_t *name) const;
TensorDesc GetInputDesc(uint32_t index) const;
```

#### 参数说明

| 参数名 | 输入/输出 | 描述 |
| :-- | :-- | :-- |
| name | 输入 | 
算子Input名称。

当无此算子Input名称时，则返回TensorDesc默认构造的对象，其中，主要设置[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)为DT\_FLOAT（表示float类型），[Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-format)为FORMAT\_NCHW（表示NCHW）。

 |
| index | 输入 | 

算子Input索引。

当无此算子Input索引时，则返回TensorDesc默认构造的对象，其中，主要设置[DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-datatype)为DT\_FLOAT（表示float类型），[Format](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ge-format)为FORMAT\_NCHW（表示NCHW）。

 |

#### 返回值

| 类型 | 描述 |
| :-- | :-- |
| [TensorDesc](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tensordesc-construction-and-destructor) | 算子Input的TensorDesc。 |

#### 异常处理

无

#### 约束说明

无
