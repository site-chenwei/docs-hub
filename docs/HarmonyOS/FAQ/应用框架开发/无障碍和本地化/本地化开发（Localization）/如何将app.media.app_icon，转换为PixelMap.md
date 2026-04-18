---
title: "如何将app.media.app_icon，转换为PixelMap"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-9"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "无障碍和本地化"
  - "本地化开发（Localization）"
  - "如何将app.media.app_icon，转换为PixelMap"
captured_at: "2026-04-17T02:03:15.144Z"
---

# 如何将app.media.app\_icon，转换为PixelMap

使用getMediaContent获取媒体文件内容。使用createPixelMap创建PixelMap。

参考代码如下：

import { image } from '@kit.ImageKit';

@Entry
@Component
struct Index {
  @State pixelMap: PixelMap | null = null;

  convert() {
    try {
      // Byte array of media files
      this.getUIContext().getHostContext()!.resourceManager.getMediaContent($r('app.media.startIcon').id,
        (error: BusinessError, value: Uint8Array) => {
          if (error) {
            console.error(\`getMediaContent failed: ${error.code}, ${error.message}\`);
            return;
          }
          let pixelMapInitOptions: image.InitializationOptions = {
            editable: true,
            pixelFormat: 3,
            size: { height: 4, width: 6 }
          };
          // Create an imageSource instance
          let imageSource = image.createImageSource(value.buffer);
          // Decoding to generate PixelMap
          imageSource.createPixelMap(pixelMapInitOptions).then((pixelMap) => {
            this.pixelMap = pixelMap;
            // Pixel operations or rendering can be performed here.
          }).catch((decodeError: BusinessError) => {
            console.error(\`Decode failed: ${decodeError.code}, ${decodeError.message}\`);
          });
        });
    } catch (error) {
      console.error(\`Global error: ${error.code}, ${error.message}\`);
    }
  }

  build() {
    Column() {
      Button('Click to convert')
        .onClick(() => {
          this.convert();
        })
        .margin({ bottom: 16 })
      Image(this.pixelMap)
    }
    .padding(16)
  }
}

**参考链接**

[getMediaContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager#getmediacontent9)

[image.createPixelMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmap8)
