---
title: "Class (WebSchemeHandlerRequest)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandlerrequest"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS API"
  - "@ohos.web.webview (Webview)"
  - "Class (WebSchemeHandlerRequest)"
captured_at: "2026-04-17T01:48:11.917Z"
---

# Class (WebSchemeHandlerRequest)

通过WebSchemeHandler拦截到的请求。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/A3cWvzpfS4SM5vRXhbCpoQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=67A8CEB550B29D943B3907DDB736B57268D91BE583E0FB93B447E0A034242BF8)

-   本模块首批接口从API version 9开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   示例效果请以真机运行为准。
    

#### getHeader12+

getHeader(): Array<WebHeader>

获取资源请求头信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Array<[WebHeader](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-i#webheader)\> | 返回资源请求头信息。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

#### getRequestUrl12+

getRequestUrl(): string

获取资源请求的URL信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回资源请求的URL信息。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

#### getRequestMethod12+

getRequestMethod(): string

获取请求方法。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回请求方法。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

#### getReferrer12+

getReferrer(): string

获取referrer。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 获取到的referrer。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

#### isMainFrame12+

isMainFrame(): boolean

判断资源请求是否为主frame。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 判断资源请求是否为主frame，如果资源请求是主frame则返回true，否则返回false。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

#### hasGesture12+

hasGesture(): boolean

获取资源请求是否与手势（如点击）相关联。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 返回资源请求是否与手势（如点击）相关联，如果返回资源请求与手势相关联则返回true，否则返回false。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

#### getHttpBodyStream12+

getHttpBodyStream(): WebHttpBodyStream | null

获取资源请求中的WebHttpBodyStream。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WebHttpBodyStream](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webhttpbodystream) | null | 返回资源请求中的WebHttpBodyStream，如果没有则返回null。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

#### getRequestResourceType12+

getRequestResourceType(): WebResourceType

获取资源请求的资源类型。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [WebResourceType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-e#webresourcetype12) | 返回资源请求的资源类型。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。

#### getFrameUrl12+

getFrameUrl(): string

获取触发此请求的Frame的URL。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回触发此请求的Frame的URL。 |

**示例：**

完整示例代码参考[onRequestStart](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webschemehandler#onrequeststart12)。
