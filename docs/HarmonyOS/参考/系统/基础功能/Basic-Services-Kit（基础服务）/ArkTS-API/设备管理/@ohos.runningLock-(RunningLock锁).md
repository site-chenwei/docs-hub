---
title: "@ohos.runningLock (RunningLock锁)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-runninglock"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "设备管理"
  - "@ohos.runningLock (RunningLock锁)"
captured_at: "2026-04-17T01:48:27.751Z"
---

# @ohos.runningLock (RunningLock锁)

该模块为RunningLock锁相关操作的接口，提供使能接近光亮灭屏或者设备熄屏后阻止进入睡眠的能力，包括创建、查询、持锁、释放锁等操作，类型详情见[RunningLockType](#runninglocktype)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/XFgILfEWQYy-_vVx6aSStA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=6CC14B99FEF49298456AA88A79A329B8510EC85D9B48287691C8B783C44E5E6C)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import {runningLock} from '@kit.BasicServicesKit';
```

#### runningLock.isSupported9+

isSupported(type: RunningLockType): boolean

**方法介绍：** 查询系统是否支持该类型的锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [RunningLockType](#runninglocktype) | 是 | 需要查询的锁的类型；该参数必须是一个枚举类。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回true表示支持，返回false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**示例：**

```js
try {
    let isSupported = runningLock.isSupported(runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL);
    console.info('BACKGROUND type supported: ' + isSupported);
} catch(err) {
    console.error('check supported failed, err: ' + err);
}
```

#### runningLock.create9+

create(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void

**方法介绍：** 创建RunningLock锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 锁的名字；该参数必须为字符串类型。 |
| type | [RunningLockType](#runninglocktype) | 是 | 要创建的锁的类型；该参数必须是一个枚举类。 |
| callback | AsyncCallback<[RunningLock](#runninglock)\> | 是 | 回调函数。当创建锁成功，err为undefined，data为创建的RunningLock；否则为错误对象；AsyncCallback封装了一个RunningLock类型的类。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 201 | If the permission is denied. |

**示例：**

```js
runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
    if (typeof err === 'undefined') {
        console.info('created running lock: ' + lock);
    } else {
        console.error('create running lock failed, err: ' + err);
    }
});
```

#### runningLock.create9+

create(name: string, type: RunningLockType): Promise<RunningLock>

**方法介绍：** 创建RunningLock锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 锁的名字；该参数必须为字符串类型。 |
| type | [RunningLockType](#runninglocktype) | 是 | 要创建的锁的类型；该参数必须是一个枚举类。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RunningLock](#runninglock)\> | Promise对象，返回RunningLock锁对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Parameter verification failed. |
| 201 | If the permission is denied. |

**示例：**

```js
runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL)
.then((lock: runningLock.RunningLock) => {
    console.info('created running lock: ' + lock);
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

#### runningLock.isRunningLockTypeSupported(deprecated)

isRunningLockTypeSupported(type: RunningLockType, callback: AsyncCallback<boolean>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/OrCDTiXwT9yq9WLgNm-oyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=388F34587F35A67A24E2DABBFDFF827690F2FAC9AB0C05E7299773CED6404697)

从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.isSupported](#runninglockissupported9)替代。

**方法介绍：** 查询系统是否支持该类型的锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [RunningLockType](#runninglocktype) | 是 | 需要查询的锁的类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当查询成功，err为undefined，data为获取到的支持情况，返回true表示支持，返回false表示不支持；否则为错误对象。 |

**示例：**

```js
runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND, (err: Error, data: boolean) => {
    if (typeof err === 'undefined') {
        console.info('BACKGROUND lock support status: ' + data);
    } else {
        console.error('check BACKGROUND lock support status failed, err: ' + err);
    }
});
```

#### runningLock.isRunningLockTypeSupported(deprecated)

isRunningLockTypeSupported(type: RunningLockType): Promise<boolean>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/Z5t3N6smS0qE7oIxhyYL4A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=A893E534EBA19197DF85CA8E7E318406C802CC22C18F30B1CAD9CCED1F137890)

从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.isSupported](#runninglockissupported9)替代。

**方法介绍：** 查询系统是否支持该类型的锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [RunningLockType](#runninglocktype) | 是 | 需要查询的锁的类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示支持；返回false表示不支持。 |

**示例：**

```js
runningLock.isRunningLockTypeSupported(runningLock.RunningLockType.BACKGROUND)
.then((data: boolean) => {
    console.info('BACKGROUND lock support status: ' + data);
})
.catch((err: Error) => {
    console.error('check BACKGROUND lock support status failed, err: ' + err);
});
```

#### runningLock.createRunningLock(deprecated)

createRunningLock(name: string, type: RunningLockType, callback: AsyncCallback<RunningLock>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/5aFVEF9pSrmBJro-tEsVUA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=E4CDAEBD293D92BDE6D11E6D5FB75EE8B421B1C02768EAA293CF71C4A0D13F6A)

从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.create](#runninglockcreate9)替代。

**方法介绍：** 创建RunningLock锁。使用callback异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 锁的名字。 |
| type | [RunningLockType](#runninglocktype) | 是 | 要创建的锁的类型。 |
| callback | AsyncCallback<[RunningLock](#runninglock)\> | 是 | 回调函数。当创建锁成功，err为undefined，data为创建的RunningLock；否则为错误对象。 |

**示例：**

```js
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND, (err: Error, lock: runningLock.RunningLock) => {
    if (typeof err === 'undefined') {
        console.info('created running lock: ' + lock);
    } else {
        console.error('create running lock failed, err: ' + err);
    }
});
```

#### runningLock.createRunningLock(deprecated)

createRunningLock(name: string, type: RunningLockType): Promise<RunningLock>

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/aIS2I_15R2SVNnDYVv026Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=DAEBEF95714280CABCAA0F67E9951EBCC5DB8F99D1B302307F17B0524CB8990C)

从API version 7开始支持，从API version 9开始不再维护，建议使用[runningLock.create](#runninglockcreate9)替代。

**方法介绍：** 创建RunningLock锁。使用Promise异步回调。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| name | string | 是 | 锁的名字。 |
| type | [RunningLockType](#runninglocktype) | 是 | 要创建的锁的类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[RunningLock](#runninglock)\> | Promise对象，返回RunningLock锁对象。 |

**示例：**

```js
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    console.info('created running lock: ' + lock);
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

#### RunningLock

阻止系统睡眠的锁。

#### \[h2\]hold9+

hold(timeout: number): void

**方法介绍：** 锁定和持有RunningLock。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timeout | number | 是 | 
锁定和持有RunningLock的时长，单位：毫秒。

该参数必须为数字类型：

**\-1**：永久持锁，需要主动释放。

**0**：默认3s后超时释放。

**\>0**：按传入值超时释放。

 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 201 | If the permission is denied. |

**示例：**

```ts
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static holdRunningLock(): void {
        if (RunningLockTest.recordLock) {
            RunningLockTest.recordLock.hold(500);
            console.info('hold running lock success');
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    try {
                        lock.hold(500);
                        console.info('hold running lock success');
                    } catch(err) {
                        console.error('hold running lock failed, err: ' + err);
                    }
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}
```

#### \[h2\]unhold9+

unhold(): void

**方法介绍：** 释放RunningLock锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | If the permission is denied. |

**示例：**

```ts
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static unholdRunningLock(): void {
        if (RunningLockTest.recordLock) {
            RunningLockTest.recordLock.unhold();
            console.info('unhold running lock success');
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    try {
                        lock.unhold();
                        console.info('unhold running lock success');
                    } catch(err) {
                        console.error('unhold running lock failed, err: ' + err);
                    }
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}
```

#### \[h2\]isHolding9+

isHolding(): boolean

**方法介绍：** 查询当前RunningLock是持有状态还是释放状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回true表示当前RunningLock是持有状态，返回false表示当前RunningLock是释放状态。 |

**示例：**

```ts
// RunningLockTest.ets
class RunningLockTest {
    public static recordLock: runningLock.RunningLock;

    public static isHoldingRunningLock(): void {
        if (RunningLockTest.recordLock) {
            let isHolding = RunningLockTest.recordLock.isHolding();
            console.info('check running lock holding status: ' + isHolding);
        } else {
            runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL, (err: Error, lock: runningLock.RunningLock) => {
                if (typeof err === 'undefined') {
                    console.info('create running lock: ' + lock);
                    RunningLockTest.recordLock = lock;
                    let isHolding = lock.isHolding();
                    console.info('check running lock holding status: ' + isHolding);
                } else {
                    console.error('create running lock failed, err: ' + err);
                }
            });
        }
    }
}
```

#### \[h2\]lock(deprecated)

lock(timeout: number): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/xguGBQP3RIOzJd1CZ5_KAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=B4FDC65D7E1A6701BB58C233912018FB97C76C7F8C5ECB0AAA20D94AD90E989B)

从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.hold](#hold9)替代。

**方法介绍：** 锁定和持有RunningLock。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timeout | number | 是 | 锁定和持有RunningLock的时长，单位：毫秒。 |

**示例：**

```js
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    lock.lock(500);
    console.info('create running lock and lock success');
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

#### \[h2\]unlock(deprecated)

unlock(): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/WAjcSAiMQWCAbiO5j1Kqkg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=14B19E51AA395B9714979447E99DD08292F9A6CCA1194E6ECDBDA41232881065)

从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.unhold](#unhold9)替代。

**方法介绍：** 释放RunningLock锁。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**需要权限：** ohos.permission.RUNNING\_LOCK

**示例：**

```js
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    lock.unlock();
    console.info('create running lock and unlock success');
})
.catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
});
```

#### \[h2\]isUsed(deprecated)

isUsed(): boolean

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/ZNbq_3s5RTupB-DfoRfmFw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=551DCC79A42B8349D9916A5329E5BECA7E2D6869F7C84AEDA5541B4A38D951F7)

从API version 7开始支持，从API version 9开始不再维护，建议使用[RunningLock.isHolding](#isholding9)替代。

**方法介绍：** 查询当前RunningLock是持有状态还是释放状态。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回true表示当前RunningLock是持有状态，返回false表示当前RunningLock是释放状态。 |

**示例：**

```js
runningLock.createRunningLock('running_lock_test', runningLock.RunningLockType.BACKGROUND)
.then((lock: runningLock.RunningLock) => {
    let isUsed = lock.isUsed();
    console.info('check running lock used status: ' + isUsed);
})
.catch((err: Error) => {
    console.error('check running lock used status failed, err: ' + err);
});
```

#### RunningLockType

RunningLock锁的类型。

**系统能力：** SystemCapability.PowerManager.PowerManager.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| BACKGROUND(deprecated) | 1 | 
阻止系统睡眠的锁。

**说明：** 从API version 7开始支持，从API version 10开始废弃。

 |
| PROXIMITY\_SCREEN\_CONTROL | 2 | 接近光锁，使能接近光传感器，并根据传感器与障碍物的距离远近发起亮灭屏流程。 |
| BACKGROUND\_USER\_IDLE23+ | 129 | 阻止系统自动睡眠的后台闲时任务锁，持锁能保证一段时间用户不活动后系统不进入自动睡眠。注意：不能阻止如PC合盖等场景系统进入强制睡眠，使用方必须监听[进入强制睡眠公共事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/commoneventmanager-definitions#common_event_enter_force_sleep12)，监听到事件后释放该锁。该类型锁行为存在设备差异，使用该类型锁请参考[阻止系统闲时进入睡眠开发指南](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/runninglock-dev)。 |
