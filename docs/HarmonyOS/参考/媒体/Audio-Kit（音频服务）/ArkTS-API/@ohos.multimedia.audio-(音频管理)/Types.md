---
title: "Types"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-t"
menu_path:
  - "参考"
  - "媒体"
  - "Audio Kit（音频服务）"
  - "ArkTS API"
  - "@ohos.multimedia.audio (音频管理)"
  - "Types"
captured_at: "2026-04-17T01:48:36.025Z"
---

# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/NbkUJNOwTui3H6yEeFMCsw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=348CA028397E7F4A0C6F4165FFA77DB32AFDEADB32A0406A3C070E9560E3F955)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### AudioRendererChangeInfoArray9+

type AudioRendererChangeInfoArray = Array<Readonly<AudioRendererChangeInfo>>

数组类型，AudioRendererChangeInfo数组，只读。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 类型 | 说明 |
| :-- | :-- |
| Array<Readonly<AudioRendererChangeInfo>> | 数组类型，[AudioRendererChangeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiorendererchangeinfo9)数组，只读。 |

#### AudioCapturerChangeInfoArray9+

type AudioCapturerChangeInfoArray = Array<Readonly<AudioCapturerChangeInfo>>

数组类型，AudioCapturerChangeInfo数组，只读。

**系统能力：** SystemCapability.Multimedia.Audio.Capturer

| 类型 | 说明 |
| :-- | :-- |
| Array<Readonly<AudioCapturerChangeInfo>> | 数组类型，[AudioCapturerChangeInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiocapturerchangeinfo9)数组，只读。 |

#### AudioEffectInfoArray10+

type AudioEffectInfoArray = Array<Readonly<AudioEffectMode>>

待查询ContentType和StreamUsage组合场景下的音效模式数组类型，[AudioEffectMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioeffectmode10)数组，只读。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

| 类型 | 说明 |
| :-- | :-- |
| Array<Readonly<AudioEffectMode>> | 待查询ContentType和StreamUsage组合场景下的音效模式数组类型，[AudioEffectMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audioeffectmode10)数组，只读。 |

#### AudioDeviceDescriptors

type AudioDeviceDescriptors = Array<Readonly<AudioDeviceDescriptor>>

设备属性数组类型，为[AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor)的数组，只读。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.Audio.Device

| 类型 | 说明 |
| :-- | :-- |
| Array<Readonly<AudioDeviceDescriptor>> | 设备属性数组类型，为[AudioDeviceDescriptor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-i#audiodevicedescriptor)的数组，只读。 |

#### AudioRendererWriteDataCallback12+

type AudioRendererWriteDataCallback = (data: ArrayBuffer) => AudioDataCallbackResult | void

回调函数类型，用于音频渲染器的数据写入，回调函数结束后，音频服务会把data指向的数据放入队列里等待播放，因此请勿在回调外再次更改data指向的数据, 且务必保证往data填满待播放数据, 否则会导致音频服务播放杂音。

**系统能力：** SystemCapability.Multimedia.Audio.Renderer

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | ArrayBuffer | 是 | 待写入缓冲区的数据。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [AudioDataCallbackResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-e#audiodatacallbackresult12) | void | 如果返回 void 或 AudioDataCallbackResult.VALID：表示数据有效，将播放音频数据；如果返回 AudioDataCallbackResult.INVALID：表示数据无效，且音频数据不播放。 |
