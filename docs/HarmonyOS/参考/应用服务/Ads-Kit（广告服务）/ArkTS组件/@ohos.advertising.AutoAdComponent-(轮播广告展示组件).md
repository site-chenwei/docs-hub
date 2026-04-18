---
title: "@ohos.advertising.AutoAdComponent (轮播广告展示组件)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-autoadcomponent"
menu_path:
  - "参考"
  - "应用服务"
  - "Ads Kit（广告服务）"
  - "ArkTS组件"
  - "@ohos.advertising.AutoAdComponent (轮播广告展示组件)"
captured_at: "2026-04-17T01:48:56.447Z"
---

# @ohos.advertising.AutoAdComponent (轮播广告展示组件)

本模块提供展示轮播广告的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/hiMj1Y0-RdWLIkaNHgltEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=D00DAB68CB785CF920F7C153D5C24BA6AABD546765538530AB29ECD192326A8D)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```typescript
import { AutoAdComponent } from '@kit.AdsKit';
```

#### AutoAdComponent

```typescript
AutoAdComponent({
  adParam: advertising.AdRequestParams,
  adOptions: advertising.AdOptions,
  displayOptions: advertising.AdDisplayOptions,
  interactionListener: advertising.AdInteractionListener
})
```

用于展示轮播广告的组件。

**装饰器类型：**@Component

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | **装饰器类型** | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| adParam | advertising.[AdRequestParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#adrequestparams) | 是 | \- | 广告请求参数。 |
| adOptions | advertising.[AdOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#adoptions) | 是 | \- | 广告配置参数。 |
| displayOptions | advertising.[AdDisplayOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#addisplayoptions) | 是 | \- | 广告展示参数。 |
| interactionListener | advertising.[AdInteractionListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#adinteractionlistener) | 是 | \- | 广告状态变化回调。 |

**示例：**

```typescript
import { advertising, AutoAdComponent } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // 广告请求参数
  private adRequestParams: advertising.AdRequestParams = {
    // 广告位ID
    adId: 'testw6vs28auh3',
    // 广告类型
    adType: 8,
    // 广告位宽，单位vp
    adWidth: 360,
    // 广告位高，单位vp
    adHeight: 57
  };
  // 广告配置参数
  private adOptions: advertising.AdOptions = {};
  // 广告展示参数
  private adDisplayOptions: advertising.AdDisplayOptions = {
    // 广告轮播的时间间隔，单位ms，取值范围[30000, 120000]
    refreshTime: 30000
  };
  private ratio: number = -1;

  aboutToAppear() {
    if (this.adRequestParams.adWidth && this.adRequestParams.adHeight) {
      this.ratio = this.adRequestParams.adWidth / this.adRequestParams.adHeight;
    }
  }
  
  build() {
    Column() {
      AutoAdComponent({
        adParam: this.adRequestParams,
        adOptions: this.adOptions,
        displayOptions: this.adDisplayOptions,
        interactionListener: {
          onStatusChanged: (status: string, ad: advertising.Advertisement, data: string) => {
            switch (status) {
              case 'onAdOpen':
                hilog.info(0x0000, 'testTag', 'onAdOpen');
                break;
              case 'onAdClick':
                hilog.info(0x0000, 'testTag', 'onAdClick');
                break;
              case 'onAdClose':
                hilog.info(0x0000, 'testTag', 'onAdClose');
                break;
            }
          }
        }
      })
        .width('100%')
        .aspectRatio(this.ratio)
    }
    .width('100%')
    .height('100%')
  }
}
```

**效果图：**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/VACYt7rCSmKGitGZ1sn5vQ/zh-cn_image_0000002568899413.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=0BFE7DF636BAF18382A53E14645B7D902746D1317DA95EAE399EB17CF427552F)

#### \[h2\]build

build(): void

用于创建AutoAdComponent对象的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads
