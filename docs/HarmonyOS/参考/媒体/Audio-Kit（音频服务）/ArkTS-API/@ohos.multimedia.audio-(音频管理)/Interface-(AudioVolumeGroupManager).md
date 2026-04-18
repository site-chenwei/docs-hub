---
title: "Interface (AudioVolumeGroupManager)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumegroupmanager"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "ArkTS API"
  - "@ohos.multimedia.audio (音频管理)"
  - "Interface (AudioVolumeGroupManager)"
captured_at: "2026-04-17T01:48:35.988Z"
---

# Interface (AudioVolumeGroupManager)

管理音频组音量。

在使用AudioVolumeGroupManager的接口之前，需先通过[getVolumeGroupManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumegroupmanager9)获取AudioVolumeGroupManager实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/Nb7OdEj2QTyR0P1scxni5A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=90EF78DD4B6C795F106C874800B0631A25F2F0286F56A75A10F8D7ED625D1A1E)

-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 9开始支持。

#### 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

#### getVolume(deprecated)

getVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的音量等级。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/dBI7tGWyRwGkbdjk0UdmQw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=CDC9AEAED6B34EDC3065ACE642781AA89A68929E9D7EAA50B56A6435790E6F22)

从API version 9开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的音量成功，err为undefined，data为获取到的指定流的音量等级；否则为错误对象。指定流的音量等级范围可通过[getMinVolume](#getminvolumedeprecated)和[getMaxVolume](#getmaxvolumedeprecated)获取。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get volume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
});
```

#### getVolume(deprecated)

getVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的音量等级。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/FeXmknnaSkSPWCt1gmS58w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=FBCA268EB516E29CEAC58393676FAA5FD72E18E9537BAB34299263C64139ABA3)

从API version 9开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回指定流的音量等级。指定流的音量等级范围可通过[getMinVolume](#getminvolumedeprecated)和[getMaxVolume](#getmaxvolumedeprecated)获取。 |

**示例：**

```ts
audioVolumeGroupManager.getVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
});
```

#### getVolumeSync(deprecated)

getVolumeSync(volumeType: AudioVolumeType): number

获取指定流的音量等级。同步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/8HBObcjzQaK4y7Za52_yfg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=AB36424068C45E9BF2BA09681523D5D983446CA219B193208B43EF5FC5B92A12)

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回指定流的音量等级。指定流的音量等级范围可通过[getMinVolume](#getminvolumedeprecated)和[getMaxVolume](#getmaxvolumedeprecated)获取。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Succeeded in getting volume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get volume. Code: ${error.code}, message: ${error.message}`);
}
```

#### getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最小音量等级。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/Ww40hJyvTZqr1jUBxZ9ORA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=72D888989616DC59AA07204C677A276A7AC5C1704863C02C6D82A824E6EE0875)

从API version 9开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的最小音量成功，err为undefined，data为获取到的指定流的最小音量等级；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get minVolume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
});
```

#### getMinVolume(deprecated)

getMinVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最小音量等级。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/18q3ZbGwRuuStuHJ87o_kQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=420C5DD6F9ABE911854F0F80BCBECAEA3F804E8EDAD4D1F8C5819F30B28CCB25)

从API version 9开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回最小音量等级。 |

**示例：**

```ts
audioVolumeGroupManager.getMinVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
});
```

#### getMinVolumeSync(deprecated)

getMinVolumeSync(volumeType: AudioVolumeType): number

获取指定流的最小音量等级。同步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/SzABvJ_1QcaOB5edUON7Rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=4D0EAB22B15BF656A2759513B8471AA69C66129000F29D60157A0ABB0A48A9BC)

从API version 10开始支持，从API version 20开始废弃，建议使用[getMinVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getminvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回最小音量等级。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMinVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Succeeded in getting minVolume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get minVolume. Code: ${error.code}, message: ${error.message}`);
}
```

#### getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType, callback: AsyncCallback<number>): void

获取指定流的最大音量等级。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/NT9wdxasTN2i-Hw3D9Q5lw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=B2AB18F883DC03EFFA6BB0C3A7EEC4C96AECB4D4F2D8617C9699CD6C8E354DCF)

从API version 9开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取指定流的最大音量成功，err为undefined，data为获取到的指定流的最大音量等级；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get maxVolume. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
});
```

#### getMaxVolume(deprecated)

getMaxVolume(volumeType: AudioVolumeType): Promise<number>

获取指定流的最大音量等级。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/RtGXJBW6RXWB-w_uWVq8Vw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=0151E13263F522AD7460C772496A981C18CA69A79C18C8FC5A5ACF89FDDFE684)

从API version 9开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回最大音量等级。 |

**示例：**

```ts
audioVolumeGroupManager.getMaxVolume(audio.AudioVolumeType.MEDIA).then((value: number) => {
  console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
});
```

#### getMaxVolumeSync(deprecated)

getMaxVolumeSync(volumeType: AudioVolumeType): number

获取指定流的最大音量等级。同步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/EW4JsvIOStaLfNQ_Cp76lA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=D359E0767447DB5618C6AFFED7386F2D3CF5DF49E8604550147F51B9F6765C67)

从API version 10开始支持，从API version 20开始废弃，建议使用[getMaxVolumeByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getmaxvolumebystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回最大音量等级。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getMaxVolumeSync(audio.AudioVolumeType.MEDIA);
  console.info(`Succeeded in getting maxVolume. Volume: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get maxVolume. Code: ${error.code}, message: ${error.message}`);
}
```

#### isMute(deprecated)

isMute(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音量流静音状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Ql-zocYkRaCHchPuOGpeaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=A08AC0CD918756045FA5CFE707139A9157D16EFFEBBD8F6E52D1F2D3819A8964)

从API version 9开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定音量流静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to use isMute function. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in using isMute function. MuteState: ${value}.`);
});
```

#### isMute(deprecated)

isMute(volumeType: AudioVolumeType): Promise<boolean>

获取指定音量流是否被静音。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/RBrFLp1-ST-8zakKa4QisA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=B0325E78347675E1BDF3DB7F155930746231084D68706756E3424565DA9C402C)

从API version 9开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示静音；返回false表示非静音。 |

**示例：**

```ts
audioVolumeGroupManager.isMute(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Succeeded in using isMute function. MuteState: ${value}.`);
});
```

#### isMuteSync(deprecated)

isMuteSync(volumeType: AudioVolumeType): boolean

获取指定音量流是否被静音。同步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/MN8qGEudQqai7h2eTUTyjw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=CC3597603F21E133E9BB16618411A890989454DA915282C43269640338E1E501)

从API version 10开始支持，从API version 20开始废弃，建议使用[isSystemMutedForStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#issystemmutedforstream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 流静音状态。返回true表示静音，返回false表示非静音。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMuteSync(audio.AudioVolumeType.MEDIA);
  console.info(`Succeeded in using isMuteSync function. MuteState: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to use isMuteSync function. Code: ${error.code}, message: ${error.message}`);
}
```

#### getRingerMode9+

getRingerMode(callback: AsyncCallback<AudioRingMode>): void

获取铃声模式。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)\> | 是 | 回调函数。当获取铃声模式成功，err为undefined，data为获取到的铃声模式；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode((err: BusinessError, value: audio.AudioRingMode) => {
  if (err) {
    console.error(`Failed to get ringerMode. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
});
```

#### getRingerMode9+

getRingerMode(): Promise<AudioRingMode>

获取铃声模式。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)\> | Promise对象，返回系统的铃声模式。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getRingerMode().then((value: audio.AudioRingMode) => {
  console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get ringerMode. Code: ${err.code}, message: ${err.message}`);
});
```

#### getRingerModeSync10+

getRingerModeSync(): AudioRingMode

获取铃声模式。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode) | 返回系统的铃声模式。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: audio.AudioRingMode = audioVolumeGroupManager.getRingerModeSync();
  console.info(`Succeeded in getting ringerMode. AudioRingMode: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get ringerMode. Code: ${error.code}, message: ${error.message}`);
}
```

#### on('ringerModeChange')9+

on(type: 'ringerModeChange', callback: Callback<AudioRingMode>): void

监听铃声模式变化事件（当[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)发生变化时触发）。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'ringerModeChange'，当铃声模式发生变化时，触发该事件。 |
| callback | Callback<[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)\> | 是 | 回调函数，返回变化后的铃音模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
audioVolumeGroupManager.on('ringerModeChange', (ringerMode: audio.AudioRingMode) => {
  console.info(`Succeeded in using on function. AudioRingMode: ${ringerMode}.`);
});
```

#### off('ringerModeChange')18+

off(type: 'ringerModeChange', callback?: Callback<AudioRingMode>): void

取消监听铃声模式变化事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'ringerModeChange'，当取消监听铃声模式变化事件时，触发该事件。 |
| callback | Callback<[AudioRingMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioringmode)\> | 否 | 回调函数，返回变化后的铃音模式。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
// 取消该事件的所有监听。
audioVolumeGroupManager.off('ringerModeChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let ringerModeChangeCallback = (ringerMode: audio.AudioRingMode) => {
  console.info(`Succeeded in using on or off function. AudioRingMode: ${ringerMode}.`);
};

audioVolumeGroupManager.on('ringerModeChange', ringerModeChangeCallback);

audioVolumeGroupManager.off('ringerModeChange', ringerModeChangeCallback);
```

#### isMicrophoneMute9+

isMicrophoneMute(callback: AsyncCallback<boolean>): void

获取麦克风静音状态。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取麦克风静音状态成功，err为undefined，data为true表示静音，false表示非静音；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute((err: BusinessError, value: boolean) => {
  if (err) {
    console.error(`Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info(`Succeeded in using isMicrophoneMute function. MuteState: ${value}.`);
});
```

#### isMicrophoneMute9+

isMicrophoneMute(): Promise<boolean>

获取麦克风静音状态。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示麦克风被静音；返回false表示麦克风未被静音。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
  console.info(`Succeeded in using isMicrophoneMute function. MuteState: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to use isMicrophoneMute function. Code: ${err.code}, message: ${err.message}`);
});
```

#### isMicrophoneMuteSync10+

isMicrophoneMuteSync(): boolean

获取麦克风静音状态。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 系统麦克风静音状态。返回true表示静音，返回false表示非静音。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: boolean = audioVolumeGroupManager.isMicrophoneMuteSync();
  console.info(`Succeeded in using isMicrophoneMuteSync function. MuteState: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to use isMicrophoneMuteSync function. Code: ${error.code}, message: ${error.message}`);
}
```

#### on('micStateChange')9+

on(type: 'micStateChange', callback: Callback<MicStateChangeEvent>): void

监听系统麦克风状态更改事件（当检测到系统麦克风状态发生改变时触发）。使用callback异步回调。

目前此订阅接口在单进程多AudioManager实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例没有进行订阅）。因此，推荐使用单一AudioManager实例进行开发。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'micStateChange'，当检测到系统麦克风状态发生改变时，触发该事件。 |
| callback | Callback<[MicStateChangeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#micstatechangeevent9)\> | 是 | 回调函数，返回变更后的麦克风状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
audioVolumeGroupManager.on('micStateChange', (micStateChange: audio.MicStateChangeEvent) => {
  console.info(`Succeeded in using on function. MicStateChangeEvent: ${JSON.stringify(micStateChange)}.`);
});
```

#### off('micStateChange')12+

off(type: 'micStateChange', callback?: Callback<MicStateChangeEvent>): void

取消监听系统麦克风状态更改事件。使用callback异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'micStateChange'，当取消监听系统麦克风状态更改事件时，触发该事件。 |
| callback | Callback<[MicStateChangeEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#micstatechangeevent9)\> | 否 | 回调函数，返回变更后的麦克风状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters missing; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
// 取消该事件的所有监听。
audioVolumeGroupManager.off('micStateChange');

// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
let micStateChangeCallback = (micStateChange: audio.MicStateChangeEvent) => {
  console.info(`Succeeded in using on or off function. MicStateChangeEvent: ${JSON.stringify(micStateChange)}.`);
};

audioVolumeGroupManager.on('micStateChange', micStateChangeCallback);

audioVolumeGroupManager.off('micStateChange', micStateChangeCallback);
```

#### isVolumeUnadjustable10+

isVolumeUnadjustable(): boolean

获取固定音量模式开关状态，打开时进入固定音量模式，此时音量固定无法被调节。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 固定音量模式开关状态。返回true表示固定音量模式，返回false表示非固定音量模式。 |

**示例：**

```ts
let volumeAdjustSwitch: boolean = audioVolumeGroupManager.isVolumeUnadjustable();
console.info(`Succeeded in using isVolumeUnadjustable function. VolumeUnadjustable: ${volumeAdjustSwitch}.`);
```

#### getSystemVolumeInDb(deprecated)

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType, callback: AsyncCallback<number>): void

获取音量增益dB值。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/tPa3GNSiQFa-i061qN-zsg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=853EE81638E4124358C8ED3B1C97C97A8F04ADCD06684A08EF8DCBB2B1720886)

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#devicetype) | 是 | 设备类型。 |
| callback | AsyncCallback<number> | 是 | 回调函数。当获取音量增益dB值成功，err为undefined，data为获取到的音量增益dB值；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |
| 6800301 | System error. Return by callback. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER, (err: BusinessError, value: number) => {
  if (err) {
    console.error(`Failed to get system volume in db. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
  }
});
```

#### getSystemVolumeInDb(deprecated)

getSystemVolumeInDb(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): Promise<number>

获取音量增益dB值。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/aq_Z_8cDQ8CRCgOrRwKvUA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=5A74B64E9586828536F22F96C0EDE00CF6E9F84DB07230257118818BDD54ADA7)

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#devicetype) | 是 | 设备类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回对应的音量增益dB值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.getSystemVolumeInDb(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER).then((value: number) => {
  console.info(`Succeeded in getting system volume in db. DB: ${value}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get system volume in db. Code: ${err.code}, message: ${err.message}`);
});
```

#### getSystemVolumeInDbSync(deprecated)

getSystemVolumeInDbSync(volumeType: AudioVolumeType, volumeLevel: number, device: DeviceType): number

获取音量增益dB值。同步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/x6ebJFBcTPasRsuvalOaWg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=7BA37A9A00E089F4B1E274D7F422E73292C5B69671E81CF83F8EAAE2C1E0832A)

从API version 10开始支持，从API version 20开始废弃，建议使用[getVolumeInUnitOfDbByStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiovolumemanager#getvolumeinunitofdbbystream20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频音量类型。 |
| volumeLevel | number | 是 | 音量等级。 |
| device | [DeviceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#devicetype) | 是 | 设备类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回对应的音量增益dB值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let value: number = audioVolumeGroupManager.getSystemVolumeInDbSync(audio.AudioVolumeType.MEDIA, 3, audio.DeviceType.SPEAKER);
  console.info(`Succeeded in getting system volume in db sync. DB: ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get system volume in db sync. Code: ${error.code}, message: ${error.message}`);
}
```

#### getMaxAmplitudeForInputDevice12+

getMaxAmplitudeForInputDevice(inputDevice: AudioDeviceDescriptor): Promise<number>

获取输入设备音频流的最大电平值，取值范围为\[0, 1\]。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| inputDevice | [AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor) | 是 | 获取最大电平值的设备信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回对应设备的电平值，大小在\[0, 1\]之间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let capturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC, // 音源类型：Mic音频源。根据业务场景配置，参考SourceType。
  capturerFlags: 0 // 音频采集器标志。
};

audio.getAudioManager().getRoutingManager().getPreferredInputDeviceForCapturerInfo(capturerInfo).then((data) => {
  audioVolumeGroupManager.getMaxAmplitudeForInputDevice(data[0]).then((value) => {
    console.info(`Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}`);
  })
}).catch((err: BusinessError) => {
  console.error(`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
})
```

#### getMaxAmplitudeForOutputDevice12+

getMaxAmplitudeForOutputDevice(outputDevice: AudioDeviceDescriptor): Promise<number>

获取输出设备音频流的最大电平值，取值范围为\[0, 1\]。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| outputDevice | [AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor) | 是 | 获取最大电平值的设备信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回对应设备的电平值，大小在\[0, 1\]之间。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |
| 6800301 | System error. Return by promise. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let rendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};

audio.getAudioManager().getRoutingManager().getPreferOutputDeviceForRendererInfo(rendererInfo).then((data) => {
  audioVolumeGroupManager.getMaxAmplitudeForOutputDevice(data[0]).then((value) => {
    console.info(`Succeeded in getting maxAmplitude for input device. Amplitude: ${value}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to get maxAmplitude for input device. Code: ${err.code}, message: ${err.message}`);
  })
}).catch((err: BusinessError) => {
  console.error(`Failed to get preferred input device for capturer info. Code: ${err.code}, message: ${err.message}`);
})
```

#### setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean, callback: AsyncCallback<void>): void

设置麦克风静音状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/FqAXjTcBQF2ZkHWqHU1YLQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=3ADCB6DD57B2B058514122DC02FD2AFCC2266F3791F0DAF24C956C5F9DF40995)

从API version 9开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_AUDIO\_CONFIG，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置麦克风静音状态成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioVolumeGroupManager.setMicrophoneMute(true, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set microphone mute. Code: ${err.code}, message: ${err.message}`);
    return;
  }
  console.info('Succeeded in setting microphone mute.');
});
```

#### setMicrophoneMute(deprecated)

setMicrophoneMute(mute: boolean): Promise<void>

设置麦克风静音状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/wIL8e3ZPRjWlm6IddRtolQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=451B71BF59CA307A344BD97D6735995A48C29A1FF08AA1F1C008E9E99E184124)

从API version 9开始支持，从API version 11开始废弃，替代接口仅面向系统应用开放。

**需要权限：** ohos.permission.MANAGE\_AUDIO\_CONFIG，该权限仅系统应用可申请。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mute | boolean | 是 | 是否设置麦克风为静音状态。true表示静音，false表示非静音。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
audioVolumeGroupManager.setMicrophoneMute(true).then(() => {
  console.info('Succeeded in setting microphone mute.');
});
```
