---
title: "Class (VerifyPinHandler)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-verifypinhandler"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS API"
  - "@ohos.web.webview (Webview)"
  - "Class (VerifyPinHandler)"
captured_at: "2026-04-17T01:48:12.030Z"
---

# Class (VerifyPinHandler)

Web组件返回的pin码认证用户处理功能对象。示例代码参考[onVerifyPin](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onverifypin22)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/nA9Al2YaT8yrPlhwjl5V2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=843040FE3426F221246372954FBC853A12C9B4615506FEAF20545DBA53F63BE6)

-   该组件从API version 22开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 22开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor22+

constructor()

VerifyPinHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### confirm22+

confirm(result: PinVerifyResult): void

通知Web组件PIN码认证结果。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| result | [PinVerifyResult](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#pinverifyresult22) | 是 | PIN码认证结果。 |
