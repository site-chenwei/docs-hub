---
title: "@ohos.prompt (弹窗)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-prompt"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.prompt (弹窗)"
captured_at: "2026-04-17T01:47:53.894Z"
---

# @ohos.prompt (弹窗)

创建并显示文本提示框、对话框和操作菜单。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/kL8XI9KlQ8aQgkxocedqnQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=A94DB6063B4E4A2902E204755B9C2FA45BEF03D45E745DE558EC2D2A1B34AC0D)

从API version 9 开始，该接口不再维护，推荐使用新接口[@ohos.promptAction (弹窗)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-promptaction)。

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import prompt from '@ohos.prompt'
```

#### prompt.showToast

showToast(options: ShowToastOptions): void

创建并显示文本提示框。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ShowToastOptions](#showtoastoptions) | 是 | 文本弹窗选项。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showToast({
  message: 'Message Info',
    duration: 2000
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/8pTsx9J_SO-gpxoeR3Hq8g/zh-cn_image_0000002569020123.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=7A142F3686777F19D53B3AE4EDF505926585E2E1F4DA9EAC80156A471C82A719)

#### ShowToastOptions

文本提示框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| message | string | 是 | 显示的文本信息。 |
| duration | number | 否 | 默认值1500ms，取值区间：1500ms-10000ms。若小于1500ms则取默认值，若大于10000ms则取上限值10000ms。 |
| bottom | string| number | 否 | 设置弹窗边框距离屏幕底部的位置，无上限值，默认单位vp。 |

#### prompt.showDialog

showDialog(options: ShowDialogOptions): Promise<ShowDialogSuccessResponse>

创建并显示对话框，对话框响应后同步返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ShowDialogOptions](#showdialogoptions) | 是 | 对话框选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ShowDialogSuccessResponse](#showdialogsuccessresponse)\> | 对话框响应结果。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ],
})
  .then(data => {
    console.info('showDialog success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showDialog error: ' + err);
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/qDoUfUCqTVSuvx-WhpV-3A/zh-cn_image_0000002569020087.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=F3AF09421FA0027F3F2C697E4F66D3C93773D762220E31DE6AB3B59E6B524686)

#### prompt.showDialog

showDialog(options: ShowDialogOptions, callback: AsyncCallback<ShowDialogSuccessResponse>):void

创建并显示对话框，对话框响应结果异步返回。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ShowDialogOptions](#showdialogoptions) | 是 | 页面显示对话框信息描述。 |
| callback | AsyncCallback<[ShowDialogSuccessResponse](#showdialogsuccessresponse)\> | 是 | 对话框响应结果回调。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showDialog({
  title: 'showDialog Title Info',
  message: 'Message Info',
  buttons: [
    {
      text: 'button1',
      color: '#000000'
    },
    {
      text: 'button2',
      color: '#000000'
    }
  ]
}, (err, data) => {
  if (err) {
    console.info('showDialog err: ' + err);
    return;
  }
  console.info('showDialog success callback, click button: ' + data.index);
});
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/tiH9CHqSS52I6-2JD3Hckw/zh-cn_image_0000002568900079.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=F7B1C1F0688704C7765340B403BE14A281B46FA3CD0ECC9EDAED54A631A3F66C)

#### ShowDialogOptions

对话框的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| title | string | 否 | 标题文本。 |
| message | string | 否 | 内容文本。 |
| buttons | \[[Button](#button),[Button](#button)?,[Button](#button)?\] | 否 | 对话框中按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-3个按钮。其中第一个为positiveButton，第二个为negativeButton，第三个为neutralButton。 |

#### ShowDialogSuccessResponse

对话框的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 选中按钮在buttons数组中的索引。 |

#### prompt.showActionMenu

showActionMenu(options: ActionMenuOptions, callback: AsyncCallback<ActionMenuSuccessResponse>):void

创建并显示操作菜单，菜单响应结果异步返回。

**系统能力：** 以下各项对应的系统能力均为SystemCapability.ArkUI.ArkUI.Full。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ActionMenuOptions](#actionmenuoptions) | 是 | 操作菜单选项。 |
| callback | AsyncCallback<[ActionMenuSuccessResponse](#actionmenusuccessresponse)\> | 是 | 菜单响应结果回调。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showActionMenu({
  title: 'Title Info',
  buttons: [
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  ]
}, (err, data) => {
  if (err) {
    console.info('showActionMenu err: ' + err);
    return;
  }
  console.info('showActionMenu success callback, click button: ' + data.index);
})
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/SudoHDHYTeijZNjAwDXrYw/zh-cn_image_0000002569020089.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=6B0A53A62E9E6907ED8094AB33B93C86777539DDDF158E02B05736550B06612B)

#### prompt.showActionMenu

showActionMenu(options: ActionMenuOptions): Promise<ActionMenuSuccessResponse>

创建并显示操作菜单，菜单响应后同步返回结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [ActionMenuOptions](#actionmenuoptions) | 是 | 操作菜单选项。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[ActionMenuSuccessResponse](#actionmenusuccessresponse)\> | 菜单响应结果。 |

**示例：**

```ts
import prompt from '@ohos.prompt'
prompt.showActionMenu({
  title: 'showActionMenu Title Info',
  buttons: [
    {
      text: 'item1',
      color: '#666666'
    },
    {
      text: 'item2',
      color: '#000000'
    },
  ]
})
  .then(data => {
    console.info('showActionMenu success, click button: ' + data.index);
  })
  .catch((err:Error) => {
    console.info('showActionMenu error: ' + err);
  })
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/P0_QuWjBTqapsEpEjH0ZoA/zh-cn_image_0000002538020378.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=4F0CFF1EEB057F588022BB17608F88913200C96EC3541A80E48990B773EE7765)

#### ActionMenuOptions

操作菜单的选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| title | string | 否 | 标题文本。 |
| buttons | \[[Button](#button),[Button](#button)?,[Button](#button)?,[Button](#button)?,[Button](#button)?,[Button](#button)?\] | 是 | 菜单中菜单项按钮的数组，结构为：{text:'button', color: '#666666'}，支持1-6个按钮。大于6个按钮时弹窗不显示。 |

#### ActionMenuSuccessResponse

操作菜单的响应结果。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| index | number | 是 | 选中按钮在buttons数组中的索引，从0开始。 |

#### Button

菜单中的菜单项按钮。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 按钮文本内容。 |
| color | string | 是 | 按钮文本颜色。 |
