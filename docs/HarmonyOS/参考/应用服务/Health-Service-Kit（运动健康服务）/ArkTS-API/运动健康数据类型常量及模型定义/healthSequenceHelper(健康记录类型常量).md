---
title: "healthSequenceHelper(健康记录类型常量)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthsequencehelper"
menu_path:
  - "参考"
  - "应用服务"
  - "Health Service Kit（运动健康服务）"
  - "ArkTS API"
  - "运动健康数据类型常量及模型定义"
  - "healthSequenceHelper(健康记录类型常量)"
captured_at: "2026-04-17T01:48:58.224Z"
---

# healthSequenceHelper(健康记录类型常量)

本模块提供健康记录数据类型常量及数据模型。

**起始版本：** 5.0.0(12)

#### 导入模块

```typescript
import { healthStore } from '@kit.HealthServiceKit';
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/oGYlZ1n0S-md5_78PGCuug/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=8C0D26BA8F522B85C7C17D56AA9959A89D11B808F7D5E46F1DD171D0D9CEAD6C)

此模块为healthStore子模块，需通过healthStore.healthSequenceHelper方式使用。

#### sleepRecord

夜间睡眠数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

#### \[h2\]常量

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| DATA\_TYPE | [healthStore.DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#datatype) | 夜间睡眠数据类型。 |

#### \[h2\]Model

type Model = healthModels.SleepRecord

夜间睡眠健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| :-- | :-- |
| [healthModels.SleepRecord](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels#sleeprecord) | 夜间睡眠健康记录数据模型。 |

#### \[h2\]Fields

type Fields = healthFields.Sleep

夜间睡眠健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| :-- | :-- |
| [healthFields.Sleep](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields#sleep) | 夜间睡眠健康记录数据字段列表。 |

#### \[h2\]DetailFields

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| :-- | :-- |
| [healthFields.SleepDetail](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields#sleepdetail) | 睡眠详情数据字段列表。 |

#### sleepNapRecord

零星小睡数据类型常量及数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

#### \[h2\]常量

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 名称 | 类型 | 说明 |
| :-- | :-- | :-- |
| DATA\_TYPE | [healthStore.DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#datatype) | 零星小睡数据类型。 |

#### \[h2\]Model

type Model = healthModels.SleepNapRecord

零星小睡健康记录数据模型。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| :-- | :-- |
| [healthModels.SleepNapRecord](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthmodels#sleepnaprecord) | 零星小睡健康记录数据模型。 |

#### \[h2\]Fields

type Fields = healthFields.SleepNap

零星小睡健康记录数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| :-- | :-- |
| [healthFields.SleepNap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields#sleepnap) | 零星小睡健康记录数据字段列表。 |

#### \[h2\]DetailFields

type DetailFields = healthFields.SleepDetail

睡眠详情数据字段列表。

**系统能力：** SystemCapability.Health.HealthStore

**起始版本：** 5.0.0(12)

| 类型 | **说明** |
| :-- | :-- |
| [healthFields.SleepDetail](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthfields#sleepdetail) | 睡眠详情数据字段列表。 |
