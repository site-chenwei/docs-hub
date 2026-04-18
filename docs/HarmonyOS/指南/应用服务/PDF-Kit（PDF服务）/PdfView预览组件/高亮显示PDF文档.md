---
title: "高亮显示PDF文档"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pdf-pdfview-highlight"
menu_path:
  - "指南"
  - "应用服务"
  - "PDF Kit（PDF服务）"
  - "PdfView预览组件"
  - "高亮显示PDF文档"
captured_at: "2026-04-17T01:36:20.570Z"
---

# 高亮显示PDF文档

PDF文档在预览时，可以对页面的矩形区域或文本设置高亮显示，高亮颜色可以自定义。

[setHighlightText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#sethighlighttext)可以同时高亮多个不同的文本。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/Ocq6Tce-SgSJdz-ZoTEc9g/zh-cn_image_0000002538020048.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T013622Z&HW-CC-Expire=86400&HW-CC-Sign=C232FDBBE7D53BAA11016969960598B48A6661DE54C03E3C4FF5CF8EA4D397BA)

#### 接口说明

| 接口名 | 描述 |
| :-- | :-- |
| [setHighlightText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#sethighlighttext)(pageIndex: number, textArray: string\[\], color: number): void | 高亮指定文本。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/kVGVo6PRTm-p9WrGAYPaQw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013622Z&HW-CC-Expire=86400&HW-CC-Sign=50BDA90AD7ABF3AF80D89B36509434BFAE44B43315FABB84F10778005F786F98)

[setHighlightText](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#sethighlighttext)和[searchKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/pdf-arkts-pdfviewmanage#searchkey)功能互斥。

#### 示例代码

1.  加载PDF文档。
    
2.  调用PdfView预览组件，渲染显示。
    
3.  在按钮【setHighlightText】里，调用setHighlightText方法，设置单个或多个要高亮的文本。
    

```typescript
import { pdfService, PdfView, pdfViewManager } from '@kit.PDFKit';

@Entry
@Component
struct PdfPage {
  private controller: pdfViewManager.PdfController = new pdfViewManager.PdfController();
  private context = this.getUIContext().getHostContext() as Context;
  private loadResult: pdfService.ParseResult = pdfService.ParseResult.PARSE_ERROR_FORMAT;

  aboutToAppear(): void {
    // 确保沙箱目录有input.pdf文档
    let filePath = this.context.filesDir + '/input.pdf';
    (async () => {
      this.loadResult = await this.controller.loadDocument(filePath);
    })()
  }

  build() {
    Column() {
      Row() {
        // 设置文本的高亮显示风格
        Button('setHighlightText').onClick(async () => {
          if (this.loadResult === pdfService.ParseResult.PARSE_SUCCESS) {
            this.controller.setHighlightText(0, ['白皮书'], 0xAAF9CC00);
          }
        })
      }

      // 加载PdfView组件进行预览
      PdfView({
        controller: this.controller,
        pageFit: pdfService.PageFit.FIT_WIDTH,
        showScroll: true
      })
        .id('pdfview_app_view')
        .layoutWeight(1);
    }
    .width('100%').height('100%')
  }
}
```
