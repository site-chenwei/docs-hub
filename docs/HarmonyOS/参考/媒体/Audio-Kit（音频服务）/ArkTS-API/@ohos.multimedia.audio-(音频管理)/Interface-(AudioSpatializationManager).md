---
title: "Interface (AudioSpatializationManager)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiospatializationmanager"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "ArkTS API"
  - "@ohos.multimedia.audio (音频管理)"
  - "Interface (AudioSpatializationManager)"
captured_at: "2026-04-17T01:48:35.914Z"
---

# Interface (AudioSpatializationManager)

空间音频管理。

在使用AudioSpatializationManager的接口之前，需先通过[getSpatializationManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiomanager#getspatializationmanager18)获取AudioSpatializationManager实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/-K_KQQthQhOLSAh7E0jPHw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=8A78A36015DF972B4DF75387464146AC88BC4AEA4CD160B1BBA627B9E4499C28)

-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 18开始支持。

#### 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

#### isSpatializationEnabledForCurrentDevice18+

isSpatializationEnabledForCurrentDevice(): boolean

获取当前设备空间音频渲染是否开启。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 当前设备空间音频渲染是否开启。true表示开启，false表示未开启。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

let isSpatializationEnabledForCurrentDevice: boolean = audioSpatializationManager.isSpatializationEnabledForCurrentDevice();
console.info(`AudioSpatializationManager isSpatializationEnabledForCurrentDevice: ${isSpatializationEnabledForCurrentDevice}`);
```

#### on('spatializationEnabledChangeForCurrentDevice')18+

on(type: 'spatializationEnabledChangeForCurrentDevice', callback: Callback<boolean>): void

监听当前设备空间音频渲染开关状态变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'spatializationEnabledChangeForCurrentDevice'，当空间音频渲染开关状态变化时，触发该事件。 |
| callback | Callback<boolean> | 是 | 回调函数。返回true表示打开空间音频渲染状态；返回false表示关闭空间音频渲染状态。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

audioSpatializationManager.on('spatializationEnabledChangeForCurrentDevice', (isSpatializationEnabledForCurrentDevice: boolean) => {
  console.info(`isSpatializationEnabledForCurrentDevice: ${isSpatializationEnabledForCurrentDevice}`);
});
```

#### off('spatializationEnabledChangeForCurrentDevice')18+

off(type: 'spatializationEnabledChangeForCurrentDevice', callback?: Callback<boolean>): void

取消监听当前设备空间音频渲染开关状态变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Spatialization

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'spatializationEnabledChangeForCurrentDevice'，当取消订阅当前设备空间音频渲染开关状态变化事件时，触发该事件。 |
| callback | Callback<boolean> | 否 | 回调函数。返回true表示打开空间音频渲染状态；返回false表示关闭空间音频渲染状态。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { audio } from '@kit.AudioKit';
audioSpatializationManager.off('spatializationEnabledChangeForCurrentDevice');
```
