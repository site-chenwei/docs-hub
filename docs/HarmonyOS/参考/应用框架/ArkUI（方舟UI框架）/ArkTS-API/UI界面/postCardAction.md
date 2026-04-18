---
title: "postCardAction"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-postcardaction"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "postCardAction"
captured_at: "2026-04-17T01:47:53.333Z"
---

# postCardAction

用于卡片内部和提供方应用间的交互，当前支持router、message和call三种类型的事件，仅在卡片中可以调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/qoxSQ8n2Q-GWtoEdzGfvQg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=FF9F5584A3D6821A2A78DFA60E03CF309E4AFAF38FDFAFA9D3B8646CBB8DC160)

本接口从API version 9开始支持。

#### postCardAction

postCardAction(component: Object, action: Object): void

执行函数内部的交互，处理component和action对象的相关操作，不返回任何内容。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| :-- | :-- | :-- | :-- |
| component | Object | 是 | 当前自定义组件的实例，通常传入this。 |
| action | Object | 是 | action的具体描述，详情见下表。 |

action参数说明：

| **参数名** | **类型** | **必填** | **取值说明** |
| :-- | :-- | :-- | :-- |
| action | string | 是 | 
action的类型，支持三种预定义的类型：

\- router：跳转到提供方应用的指定UIAbility，只允许在点击事件中触发。

\- message：自定义消息，触发后会调用提供方FormExtensionAbility的[onFormEvent()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability#formextensionabilityonformevent)生命周期回调。

\- call：后台启动提供方应用。触发后会拉起提供方应用的指定UIAbility（仅支持launchType为singleton的[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uiability-launch-type)，即启动模式为单实例的UIAbility），但不会调度到前台。提供方应用需要具备后台运行权限([ohos.permission.KEEP\_BACKGROUND\_RUNNING](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/permissions-for-all#ohospermissionkeep_background_running))。

 |
| bundleName | string | 否 | action为router / call 类型时跳转的包名。 |
| moduleName | string | 否 | action为router / call 类型时跳转的模块名。 |
| abilityName | string | 否 | action为router / call 类型时跳转的UIAbility名。 |
| uri11+ | string | 否 | action为router 类型时跳转的UIAbility的统一资源标识符。uri和abilityName同时存在时，abilityName优先。 |
| params | Object | 否 | 当前action携带的额外参数，内容使用JSON格式的键值对形式。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/GKzd-BtxQC-J4E4pV2ZdMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=4CFB928FFAA45990763C8C6C4BB324D5BA3CB0FB6F0DCD624D761A915020679E)

"action"为"call" 类型时，"params"需填入参数'method'，且类型需为string类型，用于触发UIAbility中对应的方法。

**示例：**

```ts
Button('跳转')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'router',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      params: {
        message: 'testForRouter' // 自定义要发送的message
      }
    });
  })

Button('拉至后台')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'call',
      bundleName: 'com.example.myapplication',
      abilityName: 'EntryAbility',
      params: {
        method: 'fun', // 自定义调用的方法名，必填
        message: 'testForCall' // 自定义要发送的message
      }
    });
  })

Button('URI跳转')
  .width('40%')
  .height('20%')
  .onClick(() => {
    postCardAction(this, {
      action: 'router',
      uri: 'example://uri.ohos.com/link_page',
      params: {
        message: 'router msg for dynamic uri deeplink' // 自定义要发送的message
      }
    });
  })
```

**待跳转应用 [module.json5](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#skills标签) uris 配置示例：**

```json
"abilities": [
  {
    "skills": [
      {
        "uris": [
          {
            "scheme": "example",
            "host": "uri.ohos.com",
            "path": "link_page"
          }
        ]
      }
    ]
  }
]
```
