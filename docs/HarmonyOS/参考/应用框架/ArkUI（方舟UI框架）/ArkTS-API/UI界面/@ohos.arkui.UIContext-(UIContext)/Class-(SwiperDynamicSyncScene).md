---
title: "Class (SwiperDynamicSyncScene)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-swiperdynamicsyncscene"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "@ohos.arkui.UIContext (UIContext)"
  - "Class (SwiperDynamicSyncScene)"
captured_at: "2026-04-17T01:47:52.967Z"
---

# Class (SwiperDynamicSyncScene)

提供Swiper组件相关帧率的配置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/zPB455y6SSmEVA2uRfd2PA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=7C905F0E7220D1BAD2AA4BA58E267029CC17BE0062F0EE8DF38002CD14A496A4)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   SwiperDynamicSyncScene继承自[DynamicSyncScene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-dynamicsyncscene)，对应Swiper的动态帧率场景。
    

#### 属性

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type12+ | [SwiperDynamicSyncSceneType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-e#swiperdynamicsyncscenetype12) | 是 | 否 | Swiper的动态帧率场景。 |

**示例：**

```ts
import { SwiperDynamicSyncSceneType, SwiperDynamicSyncScene } from '@kit.ArkUI';

@Entry
@Component
struct Frame {
  @State ANIMATION: ExpectedFrameRateRange = { min: 0, max: 120, expected: 90 };
  @State GESTURE: ExpectedFrameRateRange = { min: 0, max: 120, expected: 30};
  private scenes: SwiperDynamicSyncScene[] = [];

  build() {
    Column() {
      Text("动画"+ JSON.stringify(this.ANIMATION))
      Text("跟手"+ JSON.stringify(this.GESTURE))
      Row(){
        Swiper() {
          Text("one")
          Text("two")
          Text("three")
        }
        .width('100%')
        .height('300vp')
        .id("dynamicSwiper")
        .backgroundColor(Color.Blue)
        .autoPlay(true)
        .onAppear(()=>{
          let scenes = this.getUIContext().requireDynamicSyncScene("dynamicSwiper") as SwiperDynamicSyncScene[];
          if (scenes) {
            this.scenes = scenes;
          }
        })
      }

      Button("set frame")
        .onClick(() => {
          this.scenes.forEach((scenes: SwiperDynamicSyncScene) => {

            if (scenes.type == SwiperDynamicSyncSceneType.ANIMATION) {
              scenes.setFrameRateRange(this.ANIMATION);
            }

            if (scenes.type == SwiperDynamicSyncSceneType.GESTURE) {
              scenes.setFrameRateRange(this.GESTURE);
            }
          });
        })
    }
  }
}
```
