---
title: "基于DialogHub的通用弹窗"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hadss_dialoghub"
menu_path:
  - "最佳实践"
  - "布局与弹窗"
  - "基于DialogHub的通用弹窗"
captured_at: "2026-04-17T01:54:13.612Z"
---

# 基于DialogHub的通用弹窗

#### 概述

在HarmonyOS开发中，弹窗是每个应用都会遇到的场景，其重要性不容忽视。一方面，弹窗可以作为一种即时反馈机制，向用户传递重要的信息或提示，如登录提示、网络请求状态、操作确认等。这些弹窗通常具有模态或半模态特性，能够暂时阻断用户的其他操作，确保用户能够注意到并处理这些信息。另一方面，弹窗还可以用于展示广告、推广内容或引导用户进行下一步操作。例如，在App首页或某些关键页面，通过弹窗展示全屏广告或引导用户参与某项活动，可以有效地提升用户参与度。为了方便开发者在HarmonyOS上高效使用不同的弹窗能力，DialogHub解决方案应运而生。

DialogHub作为ArkUI弹窗能力的解决方案，提供了以下功能特性：

1.  **页面级弹窗能力**
    
    确保弹窗与页面生命周期紧密绑定，页面销毁时自动清理弹窗资源。
    
    在页面切换或导航时，自动检查并隐藏旧页面的弹窗。
    
2.  **弹窗管理能力**
    
    提供弹窗状态管理，区分弹窗是否正在显示、是否已关闭。
    
    提供监听机制，允许开发者在弹窗状态变化时执行自定义逻辑，包括弹出、即将弹出、关闭、即将关闭4种状态。
    
3.  **简化创建弹窗流程**
    
    精简链式调用的API设计，确保常用弹窗可以通过简洁的语法创建。
    
    提供默认配置，减少不必要的参数设置，提高调用效率。
    
4.  **自定义弹窗模板提升易用性**
    
    允许开发者自定义模板并保存到模板库中，便于后续复用。
    
5.  **层级管理、手势透传等多种自定义配置属性**
    
    提供更灵活的层级管理机制，允许开发者动态调整弹窗的Z轴顺序。
    
    提供层级冲突的解决策略，如新旧置顶弹窗的解决策略。
    
    允许开发者自定义手势透传的行为，如是否允许手势穿透弹窗作用到底层页面。
    
    提供更多自定义属性，如弹窗的动画效果、背景颜色、圆角半径等。
    
6.  **弹窗刷新机制**
    
    提供属性值的动态更新机制，允许开发者在弹窗显示过程中修改属性。
    

本文主要以实际开发中的各项场景为例，介绍DialogHub的使用。

#### 实现原理

-   **弹窗能力****：**基于ArkUI框架中的OverlayManager和BindSheet能力实现。[OverlayManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-overlaymanager)为弹窗提供一个可以覆盖在其他UI元素之上的显示层，而[BindSheet](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-sheet-transition#bindsheet)则支持将弹窗与特定的页面或组件绑定，实现更精细的控制。
-   **页面级弹窗控制：**通过[UIObserver](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiobserver)实时监听应用内的路由变化，当路由发生变化时，触发相应的回调，从而允许DialogHub根据当前页面的状态来决定是否显示或隐藏弹窗。

#### 开发流程

**前提**

开发者参考[DialogHub简介](https://gitcode.com/openharmony-sig/dialoghub/blob/master/README.md)进行安装配置。

开发者调用init()接口并传入UIContext以初始化DialogHub。

DialogHub.init(this.getUIContext());

#### \[h2\]弹窗能力开发流程

通过DialogHub直接创建弹窗然后进行显示或者销毁。

1.  **获取弹窗构造器：**
    
    调用 DialogHub 的 getToast()等接口，获取不同类型的弹窗构造器 DialogBuilder。
    
    DialogHub.getToast()
    
2.  **配置弹窗内容：**
    
    调用 DialogBuilder 的 setContent()、setAnimation()等接口，配置弹窗的具体内容、动画效果、样式等。
    
    DialogHub.getToast()
      .setContent(wrapBuilder(TextToastBuilder), new TextToastParams(CommonConstant.TOAST\_TITLE))
      .setAnimation({ dialogAnimation: AnimationType.UP\_DOWN })
      .setConfig({ dialogBehavior: { isModal: true } })
      .setStyle({ backgroundColor: Color.White })
    
3.  **创建弹窗实例：**
    
    调用 DialogBuilder 的 build() 接口，创建弹窗实例 InfDialog 对象。
    
    let dialog:InfToast = DialogHub.getToast()
      // ...
      .build()
    
4.  **显示与销毁弹窗：**
    
    调用 InfDialog 对象的 show() 方法显示弹窗。
    
    dialog.show()
    
    调用 InfDialog 对象的 dismiss() 方法销毁弹窗。
    
    dialog.dismiss()
    

#### \[h2\]模板复用能力开发流程

开发者自定义模板并注册到模板库中，便于后续复用。

1.  **创建弹窗模板构造器：**
    
    调用 DialogHub 的 createToastTemplate()等接口，创建不同类型弹窗的模板构造器 DialogTemplate。
    
    DialogHub.createToastTemplate('SimpleToast')
    
2.  **配置模板内容：**
    
    调用 DialogTemplate 的 setContent()、setAnimation()等接口，配置模板的具体内容、动画效果、样式等。
    
    DialogHub.createToastTemplate('SimpleToast')
      .setContent(wrapBuilder(TextToastBuilder), new TextToastParams(CommonConstant.TOAST\_TITLE))
      .setAnimation({ dialogAnimation: AnimationType.UP\_DOWN })
      .setConfig({ dialogBehavior: { isModal: true } })
      .setStyle({ backgroundColor: Color.White })
    
3.  **注册模板：**
    
    调用 DialogTemplate 的 register() 接口，将配置好的模板注册并存储。
    
    DialogHub.createToastTemplate('SimpleToast')
      // ...
      .register()
    
4.  **获取并使用弹窗模板：**
    
    调用 DialogHub 的 getToastTemplate()等接口，根据模板名称获取对应的 DialogBuilder。
    
    然后按照弹窗能力开发流程中的步骤2~4，使用 DialogBuilder 配置并显示弹窗。
    
    DialogHub.getToastTemplate('SimpleToast')
      ?.setAnimation({dialogAnimation:AnimationType.FADE\_IN\_AND\_OUT})
      .build()
      .show()
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/ckIhjla_S2STIOrC360PCQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=304C2A1E89603C7C273C54449BD91874F95671D84213914A1AC1652864251F01)
    
    获取模板后配置的属性(如动画、位置等)只针对当前弹窗对象生效，不会修改模板内容。
    
5.  **(可选) 更新模板：**
    
    调用 DialogHub 的 updateToastTemplate()、updatePopupTemplate() 等接口，更新对应模板名称的配置，并重新注册。
    
    DialogHub.updateToastTemplate('SimpleToast')
      ?.setStyle({backgroundColor:Color.Blue})
      .register()
    
6.  **(可选) 删除模板：**
    
    调用 DialogHub 的 removeTemplate() 接口，删除对应模板名称的弹窗模板。
    
    DialogHub.removeTemplate('SimpleToast')
    
7.  **(可选) 判断模板是否存在：**
    
    调用 DialogHub 的 isTemplateExist() 接口，判断指定模板名称的弹窗模板是否已被注册。
    
    DialogHub.isTemplateExist('SimpleToast')
    

#### 常见业务弹窗

#### \[h2\]纯文本有持续时间的提示窗

一个简单的文本Toast弹窗，到达指定时间后消失。setDuration()设置Toast持续时间。

DialogHub.getToast()
  .setContent(wrapBuilder(TextToastBuilder))
    // ...
  .setDuration(CommonConstant.DURATION\_3000)
  .build()
  .show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/zkCJhIw0RuSewJhIBjagFQ/zh-cn_image_0000002194011644.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=BD91C0D1D6A19C1595A352C08C22C8230FCA4E068EF9D2C5269D54C084BDB62F "点击放大")

#### \[h2\]指定位置弹窗的非模态弹窗

在屏幕底部弹出SnackBar，该弹窗可以响应用户点击跳转页面或者关闭弹窗。

this.specifiedLocationDialog = this.specifiedLocationDialog ?? DialogHub.getCustomDialog()
  .setOperableContent(wrapBuilder(SnackbarBuilder), (action: DialogAction) => {
    let param = new SnackbarParams(() => {
      action.dismiss()
    }, this.pageInfos)
    return param
  })
    // ...
  .setConfig({
    dialogBehavior: { isModal: false, passThroughGesture: true },
    dialogPosition: {
      alignment: DialogAlignment.Bottom,
      offset: { dx: 0, dy: $r('app.float.specified\_location\_offset') }
    }
  })
  .build();
this.specifiedLocationDialog.show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/qAwFs2soSSqBhP8L2xLzLA/zh-cn_image_0000002229451969.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=04F22A576F92C2AE3E6EBB69B5AC978FB43E41B221D71A7A705712A95E5088E1 "点击放大")

#### \[h2\]会定时消失且带弹出动效的弹窗

实现一个定时弹窗，6s自动关闭。

-   通过setAnimation()设置弹窗弹出动效。
-   通过dialog实例的updateContent()，定时动态刷新弹窗内容。
    
    this.intervalsDisappearsDialog = this.intervalsDisappearsDialog ?? DialogHub.getCustomDialog()
      .setContent(wrapBuilder(TimeToastBuilder), params)
      .setStyle({
        radius: $r('app.float.popup\_disappears\_intervals\_radius'),
        shadow: CommonConstant.CUSTOM\_SAMPLE\_STYLE\_SHADOW
      })
      .setAnimation({ dialogAnimation: AnimationType.UP\_DOWN })
      .setConfig({
        dialogBehavior: { isModal: false, passThroughGesture: true },
        dialogPosition: {
          alignment: DialogAlignment.Top,
          offset: { dy: $r('app.float.popup\_disappears\_intervals\_offset'), dx: 0 }
        }
      })
      .build();
    
    this.intervalsDisappearsDialog.show();
    
    intervalID = setInterval(() => {
      time -= 1;
      params.content = time + CommonConstant.TIMED\_CLOSED;
      this.intervalsDisappearsDialog?.updateContent(params)
      if (time <= 0 && intervalID) {
        this.intervalsDisappearsDialog?.dismiss();
        clearInterval(intervalID);
      }
    }, CommonConstant.DURATION\_1000);
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/BoVCrFypTtiOPJ1HbXeaBQ/zh-cn_image_0000002229451937.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=79C158DF1C375FC1A6AE7E547F3C4345AEAB7EAB0D24BF0C74A066BC0242480B "点击放大")

#### \[h2\]会避让键盘的弹窗

通过setConfig()的keyboardAvoidMode可以配置避让模式，CustomKeyboardAvoidMode.CONTENT\_AVOID为弹窗内容避让。

requestFocusWhenShow配置为true，弹窗显示时，弹窗自动获焦。

this.avoidKeyboardDialog = this.avoidKeyboardDialog ?? DialogHub.getCustomDialog()
  .setContent(wrapBuilder(InputBuilder), param)
    // ...
  .setConfig({
    dialogBehavior: {
      isModal: false,
      passThroughGesture: true,
      requestFocusWhenShow: true,
      keyboardAvoidMode: CustomKeyboardAvoidMode.CONTENT\_AVOID
    },
    dialogPosition: { alignment: DialogAlignment.Bottom }
  })
  .build();
this.avoidKeyboardDialog.show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/KEk8Y30iTkSkga4qq2Bn8g/zh-cn_image_0000002193852076.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=FB0395B8384A86C18A5733B88ABFC1663C4B0AAF2D18C93E5B2B9B957C20613E "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/Dq1nNK5YRM2l1cx_1ZUYaA/zh-cn_image_0000002193852080.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=9C56169F545C09A81930D5271263AD60255C90FFB9644904F9246543E21B6EC4 "点击放大")

#### \[h2\]指向选定组件的带箭头弹窗

通过getPopup()构造Popup弹窗实例，setStyle()中enableArrow、arrowOffset、arrowWidth、arrowHeight可配置箭头属性；

setConfig()中preferPlacement可配置箭头偏向。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/U0Zu12k5RLmG-N512tSjYw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=87FEB185BE14309A748490E3FFD217DC0C289465D12137E5290CD13216B2CC92)

绑定组件需要调用setComponentTargetId(targetCompId)，targetCompId组件id标识确保唯一，否则会报错且弹窗位置异常。

DialogHub.getPopup()
  // ...
  .setComponentTargetId('PopupDialog1')
  .setStyle({
    radius: $r('app.float.image\_popup\_builder\_borderRadius'),
    backgroundColor: Color.White,
    shadow: {
      radius: $r('app.float.image\_popup\_shadow\_radius'),
      color: $r('app.color.image\_popup\_shadow\_color')
    },
  })
  .setConfig({
    dialogPosition: {
      preferPlacement: Placement.Bottom
    }
  })
  .build()
  .show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/o9UgOvA9ROehFFDcetIVvA/zh-cn_image_0000002194011660.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=D2011E03AB607968E3D7C76445A72C187B8A07956EAF4657DC380FEFF074131A "点击放大")

#### \[h2\]点击蒙层自动关闭的弹窗

弹出此类型弹窗需要打开isModal蒙层开关，并将autoDismiss设置为true

this.maskCloseDialog = this.maskCloseDialog ?? DialogHub.getCustomDialog()
  // ...
  .setConfig({ dialogBehavior: { isModal: true, autoDismiss: true, passThroughGesture: false } })
  .build();
this.maskCloseDialog.show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/LUIdpaZESRSekZkfDu94JQ/zh-cn_image_0000002229337453.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=3FD959F30BBD0BF2169BBF968D818C8CA4F2794DFE6DD327BB5571A78FA8F1C7 "点击放大")

#### \[h2\]可主动关闭的弹窗

能够通过点击弹窗按钮关闭弹窗，设置弹窗Content时，调用setOperableContent()，并将DialogHub的Dismiss事件作为参数传递给Builder。

this.activelyCloseDialog = this.activelyCloseDialog ?? DialogHub.getCustomDialog()
  .setOperableContent(wrapBuilder(ActiveCloseBuilder), (action: DialogAction) => {
    let param =
      new ActiveCloseParams(CommonConstant.LOGOUT, CommonConstant.LOGOUT\_TIPS,
        CommonConstant.CANCEL, CommonConstant.OUT, () => {
          action.dismiss();
        }, () => {
          this.activelyCloseDialog?.dismiss();
        })
    return param;
  })
  .setConfig({ dialogBehavior: { isModal: true, autoDismiss: false, passThroughGesture: false } })
  .setStyle({
    radius: $r('app.float.active\_close\_builder\_borderRadius'),
    backgroundColor: Color.White,
  })
  .build();
this.activelyCloseDialog.show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Lx16Ga3RRp2Cn8b6190-6A/zh-cn_image_0000002229451961.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=8F36C6A8D9A38BFE20A26528D36F4BAF33B4A9CA831A9686A8F2A5BAB7DE9F73 "点击放大")

#### \[h2\]能够动态调整高度的底部弹窗

实现动态调整弹窗高度，不同高度展示不同弹窗内容。

-   获取DialogHub的Sheet类型弹窗实例
    
    this.adjustSheetDialog = DialogHub.getSheet()
      .setContent(wrapBuilder(SheetBuilder), sheetParams)
      .setStyle({ preferType:SheetType.BOTTOM, detents: \[CommonConstant.SHEET\_MIDDLE, CommonConstant.SHEET\_LARGE\] })
      .setConfig({ enableOutsideInteractive: false, scrollSizeMode: ScrollSizeMode.CONTINUOUS })
      .setComponentTargetId(CommonConstant.ADJUST\_SHEET\_DIALOG\_ID)
      .build();
    
-   弹窗实例增加Sheet高度监听onHeightDidChange()，当高度变化到一定程度，updateContent()刷新弹窗内容
    
    this.adjustSheetDialog.addLifeCycleListener({
      onHeightDidChange: (h: number) => {
        let vpValue = this.getUIContext().px2vp(h)
        if (vpValue <= CommonConstant.SHEET\_MIDDLE && sheetParams.type != 0) {
          sheetParams.type = 0
          this.adjustSheetDialog?.updateContent(sheetParams)
        } else if (vpValue > CommonConstant.SHEET\_MIDDLE && sheetParams.type != 1) {
          sheetParams.type = 1
          this.adjustSheetDialog?.updateContent(sheetParams)
        }
      },
      // ...
    });
                    this.adjustSheetDialog?.show();
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/y7_-tyZpQlegxW3auM8vCQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=73DE3331B3DE4E4D0883D078BAEA5092E7B8460752A130521176DB305B558FC1)

sheet类型弹窗须调用setComponentTargetId(targetCompId)以实现页面级弹窗，并且保证绑定的组件id存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/HbFGnvpAQQGQKhdW_W9GCg/zh-cn_image_0000002229337473.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=DC01FE3DBB38A02ECB40208AC61F89A93983426120342C531E738C3859785ED6 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/4qFaLAysRr-MXtiyJSn8Og/zh-cn_image_0000002194011664.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=58EEFE0B1B55DAB9702CF3555CFDE6407250BB873A5A168D82FFDD1C2718736D "点击放大")

#### \[h2\]应用感知弹窗的打开、关闭

-   对弹窗实例增加生命周期，拦截弹窗的展示与销毁。
    
    this.sensorDialog?.addLifeCycleListener({
      onWillShow: () => {
        this.isSensorDialogShow = true
        return true;
      },
      onWillDismiss: (reason: DialogDismissReason) => {
        this.isSensorDialogShow = false
        return true;
      }
    })
    
-   直接获取弹窗状态
    
    // SHOW: 显示，HIDE: 隐藏， DEFAULT: 默认状态
    this.sensorDialog?.getStatus();
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/n5pRgLpFT_inxpH9Adekag/zh-cn_image_0000002229337477.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=94CD4CA7BF8E551B809C99150EA688B26BA39634C9E68DC7ADF96D7B5B8BB739 "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Idb5AmTRSfabM3GleNk_KA/zh-cn_image_0000002229337469.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=84CC2C68A802844EB7CC09D7586757A6EB03ED1185688EEF5A2E9262D968F4B8 "点击放大")

#### 弹窗与周边的交互

#### \[h2\]弹窗存在时如何定义返回手势是退出页面或关闭弹窗

配置状态变量backCloseDialog，设置true表示返回手势作用于弹窗，false表示作用于页面。

@State backCloseDialog: boolean = false;

在onBackPressed()中拦截手势并选择是退出页面还是关闭最上层弹窗

.onBackPressed(() => {
  if (this.backCloseDialog) {
    let tmp: DialogBackPressResult = DialogHub.dispatchBackPressToDialog();
    if (tmp !== DialogBackPressResult.NO\_DIALOG) {
      return true;
    }
  }
  this.pageInfos.pop();
  return true;
})

#### \[h2\]用户可以透过弹窗内容操作页面

弹出Toast类型的弹窗，或者主动调用setConfig()设置passThroughGesture为true，可实现弹窗内容透传手势。

this.passThroughGestureDialog = DialogHub.getToast()
  .setContent(wrapBuilder(IconToastBuilder))
  // ...
  .setDuration(CommonConstant.DURATION\_2000)
  .build();
this.passThroughGestureDialog.show();

DialogHub.createCustomTemplate(CommonConstant.CUSTOM\_TEMPLATE\_SIMPLE)
  .setContent(wrapBuilder(TextToastBuilder))
  .setStyle({ backgroundColor: Color.White })
  .setConfig({ dialogBehavior: { passThroughGesture: true, isModal: false } })

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/L-c7oyYNR8WbP4J33G0tGg/zh-cn_image_0000002193852068.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=1A92AB43EFB8480ED35304434A68DC1876DDC154BAC794A404B6AF51A0E42DDB "点击放大")

#### \[h2\]需要向页面返回数据的弹窗

给Builder参数传递修改页面数据的回调函数，在Builder里面进行调用。

this.returnDataDialog = DialogHub.getCustomDialog()
  .setOperableContent(wrapBuilder(InputCallbackBuilder), (action: DialogAction) => {
    let parms = new InputCallbackParams(CommonConstant.UPDATE\_TAG, () => {
      action.dismiss();
    }, (value) => {
      this.tagName = value;
    })
    return parms;
  })
  .setStyle({
    radius: $r('app.float.InputCallbackBuilderBorderRadius')
  })
  .setConfig({ dialogBehavior: { isModal: true, autoDismiss: false } })
  .build();
this.returnDataDialog.show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/T4brIh47SFuldbXQRm5uyw/zh-cn_image_0000002193852084.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=D009EFA35B9EA3BB54EDE3BE4DDF0E243A7715D3B2BC4950AED8BB1D56BB97BA "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/lZlDrvq-RnG6x2o831pYfw/zh-cn_image_0000002229451965.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=2D3ACC53D0C7BF12AE1B97A1703E353417ED23D0A60909BBD4741EAF0941DF9A "点击放大")

#### \[h2\]父页面刷新正在展示的弹窗内容

修改Builder参数内容，再调用updateContent()进行修改。

let params = new ProgressParams(CommonConstant.ProgressName, CommonConstant.ProgressNameStart,
  CommonConstant.ProgressNameTotal);

this.updateByParentDialog = DialogHub.getCustomDialog()
  .setContent(wrapBuilder(ProgressBuilder), params)
  .setStyle({ radius: $r('app.float.ProgressBuilderProgressBorderRadius') })
  .setConfig({ dialogBehavior: { isModal: true, autoDismiss: false } })
  .build();
this.updateByParentDialog.show();

this.intervalID = setInterval(() => {
  params.value += 1
  if (params.value >= CommonConstant.ProgressNameTotal && this.intervalID >= 0) {
    this.updateByParentDialog?.dismiss();
    clearInterval(this.intervalID);
  }
  this.updateByParentDialog?.updateContent(params);
}, CommonConstant.Interval\_20);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/YT7SMfXxQV-truqlTbYHwA/zh-cn_image_0000002229337481.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=273F1653A5D975B8B537AF30F169CC0E7EDD042B526D79C14ACE194717D40005 "点击放大")

#### \[h2\]页面需要感知当前页面是否存在弹窗

DialogHub注册页面弹窗数监听，当前页面弹窗数量发生变化会触发。

DialogHub.addEventListener({
  OnCurentPageDialogNumberChange: (newNum: number, oldNum: number) => {
    this.dialogNum = newNum;
  }
})

#### \[h2\]存在跳转链接的弹窗

点击弹窗上特定内容，跳转到其他页面。

router：在弹窗Builder里通过router模板跳转。

Navigation：将pageInfos传入弹窗Builder，然后在弹窗里进行push页面。

let parms = new SkipParams(() => {
  this.skipDialog?.dismiss();
}, 1, this.pageInfos);
this.skipDialog?.updateContent(parms);
this.skipDialog?.updateConfig({
  dialogPosition: { offset: { dx: 0, dy: 0 } }
});
this.skipDialog?.show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/VSJKnGbSSISEQcS1IhpsVw/zh-cn_image_0000002194011656.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=CE0B446C7C1F06EE11E2A9BB9AFA39EFB6423520788B75EA7192462F040FEEF2 "点击放大")

#### \[h2\]折叠屏展开态不同位置的弹窗

弹窗默认在屏幕中间；通过设置弹窗偏移量可以在不同位置进行弹窗。

弹窗在左半屏：

let parms = new SkipParams(() => {
  this.skipDialog?.dismiss()
}, 1, this.pageInfos);
this.skipDialog?.updateContent(parms);
this.skipDialog?.updateConfig({
  dialogPosition: { offset: CommonConstant.LEFT\_DIALOG\_OFFSET }
});
this.skipDialog?.show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/mCPm0K22SnqX0Z9WCDjM6g/zh-cn_image_0000002229451949.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=94A71309667BB803695FA1AF78EE383B7F1F3776F3900393E4AA36AFEBE7EE03 "点击放大")

弹窗在右半屏：

let parms = new SkipParams(() => {
  this.skipDialog?.dismiss();
}, 1, this.pageInfos);
this.skipDialog?.updateContent(parms);
this.skipDialog?.updateConfig({
  dialogPosition: { offset: CommonConstant.RIGHT\_DIALOG\_OFFSET }
});
this.skipDialog?.show();

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/Eg7vQ2KFRdmSmdig6O4Fxw/zh-cn_image_0000002229337445.png?HW-CC-KV=V1&HW-CC-Date=20260417T015415Z&HW-CC-Expire=86400&HW-CC-Sign=32B628DA2EEACFBA7C22B1A8D9211FB8C60F5D82ECDF9F89E50BBCB46B11A6C5 "点击放大")

#### 弹窗内容复用场景

#### \[h2\]通过自定义弹窗模版进行弹窗

-   创建弹窗模板
    
    DialogHub.createToastTemplate(CommonConstant.MY\_TEMPLATE\_NAME)
      .setTextContent(CommonConstant.TOAST\_DISPLAYED\_CONTENT)
        // ...
      .setDuration(CommonConstant.TOAST\_DISPLAY\_DURATION)
      .register();
    
-   直接弹出模板
    
    DialogHub.getToastTemplate(CommonConstant.MY\_TEMPLATE\_NAME)?.build().show();
    
-   删除弹窗模板
    
    DialogHub.removeTemplate(CommonConstant.MY\_TEMPLATE\_NAME);
    
-   随机修改弹窗模板背景色
    
    let r = (Math.ceil(Math.random() \* 239 + 16) % 255).toString(16);
    let g = (Math.ceil(Math.random() \* 239 + 16) % 255).toString(16);
    let b = (Math.ceil(Math.random() \* 239 + 16) % 255).toString(16);
    let color = '#ff' + r + g + b;
    DialogHub.updateToastTemplate(CommonConstant.MY\_TEMPLATE\_NAME)?.setStyle({
      backgroundColor: color
    }).register();
    
-   (可选)通过弹窗模板，定义本次弹出动画后弹出
    
    DialogHub.getToastTemplate(CommonConstant.MY\_TEMPLATE\_NAME)?.setAnimation({
      dialogAnimation: AnimationType.UP\_DOWN
    }).build().show();
    

#### \[h2\]定义一个可复用的弹窗

将弹窗实例对象记录，下次弹窗复用。

originalTemplateDialog?: InfToast;

this.originalTemplateDialog =
  DialogHub.getToastTemplate(CommonConstant.MY\_TEMPLATE\_NAME)?.build();

this.originalTemplateDialog?.show();

#### 多个弹窗并存场景

#### \[h2\]新弹窗被已有弹窗抑制

-   **弹窗A弹出时抑制弹窗B的弹出**
    
    可以通过弹窗A对象的getStatus()方法获取弹窗A的状态，以判断是否允许弹窗B弹出。
    
    if (this.dialogA?.getStatus() != DialogStatus.SHOW) {
      this.dialogB?.show();
    }
    

-   **当前页面存在弹窗时抑制弹窗C的弹出**
    
    通过调用DialogHub的getCurrentPageDialogs()方法获取当前页面的弹窗数量，判断数量是否为0，并据此控制弹窗C的弹出。
    
    if (DialogHub.getCurrentPageDialogs().length === 0) {
      this.dialogC?.show();
    }
    

#### \[h2\]开发者可以控制弹窗层级实现弹窗的相互覆盖

-   设置弹窗层级setLayerIndex()
    
    this.dialogF = this.dialogF ??
    this.createMessageBuilder(CommonConstant.DIALOG\_F, CommonConstant.DIALOG\_F\_CONTENT)
      .setLayerIndex(CommonConstant.DIALOG\_F\_LAYER\_INDEX)
      .build();
    

-   设置置顶弹窗OLD\_FIRST (老置顶弹窗优先，新的置顶弹窗无法弹出)
    
    this.dialogG = this.dialogG ??
    this.createMessageBuilder(CommonConstant.DIALOG\_G, CommonConstant.DIALOG\_G\_CONTENT).setConfig({
      dialogBehavior: {
        layerPolicy: { alwaysTop: true, topDialogPriority: TopDialogPriority.OLD\_FIRST }
      }
    }).build();
    

-   设置置顶弹窗NEW\_FIRST (新弹窗优先，新的置顶弹窗弹出，老置顶弹窗被覆盖)
    
    this.dialogH = this.dialogH ??
    this.createMessageBuilder(CommonConstant.DIALOG\_H, CommonConstant.DIALOG\_H\_CONTENT).setConfig({
      dialogBehavior: {
        layerPolicy: { alwaysTop: true, topDialogPriority: TopDialogPriority.NEW\_FIRST }
      }
    }).build();
    

#### 常见问题

#### \[h2\]如何处理弹窗的获焦问题

-   对于Sheet类别的弹窗，弹窗弹出后的焦点行为与系统BindSheet保持一致；
-   DialogHub提供的其他类别弹窗，如CustomDialg，在弹窗弹出时父页面的焦点默认不会转移到弹窗上。
    
    开发者可以配置弹窗的requestFocusWhenShow属性实现：弹窗弹出时，将页面的焦点转移到弹窗中。进而实现[会避让键盘的弹窗](#section395448164119)的效果。
    

#### \[h2\]Popup绑定组件，id报错

[组件标识id](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-component-id#id)需要开发者保证唯一性。setComponentTargetId()设置绑定的组件id后，如果id有问题，会导致在show的时候报错且弹窗位置异常。

-   id不存在：不存在此id的节点，排查绑定组件是否设置该id属性。错误码70000001。

#### \[h2\]调用build()与show()接口后，无法继续添加属性

调用build()接口后返回的是Dialog实例，只提供更新配置的接口。

#### \[h2\]removeTemplate()后，使用模板创建的弹窗实例可以继续显示

删除模板不影响之前通过模板已经创建的弹窗的显示和相关调用。

#### \[h2\]调用isTemplateExist()判断模板存在，getxxxTemplate模板报错50000003

模板创建和获取时，需要保证弹窗类型一致，否则无法获取模板并报错，错误码50000003。

可在获取模板前调用queryTemplate()查询模板的弹窗类型。

#### \[h2\]Toast弹窗置顶策略

Toast弹窗默认为置顶弹窗，且置顶冲突策略为TopDialogPriority.NEW\_FIRST。

#### \[h2\]键盘避让模式变化

在使用DialogHub进行弹窗后，会将页面键盘避让模式修改为RESIZE，当页面无弹窗或者页面跳转时，避让模式还原。

#### \[h2\]弹窗如何处理用户的返回手势

开发者可以通过Dialoghub.init(xxx，xx)设置不同的[弹窗模式](https://gitcode.com/openharmony-sig/dialoghub/blob/master/docs/Reference.md#dialogmode枚举说明)，不同的模式下处理措施不同。

-   DialogMode.OverlayManager（默认）模式下，返回手势会优先作用于页面，由页面消费该事件。
    
    处理方法如下：
    
    1.  在页面的onBackPress()中调用dispatchBackPressToDialog()方法将事件传递给弹窗。
    2.  在弹窗的onWillDismiss()方法中，针对【DialogDismissReason.PRESS\_BACK】原因，对返回手势进行处理。
    

-   DialogMode.CustomDialog模式下，返回手势会作用于弹窗，由弹窗消费该事件。
    
    处理方法如下：
    
    1.  直接在弹窗的onWillDismiss()方法中，针对【DialogDismissReason.PRESS\_BACK】原因，对返回手势进行处理
    2.  在弹窗的onWillDismiss()方法中继续处理页面操作，如通过页面栈进行处理。

#### 示例代码

-   [基于DialogHub实现通用弹窗库案例](https://gitcode.com/harmonyos_samples/DialogHub)
