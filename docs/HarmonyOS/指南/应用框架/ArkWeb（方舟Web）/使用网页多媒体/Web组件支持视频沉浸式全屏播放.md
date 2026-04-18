---
title: "Web组件支持视频沉浸式全屏播放"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web_full_screen"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "使用网页多媒体"
  - "Web组件支持视频沉浸式全屏播放"
captured_at: "2026-04-17T01:35:42.657Z"
---

# Web组件支持视频沉浸式全屏播放

Web组件提供了视频进入全屏和退出全屏的事件功能，应用可通过监听这些事件实现进入和退出沉浸式全屏模式。

Web组件引用第三方H5页面加载的视频，当点击视频全屏时，视频仅扩展至整个Web组件区域，无法实现系统全屏显示（如图2所示）。若要达到系统全屏的沉浸式视频播放效果（如图3所示），则需应用监听进入全屏的事件并调整页面其他组件的属性。

| 图1 退出全屏模式 | 图2 非沉浸式全屏模式 | 图3 沉浸式全屏模式 |
| :-- | :-- | :-- |
| ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/bvDrArZuRKa3teH9w5jj-Q/zh-cn_image_0000002569018871.png?HW-CC-KV=V1&HW-CC-Date=20260417T013544Z&HW-CC-Expire=86400&HW-CC-Sign=89F776FD4F3EAE548DF0DEA007C237B6F7A6B82CBF443CA77C5FE71CA5DCB44E) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/OfiGaNqdRI2CfXzg1OO5Zg/zh-cn_image_0000002568898861.png?HW-CC-KV=V1&HW-CC-Date=20260417T013544Z&HW-CC-Expire=86400&HW-CC-Sign=8FDDB30952892767BA6C26064E05F3C9BA7B29D580D0F309EE38B44CC7E95BC4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/3bc7FqcoSlS3JOBB0S7w4A/zh-cn_image_0000002538019156.png?HW-CC-KV=V1&HW-CC-Date=20260417T013544Z&HW-CC-Expire=86400&HW-CC-Sign=5DE350D3C7C210BB4FDC5DC564A1A83A55AD4CB088A41E2CCDD9D0E937790B9C) |

Web组件可通过[onFullScreenEnter](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onfullscreenenter9)和[onFullScreenExit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onfullscreenexit9)回调监听全屏按键的点击事件。其中，onFullScreenEnter表示Web组件进入全屏模式，onFullScreenExit表示Web组件退出全屏模式。在这两个监听事件中，可根据具体业务场景调整某些全局变量，例如组件的显隐状态、组件的margin属性等，以实现退出和进入沉浸式全屏模式的页面效果，如图1和图3所示。

显隐控制[visibility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility#visibility)是ArkUI开发框架提供的组件通用属性。开发者可通过设置组件属性visibility的不同值，控制组件的显隐状态。

import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct ShortWebPage {
  controller: webview.WebviewController = new webview.WebviewController();
  CONSTANT\_HEIGHT = 100;
  @State marginTop: number = this.CONSTANT\_HEIGHT;
  @State isVisible: boolean = true; // 自定义标志位isVisible，来控制是否需要显示组件

  build() {
    Column() {
      Text('TextTextTextText')
        .width('100%')
        .height(this.CONSTANT\_HEIGHT)
        .backgroundColor('#e1dede') // 当isVisible标志位为true的时候，组件状态为可见，否则组件状态为不可见，不参与布局、不进行占位
        .visibility(this.isVisible ? Visibility.Visible :
          Visibility.None)
      Web({
        src: $rawfile('FullScreen.html'), // 示例网址
        controller: this.controller
      })
        .onFullScreenEnter((event) => {
          console.info('onFullScreenEnter...');
          // 当全屏的时候，isVisible标志位为false，组件状态为不可见，不参与布局、不进行占位
          this.isVisible = false;
        })
        .onFullScreenExit(() => {
          console.info('onFullScreenExit...');
          // 当退出全屏的时候，isVisible标志位为true，组件状态为可见
          this.isVisible = true;
        })
        .width('100%')
        .height('100%')
        .zIndex(10)
        .zoomAccess(true)
    }.width('100%').height('100%')
  }
}
