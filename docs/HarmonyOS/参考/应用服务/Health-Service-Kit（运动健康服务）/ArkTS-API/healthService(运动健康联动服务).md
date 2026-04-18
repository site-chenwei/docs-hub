---
title: "healthService(运动健康联动服务)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthservice"
menu_path:
  - "参考"
  - "应用服务"
  - "Health Service Kit（运动健康服务）"
  - "ArkTS API"
  - "healthService(运动健康联动服务)"
captured_at: "2026-04-17T01:48:58.104Z"
---

# healthService(运动健康联动服务)

本模块提供运动健康联动服务。

**起始版本：** 5.0.0(12)

#### 导入模块

```typescript
import { healthService } from '@kit.HealthServiceKit';
```

#### SampleEvent

联动控制事件。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| :-- | :-- | :-- | :-- | :-- |
| eventId | number | 否 | 否 | 事件ID。 |
| eventLevel | number | 否 | 否 | 
事件等级。

取值参考：\[0, 255\]

 |
| eventData | string | 否 | 否 | 事件携带的信息。 |
| srcPkgName | string | 否 | 是 | 事件发送源包名，若未填写，默认为空。 |
| destPkgName | string | 否 | 是 | 事件发送目标包名，若未填写，默认为空。 |

#### SampleReal

SampleReal<K extends Record<string, [healthStore.HealthValueType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthvaluetype)\> = Record<string, [healthStore.HealthValueType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthvaluetype)\>>

联动实时运动数据。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| :-- | :-- | :-- | :-- | :-- |
| dataType | [healthStore.DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#datatype) | 否 | 否 | 实时融合数据类型。 |
| time | number | 否 | 否 | 实时融合数据产生时间，Unix时间戳，以毫秒为单位。 |
| fields | Pick<K, keyof K> | 否 | 否 | 实时融合数据字段。 |
| deviceUniqueId | string | 否 | 是 | 实时融合数据来源，若未填写，默认为空。 |

#### workout

提供运动健康实时数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

#### \[h2\]ActivityReport

实时三环数据。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| :-- | :-- | :-- | :-- | :-- |
| steps | number | 否 | 否 | 步数。 |
| stepsGoal | number | 否 | 是 | 步数目标（若未设置过，无法读取到运动健康App中展示的默认目标）。 |
| activeCalories | number | 否 | 否 | 
活动热量。

单位：卡

 |
| activeCaloriesGoal | number | 否 | 是 | 

活动热量目标。

单位：卡

 |
| exercise | number | 否 | 否 | 

锻炼时长。

单位：分钟

 |
| exerciseGoal | number | 否 | 是 | 

锻炼时长目标。

单位：分钟

 |
| activeHours | number | 否 | 否 | 活动小时数。 |
| activeHoursGoal | number | 否 | 是 | 活动小时数目标。 |

#### \[h2\]ConfigType

type ConfigType = number | string | boolean

联动配置项类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| 类型 | **说明** |
| :-- | :-- |
| number | 表示值类型为数字，可取任意值。 |
| string | 表示值类型为字符串，可取任意值。 |
| boolean | 表示值类型为布尔类型，可取true或false，具体含义以实际使用场景为准。 |

#### \[h2\]DeviceState

联动设备状态。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | string | 否 | 否 | 设备ID。 |
| state | number | 否 | 否 | 设备状态。 |
| deviceName | string | 否 | 是 | 设备名称，若未填写，默认为空。 |

#### \[h2\]Goal

联动运动目标。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| :-- | :-- | :-- | :-- | :-- |
| type | number | 否 | 否 | 目标类型，取值参考：[TargetType](#targettype)。 |
| value | number | 否 | 否 | 目标值。 |

#### \[h2\]LinkageType

联动类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| COURSE\_LINK | 0 | 课程联动。 |
| ACTIVITY\_LINK | 1 | 运动联动。 |

#### \[h2\]StartCode

联动开启结果码。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SUCCESS | 0 | 联动开启成功。 |
| WORKOUT\_WORKING | 1 | 联动已开始。 |
| NO\_SUPPORTED\_DEVICE | 2 | 无可支持联动的设备。 |
| DEVICE\_BUSY | 3 | 联动设备忙碌。 |

#### \[h2\]StartResult

联动开启结果。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| :-- | :-- | :-- | :-- | :-- |
| startCode | [StartCode](#startcode) | 否 | 否 | 联动开启结果码。 |
| deviceState | [DeviceState](#devicestate)\[\] | 否 | 否 | 联动设备状态。 |

#### \[h2\]TargetType

联动目标类型。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| NONE | 0 | 无目标。 |
| DISTANCE | 1 | 距离。 |
| CALORIE | 2 | 卡路里。 |
| TIME | 3 | 时长。 |
| SKIPPING\_TIMES | 4 | 跳绳次数。 |

#### \[h2\]WorkoutConfig

联动配置项。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

| **名称** | **类型** | 只读 | 可选 | **说明** |
| :-- | :-- | :-- | :-- | :-- |
| linkageType | [LinkageType](#linkagetype) | 否 | 否 | 联动类型。 |
| sportType | number | 否 | 否 | 运动类型，参见[锻炼记录类型常量](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-exercisedequencehelper)子数据类型id。 |
| activityGoals | [Goal](#goal)\[\] | 否 | 是 | 联动运动目标，若未填写，默认为空。 |
| extensionConfig | Record<string, [ConfigType](#configtype)\> | 否 | 是 | 扩展配置项，若未填写，默认为空。 |

#### \[h2\]workout.config

config(workoutConfig: WorkoutConfig): Promise<void>

配置联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| workoutConfig | [WorkoutConfig](#workoutconfig) | 是 | 联动配置项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |
| [1009104003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104003-非法指令) | Illegal command. Called when workout not in stoped or idle state. |
| [1009104999](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104999-通用错误码) | System internal error. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/uKyuS1qyQhaN6StBOiPafA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=2405C9A4D401AB4B83F68907815A2209C737EF9FF07D12D536B2780943D290BD)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  let workoutOptions: healthService.workout.WorkoutConfig = {
    linkageType: healthService.workout.LinkageType.COURSE_LINK,
    sportType: healthStore.exerciseSequenceHelper.running.EXERCISE_TYPE.id
  };
  await healthService.workout.config(workoutOptions);
  hilog.info(0x0000, 'testTag', 'Succeed in configuring workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to configure workout. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.start

start(): Promise<StartResult>

开启联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[StartResult](#startresult)\> | Promise对象，返回联动开启结果。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [1009104001](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104001-联动已开启) | Sport service busy. Workout is already started by other application. |
| [1009104002](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104002-不支持运动类型) | Unsupported sport type. |
| [1009104003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104003-非法指令) | Illegal command. Called when workout in sporting, paused or stoped state. |
| [1009104004](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104004-权限校验异常) | Permission verification error. Application has no permission, such as Motion Permission. |
| [1009104999](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104999-通用错误码) | System internal error. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/S4KZwALKQ_6x8_l2Qj6_lw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=2829CD90932541A903D5A5B1E53A2F784E0100E8D5525BCB8BD0720F833B1609)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.start();
  hilog.info(0x0000, 'testTag', 'Succeed in starting workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to start workout. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.pause

pause(): Promise<void>

暂停联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [1009104003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104003-非法指令) | Illegal command. Called when workout in ready, paused or stoped state. |
| [1009104999](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104999-通用错误码) | System internal error. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/JvHwS7PzQFW5f7CCKUr_eg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=CAADF48529FD683295D45FD8FBF717FFE5A79DC7F6D7421D567E6A50036D0D1C)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.pause();
  hilog.info(0x0000, 'testTag', 'Succeed in pausing workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to pause workout. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.resume

resume(): Promise<void>

恢复联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [1009104003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104003-非法指令) | Illegal command. Called when workout in ready, sporting or stoped state. |
| [1009104999](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104999-通用错误码) | System internal error. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/aB_OomIQQ5ynVkh3tCpJhg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=0F07BEFCDE70A830BE05CE665B830D3CC8A319060368760AA9133FB4F9CFB115)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.resume();
  hilog.info(0x0000, 'testTag', 'Succeed in resuming workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to resume workout. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.stop

stop(): Promise<void>

停止联动，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [1009104003](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104003-非法指令) | Illegal command. Called when workout is not started. |
| [1009104999](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section1009104999-通用错误码) | System internal error. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/hCf8MVepSA2TP6VOXSD1nw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=FAF4431990927124B9B99E457779B970BC545D9420134B9232D4EC40ACA7E670)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  await healthService.workout.stop();
  hilog.info(0x0000, 'testTag', 'Succeed in stopping workout');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to stop workout. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.onData

onData(dataType: healthStore.DataType, listener: Callback<SampleReal\[\]>): Promise<void>

注册指定联动运动数据监听，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| dataType | [healthStore.DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#datatype) | 是 | 联动运动数据类型。 |
| listener | Callback<[SampleReal](#samplereal)\[\]> | 是 | 联动运动数据监听回调。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/rXt-1hS-RBKWZ7xgJOF-wA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=ABFFB5A438971579D88A7089A30AD593B5945DC7579F2E91322B479000814DE5)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', `Workout onData receive data. The sampleReals size is ${sampleReals.length}`);
  };
  const realTimeMotionDataType: healthStore.DataType = {
    id: 50004
  };
  await healthService.workout.onData(realTimeMotionDataType, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to onData. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.onData

onData(dataType: undefined, listener: Callback<SampleReal\[\]>): Promise<void>

注册所有联动运动数据监听，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| dataType | undefined | 是 | 监听所有联动运动数据类型。 |
| listener | Callback<[SampleReal](#samplereal)\[\]> | 是 | 联动运动数据监听回调。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/AqVvhWWPSzGb9vK8N2lqLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=374B1C3C888F9BDB046C20234B06F2DB1C3F84F82C8514BA0BB89FEF5BE4F4EB)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', `Workout onData receive data. The sampleReals size is ${sampleReals.length}`);
  };
  await healthService.workout.onData(undefined, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to onData. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.offData

offData(dataType: healthStore.DataType, listener: Callback<SampleReal\[\]>): Promise<void>

取消指定联动运动数据的监听，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| dataType | [healthStore.DataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#datatype) | 是 | 联动运动数据类型。 |
| listener | Callback<[SampleReal](#samplereal)\[\]> | 是 | 联动运动数据监听回调。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/crg8q11mQbqhhB4s9Y67zQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=7239E7406E263EDCF1BC9B2969F4350A88811E14C5CEAF43147A8DE8791D85D2)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService, healthStore } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', `Workout offData receive data. The sampleReals size is ${sampleReals.length}`);
  };
  await healthService.workout.offData(healthStore.healthDataTypes.WORKOUT, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to offData. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.offData

offData(dataType: undefined, listener: Callback<SampleReal\[\]>): Promise<void>

取消所有联动运动数据的监听，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| dataType | undefined | 是 | 监听所有联动运动数据类型。 |
| listener | Callback<[SampleReal](#samplereal)\[\]> | 是 | 联动运动数据监听回调。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Parameter verification failed. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Z8BQrLCwTEW47C9RZsEt1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=172CFEED4B5F852B038D5052DE77E8ACCBAB9A3E75EE3388645F189EA76DCC9A)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleReal[]> = (sampleReals) => {
    hilog.info(0x0000, 'testTag', `Workout offData receive data. The sampleReals size is ${sampleReals.length}`);
  };
  await healthService.workout.offData(undefined, callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to offData. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.onEvent("\*")

onEvent(event: "\*", listener: Callback<SampleEvent>): Promise<void>

注册联动设备事件监听，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| event | string | 是 | 联动设备事件类型，支持的事件为："\*"，当联动设备运动状态改变时，触发该事件。 |
| listener | Callback<[SampleEvent](#sampleevent)\> | 是 | 联动设备事件监听回调。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/ExylYO3-SbiK7zPcqanFlg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=16CB990B990FAF2ABEE04F3CA5717A9A1A9AE13FEAC026A7B18600A1F6BF2CE4)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleEvent> = (event) => {
    hilog.info(0x0000, 'testTag', `Workout onEvent receive event. Event data: ${event.eventData}, event id: ${event.eventId}`);
  };
  await healthService.workout.onEvent('*', callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to onEvent. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.offEvent("\*")

offEvent(event: "\*", listener: Callback<SampleEvent>): Promise<void>

取消联动设备事件的监听，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| event | string | 是 | 联动设备事件类型，支持的事件为："\*"，当联动设备运动状态改变时，触发该事件。 |
| listener | Callback<[SampleEvent](#sampleevent)\> | 是 | 联动设备事件监听回调。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Parameter verification failed. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/BeYTa37QQ5mjEwEPEfKJiA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=05A09D73A414E020A653839F8173FCD7177C398EBD57A59D36FF6DF2F15CB25F)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const callback: Callback<healthService.SampleEvent> = (event) => {
    hilog.info(0x0000, 'testTag', `Workout offEvent receive event. Event data: ${event.eventData}, event id: ${event.eventId}`);
  };
  await healthService.workout.offEvent('*', callback);
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to offEvent. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.readActivityReport

readActivityReport(): Promise<ActivityReport>

读取实时三环数据，使用Promise异步方式。

该接口从API 19 Release开始，支持Wearable设备开发。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Health.HealthService

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ActivityReport](#activityreport)\> | Promise对象，返回实时三环数据。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission denied. |
| [14500101](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section14500101-服务异常) | Service exception. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/jpSu8m4bSGma6Z47M_OKSQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=CA42068F41E7BD799DBE9946E6837255F096265D812EF2AA83C895691EB4CAB8)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const result: healthService.workout.ActivityReport = await healthService.workout.readActivityReport();
  
  hilog.info(0x0000, 'testTag', 'Succeeded in reading ActivityReport');
  Object.keys(result).forEach(key => {
    hilog.info(0x0000, 'testTag', `the ${key} is ${result[key]}`);
  });
} catch(err) {
  hilog.error(0x0000, 'testTag', `Failed to read ActivityReport. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.sendData

sendData(sampleReal: SampleReal\[\]): Promise<void>

下发融合运动数据到联动设备，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| sampleReal | [SampleReal](#samplereal)\[\] | 是 | 融合运动数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/PNBYC5RvTMOHmBvCTCyiow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=5311196303E3AAB60E5932FB026B2C3FAAB5D80EFCBE45A371490F636AFA62D7)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const sampleReal: healthService.SampleReal = {
    dataType: { id: 50004 },
    time: 1695740400000, // 2023-09-26 23:00:00,
    fields: {
      hr: 90
    }
  };
  await healthService.workout.sendData([sampleReal]);
  hilog.info(0x0000, 'testTag', 'Succeed in sending data.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to send data. Code: ${err.code}, message: ${err.message}`);
}
```

#### \[h2\]workout.sendEvent

sendEvent(event: SampleEvent): Promise<void>

下发控制事件到联动设备，使用Promise异步方式。

**系统能力：** SystemCapability.Health.HealthService

**设备行为差异：** 该接口在Phone、Tablet中可正常调用，在Wearable中返回401错误码。

**起始版本：** 5.1.0(18)

**参数：**

| **参数名** | **类型** | 必填 | **说明** |
| :-- | :-- | :-- | :-- |
| event | [SampleEvent](#sampleevent) | 是 | 联动控制事件。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 无结果返回的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[运动健康服务ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| [201](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section201-鉴权失败) | Permission verification failed. |
| [401](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-healthservice#section401-参数不合法) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/56Lk3UVLQemkmqkgFPMsBw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014858Z&HW-CC-Expire=86400&HW-CC-Sign=899C8BA17080BFCCA4148DA3253702499C64BEC660ADD34459AF8EC8982E5651)

上述接口调用前，需先使用[init](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/health-api-healthstore#healthstoreinit)方法进行初始化。

**示例：**

```typescript
import { healthService } from '@kit.HealthServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  const sampleEvent: healthService.SampleEvent = {
    eventId: 800400002,
    eventLevel: 0,
    eventData: 'start'
  };
  await healthService.workout.sendEvent(sampleEvent);
  hilog.info(0x0000, 'testTag', 'Succeed in sending event.');
} catch (err) {
  hilog.error(0x0000, 'testTag', `Failed to send event. Code: ${err.code}, message: ${err.message}`);
}
```
