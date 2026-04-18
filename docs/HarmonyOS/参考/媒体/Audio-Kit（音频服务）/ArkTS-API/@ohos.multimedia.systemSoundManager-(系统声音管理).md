---
title: "@ohos.multimedia.systemSoundManager (系统声音管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-systemsoundmanager"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "ArkTS API"
  - "@ohos.multimedia.systemSoundManager (系统声音管理)"
captured_at: "2026-04-17T01:48:36.096Z"
---

# @ohos.multimedia.systemSoundManager (系统声音管理)

系统声音管理提供管理系统声音的基础能力，包括对系统音效类型的定义、获取系统音效播放器等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/tkJyHOwTRGim84AVXTZYOg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=16E179BD89FC67BB55D4C5E9CE03CA1CB5B3CF6952E6FC1E7061BBDE3F8A1AF6)

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { systemSoundManager } from '@kit.AudioKit';
```

#### SystemSoundType

枚举，表示系统音效类型。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| PHOTO\_SHUTTER | 0 | 拍照音效。 |
| VIDEO\_RECORDING\_BEGIN | 1 | 视频录制开始音效。 |
| VIDEO\_RECORDING\_END | 2 | 视频录制结束音效。 |

#### systemSoundManager.createSystemSoundPlayer

createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>

创建系统音效播放器对象。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[SystemSoundPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-systemsoundplayer#systemsoundplayer) | null> | 成功返回系统音效播放器对象，失败返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-media)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 5400101 | No memory. Return by promise. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let systemSoundPlayer: systemSoundManager.SystemSoundPlayer | null = null;

systemSoundManager.createSystemSoundPlayer().then((systemSoundPlayerInstance) => {
  console.info('Succeeded in creating the system sound player.');
  systemSoundPlayer = systemSoundPlayerInstance;
}).catch((err: BusinessError) => {
  console.error(`Failed to create the system sound player. Code: ${err.code}, message: ${err.message}`);
});
```

#### SystemSoundPlayer

type SystemSoundPlayer = \_SystemSoundPlayer

系统音效播放器对象。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

| 类型 | 说明 |
| :-- | :-- |
| [\_SystemSoundPlayer](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-systemsoundplayer#systemsoundplayer) | 系统音效播放器对象。 |
