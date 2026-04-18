---
title: "Class (JsResult)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-jsresult"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (JsResult)"
captured_at: "2026-04-17T01:48:12.447Z"
---

# Class (JsResult)

Web组件返回的弹窗确认或弹窗取消功能对象。示例代码参考[onAlert事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onalert)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/vKUETzCBQbOURHL4j9gUSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=9101347CE6ABA0DF40617011E1BBC28BDDB9E7F89F4534D8CD47A6E9658560C1)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 8开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor

constructor()

JsResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleCancel

handleCancel(): void

通知Web组件用户取消弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleConfirm

handleConfirm(): void

通知Web组件用户确认弹窗操作。

**系统能力：** SystemCapability.Web.Webview.Core

#### handlePromptConfirm9+

handlePromptConfirm(result: string): void

通知Web组件用户确认弹窗操作及对话框内容。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| result | string | 是 | 用户输入的对话框内容。 |
