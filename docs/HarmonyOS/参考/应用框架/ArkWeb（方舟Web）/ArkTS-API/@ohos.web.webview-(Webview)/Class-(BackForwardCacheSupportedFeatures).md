---
title: "Class (BackForwardCacheSupportedFeatures)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/kts-apis-webview-backforwardcachesupportedfeatures"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS API"
  - "@ohos.web.webview (Webview)"
  - "Class (BackForwardCacheSupportedFeatures)"
captured_at: "2026-04-17T01:48:11.555Z"
---

# Class (BackForwardCacheSupportedFeatures)

选择性允许使用以下特性的页面进入前进后退缓存。完整示例代码参考[enableBackForwardCache](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller#enablebackforwardcache12)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/vRmcN08rRfKXeW8zXpowSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014811Z&HW-CC-Expire=86400&HW-CC-Sign=3FA8BF0600663137EEE90DD2B01D4066881DBCFB97BE98F2D2D819F1B07BAD36)

-   本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   示例效果请以真机运行为准。
    

#### 属性

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| nativeEmbed12+ | boolean | 否 | 否 | 
是否允许使用同层渲染的页面进入前进后退缓存。

如果设置为允许，需要维护为同层渲染元素创建的系统控件的生命周期，避免造成泄漏。

true：允许使用同层渲染的页面进入前进后退缓存，false：不允许使用同层渲染的页面进入前进后退缓存。

默认值：false。

 |
| mediaTakeOver12+ | boolean | 否 | 否 | 

是否允许使用视频托管的页面进入前进后退缓存。

如果设置为允许，需要维护为视频元素创建的系统控件的生命周期，避免造成泄漏。

true：允许使用视频托管的页面进入前进后退缓存，false：不允许使用视频托管的页面进入前进后退缓存。

默认值：false。

 |

#### constructor12+

constructor()

BackForwardCacheSupportedFeatures的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core
