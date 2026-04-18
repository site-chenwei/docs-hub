---
title: "Class (MediaSourceInfo)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-mediasourceinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS API"
  - "@ohos.web.webview (Webview)"
  - "Class (MediaSourceInfo)"
captured_at: "2026-04-17T01:48:11.574Z"
---

# Class (MediaSourceInfo)

表示媒体源的信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/E43uEYrLQtSg85HZ8-BrZA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014811Z&HW-CC-Expire=86400&HW-CC-Sign=4AC2DA1135A6D59B5102BEC9C1AF7BA0036CCE04C16DAFC72600DD0B5FB977E6)

-   本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   示例效果请以真机运行为准。
    

#### 属性

**系统能力：** SystemCapability.Web.Webview.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type12+ | [SourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-e#sourcetype12) | 否 | 否 | 媒体源的类型。 |
| source12+ | string | 否 | 否 | 媒体源地址。 |
| format12+ | string | 否 | 否 | 媒体源格式， 可能为空， 需要使用者自己去判断格式。 |
