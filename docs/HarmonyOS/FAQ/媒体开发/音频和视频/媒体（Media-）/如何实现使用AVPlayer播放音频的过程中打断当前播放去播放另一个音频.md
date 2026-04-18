---
title: "如何实现使用AVPlayer播放音频的过程中打断当前播放去播放另一个音频"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-3"
menu_path:
  - "FAQ"
  - "媒体开发"
  - "音频和视频"
  - "媒体（Media ）"
  - "如何实现使用AVPlayer播放音频的过程中打断当前播放去播放另一个音频"
captured_at: "2026-04-17T02:03:19.337Z"
---

# 如何实现使用AVPlayer播放音频的过程中打断当前播放去播放另一个音频

需要先调用[reset()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-media-avplayer#reset9)打断前一个音频，然后切换音频源。因为reset()是异步的，所以调用reset()的语句需加上await关键字。
