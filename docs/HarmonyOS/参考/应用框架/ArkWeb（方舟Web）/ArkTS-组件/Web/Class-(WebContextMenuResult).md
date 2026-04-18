---
title: "Class (WebContextMenuResult)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webcontextmenuresult"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (WebContextMenuResult)"
captured_at: "2026-04-17T01:48:12.571Z"
---

# Class (WebContextMenuResult)

实现长按页面元素或鼠标右键弹出来的菜单所执行的响应事件。示例代码参考[onContextMenuShow事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oncontextmenushow9)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/vcqIEckNQPmyC0QAYei-1Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=F182EDD1B90AFC0A8B4BEF1E18FE5214392EB6199A4B658E52CE809EC9576226)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 9开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor9+

constructor()

WebContextMenuResult的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### closeContextMenu9+

closeContextMenu(): void

不执行WebContextMenuResult其他接口操作时，需要调用此接口关闭菜单。

**系统能力：** SystemCapability.Web.Webview.Core

#### copyImage9+

copyImage(): void

当WebContextMenuParam包含图片内容时，用于复制该图片。

**系统能力：** SystemCapability.Web.Webview.Core

#### copy9+

copy(): void

执行拷贝文本操作。

**系统能力：** SystemCapability.Web.Webview.Core

#### paste9+

paste(): void

执行粘贴操作。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/eNmlOgyWT7OOIdZmj4uu9g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=F606960FFCB581FCD20558AB7E74B817F1517ED8C6C977DB7E71AF665B184AC5)

需要配置权限：[ohos.permission.READ\_PASTEBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard)。

**系统能力：** SystemCapability.Web.Webview.Core

#### cut9+

cut(): void

执行剪切操作。

**系统能力：** SystemCapability.Web.Webview.Core

#### selectAll9+

selectAll(): void

执行全选操作。

**系统能力：** SystemCapability.Web.Webview.Core

#### undo20+

undo(): void

执行撤销操作。

**系统能力：** SystemCapability.Web.Webview.Core

#### redo20+

redo(): void

执行重做操作，即取消用户上一次的撤销操作。

**系统能力：** SystemCapability.Web.Webview.Core

#### pasteAndMatchStyle20+

pasteAndMatchStyle(): void

执行一个和上下文菜单相关的粘贴操作，粘贴的内容会匹配目标格式，以纯文本形式呈现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/YJUtTJAzT0yC08jzGuVFiw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=6F8C9B9904B121C17A0C17FA8204E41EC5E4CE422AB839D7CF9088D345375A3C)

需要配置权限：[ohos.permission.READ\_PASTEBOARD](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/restricted-permissions#ohospermissionread_pasteboard)。

**系统能力：** SystemCapability.Web.Webview.Core

#### requestPasswordAutoFill23+

requestPasswordAutoFill(): void

请求密码保险箱中的用户名或密码数据自动填充到当前获得焦点的输入框中。

**系统能力：** SystemCapability.Web.Webview.Core
