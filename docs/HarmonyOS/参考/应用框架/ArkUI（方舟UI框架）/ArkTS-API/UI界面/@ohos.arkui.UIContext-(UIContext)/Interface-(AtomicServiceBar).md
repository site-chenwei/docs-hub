---
title: "Interface (AtomicServiceBar)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-atomicservicebar"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "@ohos.arkui.UIContext (UIContext)"
  - "Interface (AtomicServiceBar)"
captured_at: "2026-04-17T01:47:53.102Z"
---

# Interface (AtomicServiceBar)

提供设置元服务menuBar的属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ppuL0mfcQUCtONGhETjaLg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=8998C423C0136E0EC333F26A09F4DCFF06CBD31D517E63D9AF4FDD616892AB30)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本Interface首批接口从API version 11开始支持。
    
-   以下接口需要先使用UIContext中的[getAtomicServiceBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getatomicservicebar11)方法获取到AtomicServiceBar对象，再通过该对象调用对应方法。
    
-   从API version 12开始元服务menuBar样式变更，以下接口将失效。
    

#### setVisible11+

setVisible(visible: boolean): void

通过该方法设置元服务menuBar是否可见。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/2_YPgwCrQNmfAyos6Orajw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=EC4E99B317516BD1366DA3390B8D28E82675E39C073D5733095C185111400669)

从API version 12开始元服务menuBar样式变更，menuBar默认隐藏，变为悬浮按钮，通过该接口无法改变menuBar的可见性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| visible | boolean | 是 | 元服务menuBar是否可见。true表示设置menuBar可见，false表示设置menuBar不可见。 |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setVisible(false);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```

#### setBackgroundColor11+

setBackgroundColor(color:Nullable<Color | number | string>): void

通过该方法设置元服务menuBar的背景颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Q4uUnxKXRF-JA1aJIOFcLw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=AB49C88020D7837865495EBB029DFC6FCF67B9EE78E97C5C0FBE38A883E99951)

从API version 12开始元服务menuBar样式变更，menuBar的背景默认隐藏，通过该接口无法改变menuBar的背景颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| color | Nullable<[Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#color) | number | string> | 是 | 通过该方法设置元服务menuBar的背景颜色，undefined代表使用默认颜色。number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setBackgroundColor(0x88888888);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```

#### setTitleContent11+

setTitleContent(content:string): void

通过该方法设置元服务menuBar的标题内容。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/PM-pmVnyS12l4LDcXLtbGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=CE036447034F5E270008304B37347E099CA0B61A2BB6B295B7959BAD748C12DE)

从API version 12开始元服务menuBar样式变更，menuBar的标题默认隐藏，通过该接口无法改变menuBar的标题内容。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| content | string | 是 | 元服务menuBar中的标题内容。 |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setTitleContent('text2');
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```

#### setTitleFontStyle11+

setTitleFontStyle(font:FontStyle):void

通过该方法设置元服务menuBar的字体样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/Hdxym3fHSU61Dd_mJ0Q1QA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=50D57BC395F24E5A64C2EF614E3CF6D7FAF77CFAE5D18EC2767C222A63DD96EC)

从API version 12开始元服务menuBar样式变更，menuBar的标题默认隐藏，通过该接口无法改变menuBar的字体样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| font | [FontStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontstyle) | 是 | 元服务menuBar中的字体样式。 |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setTitleFontStyle(FontStyle.Normal);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```

#### setIconColor11+

setIconColor(color:Nullable<Color | number | string>): void

通过该方法设置元服务图标的颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/573AK758TT6OzEmMAvkG6A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=FF5FBF72C9B4A1B0090C17BB2404A2E8790F94E0E8E3785DEF495FECCBCCA087)

从API version 12开始元服务menuBar样式变更，menuBar默认隐藏，悬浮按钮图标不予用户设置，通过该接口无法改变menuBar的图标颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| color | Nullable<[Color](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#color) | number | string> | 是 | 元服务图标的颜色，undefined代表使用默认颜色。number为HEX格式颜色，支持rgb或者argb，示例：0xffffff。string为rgb或者argb格式颜色，示例：'#ffffff'。 |

**示例：**

```ts
import { UIAbility } from '@kit.AbilityKit';
import { UIContext, AtomicServiceBar, window } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', 'Ability onWindowStageCreate');
    windowStage.loadContent('pages/Index', (err, data) => {
      let uiContext: UIContext = windowStage.getMainWindowSync().getUIContext();
      let atomicServiceBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
      if (atomicServiceBar != undefined) {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully.');
        atomicServiceBar.setIconColor(0x12345678);
      } else {
        hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
      }
    });
  }
}
```

#### getBarRect15+

getBarRect(): Frame

获取元服务menuBar相对窗口的布局信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/WuDOUQJVSQmdGTpDOQfzjw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=D805E11015EB6B4A39834E03C0DA8A7CE650585E8C03DC08B3B0119DF260037C)

布局信息包含了元服务menuBar的左右margin。

**元服务API：** 从API version 15开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [Frame](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-graphics#frame) | 元服务menuBar的大小和位置。 |

**示例：**

```ts
import { AtomicServiceBar } from '@kit.ArkUI';
import { hilog } from '@kit.PerformanceAnalysisKit';

@Entry
@Component
struct Index {
  build() {
    Button("getBarRect")
      .onClick(() => {
        let uiContext: UIContext = this.getUIContext();
        let currentBar: Nullable<AtomicServiceBar> = uiContext.getAtomicServiceBar();
        if (currentBar != undefined) {
          let rect = currentBar.getBarRect();
          hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar Successfully. x:'
            + rect.x + ' y:' + rect.y + ' width:' + rect.width + ' height:' + rect.height);
        } else {
          hilog.info(0x0000, 'testTag', 'Get AtomicServiceBar failed.');
        }
      })
  }
}
```
