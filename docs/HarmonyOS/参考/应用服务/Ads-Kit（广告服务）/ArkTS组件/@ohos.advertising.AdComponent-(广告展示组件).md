---
title: "@ohos.advertising.AdComponent (广告展示组件)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-adcomponent"
menu_path:
  - "参考"
  - "应用服务"
  - "Ads Kit（广告服务）"
  - "ArkTS组件"
  - "@ohos.advertising.AdComponent (广告展示组件)"
captured_at: "2026-04-17T01:48:56.416Z"
---

# @ohos.advertising.AdComponent (广告展示组件)

本模块提供展示广告的能力，覆盖了原生、贴片、开屏等广告样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/kNCr39b-RwKeowrBiAfopQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=5AD827EF033939969A5CF21D8AEEB7EBCCB5B98D17E5EDC759D1204039C64D52)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```typescript
import { AdComponent } from '@kit.AdsKit';
```

#### AdComponent

```typescript
AdComponent({
  ads: advertising.Advertisement[],
  displayOptions: advertising.AdDisplayOptions,
  interactionListener: advertising.AdInteractionListener,
  @BuilderParam adRenderer?: () => void,
  @Prop rollPlayState?: number
})
```

广告展示组件，提供展示原生、贴片、开屏等广告的能力。

**装饰器类型：**@Component

**系统能力：** SystemCapability.Advertising.Ads

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| ads | advertising.[Advertisement](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#advertisement)\[\] | 是 | 
广告对象数组。

说明：非贴片广告类型，组件只展示数组第一个数据。

元服务API：从API version 12开始，该接口支持在元服务中使用。

 |
| displayOptions | advertising.[AdDisplayOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#addisplayoptions) | 是 | 

广告展示参数。

元服务API：从API version 12开始，该接口支持在元服务中使用。

 |
| interactionListener | advertising.[AdInteractionListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-advertising#adinteractionlistener) | 是 | 

广告状态变化回调。

元服务API：从API version 12开始，该接口支持在元服务中使用。

 |
| adRenderer12+ | () => void | 否 | 

应用自渲染广告样式。应用自渲染广告样式为受限使用能力，具体请前往[流量变现官网客服支持](https://developer.huawei.com/consumer/cn/doc/monetize/kefuzhichi-0000001104461922)进行咨询。

元服务API：从API version 20开始，该接口支持在元服务中使用。

装饰器类型：@BuilderParam

 |
| rollPlayState15+ | number | 否 | 

用于对外提供贴片广告播放状态，设置1为播放，2为暂停，默认值为2，其他值为非法值，不改变之前的播放状态。在贴片广告所在页面需要通过@State关联属性，使用方法参考[示例代码](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-roll#展示广告)。

元服务API：从API version 20开始，该接口支持在元服务中使用。

装饰器类型：@Prop

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/jRXXVlqFTlOY4OJ4hT1kLg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=BC2463AB3AFED9741CAA325E36EB9E0F31393907AC49E229D83830A447A65D06)

为了保证广告能正确展示，该接口必须和请求广告接口配套使用。效果和使用方法可参考[原生广告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-native)、[贴片广告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-roll)、[开屏广告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-publisher-service-splash)接入和展示。

**示例：**

```typescript
import { AdComponent, advertising } from '@kit.AdsKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  // 请求到的广告内容
  private ads: advertising.Advertisement[] = [];
  // 广告展示参数
  private adDisplayOptions: advertising.AdDisplayOptions = {};

  build() {
    Column() {
      AdComponent({
        ads: this.ads,
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
        .height('100%')
    }
    .width('100%')
    .height('100%')
  }
}
```

#### \[h2\]build

build(): void

用于创建AdComponent对象的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Advertising.Ads
