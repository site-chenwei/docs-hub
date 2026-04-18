---
title: "如何在AVRecorder录制WAV格式的音频文件时正确配置AVRecorderProfile参数"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-20"
menu_path:
  - "FAQ"
  - "媒体开发"
  - "音频和视频"
  - "音频（Audio）"
  - "如何在AVRecorder录制WAV格式的音频文件时正确配置AVRecorderProfile参数"
captured_at: "2026-04-17T02:03:19.288Z"
---

# 如何在AVRecorder录制WAV格式的音频文件时正确配置AVRecorderProfile参数

**问题现象**

使用AVRecorder录制WAV格式音频时，发生异常错误。

**问题原因**

AVRecorderProfile参数配置错误，WAV格式需要匹配相应的比特率、声道数、编码格式、采样率和封装格式。

**解决措施**

给[AVRecorderProfile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-i#avrecorderprofile9)配置相应的比特率、声道数、编码格式、采样率和封装格式。

private avProfile: media.AVRecorderProfile = {
  audioBitrate: 64000, // set audioBitrate according to device ability.
  audioChannels: 1, // set audioChannels,valid value 1-8,CFT\_WAV supports 1.
  audioCodec: media.CodecMimeType.AUDIO\_G711MU, // set audioCodec,AUDIO\_G711MU matching CFT\_WAV.
  audioSampleRate: 8000, // set audioSampleRate according to device ability.
  fileFormat: media.ContainerFormatType.CFT\_WAV // set fileFormat,CFT\_WAV.
}
