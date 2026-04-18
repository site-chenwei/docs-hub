---
title: "@ohos.thermal (热管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-thermal"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "设备管理"
  - "@ohos.thermal (热管理)"
captured_at: "2026-04-17T01:48:27.795Z"
---

# @ohos.thermal (热管理)

该模块提供热管理相关的接口，包括热档位查询及注册回调等功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/bG48Yu5XQamSvxYdR0IVjg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=9A7084A4D5955B1D6CD7710B094BA58CB7D9E33D30719D38FB09DCB384AAB99B)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import {thermal} from '@kit.BasicServicesKit';
```

#### thermal.registerThermalLevelCallback9+

registerThermalLevelCallback(callback: Callback<ThermalLevel>): void

**方法介绍：** 订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | Callback<[ThermalLevel](#thermallevel)\> | 是 | 回调函数，返回变化后的热档位；该参数是一个函数类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```js
try {
    thermal.registerThermalLevelCallback((level: thermal.ThermalLevel) => {
        console.info('thermal level is: ' + level);
    });
    console.info('register thermal level callback success.');
} catch(err) {
    console.error('register thermal level callback failed, err: ' + err);
}
```

#### thermal.unregisterThermalLevelCallback9+

unregisterThermalLevelCallback(callback?: Callback<void>): void

**方法介绍：** 取消订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | Callback<void> | 否 | 可选参数，回调函数，无返回值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```js
try {
    thermal.unregisterThermalLevelCallback(() => {
        console.info('unsubscribe thermal level success.');
    });
    console.info('unregister thermal level callback success.');
} catch(err) {
    console.error('unregister thermal level callback failed, err: ' + err);
}
```

#### thermal.getLevel9+

getLevel(): ThermalLevel

**方法介绍：** 获取当前热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ThermalLevel](#thermallevel) | 热档位信息。 |

**示例：**

```js
let level = thermal.getLevel();
console.info('thermal level is: ' + level);
```

#### thermal.subscribeThermalLevel(deprecated)

subscribeThermalLevel(callback: AsyncCallback<ThermalLevel>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Ea5hDZuYSregAcXluPgEyA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=3EAC89FA38F0C273F314E49D455EC648EE307ADCAD59EBC40624228E05C351A8)

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.registerThermalLevelCallback](#thermalregisterthermallevelcallback9)替代。

**方法介绍：** 订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[ThermalLevel](#thermallevel)\> | 是 | 回调函数。AsyncCallback只返回一个参数，为热档位信息。 |

**示例：**

```js
thermal.subscribeThermalLevel((err: Error, level: thermal.ThermalLevel) => {
    console.info('thermal level is: ' + level);
});
```

#### thermal.unsubscribeThermalLevel(deprecated)

unsubscribeThermalLevel(callback?: AsyncCallback<void>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/hExO9PGYQRK1aILIhDeJBg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=3B9C29C7F5805CC3152FDD1AA27B10BACE39D7DE13D066CE6F34E485D20751A9)

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.unregisterThermalLevelCallback](#thermalunregisterthermallevelcallback9)替代。

**方法介绍：** 取消订阅热档位变化时的回调提醒。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 否 | 回调函数，无返回值。不填该参数则取消所有回调。 |

**示例：**

```js
thermal.unsubscribeThermalLevel(() => {
    console.info('unsubscribe thermal level success.');
});
```

#### thermal.getThermalLevel(deprecated)

getThermalLevel(): ThermalLevel

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/SsbJW50xSQe1pO_Ln0PYSg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=49E635C85F6EB26944D908B7D6B1089026FFE568D112B09DCA7F6E22D9C82EC7)

从API version 8开始支持，从API version 9开始不再维护，建议使用[thermal.getLevel](#thermalgetlevel9)替代。

**方法介绍：** 获取当前热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ThermalLevel](#thermallevel) | 热档位信息。 |

**示例：**

```js
let level = thermal.getThermalLevel();
console.info('thermal level is: ' + level);
```

#### ThermalLevel

热档位信息。

**系统能力：** SystemCapability.PowerManager.ThermalManager

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| COOL | 0 | 表明设备处于清凉状态，业务执行不受热控的限制。 |
| NORMAL | 1 | 表明设备温度正常，但邻近温热状态，无感知业务应降低规格和负载。 |
| WARM | 2 | 表明设备进入温热状态，无感知业务应暂停或延迟运行。 |
| HOT | 3 | 表明设备发热明显，无感知业务应停止，非关键业务应降低规格及负载。 |
| OVERHEATED | 4 | 表明设备发热严重，无感知业务与非关键业务应停止，前台关键业务应降低规格及负载。 |
| WARNING | 5 | 表明设备过热即将进入紧急状态，整机资源供给大幅降低，停止所有非关键业务，前台关键业务应降低至最低规格。 |
| EMERGENCY | 6 | 表明设备已经进入过热紧急状态，整机资源供给降至最低，设备功能受限，仅保留基础功能可用。 |
| ESCAPE11+ | 7 | 
表明设备即将进入热逃生状态，所有业务将被强制停止，业务需做好逃生措施，例如保存重要数据等。

**说明**: 从API version 11开始支持。

 |
