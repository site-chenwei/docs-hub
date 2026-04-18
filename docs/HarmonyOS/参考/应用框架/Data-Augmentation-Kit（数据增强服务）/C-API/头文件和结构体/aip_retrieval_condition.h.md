---
title: "aip_retrieval_condition.h"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-aip-retrieval-condition"
menu_path:
  - "参考"
  - "应用框架"
  - "Data Augmentation Kit（数据增强服务）"
  - "C API"
  - "头文件和结构体"
  - "aip_retrieval_condition.h"
captured_at: "2026-04-17T01:48:14.801Z"
---

# aip\_retrieval\_condition.h

#### 概述

提供与检索条件相关的接口。

**引用文件：** #include "dataaugmentation/retrieval/aip\_retrieval\_condition.h"

**库：** libretrieval\_ndk.so

**系统能力：** SystemCapability.DataAugmentation.Retrieval

**起始版本：** 6.0.0(20)

**相关模块：** [Retrieval](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval)

#### 汇总

#### \[h2\]类型定义

| 名称 | 描述 |
| :-- | :-- |
| typedef struct [OH\_Retrieval\_Condition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_condition) [OH\_Retrieval\_Condition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_condition) | 定义检索条件，可包含多个子检索条件等。 |
| typedef struct [OH\_Retrieval\_SubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_subcondition) [OH\_Retrieval\_SubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_subcondition) | 定义子检索条件，可以是向量检索。 |

#### \[h2\]函数

| 名称 | 描述 |
| :-- | :-- |
| [OH\_Retrieval\_Condition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_condition) \* [OH\_Retrieval\_CreateCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_createcondition) () | 创建检索条件，作为检索接口的入参。 |
| int [OH\_Retrieval\_DestroyCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_destroycondition) ([OH\_Retrieval\_Condition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_condition) \*condition) | 销毁通过[OH\_Retrieval\_CreateCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_createcondition)获得的检索条件。 |
| int [OH\_Retrieval\_DestroySubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_destroysubcondition) ([OH\_Retrieval\_SubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_subcondition) \*condition) | 销毁通过[OH\_Retrieval\_SubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_subcondition)创建的条件。 |
| int [OH\_Retrieval\_AddSubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_addsubcondition) ([OH\_Retrieval\_Condition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_condition) \*condition, [OH\_Retrieval\_SubCondition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataaugmentation-capi-retrieval#oh_retrieval_subcondition) \*subCondition) | 在检索条件中，增加子检索条件。 |
