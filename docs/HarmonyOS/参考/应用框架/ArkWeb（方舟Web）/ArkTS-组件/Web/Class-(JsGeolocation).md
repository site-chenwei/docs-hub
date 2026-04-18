---
title: "Class (JsGeolocation)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsgeolocation"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (JsGeolocation)"
captured_at: "2026-04-17T01:48:12.441Z"
---

# Class (JsGeolocation)

Web组件返回授权或拒绝权限功能的对象。示例代码参考[onGeolocationShow事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#ongeolocationshow)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/ndHaqm59RuOLzB0AcYgqtg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=81612ED1F1F3D534422DAC8A1B64F474F6A1BA3BB3C688CF0B2A9F4AF1A54981)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 8开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor

constructor()

JsGeolocation的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### invoke

invoke(origin: string, allow: boolean, retain: boolean): void

设置网页地理位置权限状态。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| origin | string | 是 | 指定源的字符串索引。 |
| allow | boolean | 是 | 
设置的地理位置权限状态。

true表示开启地理位置权限，false表示不开启地理位置权限。

 |
| retain | boolean | 是 | 

是否允许将地理位置权限状态保存到系统中。可通过[GeolocationPermissions9+](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-geolocationpermissions)接口管理保存到系统的地理位置权限。

true表示允许将地理位置权限状态保存到系统中，false表示不允许将地理位置权限状态保存到系统中。

 |
