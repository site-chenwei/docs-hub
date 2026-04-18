---
title: "MultiWindowEntryInAPP"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-multiwindowentryinapp-api"
menu_path:
  - "参考"
  - "应用框架"
  - "UI Design Kit（UI设计套件）"
  - "ArkTS组件"
  - "MultiWindowEntryInAPP"
captured_at: "2026-04-17T01:48:17.184Z"
---

# MultiWindowEntryInAPP

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/7bX7Q6VsRNKsN_4pR4vtMw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014817Z&HW-CC-Expire=86400&HW-CC-Sign=BCA977AB8F4DBBC840D4242BC45F41E0D5F066B75A1664A2F8A22B50DDA0EBAB)

依赖全景多窗特性，只有当前设备及屏幕状态支持全景多窗，才支持设置此功能。目前支持全景多窗的设备形态有：

-   双折叠：展开态。
    
-   三折叠：双屏态，三屏态的横屏态。
    
-   平板：横屏态。
    

对于不支持的设备形态，该组件不可交互，不响应点击事件。

MultiWindowEntryInAPP组件承载单应用多窗口并行逻辑的实现，应用开发者结合本应用业务特点，通过MultiWindowEntryInAPP实现一个应用多个窗口任务并行场景的开发。

**设备行为差异：** 该组件在Phone、Tablet设备中上述特定设备形态下可正常使用，在其他设备中不可交互。

**起始版本：** 6.0.0(20)

#### 导入模块

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/LSvHcmdzR0i4mSMlEDBk4w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014817Z&HW-CC-Expire=86400&HW-CC-Sign=62CC80007CE44548F4756132BF296CA7CE9CA004F1A43835B380B404C4B3192B)

-   MultiWindowEntryInAPPAttribute是用于配置MultiWindowEntryInAPP组件属性的关键接口。6.0.1(21)及之前版本，导入MultiWindowEntryInAPP组件后需要开发者手动导入MultiWindowEntryInAPPAttribute，否则会编译报错。从6.0.2(22)版本开始，编译工具链识别到导入MultiWindowEntryInAPP组件后，会自动导入MultiWindowEntryInAPPAttribute，无需开发者手动导入。
-   如果开发者手动导入MultiWindowEntryInAPPAttribute，DevEco Studio会显示置灰，6.0.1(21)及之前版本删除会编译报错，从6.0.2(22)版本开始，删除对功能无影响。

6.0.1(21)及之前版本：

```typescript
import { MultiWindowEntryInAPP, MultiWindowEntryInAPPParams, MultiWindowEntryInAPPIconOptions, MultiWindowEntryInAPPSubtitleOptions, MultiWindowEntryInAPPAttribute } from '@kit.UIDesignKit';
```

6.0.2(22)及之后版本：

```typescript
import { MultiWindowEntryInAPP, MultiWindowEntryInAPPParams, MultiWindowEntryInAPPIconOptions, MultiWindowEntryInAPPSubtitleOptions } from '@kit.UIDesignKit';
```

#### 子组件

无

#### 接口

MultiWindowEntryInAPP(params: MultiWindowEntryInAPPParams)

创建应用内多窗组件接口。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| params | [MultiWindowEntryInAPPParams](#multiwindowentryinappparams) | 是 | 应用内多窗组件参数。 |

#### MultiWindowEntryInAPPParams

MultiWindowEntryInAPP组件参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 否 | 否 | 
要启动窗口的参数，有以下要求：

1\. 必填字段：abilityName, moduleName和bundleName；

2\. 应用限制：所有指定的名称（abilityName, moduleName 和bundleName）必须属于当前应用；

3\. 跨应用限制：多窗口功能不支持跨应用的能力。

 |
| isShowSubtitle | boolean | 否 | 是 | 

是否显示组件文本标题。

true：显示默认文本标题。

false：不显示默认文本标题。

默认值：false。

 |
| multiWindowEntryInAPPStyle | [MultiWindowEntryInAPPStyle](#multiwindowentryinappstyle) | 否 | 是 | 组件风格参数。 |

#### MultiWindowEntryInAPPStyle

MultiWindowEntryInAPP组件风格参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| iconOptions | [MultiWindowEntryInAPPIconOptions](#multiwindowentryinappiconoptions) | 否 | 是 | 组件图标参数。 |
| subtitleOptions | [MultiWindowEntryInAPPSubtitleOptions](#multiwindowentryinappsubtitleoptions) | 否 | 是 | 组件文本标题参数。 |

#### MultiWindowEntryInAPPIconOptions

MultiWindowEntryInAPP组件图标参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| iconColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 
组件图标颜色。

默认值：$r('sys.color.font\_primary')。

 |
| iconWeight | number | [FontWeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#fontweight) | string | 否 | 是 | 

组件图标粗细。

默认值：400。

**说明**：

\- number类型取值\[100,900\]，取值间隔为100，默认为400，取值越大，字体越粗。

\- string类型仅支持number类型取值的字符串形式，例如“400”，以及“Bold”、“Bolder”、“Lighter”、“Regular” 、“Medium”分别对应FontWeight中相应的枚举值。

 |
| iconSize | number | string | [Resource](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resource) | 否 | 是 | 

组件图标尺寸。

默认值：24\*24 vp。

**说明**：暂不支持百分比。

 |
| backgroundColor | [ResourceColor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types#resourcecolor) | 否 | 是 | 

组件背景颜色。

默认值：$r('sys.color.comp\_background\_tertiary')。

 |

#### MultiWindowEntryInAPPSubtitleOptions

MultiWindowEntryInAPP组件标题文本参数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.UIDesign.HDSComponent.Core

**起始版本：** 6.0.0(20)

**参数：**

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| modifier | [TextModifier](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-attribute-modifier#自定义modifier) | 否 | 是 | 组件文本标题修改器。 |

#### 属性

支持大部分[通用属性](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-attributes)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/VQP3o3OQT4yKoCImxt0LiA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014817Z&HW-CC-Expire=86400&HW-CC-Sign=684BC11BB1C2A8BA77550DEBA3BF062DC56D428D4E6CF853DD6484AD837E31D3)

width、height、size属性暂不支持百分比。

该组件暂不支持accessibilityDescription、accessibilityText属性。

#### 事件

支持大部分[通用事件](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-component-general-events)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/nG1tijxyQTWCIlDUSdo-4g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014817Z&HW-CC-Expire=86400&HW-CC-Sign=E6141D840C52C0F32080C786CEB50764B58F6578379A5473DFE1D2E2208D7DD7)

该组件暂不支持onClick事件，如要监听点击请使用onTouch事件。

#### 示例

集成应用内多窗组件，用户点击按钮后可与应用内的其他UIAbility组成分屏或进入全景多窗。

```typescript
// 从6.0.2(22)版本开始，无需手动导入MultiWindowEntryInAPPAttribute。具体请参考MultiWindowEntryInAPP的导入模块说明。
import { MultiWindowEntryInAPP, MultiWindowEntryInAPPAttribute } from '@kit.UIDesignKit';
import { Want } from '@kit.AbilityKit';
import { TextModifier } from '@kit.ArkUI';

@Entry
@Component
struct MultiWindowEntryInAPPTest {
  @State textModifier: TextModifier = new TextModifier();
  private want: Want = {
    // 修改为当前应用的bundleName、moduleName、abilityName，启动应用内的UIAbility
    bundleName: "com.example.myapplication",
    moduleName: "entry",
    abilityName: "FuncAbility",
  };

  build() {
    Row() {
      MultiWindowEntryInAPP({
        want: this.want, isShowSubtitle: true, multiWindowEntryInAPPStyle: {
          iconOptions: {
            iconSize: 24,
            iconColor: $r('sys.color.font_primary'),
            iconWeight: FontWeight.Normal,
            backgroundColor: $r('sys.color.comp_background_tertiary')
          },
          subtitleOptions: {
            modifier: this.textModifier.fontColor(Color.Black)
          }
        }
      })
        .size({ width: 48, height: 48 })
        .position({ x: 400, y: 30 })
    }
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/BYMupa6DSEymxxFpZRsOxA/zh-cn_image_0000002538021484.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T014817Z&HW-CC-Expire=86400&HW-CC-Sign=1344C204BD1CE7E56C6C904CC95FBC4091736DB54F02624C07A0098D33E6A112)
