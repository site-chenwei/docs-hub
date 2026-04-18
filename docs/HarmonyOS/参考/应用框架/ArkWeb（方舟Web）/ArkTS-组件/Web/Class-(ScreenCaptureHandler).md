---
title: "Class (ScreenCaptureHandler)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-screencapturehandler"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (ScreenCaptureHandler)"
captured_at: "2026-04-17T01:48:12.509Z"
---

# Class (ScreenCaptureHandler)

Web组件返回授权或拒绝屏幕捕获功能的对象。示例代码参考[onScreenCaptureRequest事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onscreencapturerequest10)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/DuAEJcOYSMOYpU2YfaCFDA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=19400EB3163937279751F659A177872426E95F5DFC6C2524A017F7BD94F9E14F)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 10开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor10+

constructor()

ScreenCaptureHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### deny10+

deny(): void

拒绝网页所请求的屏幕捕获操作。

**系统能力：** SystemCapability.Web.Webview.Core

#### getOrigin10+

getOrigin(): string

获取网页来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 当前请求权限网页的来源。 |

#### grant10+

grant(config: ScreenCaptureConfig): void

对网页访问的屏幕捕获操作进行授权。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/0r6-Ip89QP6PQlSG7ZRFvA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=7D203A7D7DF8BBE31246DF74E4E24C458C04CDA7854FE8849DAB9E990C688157)

需要配置权限：ohos.permission.MICROPHONE。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| config | [ScreenCaptureConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#screencaptureconfig10) | 是 | 屏幕捕获配置。 |
