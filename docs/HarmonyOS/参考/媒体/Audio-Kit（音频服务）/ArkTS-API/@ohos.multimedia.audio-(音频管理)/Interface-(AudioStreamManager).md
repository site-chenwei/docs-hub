---
title: "Interface (AudioStreamManager)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "ArkTS API"
  - "@ohos.multimedia.audio (音频管理)"
  - "Interface (AudioStreamManager)"
captured_at: "2026-04-17T01:48:35.967Z"
---

# Interface (AudioStreamManager)

音频流管理。

在使用AudioStreamManager的接口之前，需先通过[getStreamManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiomanager#getstreammanager9)获取AudioStreamManager实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/SssUhy8OTyqfFeHPwNkwNQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=E92F14196BB41031CB2FBB8A890FD5521A0873F634F59EB5A2C1360E5DA3F29F)

-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 9开始支持。

#### 导入模块

```ts
import { audio } from '@kit.AudioKit';
```

#### getCurrentAudioRendererInfoArray9+

getCurrentAudioRendererInfoArray(callback: AsyncCallback<AudioRendererChangeInfoArray>): void

获取当前音频渲染器的信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/5RRLI-BxQY2H7yxf47SuBQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=F220BE3A986841F4FC9D6686EE7CBBF17884D1BEBCB99AF4C78974DCC891D5C3)

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力**: SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioRendererChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiorendererchangeinfoarray9)\> | 是 | 回调函数。当获取当前音频渲染器的信息成功，err为undefined，data为获取到的当前音频渲染器的信息；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getCurrentAudioRendererInfoArray((err: BusinessError, audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  if (err) {
    console.error(`Failed to get current audio renderer info array. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
  }
});
```

#### getCurrentAudioRendererInfoArray9+

getCurrentAudioRendererInfoArray(): Promise<AudioRendererChangeInfoArray>

获取当前音频渲染器的信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/r7jWMLXBTNSWeptsxmIzXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=8EE3147F263B2A95CEA808D0BDCA7AE09113DCBC238CC8E6E16FF9895852F566)

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AudioRendererChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiorendererchangeinfoarray9)\> | Promise对象，返回当前音频渲染器信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getCurrentAudioRendererInfoArray().then((audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  console.info(`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get current audio renderer info array. Code: ${err.code}, message: ${err.message}`);
});
```

#### getCurrentAudioRendererInfoArraySync10+

getCurrentAudioRendererInfoArraySync(): AudioRendererChangeInfoArray

获取当前音频渲染器的信息。同步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/jILgb3m2S-ygLzDGDjFfXw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=57A12C95198BA0D0E3A2EF0E4A29D7D3857EB881E69ADCA34DFDB292E9A52F89)

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AudioRendererChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiorendererchangeinfoarray9) | 返回当前音频渲染器信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray = audioStreamManager.getCurrentAudioRendererInfoArraySync();
  console.info(`Succeeded in getting current audio renderer info array, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get current audio renderer info array. Code: ${error.code}, message: ${error.message}`);
}
```

#### getCurrentAudioCapturerInfoArray9+

getCurrentAudioCapturerInfoArray(callback: AsyncCallback<AudioCapturerChangeInfoArray>): void

获取当前音频采集器的信息。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/pIiaoAzyQwGles0Ht-AgkA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=DB84821E7BD26D614E4D8D01A4B388E524AF3728555B9018700DDD092BBCA00D)

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AudioCapturerChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiocapturerchangeinfoarray9)\> | 是 | 回调函数。当获取当前音频采集器的信息成功，err为undefined，data为获取到的当前音频采集器的信息；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getCurrentAudioCapturerInfoArray((err: BusinessError, audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) => {
  if (err) {
    console.error(`Failed to get current audio capturer info array. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
  }
});
```

#### getCurrentAudioCapturerInfoArray9+

getCurrentAudioCapturerInfoArray(): Promise<AudioCapturerChangeInfoArray>

获取当前音频采集器的信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/lDIHZpqOQvqylorkoBbuTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=85F50FA3E664FDAA5F6F5217747D0E2C9471FE683CB3C09923C86785A2CE5392)

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AudioCapturerChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiocapturerchangeinfoarray9)\> | Promise对象，返回当前音频采集器信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getCurrentAudioCapturerInfoArray().then((audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) => {
  console.info(`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get current audio capturer info array. Code: ${err.code}, message: ${err.message}`);
});
```

#### getCurrentAudioCapturerInfoArraySync10+

getCurrentAudioCapturerInfoArraySync(): AudioCapturerChangeInfoArray

获取当前音频采集器的信息。同步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/LYm1bUDHRQi_mrxBPL4oKg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=F58D0047E9BFEB40851E8991DEFCB4ADDB66CA682AE9DD1F11551A74DEBB5C79)

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AudioCapturerChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiocapturerchangeinfoarray9) | 返回当前音频采集器信息。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let audioCapturerChangeInfoArray = audioStreamManager.getCurrentAudioCapturerInfoArraySync();
  console.info(`Succeeded in getting current audio capturer info array, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get current audio capturer info array. Code: ${error.code}, message: ${error.message}`);
}
```

#### on('audioRendererChange')9+

on(type: 'audioRendererChange', callback: Callback<AudioRendererChangeInfoArray>): void

监听音频渲染器更改事件（当音频播放流状态变化或设备变化时触发）。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/8wy0cBVGSUGjGwSuPOlFxA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=FC9218E0560373E0DFD014F0D8689D42B503863EB7DD1A44F10732EEBB0EFF48)

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'audioRendererChange'，当音频播放流状态变化或设备变化时，触发该事件。 |
| callback | Callback<[AudioRendererChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiorendererchangeinfoarray9)\> | 是 | 回调函数，返回当前音频渲染器信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
audioStreamManager.on('audioRendererChange',  (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  console.info(`Succeeded in using on function, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
});
```

#### off('audioRendererChange')9+

off(type: 'audioRendererChange', callback?: Callback<AudioRendererChangeInfoArray>): void

取消监听音频渲染器更改事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/xl58w5SKQAG6OOmsnmIqMA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=3B64EC3F54CFA6C6F890283D63C85A26483D9202DE443B073F866B429DA6F26F)

该接口返回的音频渲染器信息，可能包含系统内部音频播放流，如蜂窝通话、超声波等。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'audioRendererChange'，当取消监听音频渲染器更改事件时，触发该事件。 |
| callback18+ | Callback<[AudioRendererChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiorendererchangeinfoarray9)\> | 否 | 回调函数，返回当前音频渲染器信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
// 当订阅了多个该事件的监听时，可通过 audioStreamManager.off('audioRendererChange'); 取消该事件的所有监听。
let audioRendererChangeCallback = (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
  console.info(`Succeeded in using on or off function, AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}.`);
};

audioStreamManager.on('audioRendererChange', audioRendererChangeCallback);

audioStreamManager.off('audioRendererChange', audioRendererChangeCallback);
```

#### on('audioCapturerChange')9+

on(type: 'audioCapturerChange', callback: Callback<AudioCapturerChangeInfoArray>): void

监听音频采集器更改事件（当音频录制流状态变化或设备变化时触发）。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ULGdOPIGRNqTB-Y9hby4iQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=F10BC2BFFEE8046D3045979C6B153C99FF85FA06BA3EE841719B85FE693641CF)

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'audioCapturerChange'，当音频录制流状态变化或设备变化时，触发该事件。 |
| callback | Callback<[AudioCapturerChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiocapturerchangeinfoarray9)\> | 是 | 回调函数，返回当前音频采集器信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
audioStreamManager.on('audioCapturerChange', (audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) =>  {
  console.info(`Succeeded in using on function, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
});
```

#### off('audioCapturerChange')9+

off(type: 'audioCapturerChange', callback?: Callback<AudioCapturerChangeInfoArray>): void

取消监听音频采集器更改事件。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/puurCOyCQtS_OTJsJv8gDw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=FA18DA1C0A6FE5F798C8DAF247F3C173C044321EECEE33C31BD121C830589562)

该接口返回的音频采集器信息，可能包含系统内部音频录制流，如语音唤醒、蜂窝通话等。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 事件回调类型，支持的事件为'audioCapturerChange'，当取消监听音频采集器更改事件时，触发该事件。 |
| callback18+ | Callback<[AudioCapturerChangeInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t#audiocapturerchangeinfoarray9)\> | 否 | 回调函数，返回当前音频采集器信息。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
// 同一监听事件中，on方法和off方法传入callback参数一致，off方法取消对应on方法订阅的监听。
// 当订阅了多个该事件的监听时，可通过 audioStreamManager.off('audioCapturerChange'); 取消该事件的所有监听。
let audioCapturerChangeCallback = (audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) =>  {
  console.info(`Succeeded in using on or off function, AudioCapturerChangeInfoArray: ${JSON.stringify(audioCapturerChangeInfoArray)}.`);
};

audioStreamManager.on('audioCapturerChange', audioCapturerChangeCallback);

audioStreamManager.off('audioCapturerChange', audioCapturerChangeCallback);
```

#### isActive(deprecated)

isActive(volumeType: AudioVolumeType, callback: AsyncCallback<boolean>): void

获取指定音频流活跃状态。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/gM2wKGqzSPuhM7bIRL0pXQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=17958CA080C0D39E5B71AB827E97F536FEFC7EEC016C3745E77C714544820450)

从API version 9开始支持，从API version 20开始废弃，建议使用[isStreamActive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频流类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当获取指定音频流活跃状态成功，err为undefined，data为true表示活跃，false表示不活跃；否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.isActive(audio.AudioVolumeType.MEDIA, (err: BusinessError, value: boolean) => {
if (err) {
  console.error(`Failed to obtain the active status of the stream. ${err}`);
  return;
}
  console.info(`Callback invoked to indicate that the active status of the stream is obtained ${value}.`);
});
```

#### isActive(deprecated)

isActive(volumeType: AudioVolumeType): Promise<boolean>

获取指定音频流是否为活跃状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/EQvX6JqtRp6F1Yr6J_FGcw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=FBE4577C8FE37A13CA0A20BF428A7B6BD99B5872F8111DCE05AC7EA4010DC20A)

从API version 9开始支持，从API version 20开始废弃，建议使用[isStreamActive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频流类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回true表示流状态为活跃；返回false表示流状态不活跃。 |

**示例：**

```ts
audioStreamManager.isActive(audio.AudioVolumeType.MEDIA).then((value: boolean) => {
  console.info(`Promise returned to indicate that the active status of the stream is obtained ${value}.`);
});
```

#### isActiveSync(deprecated)

isActiveSync(volumeType: AudioVolumeType): boolean

获取指定音频流是否为活跃状态。同步返回结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/xw7tGWuYROeJAZtuRiD0WQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=471D470A4C0CB04D80BF4E8257898FEC2D8BBC611539F1AC097B0D033C15E4EB)

从API version 10开始支持，从API version 20开始废弃，建议使用[isStreamActive](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#isstreamactive20)替代。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| volumeType | [AudioVolumeType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiovolumetype) | 是 | 音频流类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 流的活跃状态。返回true表示活跃，返回false表示不活跃。 |

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
  let value: boolean = audioStreamManager.isActiveSync(audio.AudioVolumeType.MEDIA);
  console.info(`Indicate that the active status of the stream is obtained ${value}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to obtain the active status of the stream ${error}.`);
}
```

#### isStreamActive20+

isStreamActive(streamUsage: StreamUsage): boolean

获取指定音频流是否为活跃状态。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| streamUsage | [StreamUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#streamusage) | 是 | 音频流使用类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 流是否处于活跃状态。返回true表示活跃，返回false表示不活跃。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isStreamActive = audioStreamManager.isStreamActive(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Succeeded in using isStreamActive function, IsStreamActive: ${isStreamActive}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to use isStreamActive function. code: ${error.code}, message: ${error.message}`);
}
```

#### getAudioEffectInfoArray10+

getAudioEffectInfoArray(usage: StreamUsage, callback: AsyncCallback<AudioEffectInfoArray>): void

获取当前音效模式的信息。使用callback异步回调。

**系统能力**: SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| usage | [StreamUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#streamusage) | 是 | 音频流使用类型。 |
| callback | AsyncCallback<[AudioEffectInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#getaudioeffectinfoarray10)\> | 是 | 回调函数。当获取当前音效模式的信息成功，err为undefined，data为获取到的当前音效模式的信息；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by callback. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getAudioEffectInfoArray(audio.StreamUsage.STREAM_USAGE_MUSIC, (err: BusinessError, audioEffectInfoArray: audio.AudioEffectInfoArray) => {
  if (err) {
    console.error(`Failed to get audio effect info array. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info(`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.`);
  }
});
```

#### getAudioEffectInfoArray10+

getAudioEffectInfoArray(usage: StreamUsage): Promise<AudioEffectInfoArray>

获取当前音效模式的信息。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| usage | [StreamUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#streamusage) | 是 | 音频流使用类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AudioEffectInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#getaudioeffectinfoarray10)\> | Promise对象，返回当前音效模式的信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2.Incorrect parameter types. |
| 6800101 | Parameter verification failed. Return by promise. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

audioStreamManager.getAudioEffectInfoArray(audio.StreamUsage.STREAM_USAGE_MUSIC).then((audioEffectInfoArray: audio.AudioEffectInfoArray) => {
  console.info(`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get audio effect info array. Code: ${err.code}, message: ${err.message}`);
});
```

#### getAudioEffectInfoArraySync10+

getAudioEffectInfoArraySync(usage: StreamUsage): AudioEffectInfoArray

获取当前音效模式的信息。同步返回结果。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| usage | [StreamUsage](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#streamusage) | 是 | 音频流使用类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AudioEffectInfoArray](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-audiostreammanager#getaudioeffectinfoarray10) | 返回当前音效模式的信息。 |

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
  let audioEffectInfoArray = audioStreamManager.getAudioEffectInfoArraySync(audio.StreamUsage.STREAM_USAGE_MUSIC);
  console.info(`Succeeded in getting effect info array, AudioEffectInfoArray: ${JSON.stringify(audioEffectInfoArray)}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to get audio effect info array. Code: ${error.code}, message: ${error.message}`);
}
```

#### isAcousticEchoCancelerSupported20+

isAcousticEchoCancelerSupported(sourceType: SourceType): boolean

查询指定的source type是否支持回声消除。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sourceType | [SourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8) | 是 | 音源类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 是否支持回声消除。true表示支持回声消除，false表示不支持回声消除。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isAcousticEchoCancelerSupported = audioStreamManager.isAcousticEchoCancelerSupported(audio.SourceType.SOURCE_TYPE_LIVE);
  console.info(`Succeeded in using isAcousticEchoCancelerSupported function, IsAcousticEchoCancelerSupported: ${isAcousticEchoCancelerSupported}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to use isAcousticEchoCancelerSupported function. code: ${error.code}, message: ${error.message}`);
}
```

#### isAudioLoopbackSupported20+

isAudioLoopbackSupported(mode: AudioLoopbackMode): boolean

查询当前系统是否支持指定的音频返听模式。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| mode | [AudioLoopbackMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioloopbackmode20) | 是 | 音频返听模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 是否支持指定的音频返听模式。true表示支持，false表示不支持。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isAudioLoopbackSupported = audioStreamManager.isAudioLoopbackSupported(audio.AudioLoopbackMode.HARDWARE);
  console.info(`Succeeded in using isAudioLoopbackSupported function, IsAudioLoopbackSupported: ${isAudioLoopbackSupported}.`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`Failed to use isAudioLoopbackSupported function. code: ${error.code}, message: ${error.message}`);
}
```

#### isRecordingAvailable20+

isRecordingAvailable(capturerInfo: AudioCapturerInfo): boolean

检查传入的音频采集器信息中音源类型的录制是否可以启动成功。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| capturerInfo | [AudioCapturerInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiocapturerinfo8) | 是 | 音频采集器信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 
代表录制是否可以启动成功。true表示成功，false表示失败。

仅检测是否可以获取音频采集器信息中音源类型的焦点。通常在音频录制启动前调用，否则已存在的录制流可能会拒绝其启动。

 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
  channels: audio.AudioChannel.CHANNEL_2,
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
};

let audioCapturerInfo: audio.AudioCapturerInfo = {
  source: audio.SourceType.SOURCE_TYPE_MIC,
  capturerFlags: 0
};

let audioCapturerOptions: audio.AudioCapturerOptions = {
  streamInfo: audioStreamInfo,
  capturerInfo: audioCapturerInfo
};

audio.createAudioCapturer(audioCapturerOptions, (err: BusinessError, audioCapturer: audio.AudioCapturer) => {
  if (err) {
    console.error(`Failed to create AudioCapturer. Code: ${err.code}, message: ${err.message}`);
  } else {
    console.info('Succeeded in creating AudioCapturer.');
    try {
      let isRecordingAvailable = audioStreamManager.isRecordingAvailable(audioCapturerInfo);
      console.info(`Succeeded in using isRecordingAvailable function, IsRecordingAvailable: ${isRecordingAvailable}.`);
    } catch (err) {
      let error = err as BusinessError;
      console.error(`Failed to use isRecordingAvailable function. code: ${error.code}, message: ${error.message}`);
    }
  }
});
```

#### isIntelligentNoiseReductionEnabledForCurrentDevice21+

isIntelligentNoiseReductionEnabledForCurrentDevice(sourceType: SourceType): boolean

查询指定的音源类型智能降噪开关是否打开。

**系统能力：** SystemCapability.Multimedia.Audio.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| sourceType | [SourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#sourcetype8) | 是 | 表示音源类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 智能降噪开关的状态。true表示打开，false表示关闭。 |

**错误码：**

以下错误码的详细介绍请参见[Audio错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-audio)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 6800101 | Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let isSupport = audioStreamManager.isIntelligentNoiseReductionEnabledForCurrentDevice(audio.SourceType.SOURCE_TYPE_LIVE);
  console.info(`SourceType: ${audio.SourceType.SOURCE_TYPE_LIVE} intelligent noise reduction enabled is: ${isSupport}`);
} catch (err) {
  let error = err as BusinessError;
  console.error(`isIntelligentNoiseReductionEnabledForCurrentDevice ERROR: ${error}`);
}
```
