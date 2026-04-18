---
title: "Constants"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-c"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "ArkTS API"
  - "@ohos.multimedia.audio (音频管理)"
  - "Constants"
captured_at: "2026-04-17T01:48:36.003Z"
---

# Constants

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/cRVz9c_BTZqW4NtIls5ybQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=3AEC6B8803F1AFB74746AE57D265A98DB96672664673D3CFC195208ED6D2378E)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

| 名称 | 类型 | 只读 | 说明 |
| :-- | :-- | :-- | :-- |
| DEFAULT\_VOLUME\_GROUP\_ID9+ | number | 是 | 
默认音量组id。

**系统能力：** SystemCapability.Multimedia.Audio.Volume

 |
| DEFAULT\_INTERRUPT\_GROUP\_ID9+ | number | 是 | 

默认音频中断组id。

**系统能力：** SystemCapability.Multimedia.Audio.Interrupt

 |

**示例：**

```ts
import { audio } from '@kit.AudioKit';

const defaultVolumeGroupId = audio.DEFAULT_VOLUME_GROUP_ID;
const defaultInterruptGroupId = audio.DEFAULT_INTERRUPT_GROUP_ID;
```
