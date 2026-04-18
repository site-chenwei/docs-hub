---
title: "LiveFormExtensionContext"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-liveformextensioncontext"
menu_path:
  - "参考"
  - "应用框架"
  - "Form Kit（卡片开发服务）"
  - "ArkTS API"
  - "application"
  - "LiveFormExtensionContext"
captured_at: "2026-04-17T01:48:15.007Z"
---

# LiveFormExtensionContext

LiveFormExtensionContext是[LiveFormExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-liveformextensionability)的上下文，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QW8iYwe0S3Skolc_02TZZw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=44709E24A3C1348DB5E03351B9E7E418A847A8E1A867157B878D11B0B177C451)

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

#### 导入模块

```ts
import { common } from '@kit.AbilityKit';
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/uz5np0KERiiT8GsFrArr2A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=A0B8794E29E287D77A9E8B5465AAAA65B904878520AC9E78DB8033E81CA13824)

-   在API version 22以前，需要通过import LiveFormExtensionContext from 'application/LiveFormExtensionContext'; 导入LiveFormExtensionContext。该导入方式在DevEco Studio中标红，但不影响编译运行，可以直接使用LiveFormExtensionContext。
    
-   在API version 22及以后，支持通过import { common } from '@kit.AbilityKit'; 导入LiveFormExtensionContext，并通过common.LiveFormExtensionContext的方式使用。
    

#### LiveFormExtensionContext

LiveFormExtensionContext提供允许访问特定于LiveFormExtensionAbility资源的能力，继承自[ExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-extensioncontext)。

#### \[h2\]startAbilityByLiveForm

startAbilityByLiveForm(want: Want): Promise<void>

拉起互动卡片提供方（应用）的页面，使用Promise异步回调。

该接口仅支持拉起互动卡片提供方（应用）的页面，不支持拉起其他应用的页面，否则会抛出错误码16501011。

该接口建议在点击事件回调中调用，不建议在其他手势事件回调中调用，不支持非手势事件直接调用，否则会抛出错误码16501011。

另外，在点击事件回调中，支持直接调用，不支持延时后调用，否则会抛出错误码16501011。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Ability.Form

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 是 | 需要被拉起的应用页面信息。[仅支持使用显式want。](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ability-startup-with-explicit-want) |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[卡片错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-form)和[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 801 | Capability not supported due to limited device capabilities. |
| 16500050 | An IPC connection error happened. |
| 16500100 | Failed to obtain the configuration information. |
| 16501000 | An internal functional error occurred. |
| 16501011 | The form can not support this operation. |

**示例：**

```ts
// MyLiveFormExtensionAbility.ets
import { formInfo, LiveFormInfo, LiveFormExtensionAbility } from '@kit.FormKit';
import { UIExtensionContentSession } from '@kit.AbilityKit';

export default class MyLiveFormExtensionAbility extends LiveFormExtensionAbility {
  onLiveFormCreate(liveFormInfo: LiveFormInfo, session: UIExtensionContentSession) {
    // 1.将LiveFormExtensionContext传给互动卡片的页面组件
    let storage: LocalStorage = new LocalStorage();
    storage.setOrCreate('context', this.context);
    session.loadContent('pages/MyLiveFormPage', storage);
  }
};
```

```ts
// pages/MyLiveFormPage.ets
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct MyLiveFormPage {
  private storageForMyLiveFormPage: LocalStorage | undefined = undefined;
  private liveFormContext: common.LiveFormExtensionContext | undefined = undefined;

  aboutToAppear(): void {
    // 2.获取LiveFormExtensionContext
    this.storageForMyLiveFormPage = this.getUIContext().getSharedLocalStorage();
    this.liveFormContext = this.storageForMyLiveFormPage?.get<common.LiveFormExtensionContext>('context');
  }

   private startAbilityByLiveForm(): void {
    try {
      // 请开发者替换为实际的want信息
      this.liveFormContext?.startAbilityByLiveForm({
        bundleName: 'com.example.liveformdemo',
        abilityName: 'EntryAbility',
      })
        .then(() => {
          console.info('startAbilityByLiveForm succeed');
        })
        .catch((err: BusinessError) => {
          console.error(`startAbilityByLiveForm failed, code is ${err?.code}, message is ${err?.message}`);
        });
    } catch (e) {
      console.error(`startAbilityByLiveForm failed, code is ${e?.code}, message is ${e?.message}`);
    }
  }

  build() {
    // 请开发者替换为实际的页面
    Stack() {
      Column()
        .width('50%')
        .height('50%')
        .backgroundColor('#2875F5')
    }
    .width('100%')
    .height('100%')
    .onClick(() => {
      // 3.在点击事件回调中直接使用该接口
      console.info('MyLiveFormPage click to start ability');
      if (!this.liveFormContext) {
        console.info('MyLiveFormPage liveFormContext is empty');
        return;
      }
      this.startAbilityByLiveForm();
    })
  }
}
```
