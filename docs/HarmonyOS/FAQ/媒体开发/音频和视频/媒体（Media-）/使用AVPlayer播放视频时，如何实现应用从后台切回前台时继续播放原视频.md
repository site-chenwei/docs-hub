---
title: "使用AVPlayer播放视频时，如何实现应用从后台切回前台时继续播放原视频"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-4"
menu_path:
  - "FAQ"
  - "媒体开发"
  - "音频和视频"
  - "媒体（Media ）"
  - "使用AVPlayer播放视频时，如何实现应用从后台切回前台时继续播放原视频"
captured_at: "2026-04-17T02:03:19.389Z"
---

# 使用AVPlayer播放视频时，如何实现应用从后台切回前台时继续播放原视频

在切换到前台的生命周期方法onPageShow()里调用AVPlayer的播放方法[avPlayer.play()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#play9)，并在切换到后台的生命周期方法onPageHide()里调用AVPlayer的暂停方法[avPlayer.pause()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#pause9)即可。
