---
title: "@ohos.mediaquery (媒体查询)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "@ohos.mediaquery (媒体查询)"
captured_at: "2026-04-17T01:47:53.227Z"
---

# @ohos.mediaquery (媒体查询)

提供根据不同媒体类型定义不同的样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/glCe8TZxTEatenGGsy7x6Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=713173E11E77471C4C93A297F08529E23F31025095D66C1C8DA598B53A5B35F8)

-   本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   该模块不支持在[UIAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiability)的文件声明处使用，即不能在UIAbility的生命周期中调用，需要在创建组件实例后使用。
    
-   本模块功能依赖UI的执行上下文，不可在[UI上下文不明确](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-global-interface#ui上下文不明确)的地方使用，参见[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)说明。
    

#### 导入模块

```ts
import { mediaquery } from '@kit.ArkUI';
```

#### mediaquery.matchMediaSync(deprecated)

matchMediaSync(condition: string): MediaQueryListener

设置媒体查询的查询条件，并返回对应的监听句柄。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/SDE_QYJwQQmCPpC0q_0F1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=3E7FCEBFE039F0022CCCDAEA05EB78869904E6A3C4FC77D17C2CEB61CEB19E24)

-   从API version 7开始支持，从API version 18开始废弃，建议使用[matchMediaSync](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery#matchmediasync)替代。matchMediaSync需先通过[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getMediaQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getmediaquery)方法获取[MediaQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery)对象，然后通过该对象进行调用。
    
-   从API version 10开始，可以通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getMediaQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getmediaquery)方法获取当前UI上下文关联的[MediaQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery)对象。
    

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| condition | string | 是 | 媒体事件的匹配条件，具体可参考[媒体查询语法规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-media-query#语法规则)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [MediaQueryListener](#mediaquerylistener) | 媒体事件监听句柄，用于注册和去注册监听回调。 |

**示例：**

```ts
import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // 监听横屏事件
```

#### MediaQueryListener

媒体查询的句柄，并包含了申请句柄时的首次查询结果。媒体查询根据设置的条件语句，比如'(width <= 600vp)'，比较系统信息，若首次查询时相关信息未初始化，matches返回false。

继承自[MediaQueryResult](#mediaqueryresult)。

**卡片能力：** 从API version 12开始，该类型支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]on('change')

on(type: 'change', callback: Callback<MediaQueryResult>): void

通过句柄向对应的查询条件注册回调，当媒体属性发生变更时会触发该回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/ucpn2b-BTh2OfuNs5a1c_w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=0324943731F25020C9224DF604B4EE18E5B29F7432BC37340AFC28D6D4C02854)

注册的回调中不允许进一步调用on或off。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 必须填写字符串'change'。 |
| callback | Callback<[MediaQueryResult](#mediaqueryresult)\> | 是 | 向媒体查询注册的回调。 |

**示例：**

详见[off('change')](#offchange)示例。

#### \[h2\]off('change')

off(type: 'change', callback?: Callback<MediaQueryResult>): void

通过句柄向对应的查询条件取消注册回调，当媒体属性发生变更时不再触发指定的回调。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 必须填写字符串'change'。 |
| callback | Callback<[MediaQueryResult](#mediaqueryresult)\> | 否 | 需要取消注册的回调，如果参数缺省则去注册该句柄下所有的回调。 |

**示例：**

```ts
import { mediaquery } from '@kit.ArkUI';

let listener: mediaquery.MediaQueryListener = mediaquery.matchMediaSync('(orientation: landscape)'); // 监听横屏事件
function onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
  if (mediaQueryResult.matches) {
    // do something here
  } else {
    // do something here
  }
}
listener.on('change', onPortrait) // 注册回调
listener.off('change', onPortrait) // 取消注册回调
```

#### MediaQueryResult

用于执行媒体查询操作。

**卡片能力：** 从API version 12开始，该类型支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| matches | boolean | 是 | 否 | 是否符合匹配条件。true表示满足查询条件，false表示不满足查询条件。 |
| media | string | 是 | 否 | 媒体事件的匹配条件。 |

#### \[h2\]示例

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/cJpWsv7USoWhNgdZ5I4keQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=8E8D3C5276C82A6B998E9D365D0B33B14928DC8C4326621AF6A6D1A2D8B78A20)

推荐通过使用[UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext)中的[getMediaQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getmediaquery)方法获取当前UI上下文关联的[MediaQuery](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery)对象。

```ts
import { mediaquery } from '@kit.ArkUI';

@Entry
@Component
struct MediaQueryExample {
  @State color: string = '#DB7093'
  @State text: string = 'Portrait'
  listener: mediaquery.MediaQueryListener = this.getUIContext().getMediaQuery().matchMediaSync('(orientation: landscape)'); // 监听横屏事件，mediaquery.matchMediaSync接口已废弃，建议使用this.getUIContext().getMediaQuery().matchMediaSync()来获取

  onPortrait(mediaQueryResult:mediaquery.MediaQueryResult) {
    if (mediaQueryResult.matches) {
      this.color = '#FFD700'
      this.text = 'Landscape'
    } else {
      this.color = '#DB7093'
      this.text = 'Portrait'
    }
  }

  aboutToAppear() {
    let portraitFunc = (mediaQueryResult: mediaquery.MediaQueryResult): void => this.onPortrait(mediaQueryResult)
    // 绑定回调函数
    this.listener.on('change', portraitFunc);
  }

  aboutToDisappear() {
    // 解绑listener中注册的回调函数
    this.listener.off('change');
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Text(this.text).fontSize(24).fontColor(this.color)
    }
    .width('100%').height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/VIX59tB8QkeZRdhnxw0F7A/zh-cn_image_0000002538180298.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=27C626118FD2F6634A5ACF4878F96ACDD177B49656062345D809E9F7F14E2804)
