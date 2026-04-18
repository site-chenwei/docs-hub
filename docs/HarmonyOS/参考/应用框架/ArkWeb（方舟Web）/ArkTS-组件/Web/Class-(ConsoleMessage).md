---
title: "Class (ConsoleMessage)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-consolemessage"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (ConsoleMessage)"
captured_at: "2026-04-17T01:48:12.299Z"
---

# Class (ConsoleMessage)

Web组件获取控制台信息对象。示例代码参考[onConsole事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#onconsole)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/JohV1fFRQrWYaDTbuhPocg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=A49F166C88E286303B506CE652808B2C0ECB2C1935AD2F2FAFE2CE8EDD74F151)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 8开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor(deprecated)

constructor(message: string, sourceId: string, lineNumber: number, messageLevel: MessageLevel)

ConsoleMessage的构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/5ipaMryyRkqi7IlxNDmURA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=FBA738E5533A36F8F6BDE0A899664710CAE75E1742FEB9268AD6D82A772A7374)

从API version 8开始支持，从API version 9开始废弃。建议使用[constructor](#constructor9)代替。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| message | string | 是 | ConsoleMessage的日志输出信息。 |
| sourceId | string | 是 | 网页源文件的路径和文件名。 |
| lineNumber | number | 是 | ConsoleMessage的行号。 |
| messageLevel | [MessageLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#messagelevel) | 是 | ConsoleMessage的日志级别。 |

#### constructor9+

constructor()

ConsoleMessage的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### getLineNumber

getLineNumber(): number

获取ConsoleMessage的行数。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| number | 返回ConsoleMessage的行数。 |

#### getMessage

getMessage(): string

获取ConsoleMessage的日志信息。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回ConsoleMessage的日志信息。 |

#### getMessageLevel

getMessageLevel(): MessageLevel

获取ConsoleMessage的信息级别。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [MessageLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#messagelevel) | 返回ConsoleMessage的信息级别。 |

#### getSourceId

getSourceId(): string

获取网页源文件路径和名字。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| string | 返回网页源文件路径和名字。 |

#### getSource23+

getSource(): ConsoleMessageSource

获取ConsoleMessage的日志来源。

**系统能力：** SystemCapability.Web.Webview.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [ConsoleMessageSource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-e#consolemessagesource23) | 返回ConsoleMessage的日志来源。 |
