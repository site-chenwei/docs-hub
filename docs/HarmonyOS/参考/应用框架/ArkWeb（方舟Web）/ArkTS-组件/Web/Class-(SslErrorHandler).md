---
title: "Class (SslErrorHandler)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-sslerrorhandler"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (SslErrorHandler)"
captured_at: "2026-04-17T01:48:12.519Z"
---

# Class (SslErrorHandler)

Web组件返回的SSL错误通知事件的处理对象。示例代码参考[onSslErrorEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onsslerrorevent12)事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/bLGi3yM8RT-Z7TQKEX8GmQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=9CF7A7E2F2B435401F2109FB0EC6825E31ABD897E847FF563C17027F158A274C)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 9开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor9+

constructor()

SslErrorHandler的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleCancel9+

handleCancel(): void

通知Web组件取消此请求。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleConfirm9+

handleConfirm(): void

通知Web组件继续使用SSL证书。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleCancel20+

handleCancel(abortLoading: boolean): void

通知Web组件取消此请求，并根据参数abortLoading决定是否停止加载。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| abortLoading | boolean | 是 | 
是否在取消请求后停止加载页面。

true表示停止加载页面，false表示继续加载页面。

默认值为false。

 |
