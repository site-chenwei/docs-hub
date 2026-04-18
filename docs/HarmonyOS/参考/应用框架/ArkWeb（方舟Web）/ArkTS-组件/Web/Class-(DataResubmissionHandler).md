---
title: "Class (DataResubmissionHandler)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-dataresubmissionhandler"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (DataResubmissionHandler)"
captured_at: "2026-04-17T01:48:12.329Z"
---

# Class (DataResubmissionHandler)

通过DataResubmissionHandler可以重新提交表单数据或取消提交表单数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/T2idNL0WQtSwX86N-VeGVA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=F9F10D7F2FFD16E6396F8E7A92F3C883AA2E7336601A9B1854A4A779E3E34808)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 9开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor9+

constructor()

DataResubmissionHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### resend9+

resend(): void

重新发送表单数据。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onDataResubmitted((event) => {
          console.info('onDataResubmitted');
          event.handler.resend();
        })
    }
  }
}
```

#### cancel9+

cancel(): void

取消重新发送表单数据。

**系统能力：** SystemCapability.Web.Webview.Core

**示例：**

```ts
// xxx.ets
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  controller: webview.WebviewController = new webview.WebviewController();

  build() {
    Column() {
      Web({ src: 'www.example.com', controller: this.controller })
        .onDataResubmitted((event) => {
          console.info('onDataResubmitted');
          event.handler.cancel();
        })
    }
  }
}
```
