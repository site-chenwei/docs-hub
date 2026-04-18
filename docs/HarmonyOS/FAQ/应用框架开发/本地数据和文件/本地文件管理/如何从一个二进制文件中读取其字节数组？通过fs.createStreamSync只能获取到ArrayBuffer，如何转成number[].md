---
title: "如何从一个二进制文件中读取其字节数组？通过fs.createStreamSync只能获取到ArrayBuffer，如何转成number[]"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-28"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "本地数据和文件"
  - "本地文件管理"
  - "如何从一个二进制文件中读取其字节数组？通过fs.createStreamSync只能获取到ArrayBuffer，如何转成number[]"
captured_at: "2026-04-17T02:03:14.303Z"
---

# 如何从一个二进制文件中读取其字节数组？通过fs.createStreamSync只能获取到ArrayBuffer，如何转成number\[\]

@Component
export struct ArrayBufferConversionArray {
  @State fileLength: number = 10;
  private tempData: number\[\] = \[\];

  aboutToAppear(): void {
    // Convert ArrayBuffer to a number array
    let arrayBuffer: ArrayBuffer = new ArrayBuffer(this.fileLength);
    let dataView: DataView = new DataView(arrayBuffer);
    for (let index = 0; index < this.fileLength; index++) {
      this.tempData\[index\] = dataView.getInt8(index);
    }
    console.info(this.tempData.toString());
  }

  build() {
    RelativeContainer() {
      Text(this.tempData.toString())
        .id('ArrayBufferHelloWorld')
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
