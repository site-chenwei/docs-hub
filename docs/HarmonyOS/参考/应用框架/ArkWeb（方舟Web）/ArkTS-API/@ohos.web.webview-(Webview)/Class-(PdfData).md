---
title: "Class (PdfData)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-pdfdata"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS API"
  - "@ohos.web.webview (Webview)"
  - "Class (PdfData)"
captured_at: "2026-04-17T01:48:11.620Z"
---

# Class (PdfData)

createPdf函数输出数据流类。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/wXV9Yt3QR2q-IZf1m163fA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=1D77837C90BC9F949B9DE774A6501A716896E0DA898EB26E5C631FB1EBE2B3C0)

-   本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 14开始支持。
    
-   示例效果请以真机运行为准。
    
-   在网页生成PDF过程中，返回的是数据流，由PdfData类封装。
    

#### pdfArrayBuffer14+

pdfArrayBuffer(): Uint8Array

获取网页生成的数据流。完整示例代码参考[createPdf](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#createpdf14)。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Uint8Array | 数据流。 |
