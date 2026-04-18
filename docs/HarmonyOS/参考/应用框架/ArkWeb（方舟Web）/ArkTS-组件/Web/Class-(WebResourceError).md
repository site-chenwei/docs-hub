---
title: "Class (WebResourceError)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webresourceerror"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (WebResourceError)"
captured_at: "2026-04-17T01:48:12.603Z"
---

# Class (WebResourceError)

Web组件资源管理错误信息对象。示例代码参考[onErrorReceive事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onerrorreceive)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/kiiqXARqTd6uKe-d0narUg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=473934D4BD7F5579EAAB35A740F333373BF7C9F624D179BCADC3594FED41D228)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 8开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor

constructor()

WebResourceError的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### getErrorCode

getErrorCode(): number

获取加载资源的错误码。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回加载资源的错误码。错误码含义参考[WebNetErrorList](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-neterrorlist#webneterrorlist)、HTTP协议状态码。 |

#### getErrorInfo

getErrorInfo(): string

获取加载资源的错误信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回加载资源的错误信息。 |
