---
title: "废弃的Interface (VideoPlayer, deprecated)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-videoplayer"
menu_path:
  - "参考"
  - "媒体"
  - "Media Kit（媒体服务）"
  - "ArkTS API"
  - "@ohos.multimedia.media (媒体服务)"
  - "废弃的Interface (VideoPlayer, deprecated)"
captured_at: "2026-04-17T01:48:43.335Z"
---

# 废弃的Interface (VideoPlayer, deprecated)

视频播放管理类，用于管理和播放视频媒体。在调用VideoPlayer的方法前，需要先通过[createVideoPlayer()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-f#mediacreatevideoplayerdeprecated)构建一个VideoPlayer实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/SHslaIotTVWNsAJxjSut_A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=91F431C233690DB19EF041C1CCB2D09BAC1C0C740542149FEA2D77FD66444F1C)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer)替代。

#### 导入模块

```ts
import { media } from '@kit.MediaKit';
```

#### 属性

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| url8+ | string | 否 | 否 | 
视频媒体URL，支持当前主流的视频格式(mp4、mpeg-ts、mkv)。

**支持路径示例**：

1\. fd类型播放：fd://xx

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/7GBYqbohQDeP_hq8jL7lMQ/zh-cn_image_0000002569021519.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=69EFF30DE992B0378382ED0B94EED7AFB6A5113DFFFD544A616EFA167B80BFE3)

2\. http网络播放: http://xx

3\. https网络播放: https://xx

4\. hls网络播放路径：http://xx或者https://xx

5\. file类型: file://xx

**说明：**

从API version 11开始不支持webm。

 |
| fdSrc9+ | [AVFileDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#avfiledescriptor9) | 否 | 否 | 

视频媒体文件描述，使用场景：应用中的视频资源被连续存储在同一个文件中。

**使用示例**：

假设一个连续存储的音乐文件:

视频1(地址偏移:0，字节长度:100)

视频2(地址偏移:101，字节长度:50)

视频3(地址偏移:151，字节长度:150)

1\. 播放视频1：AVFileDescriptor { fd = 资源句柄; offset = 0; length = 100; }

2\. 播放视频2：AVFileDescriptor { fd = 资源句柄; offset = 101; length = 50; }

3\. 播放视频3：AVFileDescriptor { fd = 资源句柄; offset = 151; length = 150; }

假设是一个独立的视频文件: 请使用src=fd://xx

 |
| loop8+ | boolean | 否 | 否 | 视频循环播放属性，设置为'true'表示循环播放。 |
| videoScaleType9+ | [VideoScaleType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#videoscaletype9) | 否 | 是 | 视频缩放模式。默认值为VIDEO\_SCALE\_TYPE\_FIT。 |
| audioInterruptMode9+ | [audio.InterruptMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#interruptmode9) | 否 | 是 | 音频焦点模式。 |
| currentTime8+ | number | 是 | 否 | 视频的当前播放位置，单位为毫秒（ms）。 |
| duration8+ | number | 是 | 否 | 视频时长，单位为毫秒（ms），返回-1表示直播模式。 |
| state8+ | [VideoPlayState](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-t#videoplaystatedeprecated) | 是 | 否 | 视频播放的状态。 |
| width8+ | number | 是 | 否 | 视频宽，单位为像素（px）。 |
| height8+ | number | 是 | 否 | 视频高，单位为像素（px）。 |

#### setDisplaySurface(deprecated)

setDisplaySurface(surfaceId: string, callback: AsyncCallback<void>): void

设置SurfaceId。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/Hv9DW8n1TByU-ond5HcfIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=DA2A61B9CD087B041D9ECAFEB222BC0E218400BA3B8478FBF1F5547EAE732804)

-   SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。
    
-   从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.surfaceId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#属性)替代。
    

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| surfaceId | string | 是 | 指定SurfaceId，应从XComponent组件获取，获取方式请参考[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置SurfaceId成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let surfaceId: string = '';
videoPlayer.setDisplaySurface(surfaceId, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set DisplaySurface!');
  } else {
    console.info('Succeeded in setting DisplaySurface!');
  }
});
```

#### setDisplaySurface(deprecated)

setDisplaySurface(surfaceId: string): Promise<void>

设置SurfaceId。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/OHYWDuHCQEC6qwPQbRsnzw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=D0B7A202E063EDF767E79828EDC8AB5D28E78859F76FC5168CBC6C8A4997FDF5)

-   SetDisplaySurface需要在设置url和Prepare之间，无音频的视频流必须设置Surface否则Prepare失败。
    
-   从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.surfaceId](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#属性)替代。
    

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| surfaceId | string | 是 | 指定SurfaceId，应从XComponent组件获取，获取方式请参考[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 设置SurfaceId的Promise返回值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let surfaceId: string = '';
videoPlayer.setDisplaySurface(surfaceId).then(() => {
  console.info('Succeeded in setting DisplaySurface');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### prepare(deprecated)

prepare(callback: AsyncCallback<void>): void

准备播放视频。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ReMGLPjETX275Ax60hVVGw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=221CDA7B917E7BC1B1787D7E398874131E2491453CAEA4E744656B5603612B6D)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.prepare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#prepare9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当准备播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare((err: BusinessError) => {
  if (err) {
    console.error('Failed to prepare!');
  } else {
    console.info('Succeeded in preparing!');
  }
});
```

#### prepare(deprecated)

prepare(): Promise<void>

准备播放视频。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/dFxFiDLMSFSPalnFUMSKRA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=748FC0E9262A496D8F85E4E6E7E47C4C87D642E6724EB9FFC2E7DFD500547829)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.prepare](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#prepare9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 准备播放视频的Promise返回值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.prepare().then(() => {
  console.info('Succeeded in preparing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### play(deprecated)

play(callback: AsyncCallback<void>): void

开始播放视频。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/K3J2ofMaRWi_aR7Lhci7Dw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=8162AFC9060446F0D8C340CF3A179E526B33DCD7EA87630BA77152390A0BFE8F)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.play](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#play9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当开始播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.play((err: BusinessError) => {
  if (err) {
    console.error('Failed to play!');
  } else {
    console.info('Succeeded in playing!');
  }
});
```

#### play(deprecated)

play(): Promise<void>

开始播放视频。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/64gK1dgxQ3Ka6_SmOcCcCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=E9BC28F21D6EC2555E1B999A5669EDE22EBBC8EFD63288257FBD115E346123F6)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.play](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#play9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 开始播放视频的Promise返回值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.play().then(() => {
  console.info('Succeeded in playing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### pause(deprecated)

pause(callback: AsyncCallback<void>): void

通过回调方式暂停播放视频。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/B-Wq8MKTRkOmJ5v12OYzWw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=2866EAF92996B80042A7424CA196BEB7F7FDCF21A7CD4941D7E2C535CE3C65EE)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.pause](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#pause9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当暂停播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause((err: BusinessError) => {
  if (err) {
    console.error('Failed to pause!');
  } else {
    console.info('Succeeded in pausing!');
  }
});
```

#### pause(deprecated)

pause(): Promise<void>

暂停播放视频。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/VTGoXwBNRkq_zQTWtpyBHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=903EC32CDF4931178773342A8EB98FF16CBF9EB9CA021CC137E5B7077207C188)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.pause](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#pause9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 暂停播放视频的Promise返回值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.pause().then(() => {
  console.info('Succeeded in pausing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### stop(deprecated)

stop(callback: AsyncCallback<void>): void

通过回调方式停止播放视频。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Fig9Xc7wSneYBhYyBqb20A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=2E84EC6E1967F52190AD0E962CCDEBF51E6FF25764E500CA1CAFC45393A4883C)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#stop9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当停止播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.stop((err: BusinessError) => {
  if (err) {
    console.error('Failed to stop!');
  } else {
    console.info('Succeeded in stopping!');
  }
});
```

#### stop(deprecated)

stop(): Promise<void>

停止播放视频。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/X5lF0sihSOKpY-yW3u7oPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=6CE05A9BCEE0AF291AB0093F5365816826CE2539625F8FF4DA05C352CFBF30D7)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.stop](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#stop9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 停止播放视频的Promise返回值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.stop().then(() => {
  console.info('Succeeded in stopping');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### reset(deprecated)

reset(callback: AsyncCallback<void>): void

重置播放视频。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/xiiEK6YYQOS1ZA1XVrX_zg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=8A3728D5C20DB9D8315531F81C1595EA7B32F539C56358FF695CA195E78C7ADF)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.reset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#reset9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当重置播放视频成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.reset((err: BusinessError) => {
  if (err) {
    console.error('Failed to reset!');
  } else {
    console.info('Succeeded in resetting!');
  }
});
```

#### reset(deprecated)

reset(): Promise<void>

重置播放视频。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/s-_y0afjR6ikJC1cBM4bnA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=81112B110650F3C60ACC5E19E14BCAC41E695A91B31D33675CCFDB9112FE73E7)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.reset](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#reset9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.reset().then(() => {
  console.info('Succeeded in resetting');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### seek(deprecated)

seek(timeMs: number, callback: AsyncCallback<number>): void

跳转到指定播放位置，默认跳转到指定时间点的上一个关键帧。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/Yq0virYxRs-TVcVgwnXXDA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=0056B3403F7C629F98BAAD1D4CAF7CB88E7549CF9F7734644D24CB115D73CCDE)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#seek9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为\[0, duration\]。 |
| callback | AsyncCallback<number> | 是 | 回调函数。跳转到指定播放位置成功时，err为undefined，data为获取到的跳转到的播放位置，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});

let seekTime: number = 5000;
videoPlayer.seek(seekTime, (err: BusinessError, result: number) => {
  if (err) {
    console.error('Failed to do seek!');
  } else {
    console.info('Succeeded in doing seek!');
  }
});
```

#### seek(deprecated)

seek(timeMs: number, mode:SeekMode, callback: AsyncCallback<number>): void

跳转到指定播放位置。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/hZL713GWSbegRW_uRJW-fw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=9DCAE52D88692838072E82FAF25615CB6914B0701C4A20840E6B350D88C88B51)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#seek9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为\[0, duration\]。 |
| mode | [SeekMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#seekmode8) | 是 | 跳转模式。 |
| callback | AsyncCallback<number> | 是 | 回调函数。跳转到指定播放位置成功时，err为undefined，data为获取到的跳转到的播放位置，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let seekTime: number = 5000;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK_NEXT_SYNC, (err: BusinessError, result: number) => {
    if (err) {
      console.error('Failed to do seek!');
    } else {
      console.info('Succeeded in doing seek!');
    }
  });
}
```

#### seek(deprecated)

seek(timeMs: number, mode?:SeekMode): Promise<number>

跳转到指定播放位置，如果没有设置mode则跳转到指定时间点的上一个关键帧。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/Jea_bYxDTzakaipzDr8izA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=6AF12C99D2360271D5FEB8E01151A86BC7AD03A500DD696B18D37A4EAAD522EA)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.seek](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#seek9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| timeMs | number | 是 | 指定的跳转时间节点，单位毫秒（ms），取值范围为\[0, duration\]。 |
| mode | [SeekMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#seekmode8) | 否 | 基于视频I帧的跳转模式，默认为SEEK\_PREV\_SYNC模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | 跳转到指定播放位置的Promise返回值，单位ms。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let seekTime: number = 5000;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).seek(seekTime).then((seekDoneTime: number) => { // seekDoneTime表示seek完成后的时间点。
    console.info('Succeeded in doing seek');
  }).catch((error: BusinessError) => {
    console.error(`video catchCallback, error:${error}`);
  });

  (videoPlayer as media.VideoPlayer).seek(seekTime, media.SeekMode.SEEK_NEXT_SYNC).then((seekDoneTime: number) => {
    console.info('Succeeded in doing seek');
  }).catch((error: BusinessError) => {
    console.error(`video catchCallback, error:${error}`);
  });
}
```

#### setVolume(deprecated)

setVolume(vol: number, callback: AsyncCallback<void>): void

设置音量。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/HMvTsPB_T7W8QlbGFuoogw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=E1E88DC633EA9E229CDB9817027A18E157D5FC55AE251CC21ADE732DBBF358A9)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.setVolume](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#setvolume9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| vol | number | 是 | 指定的相对音量大小，取值范围为\[0.00-1.00\]，1表示最大音量，即100%。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置音量成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let vol: number = 0.5;
videoPlayer.setVolume(vol, (err: BusinessError) => {
  if (err) {
    console.error('Failed to set Volume!');
  } else {
    console.info('Succeeded in setting Volume!');
  }
});
```

#### setVolume(deprecated)

setVolume(vol: number): Promise<void>

设置音量。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/0wYDW7ORQta7a-iW4aFnPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=66EB8FDBC5BAD88D68A121DEA04C8C1610E9DCC0F33AFBBAE62AFC6084B8ED83)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.setVolume](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#setvolume9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| vol | number | 是 | 指定的相对音量大小，取值范围为\[0.00-1.00\]，1表示最大音量，即100%。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 设置音量的Promise返回值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let vol: number = 0.5;
videoPlayer.setVolume(vol).then(() => {
  console.info('Succeeded in setting Volume');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### release(deprecated)

release(callback: AsyncCallback<void>): void

释放视频资源。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/_lX26KAdQBu8FAzb4CTI_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=3C7DFAD082632ACADEC45425C0B134BEABAC752A16E5F767A48AB23A11353AF2)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#release9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | 是 | 回调函数。当释放视频资源成功，err为undefined，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release((err: BusinessError) => {
  if (err) {
    console.error('Failed to release!');
  } else {
    console.info('Succeeded in releasing!');
  }
});
```

#### release(deprecated)

release(): Promise<void>

释放视频资源。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/ghkXgBLpSpiGBxw_yJCivA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=408140605D914D3608E7B5D0FAD0609DBD50625B0D51F33DBF79E73D4B00434B)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.release](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#release9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | 释放视频资源的Promise返回值。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.release().then(() => {
  console.info('Succeeded in releasing');
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### getTrackDescription(deprecated)

getTrackDescription(callback: AsyncCallback<Array<MediaDescription>>): void

获取视频轨道信息。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/58cZLuZXSuWvwPtz-AqAEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=FF4AF2106A6B8C248BDF8F095E14AD0F8D4C123406ADF95AA37B25284A38977C)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.getTrackDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#gettrackdescription9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[MediaDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#mediadescription8)\>> | 是 | 回调函数。获取视频轨道信息成功时，err为undefined，data为获取到的视频轨道信息MediaDescription数组，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
  if ((arrList) != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error(`Failed to get TrackDescription, error:${error}`);
  }
});
```

#### getTrackDescription(deprecated)

getTrackDescription(): Promise<Array<MediaDescription>>

获取视频轨道信息。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/UW05KZWNTg29-sn6HgYjAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=17B3C7D768B80C76FBE2562AC2F635F511BE8FBC3CCAD33C073010BBBF4F2649)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.getTrackDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#gettrackdescription9-1)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[MediaDescription](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#mediadescription8)\>> | Promise对象，返回获取的视频轨道信息MediaDescription数组。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.getTrackDescription().then((arrList: Array<media.MediaDescription>) => {
  if (arrList != null) {
    console.info('Succeeded in getting TrackDescription');
  } else {
    console.error('Failed to get TrackDescription');
  }
}).catch((error: BusinessError) => {
  console.error(`video catchCallback, error:${error}`);
});
```

#### setSpeed(deprecated)

setSpeed(speed: number, callback: AsyncCallback<number>): void

设置播放速度。通过回调函数获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/m2noSbtLTt-xC1QjVBYSXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=FD629DC48BF8AC867099014101B2BB08FB8D47987D06D29EDB8B274B208AEFA8)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.setSpeed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#setspeed9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| speed | number | 是 | 指定播放视频速度，具体见[PlaybackSpeed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#playbackspeed8)。 |
| callback | AsyncCallback<number> | 是 | 回调函数。设置播放速度成功时，err为undefined，data为设置的播放速度，否则为错误对象。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).setSpeed(speed, (err: BusinessError, result: number) => {
    if (err) {
      console.error('Failed to set Speed!');
    } else {
      console.info('Succeeded in setting Speed!');
    }
  });
}
```

#### setSpeed(deprecated)

setSpeed(speed: number): Promise<number>

设置播放速度。通过Promise获取返回值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/QrD8EB8xRpeZNzahnyUGZw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=E4582C34907823FD9006AF87E181EA8EB0786CF119819FA6D5825BDBEDB86A96)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.setSpeed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#setspeed9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| speed | number | 是 | 指定播放视频速度，具体见[PlaybackSpeed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#playbackspeed8)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回设置的播放速度，具体见[PlaybackSpeed](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#playbackspeed8)。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let videoPlayer: media.VideoPlayer | null = null;
media.createVideoPlayer((error: BusinessError, video: media.VideoPlayer) => {
  if (video != null) {
    videoPlayer = video;
    console.info('Succeeded in creating VideoPlayer');
  } else {
    console.error(`Failed to create VideoPlayer, error:${error}`);
  }
});
let speed = media.PlaybackSpeed.SPEED_FORWARD_2_00_X;
if (videoPlayer) {
  (videoPlayer as media.VideoPlayer).setSpeed(speed).then((result: number) => {
    console.info('Succeeded in setting Speed');
  }).catch((error: BusinessError) => {
    console.error(`Failed to set Speed, error:${error}`);// todo:: error.
  });
}
```

#### on('playbackCompleted')(deprecated)

on(type: 'playbackCompleted', callback: Callback<void>): void

开始监听视频播放完成事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/DTAkynJ0TROc169JneJfIw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=E6D551C731E69B36DF2B932F096104DA8233DCA4250F94BB84B4C4F0437A32DF)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('stateChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#onstatechange9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 视频播放完成事件回调类型，支持的事件：'playbackCompleted'。 |
| callback | Callback<void> | 是 | 视频播放完成事件回调方法。 |

**示例：**

```ts
videoPlayer.on('playbackCompleted', () => {
  console.info('playbackCompleted called!');
});
```

#### on('bufferingUpdate')(deprecated)

on(type: 'bufferingUpdate', callback: (infoType: BufferingInfoType, value: number) => void): void

开始监听视频缓存更新事件。仅网络播放支持该订阅事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/OmHsKCXRQWiPc8rbH5uLpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=794B54A4D87ADC9A994B4C995E028EADD32CB66071C04C27815BBAB7F9A77E63)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('bufferingUpdate')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#onbufferingupdate9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 视频缓存事件回调类型，支持的事件：'bufferingUpdate'。 |
| callback | function | 是 | 
视频缓存事件回调方法。

[BufferingInfoType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-e#bufferinginfotype8)value值固定为0。

 |

**示例：**

```ts
videoPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
  console.info('video bufferingInfo type: ' + infoType);
  console.info('video bufferingInfo value: ' + value);
});
```

#### on('startRenderFrame')(deprecated)

on(type: 'startRenderFrame', callback: Callback<void>): void

开始监听视频播放首帧送显上报事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/d7XEB4z0QzKIvcu6aKNwEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=2F3CC92BFE2A66968C099271DDFF328A20DF312AB1C0C408FA238FF24291A915)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('startRenderFrame')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#onstartrenderframe9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 视频播放首帧送显上报事件回调类型，支持的事件：'startRenderFrame'。 |
| callback | Callback<void> | 是 | 视频播放首帧送显上报事件回调方法。 |

**示例：**

```ts
videoPlayer.on('startRenderFrame', () => {
  console.info('startRenderFrame called!');
});
```

#### on('videoSizeChanged')(deprecated)

on(type: 'videoSizeChanged', callback: (width: number, height: number) => void): void

开始监听视频播放宽高变化事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/2UGEWTEXQpmIK6z-pG6Mpg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=7FC0256753DD1C43BED196373CD7A119738C781A294F3774ED01DD85668A8D9E)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('videoSizeChange')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#onvideosizechange9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 视频播放宽高变化事件回调类型，支持的事件：'videoSizeChanged'。 |
| callback | function | 是 | 视频播放宽高变化事件回调方法，width表示宽，height表示高。 |

**示例：**

```ts
videoPlayer.on('videoSizeChanged', (width: number, height: number) => {
  console.info('video width is: ' + width);
  console.info('video height is: ' + height);
});
```

#### on('audioInterrupt')(deprecated)

on(type: 'audioInterrupt', callback: (info: audio.InterruptEvent) => void): void

监听音频焦点变化事件，参考[audio.InterruptEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#interruptevent9)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/KlIoBKoTRYyviJVxVpciJQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=C8C894F26A373095B18B0D10F6AD87264057C2409B1BAC4BA7FC224B1B6B6FDD)

从API version 9开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('audioInterrupt')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#onaudiointerrupt9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 音频焦点变化事件回调类型，支持的事件：'audioInterrupt'。 |
| callback | function | 是 | 音频焦点变化事件回调方法。 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

videoPlayer.on('audioInterrupt', (info: audio.InterruptEvent) => {
  console.info('audioInterrupt called,and InterruptEvent info is:' + info);
});
```

#### on('error')(deprecated)

on(type: 'error', callback: ErrorCallback): void

开始监听视频播放错误事件，当上报error错误事件后，用户需处理error事件，退出播放操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/cok-PJVfTbqPqkvrFnuCVQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014845Z&HW-CC-Expire=86400&HW-CC-Sign=F101E9A42AE86A7677F007A77E0C83A6A6D1BB60AC602136ED5EEF9B2FCAB869)

从API version 8开始支持，从API version 9开始废弃，建议使用[AVPlayer.on('error')](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#onerror9)替代。

**系统能力：** SystemCapability.Multimedia.Media.VideoPlayer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 
播放错误事件回调类型，支持的事件包括：'error'。

\- 'error'：视频播放中发生错误，触发该事件。

 |
| callback | [ErrorCallback](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-base#errorcallback) | 是 | 播放错误事件回调方法。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

videoPlayer.on('error', (error: BusinessError) => {  // 设置'error'事件回调。
  console.error(`video error called, error: ${error}`);
});
videoPlayer.url = 'fd://error';  // 设置错误的播放地址，触发'error'事件。
```
