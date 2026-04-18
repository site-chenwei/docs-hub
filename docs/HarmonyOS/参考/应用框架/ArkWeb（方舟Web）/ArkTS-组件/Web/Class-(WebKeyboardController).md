---
title: "Class (WebKeyboardController)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-webkeyboardcontroller"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkWeb（方舟Web）"
  - "ArkTS 组件"
  - "Web"
  - "Class (WebKeyboardController)"
captured_at: "2026-04-17T01:48:12.610Z"
---

# Class (WebKeyboardController)

控制自定义键盘的输入、删除、关闭等操作。示例代码参考[onInterceptKeyboardAttach](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-basic-components-web-events#oninterceptkeyboardattach12)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/Xg-b6s4wQKyCIeOEEg9Ljg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014812Z&HW-CC-Expire=86400&HW-CC-Sign=C0585CBE928A3711BDC38746E3083EAD693F93077E998EAFF9653F48BFF12CBD)

-   该组件首批接口从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   示例效果请以真机运行为准。
    

#### constructor12+

constructor()

WebKeyboardController的构造函数。

**系统能力：** SystemCapability.Web.Webview.Core

#### insertText12+

insertText(text: string): void

Web输入框中插入字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 向Web输入框插入字符。 |

#### deleteForward12+

deleteForward(length: number): void

从后往前删除Web输入框中指定长度的字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 
从后往前删除Web输入框中指定长度的字符。

取值范围：\[-2147483648 , 2147483647\]，当参数值大于字符长度时，默认删除光标前面所有字符；参数值为负数时，不执行删除操作。

 |

#### deleteBackward12+

deleteBackward(length: number): void

从前往后删除Web输入框中指定长度的字符。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| length | number | 是 | 
从前往后删除Web输入框中指定长度的字符。

取值范围：\[-2147483648 , 2147483647\]，当参数值大于字符长度时，默认删除光标后面所有字符；参数值为负数时，不执行删除操作。

 |

#### sendFunctionKey12+

sendFunctionKey(key: number): void

插入功能按键，目前仅支持Enter键类型，取值见[EnterKeyType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod#enterkeytype10)。

**系统能力：** SystemCapability.Web.Webview.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | number | 是 | 向Web输入框传递功能键，目前仅支持Enter键。 |

#### close12+

close(): void

关闭自定义键盘。

**系统能力：** SystemCapability.Web.Webview.Core
