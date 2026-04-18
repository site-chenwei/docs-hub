---
title: "废弃的Interface (AudioRecorder, deprecated)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-audiorecorder"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "ArkTS API"
  - "@ohos.multimedia.media (媒体服务)"
  - "废弃的Interface (AudioRecorder, deprecated)"
captured_at: "2026-04-17T01:48:43.291Z"
---

# 废弃的Interface (AudioRecorder, deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/8-Iy5QI5S_-010nyWrWUPA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=8D41351A0F6F6045DA613AE43351497E044F7B023BDBB75FF749A17319F7FA3B)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder)替代。

音频录制管理类，用于录制音频媒体。在调用AudioRecorder的方法前，需要先通过[createAudioRecorder()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreateaudiorecorderdeprecated) 构建一个AudioRecorder实例。

#### 导入模块

```ts
import { media } from '@kit.MediaKit';
```

#### prepare(deprecated)

prepare(config: AudioRecorderConfig): void

录音准备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/oCvsyyDpQUC_Vr-hoMPytA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=5F86C264152B218063B7ADA5DEE6F4DF6E8E149A521A441DD35E790476DAC52E)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.prepare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#prepare9)替代。

**需要权限：** ohos.permission.MICROPHONE

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [AudioRecorderConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#audiorecorderconfigdeprecated) | 是 | 配置录音的相关参数，包括音频输出URI、编码格式、采样率、声道数、输出格式等。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 201 | permission denied |

**示例：**

```ts
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://1',       // 文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130},
};
audioRecorder.on('prepare', () => {    // 设置'prepare'事件回调。
  console.info('prepare called');
});
audioRecorder.prepare(audioRecorderConfig);
```

#### start(deprecated)

start(): void

开始录制，需在'prepare'事件成功触发后，才能调用start方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/20PT5iC8SWaCm_Hh3YTZhA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=4E0FAAB0C3EF83505379157C31ED5B9A795171254641A06EB570404960BB7C82)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.start](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#start9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('start', () => {    // 设置'start'事件回调。
  console.info('audio recorder start called');
});
audioRecorder.start();
```

#### pause(deprecated)

pause():void

暂停录制，需要在'start'事件成功触发后，才能调用pause方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/hxtkQ5CURyaKS69R0toVHQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=0E135E23A040C3B8E1A45933A3FE3E4461F5299C27D02859054B380C10F68708)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.pause](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#pause9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('pause', () => {    // 设置'pause'事件回调。
  console.info('audio recorder pause called');
});
audioRecorder.pause();
```

#### resume(deprecated)

resume():void

恢复录制，需要在'pause'事件成功触发后，才能调用resume方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/t_4gXtpkRWCWdyKuJD_meQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=1E4BCEDE9A21CA02548BD31919BE0282A40E72163A095617C96439AA8F600A66)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.resume](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#resume9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('resume', () => {    // 设置'resume'事件回调。
  console.info('audio recorder resume called');
});
audioRecorder.resume();
```

#### stop(deprecated)

stop(): void

停止录音。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/CQYlFk2uSwyp5NN-WTK2Cg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=F72756DC869CB38D77AD6F82207EA29652C9643D80A98D2C39231C2E6449ADF3)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#stop9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('stop', () => {    // 设置'stop'事件回调。
  console.info('audio recorder stop called');
});
audioRecorder.stop();
```

#### release(deprecated)

release(): void

释放录音资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/WNo0Z_F3TC-wg677HYEt8A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=9B7CA11630ADFD43250ADA2B3783E0F3C50CC18460E389DD8DD20160EEBF0E49)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#release9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('release', () => {    // 设置'release'事件回调。
  console.info('audio recorder release called');
});
audioRecorder.release();
audioRecorder = undefined;
```

#### reset(deprecated)

reset(): void

重置录音。

进行重置录音之前，需要先调用stop()停止录音。重置录音之后，需要调用prepare()设置录音参数项，才能再次进行录音。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/HEHQeMblRNGnh-V6_axhmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=B2D1944D2BCF1529507AFBC2A6493E4448FDE5624295D1CA3870D4DE8D1DA380)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.reset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#reset9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**示例：**

```ts
audioRecorder.on('reset', () => {    // 设置'reset'事件回调。
  console.info('audio recorder reset called');
});
audioRecorder.reset();
```

#### on('prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset')(deprecated)

on(type: 'prepare' | 'start' | 'pause' | 'resume' | 'stop' | 'release' | 'reset', callback: () => void): void

开始订阅音频录制事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/CRnQeenLRhCOhyo4swtYuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=EFD9C25DBEFD269B5AEAB4B877DF0F3FA638F96C208B129E90B373A75B768E33)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.on('stateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#onstatechange9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
录制事件回调类型，支持的事件包括：'prepare' | 'start' | 'pause' | ’resume‘ | 'stop' | 'release' | 'reset'。

\- 'prepare' ：完成prepare调用，音频录制参数设置完成，触发该事件。

\- 'start' ：完成start调用，音频录制开始，触发该事件。

\- 'pause': 完成pause调用，音频暂停录制，触发该事件。

\- 'resume': 完成resume调用，音频恢复录制，触发该事件。

\- 'stop' ：完成stop调用，音频停止录制，触发该事件。

\- 'release' ：完成release调用，音频释放录制资源，触发该事件。

\- 'reset'：完成reset调用，音频重置为初始状态，触发该事件。

 |
| callback | ()=>void | 是 | 录制事件回调方法。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let audioRecorder: media.AudioRecorder = media.createAudioRecorder();  // 创建一个音频录制实例。
let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 64000,
  audioSampleRate : 44100,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://xx',  // 文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130}
};
audioRecorder.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
  console.error(`audio error called, error: ${error}`);
});
audioRecorder.on('prepare', () => {  // 设置'prepare'事件回调。
  console.info('prepare called');
  audioRecorder.start();  // 开始录制，并触发'start'事件回调。
});
audioRecorder.on('start', () => {  // 设置'start'事件回调。
  console.info('audio recorder start called');
});
audioRecorder.on('pause', () => {  // 设置'pause'事件回调。
  console.info('audio recorder pause called');
});
audioRecorder.on('resume', () => {  // 设置'resume'事件回调。
  console.info('audio recorder resume called');
});
audioRecorder.on('stop', () => {  // 设置'stop'事件回调。
  console.info('audio recorder stop called');
});
audioRecorder.on('release', () => {  // 设置'release'事件回调。
  console.info('audio recorder release called');
});
audioRecorder.on('reset', () => {  // 设置'reset'事件回调。
  console.info('audio recorder reset called');
});
audioRecorder.prepare(audioRecorderConfig)  // 设置录制参数 ，并触发'prepare'事件回调。
```

#### on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

开始订阅音频录制错误事件，当上报error错误事件后，用户需处理error事件，退出录制操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/Wl9CbnF8TA6ioUc21PSIuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=3D60077DAF02FC2E7B7C971F72AD7388020EB2C33A3ED82FFBBEC578854E3AEE)

从API version 6开始支持，从API version 9开始废弃，建议使用[AVRecorder.on('error')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avrecorder#onerror9)替代。

**系统能力：** SystemCapability.Multimedia.Media.AudioRecorder

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
录制错误事件回调类型'error'。

\- 'error'：音频录制过程中发生错误，触发该事件。

 |
| callback | [ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback) | 是 | 录制错误事件回调方法。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let audioRecorderConfig: media.AudioRecorderConfig = {
  audioEncoder : media.AudioEncoder.AAC_LC,
  audioEncodeBitRate : 22050,
  audioSampleRate : 22050,
  numberOfChannels : 2,
  format : media.AudioOutputFormat.AAC_ADTS,
  uri : 'fd://xx',   // 文件需先由调用者创建，并给予适当的权限。
  location : { latitude : 30, longitude : 130}
};
audioRecorder.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
  console.error(`audio error called, error: ${error}`);
});
audioRecorder.prepare(audioRecorderConfig);  // prepare不设置参数，触发'error'事件。
```
