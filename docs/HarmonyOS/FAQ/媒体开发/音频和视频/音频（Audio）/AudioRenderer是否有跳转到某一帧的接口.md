---
title: "AudioRenderer是否有跳转到某一帧的接口"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-7"
menu_path:
  - "FAQ"
  - "媒体开发"
  - "音频和视频"
  - "音频（Audio）"
  - "AudioRenderer是否有跳转到某一帧的接口"
captured_at: "2026-04-17T02:03:19.093Z"
---

# AudioRenderer是否有跳转到某一帧的接口

AudioRenderer底层不支持跳转到某一帧。AudioRenderer接口由客户端主动发送数据，完成后即开始播放。而AvPlayer支持跳转到某一帧，因为它有数据源，例如文件。可使用avPlayer.seek()方法跳转到指定播放位置，只能在prepared/playing/paused/completed状态调用。

let seekTime: number = 1000
avPlayer.seek(seekTime,media.SeekMode.SEEK\_PREV\_SYNC)

**参考链接**

[seek](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#seek9)
