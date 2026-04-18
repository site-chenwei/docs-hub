---
title: "Class (WebCookie)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcookie"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (WebCookie)"
captured_at: "2026-04-17T01:48:12.605Z"
---

# Class (WebCookie)

通过WebCookie可以控制Web组件中的cookie的各种行为，其中每个应用中的所有Web组件共享一个WebCookie。通过controller方法中的getCookieManager方法可以获取WebCookie对象，进行后续的cookie管理操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/aGuEH3ogRPubs9gYp91GWQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=8C776C5E4BE0698244B61AB882F63DD1B5115C71A162E99329E030145685D2AA)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 8开始支持。
    
-   从API version 8开始支持，从API version 23开始不再维护，建议使用[WebCookieManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager)代替。
    
-   示例效果请以真机运行为准。
    

#### constructor(deprecated)

constructor()

WebCookie的构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/tcZg2Du3Sta8EHPLbk1lKQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=BF58A0B5EA964095B7300E1688E2BAB2E523A581F66B299AFA2DBADAE0855FEE)

从API version 8开始支持，从API version 23开始废弃。且不再提供新的接口作为替代。

**系统能力：** SystemCapability.Web.Webview.Core

#### setCookie(deprecated)

setCookie()

设置cookie，该方法为同步方法。设置成功返回true，否则返回false。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/7bEswqdQQQGyVy5_MxCyKg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=53336C855722212771468A55031CC54110C25F36F00C32598614C5D9CBE5B9A2)

从API version 8开始支持，从API version 9开始废弃，建议使用[setCookie9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#setcookiedeprecated)代替。

**系统能力：** SystemCapability.Web.Webview.Core

#### saveCookie(deprecated)

saveCookie()

将当前存在内存中的cookie同步到磁盘中，该方法为同步方法。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/b5sP_cYAT_6xl1M3OCqGoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=AC1AF93B4C443A8AC94C048483B99325D989721A66C5CCC757C52F9015691789)

从API version 8开始支持，从API version 9开始废弃，建议使用[saveCookieAsync9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webcookiemanager#savecookieasync)代替。

**系统能力：** SystemCapability.Web.Webview.Core
