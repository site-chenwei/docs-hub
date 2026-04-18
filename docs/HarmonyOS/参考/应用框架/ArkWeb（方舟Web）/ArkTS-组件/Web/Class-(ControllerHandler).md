---
title: "Class (ControllerHandler)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-controllerhandler"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (ControllerHandler)"
captured_at: "2026-04-17T01:48:12.321Z"
---

# Class (ControllerHandler)

设置用户新建Web组件的WebviewController对象。示例代码参考[onWindowNew事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onwindownew9)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/ITAntkjqSMKasxZuaN-40g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=28FFC7778C9C0F087601B3B0359278ED47D92C9B89BE9A14D8F4F476C9A9C589)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 9开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor9+

constructor()

ControllerHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### setWebController9+

setWebController(controller: WebviewController): void

设置WebviewController对象，如果不需要打开新窗口请设置为null。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| controller | [WebviewController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-webview-webviewcontroller) | 是 | 新建Web组件的WebviewController对象，如果不需要打开新窗口请设置为null。 |
