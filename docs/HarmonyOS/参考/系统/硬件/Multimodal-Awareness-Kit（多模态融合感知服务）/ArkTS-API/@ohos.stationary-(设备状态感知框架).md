---
title: "@ohos.stationary (设备状态感知框架)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-stationary"
menu_path:
  - "参考"
  - "系统"
  - "硬件"
  - "Multimodal Awareness Kit（多模态融合感知服务）"
  - "ArkTS API"
  - "@ohos.stationary (设备状态感知框架)"
captured_at: "2026-04-17T01:48:33.312Z"
---

# @ohos.stationary (设备状态感知框架)

设备状态感知框架提供设备状态感知能力，包括绝对静止和相对静止。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/GPKKTPcWQUy96w_tIBRj4A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014835Z&HW-CC-Expire=86400&HW-CC-Sign=8E92C598C28BD6329D26817641B07649A433F9421AA5340497196944E00D88B2)

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块不支持在x86平台上运行。

#### 导入模块

```ts
import { stationary } from '@kit.MultimodalAwarenessKit';
```

#### ActivityResponse

服务响应抽象接口。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| state | [ActivityState](#activitystate) | 否 | 否 | 设备状态变化返回值。 |

#### ActivityType

type ActivityType = 'still' | 'relativeStill'

设备状态类型。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 类型 | 说明 |
| :-- | :-- |
| 'still' | 绝对静止。 |
| 'relativeStill' | 相对静止。 |

#### ActivityEvent

设备状态事件。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ENTER | 1 | 进入事件。 |
| EXIT | 2 | 退出事件。 |
| ENTER\_EXIT | 3 | 进入和退出事件。 |

#### ActivityState

设备状态返回值。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ENTER | 1 | 进入状态。 |
| EXIT | 2 | 退出状态。 |

#### stationary.on('still' | 'relativeStill')

on(activity: ActivityType, event: ActivityEvent, reportLatencyNs: number, callback: Callback<ActivityResponse>): void

设备状态管理，订阅设备状态服务。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| activity | [ActivityType](#activitytype) | 是 | 设备状态能力类型。 |
| event | [ActivityEvent](#activityevent) | 是 | 事件类型。 |
| reportLatencyNs | number | 是 | 报告延时，单位为纳秒（ns）, 取值范围\[1000000000-3000000000\]。 |
| callback | Callback<[ActivityResponse](#activityresponse)\> | 是 | 回调函数，接收上报状态变化事件。 |

**示例：**

```ts
let reportLatencyNs = 1000000000;
stationary.on('still', stationary.ActivityEvent.ENTER, reportLatencyNs, (data) => {
    console.info('data=' + JSON.stringify(data));
})
```

#### stationary.once('still' | 'relativeStill')

once(activity: ActivityType, callback: Callback<ActivityResponse>): void

设备状态管理，查询设备状态。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| activity | [ActivityType](#activitytype) | 是 | 设备状态能力类型。 |
| callback | Callback<[ActivityResponse](#activityresponse)\> | 是 | 回调函数，接收上报状态变化事件。 |

**示例：**

```ts
stationary.once('still', (data) => {
    console.info('data=' + JSON.stringify(data));
})
```

#### stationary.off('still' | 'relativeStill')

off(activity: ActivityType, event: ActivityEvent, callback?: Callback<ActivityResponse>): void

设备状态管理，取消订阅设备状态服务。

**系统能力**：SystemCapability.Msdp.DeviceStatus.Stationary

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| activity | [ActivityType](#activitytype) | 是 | 设备状态能力类型。 |
| event | [ActivityEvent](#activityevent) | 是 | 事件类型。 |
| callback | Callback<[ActivityResponse](#activityresponse)\> | 否 | 回调函数，接收上报状态变化事件，如果没有传递callback参数或者传递的类型是undefined，会移除该进程下订阅该类型的所有callback。 |

**示例：**

```ts
stationary.off('still', stationary.ActivityEvent.ENTER);
```
