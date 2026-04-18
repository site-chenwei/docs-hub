---
title: "卡片传递消息给应用（message事件）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-event-formextensionability"
menu_path:
  - "指南"
  - "应用框架"
  - "Form Kit（卡片开发服务）"
  - "ArkTS卡片开发（推荐）"
  - "ArkTS卡片提供方开发指导"
  - "ArkTS卡片页面交互"
  - "卡片传递消息给应用（message事件）"
captured_at: "2026-04-17T01:35:44.870Z"
---

# 卡片传递消息给应用（message事件）

在卡片页面中可以通过[postCardAction](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-postcardaction#postcardaction-1)接口触发message事件拉起[FormExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability)，通过[onFormEvent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formextensionability#formextensionabilityonformevent)接口回调通知，以完成点击卡片控件后传递消息给应用的功能，然后由FormExtensionAbility刷新卡片内容，下面是这种刷新方式的简单示例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/UL7aAfsqQa-KwRncn8-zCw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013546Z&HW-CC-Expire=86400&HW-CC-Sign=386D24A21E1081AE9D816C86904610929AD232A15A8D7A9C7EC41CFCD0590242)

本文主要介绍动态卡片的事件开发。对于静态卡片，请参见[FormLink](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-formlink)。

-   在卡片页面通过注册Button的onClick点击事件回调，并在回调中调用postCardAction接口触发message事件拉起FormExtensionAbility。卡片页面中使用[LocalStorageProp](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage#localstorageprop)装饰需要刷新的卡片数据。
    
    ```typescript
    // entry/src/main/ets/updatebymessage/pages/UpdateByMessageCard.ets
    let storageUpdateByMsg = new LocalStorage();
    
    @Entry(storageUpdateByMsg)
    @Component
    struct UpdateByMessageCard {
      // $r('app.string.default_title')和$r('app.string.DescriptionDefault')需要替换为开发者所需的资源文件
      @LocalStorageProp('title') title: ResourceStr = $r('app.string.default_title');
      @LocalStorageProp('detail') detail: ResourceStr = $r('app.string.DescriptionDefault');
    
      build() {
        Column() {
          Column() {
            Text(this.title)
              .fontColor('#FFFFFF')
              .opacity(0.9)
              .fontSize(14)
              .margin({ top: '8%', left: '10%' })
            Text(this.detail)
              .fontColor('#FFFFFF')
              .opacity(0.6)
              .fontSize(12)
              .margin({ top: '5%', left: '10%' })
          }.width('100%').height('50%')
          .alignItems(HorizontalAlign.Start)
    
          Row() {
            // ...
            Button() {
              // $r('app.string.update')需要替换为开发者所需的资源文件
              Text($r('app.string.update'))
                .fontColor('#45A6F4')
                .fontSize(12)
            }
            .width(120)
            .height(32)
            .margin({ top: '30%', bottom: '10%' })
            .backgroundColor('#FFFFFF')
            .borderRadius(16)
            .onClick(() => {
              postCardAction(this, {
                action: 'message',
                params: { msgTest: 'messageEvent' }
              });
            })
          }.width('100%').height('40%')
          .justifyContent(FlexAlign.Center)
        }
        .width('100%')
        .height('100%')
        .alignItems(HorizontalAlign.Start)
        // $r('app.media.CardEvent')需要替换为开发者所需的资源文件
        .backgroundImage($r('app.media.CardEvent'))
        .backgroundImageSize(ImageSize.Cover)
      }
    }
    ```
    
-   在EntryFormAbility.ets中，导入相关模块
    
    ```typescript
    // entry/src/main/ets/entryformability/EntryFormAbility.ts
    import { formBindingData, FormExtensionAbility, formProvider } from '@kit.FormKit';
    import { Configuration, Want } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    ```
    
-   在FormExtensionAbility的onFormEvent生命周期中调用[updateForm](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-form-formprovider#formproviderupdateform)接口刷新卡片。
    
    ```typescript
    // entry/src/main/ets/entryformability/EntryFormAbility.ts
    const TAG: string = 'EntryFormAbility';
    const DOMAIN_NUMBER: number = 0xFF00;
    
    export default class EntryFormAbility extends FormExtensionAbility {
      // ...
      onFormEvent(formId: string, message: string): void {
        // 若卡片支持触发事件，则需要重写该方法并实现对事件的触发
        hilog.info(DOMAIN_NUMBER, TAG, `FormAbility onFormEvent, formId = ${formId}, message: ${message}`);
    
        class FormDataClass {
          title: string = 'Title Update.'; // 和卡片布局中对应
          detail: string = 'Description update success.'; // 和卡片布局中对应
        }
    
        // 请根据业务替换为实际刷新的卡片数据
        let formData = new FormDataClass();
        let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
        formProvider.updateForm(formId, formInfo).then(() => {
          hilog.info(DOMAIN_NUMBER, TAG, 'FormAbility updateForm success.');
        }).catch((error: BusinessError) => {
          hilog.error(DOMAIN_NUMBER, TAG, `Operation updateForm failed. Cause: ${JSON.stringify(error)}`);
        });
      }
    
      // ...
    }
    ```
    
    运行效果如下图所示。
    
    | 初始状态 | 点击刷新 |
    | :-- | :-- |
    | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/Exu25hsAS5qjh4bxQ_qouw/zh-cn_image_0000002568898925.png?HW-CC-KV=V1&HW-CC-Date=20260417T013546Z&HW-CC-Expire=86400&HW-CC-Sign=283B4CCB966B3763FDA3DAF5B0D4B5DA5F760C06334478B8389F5B3A471FA8B3) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/xDaBdfkxSXWVPG6bkknwGg/zh-cn_image_0000002538019220.png?HW-CC-KV=V1&HW-CC-Date=20260417T013546Z&HW-CC-Expire=86400&HW-CC-Sign=FE6E0375D754F3174289C7E53B339E30397643C87DBA43F740FFD76C85E0386D) |
