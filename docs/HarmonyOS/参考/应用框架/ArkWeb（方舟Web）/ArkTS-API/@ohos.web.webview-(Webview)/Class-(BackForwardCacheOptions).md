---
title: "Class (BackForwardCacheOptions)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-backforwardcacheoptions"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS API"
  - "@ohos.web.webview (Webview)"
  - "Class (BackForwardCacheOptions)"
captured_at: "2026-04-17T01:48:11.516Z"
---

# Class (BackForwardCacheOptions)

前进后退缓存相关设置对象，用来控制Web组件前进后退缓存相关选项。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/mzynH__MTFmmdxBuaTm59A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014811Z&HW-CC-Expire=86400&HW-CC-Sign=408E517DD978371F00DC678DD2050CEE58729C5B1110A980725D5B92461D1DBC)

-   本模块接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   示例效果请以真机运行为准。
    

**系统能力：** SystemCapability.Web.Webview.Core

#### 属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| size12+ | number | 否 | 否 | 
设置每个Web组件允许缓存的最大页面个数。

默认为1，最大可设置为50。

设置为0或负数时，前进后退缓存功能不生效。

Web会根据内存压力对缓存进行回收。

 |
| timeToLive12+ | number | 否 | 否 | 

设置每个Web组件允许页面在前进后退缓存中停留的时间。

设置为0或负数时，前进后退缓存功能不生效。

默认值：600。

单位：秒。

 |

#### constructor12+

constructor()

BackForwardCacheOptions的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core
