---
title: "aip_retrieval_condition_vector.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-condition-vector"
menu_path:
  - "参考"
  - "应用框架"
  - "Data Augmentation Kit（数据增强服务）"
  - "C API"
  - "头文件和结构体"
  - "aip_retrieval_condition_vector.h"
captured_at: "2026-04-17T01:48:14.800Z"
---

# aip\_retrieval\_condition\_vector.h

#### 概述

提供与向量条件相关的接口。

**引用文件：** #include "dataaugmentation/retrieval/aip\_retrieval\_condition\_vector.h"

**库：** libretrieval\_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [Retrieval](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval)

#### 汇总

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef struct [OH\_Retrieval\_SubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_subcondition) [OH\_Retrieval\_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) | 定义向量检索条件，包含检索的字段、检索参数、过滤条件等。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Retrieval\_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) \* [OH\_Retrieval\_CreateVectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_createvectorcondition) () | 创建向量检索条件。 |
| int [OH\_Retrieval\_DestroyVectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_destroyvectorcondition) ([OH\_Retrieval\_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) \*condition) | 销毁通过[OH\_Retrieval\_CreateVectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_createvectorcondition)获得的检索条件。 |
| int [OH\_Retrieval\_SetVectorRecallLimit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_setvectorrecalllimit) ([OH\_Retrieval\_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) \*condition, uint32\_t limit) | 在检索条件中，设置向量检索结果数量上限。 |
| int [OH\_Retrieval\_SetSimilarityThreshold](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_setsimilaritythreshold) ([OH\_Retrieval\_VectorCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_vectorcondition) \*condition, double threshold) | 在检索条件中，设置向量检索的相似度阈值。 |
