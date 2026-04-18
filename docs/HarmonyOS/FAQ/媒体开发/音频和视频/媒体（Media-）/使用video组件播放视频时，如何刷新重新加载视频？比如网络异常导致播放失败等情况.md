---
title: "使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-5"
menu_path:
  - "FAQ"
  - "媒体开发"
  - "音频和视频"
  - "媒体（Media ）"
  - "使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况"
captured_at: "2026-04-17T02:03:19.435Z"
---

# 使用video组件播放视频时，如何刷新重新加载视频？比如网络异常导致播放失败等情况

先将URL设置为空，再改回原来的值，示例代码如下：

@Component
export struct VideoErrorReload {
  @State url: string = 'https://\*\*\*\*\*\*';

  build() {
    Column({ space: 20 }) {
      Video({ src: this.url })
        .height(300)

      Button('重新url')
        .onClick(() => {
          let temp = this.url;
          this.url = '';
          setTimeout(() => {
            this.url = temp;
          }, 100);
        })
    }
  }
}
