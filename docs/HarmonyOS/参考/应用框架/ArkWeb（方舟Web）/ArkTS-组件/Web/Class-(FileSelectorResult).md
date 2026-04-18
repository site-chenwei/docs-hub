---
title: "Class (FileSelectorResult)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-fileselectorresult"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (FileSelectorResult)"
captured_at: "2026-04-17T01:48:12.410Z"
---

# Class (FileSelectorResult)

通知Web组件的文件选择结果。示例代码参考[onShowFileSelector事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onshowfileselector9)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/euGh-MDOQjm9A3KYcfutrw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=482A0B0E530A9E962DB00239C4751D6B97F5E47318E42B86C8D7027DC1F52D32)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 9开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor9+

constructor()

FileSelectorResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### handleFileList9+

handleFileList(fileList: Array<string>): void

通知Web组件进行文件选择操作。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fileList | Array<string> | 是 | 需要进行操作的文件列表。 |
