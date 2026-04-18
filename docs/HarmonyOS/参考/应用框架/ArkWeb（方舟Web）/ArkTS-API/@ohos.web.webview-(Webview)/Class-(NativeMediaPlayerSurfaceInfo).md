---
title: "Class (NativeMediaPlayerSurfaceInfo)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-nativemediaplayersurfaceinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS API"
  - "@ohos.web.webview (Webview)"
  - "Class (NativeMediaPlayerSurfaceInfo)"
captured_at: "2026-04-17T01:48:11.627Z"
---

# Class (NativeMediaPlayerSurfaceInfo)

[应用接管网页媒体播放功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-attributes#enablenativemediaplayer12)中用于同层渲染的 surface 信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/o-OzX_H8SCGwl5wS16OHEw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=7F86164A2398A67DD5ABF437022B3BBE24BC304459F888CAB7D3DBD5645065E1)

-   本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   示例效果请以真机运行为准。
    

#### 属性

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| id12+ | string | 否 | 否 | 
surface的id，用于同层渲染的NativeImage的psurfaceid。

详见[NativeEmbedDataInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-i#nativeembeddatainfo11)。

 |
| rect12+ | [RectEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-i#rectevent12) | 否 | 否 | surface的位置信息。 |
