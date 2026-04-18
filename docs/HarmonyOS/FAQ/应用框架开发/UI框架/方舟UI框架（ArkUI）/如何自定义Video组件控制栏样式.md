---
title: "如何自定义Video组件控制栏样式"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-97"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "如何自定义Video组件控制栏样式"
captured_at: "2026-04-17T02:03:03.611Z"
---

# 如何自定义Video组件控制栏样式

1.  通过设置属性controls为false关闭默认控制栏。
2.  设置Video组件的controller。
3.  通过ArkTS实现自定义的控制栏，并通过VideoController控制视频播放。
    
    @Entry
    @Component
    struct VideoCreateComponent {
      @State videoSrc: Resource = $rawfile('xxx.mp4')
      @State previewUri: Resource = $r('app.media.xxx')
      @State curRate: PlaybackSpeed = PlaybackSpeed.Speed\_Forward\_1\_00\_X
      @State isAutoPlay: boolean = false
      @State showControls: boolean = true
      controller: VideoController = new VideoController()
    
      build() {
        Column() {
          Video({
            src: this.videoSrc,
            previewUri: this.previewUri,
            currentProgressRate: this.curRate,
            controller: this.controller
          })
            .width('100%')
            .height(600)
            .autoPlay(this.isAutoPlay)
            .controls(this.showControls)
            .onStart(() => {
              console.info('onStart')
            })
            .onPause(() => {
              console.info('onPause')
            })
            .onFinish(() => {
              console.info('onFinish')
            })
            .onError(() => {
              console.info('onError')
            })
            .onPrepared((e) => {
              console.info('onPrepared is ' + e.duration)
            })
            .onSeeking((e) => {
              console.info('onSeeking is ' + e.time)
            })
            .onSeeked((e) => {
              console.info('onSeeked is ' + e.time)
            })
            .onUpdate((e) => {
              console.info('onUpdate is ' + e.time)
            })
          Row() {
            Button('src').onClick(() => {
              this.videoSrc = $rawfile('xxx.mp4') // Switch video source
            }).margin(5)
            Button('previewUri').onClick(() => {
              this.previewUri = $r('app.media.xxx') // Switch video preview poster
            }).margin(5)
    
            Button('controls').onClick(() => {
                this.showControls = !this.showControls // Switch whether to display the video control bar
            }).margin(5)
          }
    
          Row() {
            Button('start').onClick(() => {
              this.controller.start() // 开始播放
            }).margin(5)
            Button('pause').onClick(() => {
              this.controller.pause() // 暂停播放
            }).margin(5)
            Button('stop').onClick(() => {
              this.controller.stop() // 结束播放
            }).margin(5)
            Button('setTime').onClick(() => {
              this.controller.setCurrentTime(10, SeekMode.Accurate) // Accurately jump to the 10s position of the video
            }).margin(5)
          }
    
          Row() {
            Button('rate 0.75').onClick(() => {
              this.curRate = PlaybackSpeed.Speed\_Forward\_0\_75\_X // 0.75 times playback speed
            }).margin(5)
            Button('rate 1').onClick(() => {
              this.curRate = PlaybackSpeed.Speed\_Forward\_1\_00\_X // Original speed playback
            }).margin(5)
            Button('rate 2').onClick(() => {
              this.curRate = PlaybackSpeed.Speed\_Forward\_2\_00\_X // Play at 2x speed
            }).margin(5)
          }
        }
      }
    }
    

**参考链接**

[Video](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-video-player)
