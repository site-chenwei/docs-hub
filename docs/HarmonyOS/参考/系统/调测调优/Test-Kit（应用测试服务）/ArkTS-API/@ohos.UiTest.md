---
title: "@ohos.UiTest"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest"
menu_path:
  - "参考"
  - "系统"
  - "调测调优"
  - "Test Kit（应用测试服务）"
  - "ArkTS API"
  - "@ohos.UiTest"
captured_at: "2026-04-17T01:48:35.781Z"
---

# @ohos.UiTest

UiTest提供模拟UI操作的能力，供开发者在测试场景使用，主要支持如点击、双击、长按、滑动等UI操作能力。

该模块提供以下功能：

-   [On9+](#on9)：提供控件特征描述能力，用于控件筛选匹配查找。
-   [Component9+](#component9)：代表UI界面上的指定控件，提供控件属性获取，控件点击，滑动查找，文本注入等能力。
-   [Driver9+](#driver9)：入口类，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。
-   [UiWindow9+](#uiwindow9)：入口类，提供窗口属性获取，窗口拖动、调整窗口大小等能力。
-   [By(deprecated)](#bydeprecated)：提供控件特征描述能力，用于控件筛选匹配查找。从API version 8开始支持，从API version 9开始废弃，建议使用[On9+](#on9)替代。
-   [UiComponent(deprecated)](#uicomponentdeprecated)：代表UI界面上的指定控件，提供控件属性获取，控件点击，滑动查找，文本注入等能力。从API version 8开始支持，从API version 9开始废弃，建议使用[Component9+](#component9)替代。
-   [UiDriver(deprecated)](#uidriverdeprecated)：入口类，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。从API version 8开始支持，从API version 9开始废弃，建议使用[Driver9+](#driver9)替代。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/gnMFhji6TeC-Se4tOl94dQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=9250A4B47E7756818695FAABD711083C7F74BA019190AE00FFE4E163B0EA2D01)

-   本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本模块接口在[自动化测试脚本](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uitest-guidelines#使用arkts接口进行ui测试)中使用。
-   本模块接口不支持并发调用。

#### 导入模块

```ts
import { Component, Driver, UiWindow, ON, MatchPattern, DisplayRotation, ResizeDirection, WindowMode, PointerMatrix, UiDirection, MouseButton, UIElementInfo, UIEventObserver, UiComponent, UiDriver, BY } from '@kit.TestKit';
```

#### MatchPattern

控件属性支持的匹配模式。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| EQUALS | 0 | 
等于给定值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| CONTAINS | 1 | 

包含给定值。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| STARTS\_WITH | 2 | 

以给定值开始。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| ENDS\_WITH | 3 | 

以给定值结束。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| REG\_EXP18+ | 4 | 

正则表达式匹配。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 |
| REG\_EXP\_ICASE18+ | 5 | 

正则表达式匹配，忽略大小写。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

 |

#### ResizeDirection9+

窗口调整大小的方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| LEFT | 0 | 左方。 |
| RIGHT | 1 | 右方。 |
| UP | 2 | 上方。 |
| DOWN | 3 | 下方。 |
| LEFT\_UP | 4 | 左上方。 |
| LEFT\_DOWN | 5 | 左下方。 |
| RIGHT\_UP | 6 | 右上方。 |
| RIGHT\_DOWN | 7 | 右下方。 |

#### Point9+

坐标点信息。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| x | number | 否 | 否 | 
坐标点的横坐标，取值大于0的整数。

**说明：** 从API version 20开始，该属性不再为只读属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| y | number | 否 | 否 | 

坐标点的纵坐标，取值大于0的整数。

**说明：** 从API version 20开始，该属性不再为只读属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| displayId20+ | number | 否 | 是 | 

坐标点所属的屏幕ID，取值范围：大于等于0的整数。默认值为设备默认屏幕ID。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 |

#### Rect9+

控件的边框信息。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| left | number | 否 | 否 | 
控件边框的左上角的X坐标，取值大于0的整数。

**说明：** 从API version 20开始，该属性不再为只读属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| top | number | 否 | 否 | 

控件边框的左上角的Y坐标，取值大于0的整数。

**说明：** 从API version 20开始，该属性不再为只读属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| right | number | 否 | 否 | 

控件边框的右下角的X坐标，取值大于0的整数。

**说明：** 从API version 20开始，该属性不再为只读属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| bottom | number | 否 | 否 | 

控件边框的右下角的Y坐标，取值大于0的整数。

**说明：** 从API version 20开始，该属性不再为只读属性。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| displayId20+ | number | 否 | 是 | 

控件边框所属的屏幕ID，取值大于或等于0的整数。默认值为设备默认屏幕ID。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 |

#### WindowMode9+

窗口的窗口模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| FULLSCREEN | 0 | 全屏模式。 |
| PRIMARY | 1 | 主窗口。 |
| SECONDARY | 2 | 第二窗口。 |
| FLOATING | 3 | 浮动窗口。 |

#### DisplayRotation9+

设备显示器的显示方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| ROTATION\_0 | 0 | 设备显示器不旋转，初始形态垂直显示。 |
| ROTATION\_90 | 1 | 设备显示器顺时针旋转90°，水平显示。 |
| ROTATION\_180 | 2 | 设备显示器顺时针旋转180°，逆向垂直显示。 |
| ROTATION\_270 | 3 | 设备显示器顺时针旋转270°，逆向水平显示。 |

#### WindowFilter9+

窗口的标志属性信息。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | 否 | 是 | 
窗口归属应用的包名，默认值为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| title | string | 否 | 是 | 

窗口的标题信息，默认值为空。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| focused | boolean | 否 | 是 | 

窗口是否处于获焦状态，true：获焦状态，false：未获焦状态，默认值为false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| actived(deprecated) | boolean | 否 | 是 | 

窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。

从API version 11开始废弃，建议使用active替代。

 |
| active11+ | boolean | 否 | 是 | 

窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| displayId20+ | number | 否 | 是 | 

窗口所属的屏幕ID。取值大于或等于0的整数。默认值为设备默认屏ID。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

 |

#### UiDirection10+

进行抛滑等UI操作时的方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| LEFT | 0 | 向左。 |
| RIGHT | 1 | 向右。 |
| UP | 2 | 向上。 |
| DOWN | 3 | 向下。 |

#### MouseButton10+

模拟注入的鼠标按钮。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| MOUSE\_BUTTON\_LEFT | 0 | 鼠标左键。 |
| MOUSE\_BUTTON\_RIGHT | 1 | 鼠标右键。 |
| MOUSE\_BUTTON\_MIDDLE | 2 | 鼠标中间键。 |

#### WindowChangeType22+

支持监听的窗口变化事件类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| WINDOW\_UNDEFINED | 0 | 
非窗口变化事件。

**说明：** 该枚举值仅支持作为返回值，如果作为接口入参会抛出异常。

 |
| WINDOW\_ADDED | 1 | 窗口出现事件。 |
| WINDOW\_REMOVED | 2 | 窗口消失事件。 |
| WINDOW\_BOUNDS\_CHANGED | 3 | 窗口边框变化事件。 |

#### ComponentEventType22+

支持监听的控件操作事件类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| COMPONENT\_UNDEFINED | 0 | 
非控件操作事件。

**说明：** 该枚举值仅支持作为返回值，如果作为接口入参会抛出异常。

 |
| COMPONENT\_CLICKED | 1 | 控件被点击事件。 |
| COMPONENT\_LONG\_CLICKED | 2 | 控件被长按事件。 |
| COMPONENT\_SCROLL\_START | 3 | 控件滚动开始事件。 |
| COMPONENT\_SCROLL\_END | 4 | 控件滚动结束事件。 |
| COMPONENT\_TEXT\_CHANGED | 5 | [输入框控件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-components-text-input)文本变化事件。 |

#### WindowChangeOptions22+

窗口变化事件监听的扩展配置，用于指定监听过程配置及事件筛选条件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| timeout | number | 否 | 是 | 监听超时时间，默认值为10000，单位：ms。 |
| bundleName | string | 否 | 是 | 监听窗口对应包名，缺省时默认监听所有窗口。 |

#### ComponentEventOptions22+

控件操作事件监听的扩展配置，用于指定监听过程配置及事件筛选条件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| timeout | number | 否 | 是 | 监听超时时间，默认值为10000，单位：ms。 |
| on | [On](#on9) | 否 | 是 | 
监听目标控件的属性要求，默认监听所有控件。

**说明：** 仅支持监听指定属性要求的控件，不支持监听指定On.isBefore、On.isAfter、On.within等相对位置的控件。

 |

#### UIElementInfo10+

UI事件的相关信息。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 否 | 
应用包名。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| type | string | 是 | 否 | 

控件/窗口类型。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| text | string | 是 | 否 | 

控件/窗口的文本信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| windowChangeType22+ | [WindowChangeType](#windowchangetype22) | 是 | 是 | 

窗口变化事件类型，若非窗口变化事件返回WindowChangeType.WINDOW\_UNDEFINED。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 |
| componentEventType22+ | [ComponentEventType](#componenteventtype22) | 是 | 是 | 

控件操作事件类型，若非控件操作事件返回ComponentEventType.COMPONENT\_UNDEFINED。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 |
| windowId22+ | number | 是 | 是 | 

控件所属窗口id。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 |
| componentId22+ | string | 是 | 是 | 

控件id，若非控件操作事件返回空字符串。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 |
| componentRect22+ | [Rect](#rect9) | 是 | 是 | 

控件边框信息，若非控件操作事件则返回属性值均为0的Rect对象。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

 |

#### TouchPadSwipeOptions18+

触摸板多指滑动手势选项相关信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| stay | boolean | 否 | 是 | 触摸板多指滑动结束是否停留1s后再抬起，默认为false（不停留1s），true：停留，false：不停留。 |
| speed | number | 否 | 是 | 滑动速率，取值范围为200-40000的整数，默认值为2000，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值2000。为负数时抛出参数错误的错误码。 |

#### InputTextMode20+

输入文本的方式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| paste | boolean | 否 | 是 | 
输入文本时是否指定以复制粘贴方式输入。true：指定以复制粘贴方式输入。false：指定以逐字键入方式输入。默认为false。

**说明：** 当输入文本中包含中文、特殊字符或文本长度超过200字符时，无论该参数取值为何，均以复制粘贴方式输入。

 |
| addition | boolean | 否 | 是 | 输入文本时是否以追加的方式进行输入。true：以追加方式输入。false：不以追加方式输入。默认为false。 |

#### On9+

UiTest框架从API version 9开始，通过On类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。

On提供的API能力具有以下几个特点:

1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。

2、控件属性支持多种匹配模式。

3、支持控件绝对定位，相对定位，可通过[ON.isBefore](#isbefore9)和[ON.isAfter](#isafter9)等API限定邻近控件特征进行辅助定位。

On类提供的所有API均为同步接口，建议使用者通过静态构造器ON来链式创建On对象。

```ts
// xxx.test.ets
import { ON } from '@kit.TestKit';

ON.text('123').type('Button');
```

#### \[h2\]text9+

text(txt: string, pattern?: MatchPattern): On

指定目标控件文本属性，支持多种匹配模式，返回On对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/J2Ee6sr2QXmLV3U7yGl12A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=1322F1A47D5FCEE7841FA6A4ABFF8BDE5CAE0C055C221D26B39450827A9F720F)

如果控件的无障碍属性[accessibilityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitylevel)设置为'no'或'no-hide-descendants'，无法使用本接口指定目标控件的文本属性用于查找控件，可以使用[On.originalText()](#originaltext20)接口实现。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| txt | string | 是 | 指定控件文本，用于匹配目标控件文本。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件文本属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.text('123'); // 使用静态构造器ON创建On对象，指定目标控件的text属性。
```

#### \[h2\]id9+

id(id: string): On

指定目标控件id属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| id | string | 是 | 指定控件的id值。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件id属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.id('123'); // 使用静态构造器ON创建On对象，指定目标控件的id属性。
```

#### \[h2\]id18+

id(id: string, pattern: MatchPattern): On

指定目标控件id属性和匹配模式，返回On对象自身。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| id | string | 是 | 指定控件的id值。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](#matchpattern) | 是 | 指定的文本匹配模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件id属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.id('id', MatchPattern.REG_EXP_ICASE); // 忽略大小写匹配控件的id属性值
```

#### \[h2\]type9+

type(tp: string): On

指定目标控件的控件类型属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tp | string | 是 | 指定控件类型。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的控件类型属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.type('Button'); // 使用静态构造器ON创建On对象，指定目标控件的控件类型属性。
```

#### \[h2\]type18+

type(tp: string, pattern: MatchPattern): On

指定目标控件的控件类型属性和匹配模式，返回On对象自身。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tp | string | 是 | 指定控件类型。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](#matchpattern) | 是 | 指定的文本匹配模式。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的控件类型属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON, MatchPattern } from '@kit.TestKit';

let on: On = ON.type('Button', MatchPattern.EQUALS); // 使用静态构造器ON创建On对象，指定目标控件的控件类型属性。
```

#### \[h2\]clickable9+

clickable(b?: boolean): On

指定目标控件的可点击状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件可点击状态。true：可点击。false：不可点击。默认为true。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的可点击状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.clickable(true); // 使用静态构造器ON创建On对象，指定目标控件的可点击状态属性。
```

#### \[h2\]longClickable9+

longClickable(b?: boolean): On

指定目标控件的可长按点击状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件可长按点击状态。true：可长按点击。false：不可长按点击。默认为true。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的可长按点击状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.longClickable(true); // 使用静态构造器ON创建On对象，指定目标控件的可长按点击状态属性。
```

#### \[h2\]scrollable9+

scrollable(b?: boolean): On

指定目标控件的可滑动状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 控件可滑动状态。true：可滑动。false：不可滑动。默认为true。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的可滑动状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.scrollable(true); // 使用静态构造器ON创建On对象，指定目标控件的可滑动状态属性。
```

#### \[h2\]enabled9+

enabled(b?: boolean): On

指定目标控件的使能状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件使能状态。true：使能。false：未使能。默认为true。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的使能状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.enabled(true); // 使用静态构造器ON创建On对象，指定目标控件的使能状态属性。
```

#### \[h2\]focused9+

focused(b?: boolean): On

指定目标控件的获焦状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 控件获焦状态。true：获焦。false：未获焦。默认为true。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的获焦状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.focused(true); // 使用静态构造器ON创建On对象，指定目标控件的获焦状态属性。
```

#### \[h2\]selected9+

selected(b?: boolean): On

指定目标控件的被选中状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件被选中状态。true：被选中。false：未被选中。默认为true。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的被选中状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.selected(true); // 使用静态构造器ON创建On对象，指定目标控件的被选中状态属性。
```

#### \[h2\]checked9+

checked(b?: boolean): On

指定目标控件的被勾选状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件被勾选状态。true：被勾选。false：未被勾选。默认为true。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件的被勾选状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.checked(true); // 使用静态构造器ON创建On对象，指定目标控件的被勾选状态属性
```

#### \[h2\]checkable9+

checkable(b?: boolean): On

指定目标控件能否被勾选状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件能否被勾选状态。true：能被勾选。false：不能被勾选。默认为true。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件能否被勾选状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.checkable(true); // 使用静态构造器ON创建On对象，指定目标控件的能否被勾选状态属性。
```

#### \[h2\]isBefore9+

isBefore(on: On): On

指定目标控件位于给出的特征属性控件之前，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 特征控件的属性要求。 可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件树，以判断控件间位置关系。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件位于给出的特征属性控件之前的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之前。
let on: On = ON.type('Button').isBefore(ON.text('123')); // 查找text为123之前的第一个Button组件
```

#### \[h2\]isAfter9+

isAfter(on: On): On

指定目标控件位于给出的特征属性控件之后，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 特征控件的属性要求。 可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件树，以判断控件间位置关系。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件位于给出的特征属性控件之后的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之后。
let on: On = ON.type('Text').isAfter(ON.text('123')); // 查找 text为123之后的第一个Text组件
```

#### \[h2\]within10+

within(on: On): On

指定目标控件位于给出的特征属性控件之内，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 特征控件的属性要求。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件树，以判断控件间位置关系。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件位于给出的特征属性控件内的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

// 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之内。
let on: On = ON.text('java').within(ON.type('Scroll')); // 查找Scroller里面的text为java的子组件
```

#### \[h2\]inWindow10+

inWindow(bundleName: string): On

指定目标控件位于给出的应用窗口内，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用窗口的包名。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件位于给出的应用窗口内的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.inWindow('com.uitestScene.acts'); // 使用静态构造器ON创建On对象，指定目标控件位于给出的应用窗口内。
```

#### \[h2\]description11+

description(val: string, pattern?: MatchPattern): On

指定目标控件的描述属性，支持多种匹配模式，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | string | 是 | 控件的描述属性。 可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件description属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.description('123'); // 使用静态构造器ON创建On对象，指定目标控件的description属性。
```

#### \[h2\]hint18+

hint(val: string, pattern?: MatchPattern): On

获取指定提示文本的控件对象，返回On对象自身。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| val | string | 是 | 指定控件提示文本。 可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定提示文本控件的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { MatchPattern, On, ON } from '@kit.TestKit';

let on: On = ON.hint('welcome', MatchPattern.EQUALS); // 使用静态构造器ON创建On对象，指定目标控件的提示文本属性。
```

#### \[h2\]belongingDisplay20+

belongingDisplay(displayId: number): On

获取指定屏幕内的控件对象，返回On对象自身。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 是 | 
指定控件所属屏幕ID，取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。可通过[getAllDisplays](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-display#displaygetalldisplays9)获取当前所有的display对象，并由display对象获取对应的屏幕ID。可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定控件所属屏幕的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.belongingDisplay(0); // 使用静态构造器ON创建On对象，指定目标控件所属屏幕ID
```

#### \[h2\]originalText20+

originalText(text: string, pattern?: MatchPattern): On

指定控件的文本内容和文本匹配模式，返回On对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/ZhwaDiPIQqagirmhT2RDNw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=AEC1FA4927B5ED10CD4F7002AD3383F1DA223E677AFF4D7218424029698ED3B4)

如果控件的无障碍属性[accessibilityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitylevel)设置为'no'或'no-hide-descendants'，可以使用本接口指定目标控件的文本属性用于查找控件，使用[On.text()](#text9)接口不生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 指定控件文本，用于匹配目标控件文本。 可以借助[DevEco Testing](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deveco-testing)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [On](#on9) | 返回指定目标控件文本属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { On, ON } from '@kit.TestKit';

let on: On = ON.originalText('123'); // 使用静态构造器ON创建On对象，指定目标控件的originalText属性
```

#### Component9+

UiTest框架在API9中，Component类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。

该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

#### \[h2\]click9+

click(): Promise<void>

控件对象进行点击操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, ON, Component } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.click();
}
```

#### \[h2\]doubleClick9+

doubleClick(): Promise<void>

控件对象进行双击操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.doubleClick();
}
```

#### \[h2\]longClick9+

longClick(): Promise<void>

控件对象进行长按操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  await button.longClick();
}
```

#### \[h2\]getId9+

getId(): Promise<string>

获取控件对象的id值。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的id值。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let id = await button.getId();
}
```

#### \[h2\]getText9+

getText(): Promise<string>

获取控件对象的文本信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/hOQO2zuxRzSuhUYav5WZog/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=5B14841C716A4D0BFA005D4E204FFDE7270774D4CBE3559A8A2E27D90BE673B0)

如果控件的无障碍属性[accessibilityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitylevel)设置为'no'或'no-hide-descendants'，无法使用本接口获取控件的文本信息，可以使用[Component.getOriginalText()](#getoriginaltext20)获取控件的文本信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text = await button.getText();
}
```

#### \[h2\]getType9+

getType(): Promise<string>

获取控件对象的控件类型。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的类型。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let type = await button.getType();
}
```

#### \[h2\]getBounds9+

getBounds(): Promise<Rect>

获取控件对象的边框信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Rect](#rect9)\> | Promise对象，返回控件对象的边框信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let rect = await button.getBounds();
}
```

#### \[h2\]getBoundsCenter9+

getBoundsCenter(): Promise<Point>

获取控件对象所占区域的中心点信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise对象，返回控件对象所占区域的中心点信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let point = await button.getBoundsCenter();
}
```

#### \[h2\]isClickable9+

isClickable(): Promise<boolean>

获取控件对象可点击属性。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象是否可点击。true：可点击。false：不可点击。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isClickable()) {
    console.info('This button can be Clicked');
  } else {
    console.info('This button can not be Clicked');
  }
}
```

#### \[h2\]isLongClickable9+

isLongClickable(): Promise<boolean>

获取控件对象可长按点击属性。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象是否可长按点击。true：可长按点击。false：不可长按点击。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isLongClickable()) {
    console.info('This button can longClick');
  } else {
    console.info('This button can not longClick');
  }
}
```

#### \[h2\]isChecked9+

isChecked(): Promise<boolean>

获取控件对象被勾选状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象被勾选状态。true：被勾选。false：未被勾选。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
  if (await checkBox.isChecked()) {
    console.info('This checkBox is checked');
  } else {
    console.info('This checkBox is not checked');
  }
}
```

#### \[h2\]isCheckable9+

isCheckable(): Promise<boolean>

获取控件对象能否被勾选属性。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象能否可被勾选属性。true：可被勾选。false：不可被勾选。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
  if (await checkBox.isCheckable()) {
    console.info('This checkBox is checkable');
  } else {
    console.info('This checkBox is not checkable');
  }
}
```

#### \[h2\]isScrollable9+

isScrollable(): Promise<boolean>

获取控件对象可滑动属性。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象是否可滑动。true：可滑动。false：不可滑动。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.scrollable(true));
  if (await scrollBar.isScrollable()) {
    console.info('This scrollBar can be operated');
  } else {
    console.info('This scrollBar can not be operated');
  }
}
```

#### \[h2\]isEnabled9+

isEnabled(): Promise<boolean>

获取控件使能状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件使能状态。true：使能。false：未使能。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button can not be operated');
  }
}
```

#### \[h2\]isFocused9+

isFocused(): Promise<boolean>

判断控件对象获焦状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象获焦状态。true：获焦。false：未获焦。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}
```

#### \[h2\]isSelected9+

isSelected(): Promise<boolean>

获取控件对象被选中状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象被选中状态。true：被选中。false：未被选中。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  if (await button.isSelected()) {
    console.info('This button is selected');
  } else {
    console.info('This button is not selected');
  }
}
```

#### \[h2\]inputText9+

inputText(text: string): Promise<void>

清空组件内原有文本并输入指定文本内容，仅针对可编辑的文本组件生效。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123');
}
```

#### \[h2\]inputText20+

inputText(text: string, mode: InputTextMode): Promise<void>

向控件中输入文本，并支持指定文本输入方式，仅针对可编辑的文本组件生效。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |
| mode | [InputTextMode](#inputtextmode20) | 是 | 
输入文本的方式，取值请参考[InputTextMode](#inputtextmode20)。

**说明：** InputTextMode.addition取值为true时，在控件已有文本末尾后追加指定文本。取值为false时，指定文本将覆盖控件已有文本。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported, function can not work correctly due to limited device capabilities. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function mode_demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.inputText('123', { paste: true, addition: false });
}
```

#### \[h2\]clearText9+

clearText(): Promise<void>

清除控件的文本信息，仅针对可编辑的文本组件生效。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await text.clearText();
}
```

#### \[h2\]scrollSearch9+

scrollSearch(on: On): Promise<Component>

在控件上滑动查找目标控件（适用支持滑动的控件）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Component](#component9)\> | Promise对象，返回目标控件对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}
```

#### \[h2\]scrollSearch18+

scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>

在控件上滑动查找目标控件（适用支持滑动的控件），支持指定滑动方向和滑动起止点与组件边框的偏移量。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |
| vertical | boolean | 否 | 默认为true，表示查找方向是纵向。false表示查找方向为横向。 |
| offset | number | 否 | 滑动起点/终点到组件边框的偏移，默认80，单位：px，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Component](#component9)\> | Promise对象，返回目标控件对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  let button = await scrollBar.scrollSearch(ON.text('next page'));
}
```

#### \[h2\]scrollToTop9+

scrollToTop(speed?: number): Promise<void>

在控件上滑动到顶部（适用支持滑动的控件）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToTop();
}
```

#### \[h2\]scrollToBottom9+

scrollToBottom(speed?: number): Promise<void>

在控件上滑动到底部（适用支持滑动的控件）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
  await scrollBar.scrollToBottom();
}
```

#### \[h2\]dragTo9+

dragTo(target: Component): Promise<void>

将控件拖拽至目标控件处。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| target | [Component](#component9) | 是 | 目标控件。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text: Component = await driver.findComponent(ON.text('hello world'));
  await button.dragTo(text);
}
```

#### \[h2\]pinchOut9+

pinchOut(scale: number): Promise<void>

将控件按指定的比例进行捏合放大。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| scale | number | 是 | 指定放大的比例。取值范围大于1。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component = await driver.findComponent(ON.type('Image'));
  await image.pinchOut(1.5);
}
```

#### \[h2\]pinchIn9+

pinchIn(scale: number): Promise<void>

将控件按指定的比例进行捏合缩小。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| scale | number | 是 | 指定缩小的比例。取值范围为0~1。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let image: Component = await driver.findComponent(ON.type('Image'));
  await image.pinchIn(0.5);
}
```

#### \[h2\]getDescription11+

getDescription(): Promise<string>

获取控件对象的描述信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的描述信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let description = await button.getDescription();
}
```

#### \[h2\]getHint18+

getHint(): Promise<string>

获取控件对象的提示文本。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的提示文本。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('TextInput'));
  let hints = await button.getHint();
}
```

#### \[h2\]getDisplayId20+

getDisplayId(): Promise<number>

获取控件对象所属的屏幕ID。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回控件所属的屏幕ID。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('TextInput'));
  let displayId = await button.getDisplayId();
}
```

#### \[h2\]getOriginalText20+

getOriginalText(): Promise<string>

获取控件对象的文本信息。使用Promise异步回调。如果控件的无障碍属性[accessibilityLevel](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-accessibility#accessibilitylevel)设置为'no'或'no-hide-descendants'，可以使用本接口获取控件的文本信息，无法使用[Component.getText()](#gettext9)获取控件的文本信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.type('Button'));
  let text = await button.getOriginalText();
}
```

#### Driver9+

Driver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。

该类提供的方法除Driver.create()以外的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

#### \[h2\]create9+

static create(): Driver

静态方法，构造一个Driver对象，并返回该对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Driver | 返回构造的Driver对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000001 | Initialization failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
}
```

#### \[h2\]delayMs9+

delayMs(duration: number): Promise<void>

在给定的时间内延时。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| duration | number | 是 | 给定的时间，单位：ms，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.delayMs(1000);
}
```

#### \[h2\]findComponent9+

findComponent(on: On): Promise<Component>

根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Component](#component9)\> | Promise对象，返回控件对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.findComponent(ON.text('next page'));
}
```

#### \[h2\]findComponents9+

findComponents(on: On): Promise<Array<Component>>

根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[Component](#component9)\>> | Promise对象，返回控件对象的列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let buttonList: Array<Component> = await driver.findComponents(ON.text('next page'));
}
```

#### \[h2\]findWindow9+

findWindow(filter: WindowFilter): Promise<UiWindow>

通过指定窗口的属性来查找目标窗口。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| filter | [WindowFilter](#windowfilter9) | 是 | 目标窗口的属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[UiWindow](#uiwindow9)\> | Promise对象，返回目标窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
}
```

#### \[h2\]waitForComponent9+

waitForComponent(on: On, time: number): Promise<Component>

在用户给定的时间内，持续查找满足控件属性要求的目标控件。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |
| time | number | 是 | 查找目标控件的持续时间。单位ms，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Component](#component9)\> | Promise对象，返回控件对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let button: Component = await driver.waitForComponent(ON.text('next page'), 500);
}
```

#### \[h2\]assertComponentExist9+

assertComponentExist(on: On): Promise<void>

断言API，用于断言当前界面是否存在满足给出的目标属性的控件。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000003 | Assertion failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.assertComponentExist(ON.text('next page'));
}
```

#### \[h2\]pressBack9+

pressBack(): Promise<void>

进行点击BACK键的操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack();
}
```

#### \[h2\]pressBack20+

pressBack(displayId: number): Promise<void>

对指定屏幕进行点击BACK键的操作。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 是 | 
指定的屏幕ID，取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressBack(0);
}
```

#### \[h2\]triggerKey9+

triggerKey(keyCode: number): Promise<void>

传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyCode | number | 是 | 指定的key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // 返回键
}
```

#### \[h2\]triggerKey20+

triggerKey(keyCode: number, displayId: number): Promise<void>

在指定屏幕，传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyCode | number | 是 | 指定的key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)。 |
| displayId | number | 是 | 
指定的屏幕ID，取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK, 0); // 返回键
}
```

#### \[h2\]triggerCombineKeys9+

triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>

通过给定的key值，找到对应组合键并点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key0 | number | 是 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)。 |
| key1 | number | 是 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)。 |
| key2 | number | 否 | 指定的第三个key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035);
}
```

#### \[h2\]triggerCombineKeys20+

triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>

通过给定的key值，找到对应组合键，并在指定屏幕下进行点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key0 | number | 是 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)。 |
| key1 | number | 是 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)。 |
| key2 | number | 否 | 指定的第三个key值，取值范围：大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |
| displayId | number | 否 | 指定的屏幕ID，取值范围：大于等于0的整数，默认值为设备默认屏幕ID。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.triggerCombineKeys(2072, 2047, 2035, 0);
}
```

#### \[h2\]click9+

click(x: number, y: number): Promise<void>

在目标坐标点单击。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.click(100, 100);
}
```

#### \[h2\]clickAt20+

clickAt(point: Point): Promise<void>

在目标坐标点进行单击。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | 是 | 以Point对象的形式传入目标点信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.clickAt({ x: 100, y: 100, displayId: 0 });
}
```

#### \[h2\]doubleClick9+

doubleClick(x: number, y: number): Promise<void>

在目标坐标点双击。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClick(100, 100);
}
```

#### \[h2\]doubleClickAt20+

doubleClickAt(point: Point): Promise<void>

对目标坐标进行双击。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | 是 | 以Point对象的形式传入目标点信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.doubleClickAt({ x: 100, y: 100, displayId: 0 });
}
```

#### \[h2\]longClick9+

longClick(x: number, y: number): Promise<void>

在目标坐标点长按。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClick(100, 100);
}
```

#### \[h2\]longClickAt20+

longClickAt(point: Point, duration?: number): Promise<void>

长按目标坐标点，支持指定长按时长。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | 是 | 以Point对象的形式传入目标点信息。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.longClickAt({ x: 100, y: 100, displayId: 0 }, 1500);
}
```

#### \[h2\]swipe9+

swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>

从起始坐标点滑向目的坐标点。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.swipe(100, 100, 200, 200, 600);
}
```

#### \[h2\]swipeBetween20+

swipeBetween(from: Point, to: Point, speed?: number): Promise<void>

从起始坐标点滑向目标坐标点。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](#point9) | 是 | 
以Point对象的形式传入终止点的坐标信息和所属屏幕ID。

**说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。

 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.swipeBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800);
}
```

#### \[h2\]drag9+

drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>

从起始坐标点拖拽至目的坐标点。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.drag(100, 100, 200, 200, 600);
}
```

#### \[h2\]dragBetween20+

dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>

从起始坐标点拖拽至目标坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](#point9) | 是 | 
以Point对象的形式传入终止点的坐标信息和所属屏幕ID。

**说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。

 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.dragBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800, 1500);
}
```

#### \[h2\]screenCap9+

screenCap(savePath: string): Promise<boolean>

捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的[沙箱路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：完成，false：未完成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
```

#### \[h2\]screenCap20+

screenCap(savePath: string, displayId: number): Promise<boolean>

捕获指定屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的[沙箱路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)。 |
| displayId | number | 是 | 
指定设备屏幕ID。取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：完成。false：未完成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png', 0);
}
```

#### \[h2\]setDisplayRotation9+

setDisplayRotation(rotation: DisplayRotation): Promise<void>

将当前场景的显示方向设置为指定的显示方向。使用Promise异步回调。适用于可旋转的应用场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| rotation | [DisplayRotation](#displayrotation9) | 是 | 设备的显示方向。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, DisplayRotation } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotation(DisplayRotation.ROTATION_180);
}
```

#### \[h2\]getDisplayRotation9+

getDisplayRotation(): Promise<DisplayRotation>

获取当前设备的屏幕显示方向。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[DisplayRotation](#displayrotation9)\> | Promise对象，返回当前设备的显示方向。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**示例：**

```ts
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation();
}
```

#### \[h2\]getDisplayRotation20+

getDisplayRotation(displayId: number): Promise<DisplayRotation>

获取当前设备指定屏幕的显示方向。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 是 | 
指定设备屏幕ID。取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[DisplayRotation](#displayrotation9)\> | Promise对象，返回指定屏幕的显示方向。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { DisplayRotation, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let rotation: DisplayRotation = await driver.getDisplayRotation(0);
}
```

#### \[h2\]setDisplayRotationEnabled9+

setDisplayRotationEnabled(enabled: boolean): Promise<void>

启用/禁用设备旋转屏幕的功能。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| enabled | boolean | 是 | 能否旋转屏幕的标识。true：可以旋转。false：不可以旋转。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.setDisplayRotationEnabled(false);
}
```

#### \[h2\]getDisplaySize9+

getDisplaySize(): Promise<Point>

获取当前设备的屏幕大小。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise对象，返回Point对象，当前设备屏幕的大小为Point.x \* Point.y。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize();
}
```

#### \[h2\]getDisplaySize20+

getDisplaySize(displayId: number): Promise<Point>

获取当前设备指定屏幕的大小。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 是 | 
指定设备屏幕ID。取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise对象，返回Point对象，当前设备指定屏幕的大小为Point.x \* Point.y。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let size = await driver.getDisplaySize(0);
}
```

#### \[h2\]getDisplayDensity9+

getDisplayDensity(): Promise<Point>

获取当前设备屏幕的分辨率。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise对象，返回Point对象，当前设备屏幕的分辨率为Point.x\*Point.y。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity();
}
```

#### \[h2\]getDisplayDensity20+

getDisplayDensity(displayId: number): Promise<Point>

获取当前设备指定屏幕的分辨率。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 是 | 
指定设备屏幕ID。取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Point](#point9)\> | Promise对象，返回Point对象，当前设备指定屏幕的分辨率为Point.x\*Point.y。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let density = await driver.getDisplayDensity(0);
}
```

#### \[h2\]wakeUpDisplay9+

wakeUpDisplay(): Promise<void>

唤醒当前设备即设备亮屏。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.wakeUpDisplay();
}
```

#### \[h2\]pressHome9+

pressHome(): Promise<void>

设备注入返回桌面操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome();
}
```

#### \[h2\]pressHome20+

pressHome(displayId: number): Promise<void>

设备指定屏幕上注入返回桌面操作。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 是 | 
指定设备屏幕ID。取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.pressHome(0);
}
```

#### \[h2\]waitForIdle9+

waitForIdle(idleTime: number, timeout: number): Promise<boolean>

判断当前界面的所有控件是否已经空闲。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| idleTime | number | 是 | 空闲时间的阈值。在这个时间段控件不发生变化，视为该控件空闲，单位：毫秒，取值范围：大于等于0的整数。 |
| timeout | number | 是 | 等待空闲的最大时间，单位：毫秒，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回当前界面的所有控件是否已经空闲。true：已经空闲，false：不空闲。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let idled: boolean = await driver.waitForIdle(4000, 5000);
}
```

#### \[h2\]fling9+

fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>

模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | 是 | 手指接触屏幕的起始点坐标。 |
| to | [Point](#point9) | 是 | 手指离开屏幕时的坐标点。 |
| stepLen | number | 是 | 间隔距离，取值大于等于0的整数，单位：px。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling({ x: 500, y: 480 }, { x: 450, y: 480 }, 5, 600);
}
```

#### \[h2\]injectMultiPointerAction9+

injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>

向设备注入多指操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| pointers | [PointerMatrix](#pointermatrix9) | 是 | 滑动轨迹，包括操作手指个数和滑动坐标序列。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回操作是否成功完成。true：完成，false：未完成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
  await driver.injectMultiPointerAction(pointers);
}
```

#### \[h2\]fling10+

fling(direction: UiDirection, speed: number): Promise<void>

指定方向和滑动速率，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| direction | [UiDirection](#uidirection10) | 是 | 进行抛滑的方向。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000);
}
```

#### \[h2\]fling20+

fling(direction: UiDirection, speed: number, displayId: number): Promise<void>

指定方向、滑动速率和操作屏幕，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| direction | [UiDirection](#uidirection10) | 是 | 进行抛滑的方向。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |
| displayId | number | 是 | 
指定设备屏幕ID。取值范围：大于等于0的整数。

**说明：** 传入displayId不存在时，将抛出17000007异常。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.fling(UiDirection.DOWN, 10000, 0);
}
```

#### \[h2\]screenCapture10+

screenCapture(savePath: string, rect?: Rect): Promise<boolean>

捕获当前屏幕的指定区域，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的[沙箱路径](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-sandbox-directory)。 |
| rect | [Rect](#rect9) | 否 | 截图区域，默认为全屏。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：成功完成，false：未成功完成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.screenCapture('/data/storage/el2/base/cache/1.png', {
    left: 0,
    top: 0,
    right: 100,
    bottom: 100
  });
}
```

#### \[h2\]mouseClick10+

mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

在指定坐标点注入鼠标点击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标点击动作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 鼠标点击的坐标。 |
| btnId | [MouseButton](#mousebutton10) | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

#### \[h2\]mouseScroll10+

mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标滚轮滑动动作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 鼠标点击的坐标。 |
| down | boolean | 是 | 滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。 |
| d | number | 是 | 鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072);
}
```

#### \[h2\]mouseMoveTo10+

mouseMoveTo(p: Point): Promise<void>

将鼠标光标移到目标点。使用Promise异步回调。

**系统能力**：SystemCapability.Test.UiTest

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 目标点的坐标。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveTo({ x: 100, y: 100 });
}
```

#### \[h2\]createUIEventObserver10+

createUIEventObserver(): UIEventObserver;

创建一个UI事件监听器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [UIEventObserver](#uieventobserver10) | 返回找到的目标窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
}
```

#### \[h2\]mouseScroll11+

mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键并且指定滑动速度。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 鼠标点击的坐标。 |
| down | boolean | 是 | 滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。 |
| d | number | 是 | 鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |
| speed | number | 否 | 鼠标滚轮滚动的速度，范围：1-500的整数，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072, 20);
}
```

#### \[h2\]mouseDoubleClick11+

mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

在指定坐标点注入鼠标双击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标双击动作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 鼠标双击的坐标。 |
| btnId | [MouseButton](#mousebutton10) | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDoubleClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

#### \[h2\]mouseLongClick11+

mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 鼠标长按的坐标。 |
| btnId | [MouseButton](#mousebutton10) | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
}
```

#### \[h2\]mouseLongClick20+

mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键，支持指定长按时长。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 鼠标长按的坐标。 |
| btnId | [MouseButton](#mousebutton10) | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)，默认值为0。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, MouseButton } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072, 0, 2000);
}
```

#### \[h2\]mouseMoveWithTrack11+

mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>

鼠标从起始坐标点滑向终点坐标点。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | 是 | 起始点坐标。 |
| to | [Point](#point9) | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseMoveWithTrack({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}
```

#### \[h2\]mouseDrag11+

mouseDrag(from: Point, to: Point, speed?: number): Promise<void>

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | 是 | 起始点坐标。 |
| to | [Point](#point9) | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
}
```

#### \[h2\]mouseDrag20+

mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| from | [Point](#point9) | 是 | 起始点坐标。 |
| to | [Point](#point9) | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600, 2000);
}
```

#### \[h2\]inputText11+

inputText(p: Point, text: string): Promise<void>

在指定坐标点输入文本，不清空组件内原有文本，直接在坐标处追加输入。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 输入文本的坐标点。 |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123');
}
```

#### \[h2\]inputText20+

inputText(p: Point, text: string, mode: InputTextMode): Promise<void>

在指定坐标点输入文本，支持指定文本输入方式。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| p | [Point](#point9) | 是 | 输入文本的坐标点。 |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |
| mode | [InputTextMode](#inputtextmode20) | 是 | 
输入文本的方式，取值请参考[InputTextMode](#inputtextmode20)。

**说明：**

InputTextMode.addition取值为true时，将光标移动至文本末尾后输入指定文本。取值为false时，将在坐标点位置输入指定文本。

 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not support, function can not work correctly due to limited device capabilities. |

**示例：**

```ts
// xxx.test.ets
import { Component, Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '123', { paste: true, addition: false });
}

async function demo_Chinese() {
  let driver: Driver = Driver.create();
  let text: Component = await driver.findComponent(ON.type('TextInput'));
  let point = await text.getBoundsCenter();
  await driver.inputText(point, '中文&', { paste: false, addition: true });
  // 以复制粘贴方式输入中文、特殊符号， 指定文本追加到指定坐标所在文本段的末尾。
}
```

#### \[h2\]touchPadMultiFingerSwipe18+

touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>

模拟触摸板多指滑动手势。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在PC/2in1设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fingers | number | 是 | 触摸板多指滑动的手指数。取值为3或者4。 |
| direction | [UiDirection](#uidirection10) | 是 | 触摸板多指滑动的方向。 |
| options | [TouchPadSwipeOptions](#touchpadswipeoptions18) | 否 | 触摸板多指滑动手势附加选项，默认取TouchPadSwipeOptions中各属性的默认值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadMultiFingerSwipe(3, UiDirection.UP);
}
```

#### \[h2\]touchPadTwoFingersScroll22+

touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>

模拟触摸板双指滚动手势。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在PC/2in1设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | 是 | 触摸板双指滚动时鼠标光标的位置。 |
| direction | [UiDirection](#uidirection10) | 是 | 触摸板双指滚动的方向。 |
| d | number | 是 | 触摸板双指滚动的格数，取值为大于等于0的整数，每格对应目标点位移120px。 |
| speed | number | 否 | 触摸板双指滚动的速度，范围：1-500的整数，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiDirection } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.touchPadTwoFingersScroll({ x: 100, y: 100 }, UiDirection.UP, 20, 10);
}
```

#### \[h2\]penClick18+

penClick(point: Point): Promise<void>

模拟手写笔点击操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | 是 | 点击的坐标点。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penClick({ x: 100, y: 100 });
}
```

#### \[h2\]penLongClick18+

penLongClick(point: Point, pressure?: number): Promise<void>

模拟手写笔长按操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | 是 | 长按的坐标点。 |
| pressure | number | 否 | 手写笔滑动操作的压力，默认为1.0，取值范围为0.0到1.0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penLongClick({ x: 100, y: 100 }, 0.5);
}
```

#### \[h2\]penDoubleClick18+

penDoubleClick(point: Point): Promise<void>

模拟手写笔双击操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| point | [Point](#point9) | 是 | 双击的坐标点。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penDoubleClick({ x: 100, y: 100 });
}
```

#### \[h2\]penSwipe18+

penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>

模拟手写笔的滑动操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| startPoint | [Point](#point9) | 是 | 起始位置的坐标点。 |
| endPoint | [Point](#point9) | 是 | 结束位置的坐标点。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| pressure | number | 否 | 手写笔滑动操作的压力，默认为1.0，取值范围为0.0到1.0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  await driver.penSwipe({ x: 100, y: 100 }, { x: 100, y: 500 }, 600, 0.5);
}
```

#### \[h2\]injectPenPointerAction18+

injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>

模拟手写笔多点连续注入操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| pointers | [PointerMatrix](#pointermatrix9) | 是 | 
滑动轨迹，包括操作手指个数和滑动坐标序列。

**说明**：当前仅支持单指操作，PointerMatrix中的操作手指个数fingers必须设置为1。

 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| pressure | number | 否 | 手写笔多点连续注入的压力，默认为1.0，取值范围为0.0到1.0。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let pointer = PointerMatrix.create(1, 8);
  for (let step = 0; step < 8; step++) {
    pointer.setPoint(0, step, { x: 500, y: 1100 - 100 * step });
  }
  await driver.injectPenPointerAction(pointer, 600, 0.5);
}
```

#### \[h2\]crownRotate20+

crownRotate(d: number, speed?: number): Promise<void>

注入手表表冠旋转事件，可指定旋转速度。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Wearable设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| d | number | 是 | 手表表冠旋转的格数，正值表示顺时针旋转，负值表示逆时针旋转，取值需为整数。 |
| speed | number | 否 | 手表表冠旋转的速度，取值范围：1-500的整数，默认值为20，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |
| 801 | Capability not support, function can not work correctly due to limited device capabilities. |

**示例：**

```ts
// xxx.test.ets
import { Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 顺时针旋转50格，旋转速度为30格/秒
  await driver.crownRotate(50, 30);
  // 逆时针旋转20格，旋转速度为30格/秒
  await driver.crownRotate(-20, 30);
}
```

#### \[h2\]knuckleKnock22+

knuckleKnock(pointers: Array<Point>, times: number): Promise<void>

模拟指关节敲击屏幕操作。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/WIwF8DpqQki-kvkFANL6Fw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=8C327CDFDF32C536FC0CA18B5354E45AD3C988EC96D6DB7595689B9E5376F42D)

若设备关闭了指关节手势，则调用本接口返回17000005错误码。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在支持指关节操作的Phone、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| pointers | Array<[Point](#point9)\> | 是 | 指关节敲击屏幕坐标点的数组，数组长度取值为1或2。 |
| times | number | 是 | 指关节连续敲击屏幕的次数，取值为1或2。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, Point } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 模拟指关节单指双击手势
  let points: Array<Point> = [{ x: 100, y: 100 }];
  await driver.knuckleKnock(points, 2);
}
```

#### \[h2\]injectKnucklePointerAction22+

injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>

模拟指关节多点注入滑动操作。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/1Z-2fgxFRc6m7wD1YePNkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=0E39656F3DB4D6F34A70F6FC0209EA37DE811E28CDCF8F72D0D32B4319B9548F)

若设备关闭了指关节手势，则调用本接口返回17000005错误码。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在支持指关节操作的Phone、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| pointers | [PointerMatrix](#pointermatrix9) | 是 | 
滑动轨迹，包括操作手指个数和滑动坐标序列。

**说明**：当前仅支持单指操作，PointerMatrix中的操作手指个数fingers必须设置为1。

 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, PointerMatrix } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  // 模拟指关节滑动在屏幕上画'S'
  let pointers: PointerMatrix = PointerMatrix.create(1, 6);
  pointers.setPoint(0, 0, { x: 750, y: 300 });
  pointers.setPoint(0, 1, { x: 500, y: 100 });
  pointers.setPoint(0, 2, { x: 250, y: 300 });
  pointers.setPoint(0, 3, { x: 750, y: 800 });
  pointers.setPoint(0, 4, { x: 500, y: 1000 });
  pointers.setPoint(0, 5, { x: 250, y: 800 });
  await driver.injectKnucklePointerAction(pointers);
}
```

#### \[h2\]isComponentPresentWhenLongClick22+

isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>

在坐标点长按，并查找目标控件是否存在。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |
| point | [Point](#point9) | 是 | 长按的坐标点。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回长按操作期间目标控件是否存在。true：存在。false：不存在。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenLongClick(ON.id('123'), { x: 100, y: 100 }, 2000);
}
```

#### \[h2\]isComponentPresentWhenDrag22+

isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>

从起始点拖拽至终止点，并查找目标控件是否存在。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |
| from | [Point](#point9) | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](#point9) | 是 | 
以Point对象的形式传入终止点的坐标信息和所属屏幕ID。

**说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。

 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回拖拽操作期间目标控件是否存在。true：存在。false：不存在。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenDrag(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000, 2000);
}
```

#### \[h2\]isComponentPresentWhenSwipe22+

isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>

从起始点滑向终止点，并查找目标控件是否存在。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| on | [On](#on9) | 是 | 目标控件的属性要求。 |
| from | [Point](#point9) | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](#point9) | 是 | 
以Point对象的形式传入终止点的坐标信息和所属屏幕ID。

**说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。

 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象。返回滑动操作期间目标控件是否存在。true：存在。false：不存在。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let isExist = await driver.isComponentPresentWhenSwipe(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000);
}
```

#### PointerMatrix9+

存储多指操作中每根手指每一步动作的坐标点及其行为的二维数组。

#### \[h2\]create9+

static create(fingers: number, steps: number): PointerMatrix

静态方法，构造一个PointerMatrix对象，并返回该对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| fingers | number | 是 | 多指操作中注入的手指数，取值范围：\[1,10\]的整数。 |
| steps | number | 是 | 每根手指操作的步骤数，取值范围：\[1,1000\]的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [PointerMatrix](#pointermatrix9) | 返回构造的PointerMatrix对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3);
}
```

#### \[h2\]setPoint9+

setPoint(finger: number, step: number, point: Point): void

设置PointerMatrix对象中指定手指和步骤对应动作的坐标点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| finger | number | 是 | 手指的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的手指数。 |
| step | number | 是 | 步骤的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的操作的步骤数。 |
| point | [Point](#point9) | 是 | 该行为的坐标点。建议相邻的坐标点距离在10px至80px范围内。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { PointerMatrix } from '@kit.TestKit';

async function demo() {
  let pointers: PointerMatrix = PointerMatrix.create(2, 5);
  pointers.setPoint(0, 0, { x: 250, y: 480 });
  pointers.setPoint(0, 1, { x: 250, y: 440 });
  pointers.setPoint(0, 2, { x: 250, y: 400 });
  pointers.setPoint(0, 3, { x: 250, y: 360 });
  pointers.setPoint(0, 4, { x: 250, y: 320 });
  pointers.setPoint(1, 0, { x: 250, y: 480 });
  pointers.setPoint(1, 1, { x: 250, y: 440 });
  pointers.setPoint(1, 2, { x: 250, y: 400 });
  pointers.setPoint(1, 3, { x: 250, y: 360 });
  pointers.setPoint(1, 4, { x: 250, y: 320 });
}
```

#### UiWindow9+

UiWindow代表了UI界面上的一个窗口，提供窗口属性获取，窗口拖动、调整窗口大小等能力。

该类提供的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

#### \[h2\]getBundleName9+

getBundleName(): Promise<string>

获取窗口归属应用的包名信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回窗口归属应用的包名信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let name: string = await window.getBundleName();
}
```

#### \[h2\]getBounds9+

getBounds(): Promise<Rect>

获取窗口的边框信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[Rect](#rect9)\> | Promise对象，返回窗口的边框信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let rect = await window.getBounds();
}
```

#### \[h2\]getTitle9+

getTitle(): Promise<string>

获取窗口的标题信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回窗口的标题信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let title = await window.getTitle();
}
```

#### \[h2\]getWindowMode9+

getWindowMode(): Promise<WindowMode>

获取窗口的窗口模式信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[WindowMode](#windowmode9)\> | Promise对象，返回窗口的窗口模式信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let mode = await window.getWindowMode();
}
```

#### \[h2\]isFocused9+

isFocused(): Promise<boolean>

判断窗口是否处于获焦状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回窗口对象是否获取获焦状态。true：获焦。false：未获焦。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let focused = await window.isFocused();
}
```

#### \[h2\]isActived(deprecated)

isActived(): Promise<boolean>

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/qczEbkQeSDex46uWeVyG0A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=372D5633F5BD57D7C10DD0750AF13F3E2262D38BCB19D4CD3265127D601803CB)

从API version 9开始支持，从API version 11开始废弃，建议使用[isActive11+](#isactive11)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回窗口对象是否为用户正在交互窗口。true表示是交互窗口。false表示非交互窗口。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  let focused = await window.isActived();
}
```

#### \[h2\]focus9+

focus(): Promise<void>

让窗口获焦。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.focus();
}
```

#### \[h2\]moveTo9+

moveTo(x: number, y: number): Promise<void>

将窗口移动到目标点。使用Promise异步回调。适用于支持移动的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.moveTo(100, 100);
}
```

#### \[h2\]resize9+

resize(wide: number, height: number, direction: ResizeDirection): Promise<void>

根据传入的宽、高和调整方向来调整窗口的大小。使用Promise异步回调。适用于支持调整大小的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| wide | number | 是 | 以number的形式传入调整后窗口的宽度，取值范围：大于等于0的整数。 |
| height | number | 是 | 以number的形式传入调整后窗口的高度，取值范围：大于等于0的整数。 |
| direction | [ResizeDirection](#resizedirection9) | 是 | 以[ResizeDirection](#resizedirection9)的形式传入窗口调整的方向。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, ResizeDirection, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.resize(100, 100, ResizeDirection.LEFT);
}
```

#### \[h2\]split9+

split(): Promise<void>

将窗口模式切换成分屏模式。使用Promise异步回调。适用于支持切换分屏模式的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.split();
}
```

#### \[h2\]maximize9+

maximize(): Promise<void>

将窗口最大化。使用Promise异步回调。适用于支持窗口最大化操作的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.maximize();
}
```

#### \[h2\]minimize9+

minimize(): Promise<void>

将窗口最小化。使用Promise异步回调。适用于支持窗口最小化操作的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.minimize();
}
```

#### \[h2\]resume9+

resume(): Promise<void>

将窗口恢复到之前的窗口模式。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.resume();
}
```

#### \[h2\]close9+

close(): Promise<void>

将窗口关闭。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ actived: true });
  await window.close();
}
```

#### \[h2\]isActive11+

isActive(): Promise<boolean>

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回窗口对象是否为用户正在交互窗口。true：交互窗口。false：非交互窗口。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiWindow } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let focused = await window.isActive();
}
```

#### \[h2\]getDisplayId20+

getDisplayId(): Promise<number>

获取窗口所属的屏幕ID。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回窗口所属的屏幕ID。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```ts
// xxx.test.ets
import { UiWindow, Driver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let window: UiWindow = await driver.findWindow({ active: true });
  let id = await window.getDisplayId();
}
```

#### UIEventObserver10+

UI事件监听器。

#### \[h2\]once('toastShow')10+

once(type: 'toastShow', callback: Callback<UIElementInfo>): void

开始监听toast控件出现的事件，使用callback的形式返回结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型，取值为'toastShow'。 |
| callback | Callback<[UIElementInfo](#uielementinfo10)\> | 是 | 事件发生时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  observer.once('toastShow', callback);
}
```

#### \[h2\]once('dialogShow')10+

once(type: 'dialogShow', callback: Callback<UIElementInfo>): void

开始监听dialog控件出现的事件，使用callback的形式返回结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型，取值为'dialogShow'。 |
| callback | Callback<[UIElementInfo](#uielementinfo10)\> | 是 | 事件发生时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
  }
  observer.once('dialogShow', callback);
}
```

#### \[h2\]once('windowChange')22+

once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void

开始监听指定类型的窗口变化事件，支持设置事件监听的扩展配置，监听到指定窗口变化事件时触发callback回调。仅支持[自由多窗模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/window-terminology#自由多窗模式)的窗口监听。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型，支持的事件为'windowChange'。当监听到窗口变化时，触发该事件。 |
| windowChangeType | [WindowChangeType](#windowchangetype22) | 是 | 窗口变化事件类型。 |
| options | [WindowChangeOptions](#windowchangeoptions22) | 是 | 窗口变化事件监听的扩展配置，包括监听超时时间和监听窗口对应包名。 |
| callback | Callback<[UIElementInfo](#uielementinfo10)\> | 是 | 事件发生时执行的回调函数，返回事件的相关信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, WindowChangeOptions, WindowChangeType } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let options: WindowChangeOptions = {
    timeout: 20000,
    bundleName: 'com.example.myapplication'  // 请开发者替换为实际包名
  }
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
    console.info(UIElementInfo.windowChangeType?.toString());
    console.info(UIElementInfo.windowId?.toString());
  }
  observer.once('windowChange', WindowChangeType.WINDOW_ADDED, options, callback);
}
```

#### \[h2\]once('componentEventOccur')22+

once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void

开始监听指定类型的控件操作事件，支持设置事件监听的扩展配置，监听到指定控件操作事件时触发callback回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 订阅的事件类型，支持的事件为'componentEventOccur'。当监听到控件操作时，触发该事件。 |
| componentEventType | [ComponentEventType](#componenteventtype22) | 是 | 控件操作事件类型。 |
| options | [ComponentEventOptions](#componenteventoptions22) | 是 | 控件操作事件监听的扩展配置，包括监听超时时间和监听控件匹配条件。 |
| callback | Callback<[UIElementInfo](#uielementinfo10)\> | 是 | 事件发生时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```ts
// xxx.test.ets
import { Driver, UIElementInfo, UIEventObserver, ComponentEventOptions, ComponentEventType, ON } from '@kit.TestKit';

async function demo() {
  let driver: Driver = Driver.create();
  let observer: UIEventObserver = driver.createUIEventObserver();
  let option: ComponentEventOptions = {
    timeout: 20000,
    on: ON.id('123')  // 请开发者替换为实际存在的控件id值
  };
  let callback = (UIElementInfo: UIElementInfo) => {
    console.info(UIElementInfo.bundleName);
    console.info(UIElementInfo.text);
    console.info(UIElementInfo.type);
    console.info(UIElementInfo.componentEventType?.toString());
    console.info(UIElementInfo.windowId?.toString());
    console.info(UIElementInfo.componentId);
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
    console.info(UIElementInfo.componentRect?.left.toString());
  };
  observer.once('componentEventOccur', ComponentEventType.COMPONENT_CLICKED, option, callback);
}
```

#### By(deprecated)

UiTest框架通过By类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。

By提供的API能力具有以下几个特点:

1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。

2、控件属性支持多种匹配模式。

3、支持控件绝对定位，相对定位，可通过[By.isBefore(deprecated)](#isbeforedeprecated)和[By.isAfter(deprecated)](#isafterdeprecated)等API限定邻近控件特征进行辅助定位。

By类提供的所有API均为同步接口，建议使用者通过静态构造器BY来链式创建By对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/TFkhBhDvQB6M6RLE6jzA2A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=621478DDEEC9F7759FA7B0AA4371EFC0C1FD185EFAD8EC4303BA6E137C3F7025)

从API version 8开始支持，从API version 9开始废弃，建议使用[On9+](#on9)替代。

```ts
// xxx.test.ets
import { BY } from '@kit.TestKit';

BY.text('123').type('Button');
```

#### \[h2\]text(deprecated)

text(txt: string, pattern?: MatchPattern): By

指定目标控件文本属性，支持多种匹配模式，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/2imF4vm5RYGPoCGvwZrr-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=E29A8BDC750D2F704556FDF9C8A9B3AFD28A076A920468450E94B27050A29204)

从API version 8开始支持，从API version 9开始废弃，建议使用[text9+](#text9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| txt | string | 是 | 指定控件文本，用于匹配目标控件文本。 |
| pattern | [MatchPattern](#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件文本属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { BY, By } from '@kit.TestKit';

let by: By = BY.text('123'); // 使用静态构造器BY创建by对象，指定目标控件的text属性。
```

#### \[h2\]key(deprecated)

key(key: string): By

指定目标控件key值属性，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/HwyTKdtMS5ubVtDobaoYWQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=A0E206ECDE94EDCBB2AC1F2FE1A15A3D7D2F2B114AFE83D832B7AAB6A4C6F67F)

从API version 8开始支持，从API version 9开始废弃，建议使用[id9+](#id9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| key | string | 是 | 指定控件的Key值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件key值属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.key('123'); // 使用静态构造器BY创建by对象，指定目标控件的key值属性。
```

#### \[h2\]id(deprecated)

id(id: number): By

指定目标控件id属性，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/cPVt0hFcTMuFwDjES3Pbsw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=EF5537938100ABE2E808F5AE7D1B1BFE9B798D58C30423B89077800086213381)

从API version 8开始支持，从API version 9开始废弃，建议使用[id9+](#id9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| id | number | 是 | 指定控件的id值。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件id属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.id(123); // 使用静态构造器BY创建by对象，指定目标控件的id属性。
```

#### \[h2\]type(deprecated)

type(tp: string): By

指定目标控件的控件类型属性，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/cCEvDnMUQfGEBMzFQV-ilg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=99808ECB78F33216BB6C782386E527095AFF3951CE33EBCA583E99148051BA34)

从API version 8开始支持，从API version 9开始废弃，建议使用[type9+](#type9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| tp | string | 是 | 指定控件类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件的控件类型属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.type('Button'); // 使用静态构造器BY创建by对象，指定目标控件的控件类型属性。
```

#### \[h2\]clickable(deprecated)

clickable(b?: boolean): By

指定目标控件的可点击状态属性，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/9ZaMPbJjTZujcwtizzPueg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=9A5574EFDD2132D7CF8B559EF08745739D02741D91E6D786141A587E3621399E)

从API version 8开始支持，从API version 9开始废弃，建议使用[clickable9+](#clickable9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件可点击状态。true：可点击。false：不可点击。默认为true。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件的可点击状态属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.clickable(true); // 使用静态构造器BY创建by对象，指定目标控件的可点击状态属性。
```

#### \[h2\]scrollable(deprecated)

scrollable(b?: boolean): By

指定目标控件的可滑动状态属性，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/iz4GPeoxRTesumskFSnGeA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=3062587E92928781B20EBCAB2C9159DA36EDF0E6B6955A82F5658D30F3EB4009)

从API version 8开始支持，从API version 9开始废弃，建议使用[scrollable9+](#scrollable9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 控件可滑动状态。true：可滑动。false：不可滑动。默认为true。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件的可滑动状态属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.scrollable(true); // 使用静态构造器BY创建by对象，指定目标控件的可滑动状态属性。
```

#### \[h2\]enabled(deprecated)

enabled(b?: boolean): By

指定目标控件的使能状态属性，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/JCDVn9nRSfqVyJH5elAU9Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=B219A3122D269BD83E17FB71905D5AB52A528F6789320D08B7D70239B49A8D10)

从API version 8开始支持，从API version 9开始废弃，建议使用[enabled9+](#enabled9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件使能状态。true：使能。false：未使能。默认为true。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件的使能状态属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.enabled(true); // 使用静态构造器BY创建by对象，指定目标控件的使能状态属性。
```

#### \[h2\]focused(deprecated)

focused(b?: boolean): By

指定目标控件的获焦状态属性，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/olPLATguTvaaZ3iH4yipzQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=5E2A7A4D976F64C9CE51A2029548C0DCA8B1BBFF597715C31A6565F519548EBF)

从API version 8开始支持，从API version 9开始废弃，建议使用[focused9+](#focused9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 控件获焦状态。true：获焦。false：未获焦。默认为true。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件的获焦状态属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.focused(true); // 使用静态构造器BY创建by对象，指定目标控件的获焦状态属性。
```

#### \[h2\]selected(deprecated)

selected(b?: boolean): By

指定目标控件的被选中状态属性，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/VLzJhirRTd2RkQhSxuxXSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=AF2AFD1D3E4BB41543A8C7A60C7337CFAC0EFF1E5C6F60927249C7DBCA3A65F4)

从API version 8开始支持，从API version 9开始废弃，建议使用[selected9+](#selected9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| b | boolean | 否 | 指定控件被选中状态。true：被选中。false：未被选中。默认为true。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件的被选中状态属性的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

let by: By = BY.selected(true); // 使用静态构造器BY创建by对象，指定目标控件的被选中状态属性。
```

#### \[h2\]isBefore(deprecated)

isBefore(by: By): By

指定目标控件位于给出的特征属性控件之前，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/QWzzrFEYRBafkxlS5nYvbQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=7E5C59764C8BAE6BF73B105F741F554E4220CB73D32685F0A16A8770AA94F95F)

从API version 8开始支持，从API version 9开始废弃，建议使用[isBefore9+](#isbefore9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | 是 | 特征控件的属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件位于给出的特征属性控件之前的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// 使用静态构造器BY创建by对象，指定目标控件位于给出的特征属性控件之前。
let by: By = BY.type('Button').isBefore(BY.text('123')); // 查找text为123之前的第一个Button组件
```

#### \[h2\]isAfter(deprecated)

isAfter(by: By): By

指定目标控件位于给出的特征属性控件之后，返回By对象自身。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/O0Is9MtcRMWkioaHA10mMg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=89B7E5BF463F2672B02BA76CD02ED793911D6B6C25AD6C66A74ADFAC8BE72D25)

从API version 8开始支持，从API version 9开始废弃，建议使用[isAfter9+](#isafter9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | 是 | 特征控件的属性。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [By](#bydeprecated) | 返回指定目标控件位于给出的特征属性控件之后的By对象。 |

**示例：**

```ts
// xxx.test.ets
import { By, BY } from '@kit.TestKit';

// 使用静态构造器BY创建by对象，指定目标控件位于给出的特征属性控件之后。
let by: By = BY.type('Text').isAfter(BY.text('123')); // 查找 text为123之后的第一个Text组件
```

#### UiComponent(deprecated)

UiTest中，UiComponent类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。

该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/ZwZ2_Su4Qw62R2hsDpCXTA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=65E02A3E83C74F3A65B201D8F05E82639720DF6A7627EE68B5036D6D0C4F18CA)

从API version 8开始支持，从API version 9开始废弃，建议使用[Component9+](#component9)替代。

#### \[h2\]click(deprecated)

click(): Promise<void>

控件对象进行点击操作。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/52rozzMDRWCrvCPmyB2mwA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=B372F3F3ACD147300D5CC7EB0CBCD6E1CD8AFBAB3E8FC1038F135A2D85D3CB57)

从API version 8开始支持，从API version 9开始废弃，建议使用[click9+](#click9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, Driver, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.click();
}
```

#### \[h2\]doubleClick(deprecated)

doubleClick(): Promise<void>

控件对象进行双击操作。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/iT3logTuQB-wUHe_K_fxmg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=6F049DCF3FDA8F4EB489E5925BAB8AE8A4113C7AC7C426976C5391E1BEFC3BD4)

从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick9+](#doubleclick9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.doubleClick();
}
```

#### \[h2\]longClick(deprecated)

longClick(): Promise<void>

控件对象进行长按操作。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Lys2tQscRDuyXZeB3gjNHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=A2679FD74A8C80D90C2504F4326BC4AE56044858073BDF2F0D1F370E49AAFBB5)

从API version 8开始支持，从API version 9开始废弃，建议使用[longClick9+](#longclick9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  await button.longClick();
}
```

#### \[h2\]getId(deprecated)

getId(): Promise<number>

获取控件对象的id值。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/xbVvYd9XS5egfUU_J3CgRQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=C2C5B98FE2B1CACAF09CA3E20158C4E93D375B46E497C71E889023EF33503BA0)

从API version 8开始支持，从API version 9开始废弃，建议使用[getId9+](#getid9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<number> | Promise对象，返回控件的id值。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let id = await button.getId();
}
```

#### \[h2\]getKey(deprecated)

getKey(): Promise<string>

获取控件对象的key值。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/1YQJymq0TcuwYhExJgnjSA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=BD07A6FE1BDA351558110D1538855498E82D5BC5B8BF5166B890BDF8E6C39251)

从API version 8开始支持，从API version 9开始废弃，建议使用[getId9+](#getid9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的key值。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let str_key = await button.getKey();
}
```

#### \[h2\]getText(deprecated)

getText(): Promise<string>

获取控件对象的文本信息。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/kYQvsMbkQGqOg_UFBWVNgw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=D15184DE1856ECE1DA597397115FCB64B0D87943CF02D8388E5B7AFD0D3AE6F9)

从API version 8开始支持，从API version 9开始废弃，建议使用[getText9+](#gettext9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let text = await button.getText();
}
```

#### \[h2\]getType(deprecated)

getType(): Promise<string>

获取控件对象的控件类型。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/j7FJCOV2QzqxQzBb_AqNAQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=00E7F14CD13EAD253E90DE40C29FACC1A058D0CAE7C078A50F506E66DF04DE2D)

从API version 8开始支持，从API version 9开始废弃，建议使用[getType9+](#gettype9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<string> | Promise对象，返回控件的类型。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  let type = await button.getType();
}
```

#### \[h2\]isClickable(deprecated)

isClickable(): Promise<boolean>

获取控件对象可点击状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/WYxFCfSxTK6q2kXBCQ0qfQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=3E6CE5702B54E2D87753B0C17844F90EBEBE05DEFC0C796B1E8FE7C1B9421147)

从API version 8开始支持，从API version 9开始废弃，建议使用[isClickable9+](#isclickable9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象可点击状态。true：可点击。false：不可点击。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isClickable()) {
    console.info('This button can be Clicked');
  } else {
    console.info('This button can not be Clicked');
  }
}
```

#### \[h2\]isScrollable(deprecated)

isScrollable(): Promise<boolean>

获取控件对象可滑动状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/U6fnMe3WR-K8tNBq2DwVkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=AF18A3BB5D134CA7D9A353FCEAB6ED60FD1978579BB146422BDBD1EEDA694F94)

从API version 8开始支持，从API version 9开始废弃，建议使用[isScrollable9+](#isscrollable9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象可滑动状态。true：可滑动。false：不可滑动。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.scrollable(true));
  if (await scrollBar.isScrollable()) {
    console.info('This scrollBar can be operated');
  } else {
    console.info('This scrollBar can not be operated');
  }
}
```

#### \[h2\]isEnabled(deprecated)

isEnabled(): Promise<boolean>

获取控件使能状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/B7brtWeiThiUwsOtJbU_sQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=D3803741184482748F14492F1FE8366F4ADD371C123D4F5AEAD0CB5286BB0FA2)

从API version 8开始支持，从API version 9开始废弃，建议使用[isEnabled9+](#isenabled9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件使能状态。true：使能。false：未使能。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isEnabled()) {
    console.info('This button can be operated');
  } else {
    console.info('This button can not be operated');
  }
}
```

#### \[h2\]isFocused(deprecated)

isFocused(): Promise<boolean>

判断控件对象是否获焦。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/1EYZm4slRYKlemcklLiXgA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=C9547BBCC7666CF06315F94953153099E1535CA3D94E2FD09719E5589B8DE66E)

从API version 8开始支持，从API version 9开始废弃，建议使用[isFocused9+](#isfocused9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象是否获焦。true：获焦。false：未获焦。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isFocused()) {
    console.info('This button is focused');
  } else {
    console.info('This button is not focused');
  }
}
```

#### \[h2\]isSelected(deprecated)

isSelected(): Promise<boolean>

获取控件对象被选中状态。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/PrO1d5yKTciO6mFl9M69RA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=6602A2E00180CB91A08F7923AC264EBE7FAC94E9A7C01B701109B2FF90BC7EC0)

从API version 8开始支持，从API version 9开始废弃，建议使用[isSelected9+](#isselected9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回控件对象被选中的状态。true：被选中。false：未被选中。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.type('Button'));
  if (await button.isSelected()) {
    console.info('This button is selected');
  } else {
    console.info('This button is not selected');
  }
}
```

#### \[h2\]inputText(deprecated)

inputText(text: string): Promise<void>

向控件中输入文本，仅针对可编辑的文本组件生效。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/3dXglsvzRAGzYPZsweDWzQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=211EA7D8EFC904F2521CB2E0D6D411AA72F23A37C0BED01928C912567EE22091)

从API version 8开始支持，从API version 9开始废弃，建议使用[inputText9+](#inputtext9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| text | string | 是 | 输入的文本信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let text: UiComponent = await driver.findComponent(BY.text('hello world'));
  await text.inputText('123');
}
```

#### \[h2\]scrollSearch(deprecated)

scrollSearch(by: By): Promise<UiComponent>

在控件上滑动查找目标控件（适用于List等支持滑动的控件）。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/zkezve8HTy-s54PYjmK7YA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=23E8D6C8D7CCB15F7F24215DA20D71FDFECE2F88BBE52BD3DD1A16198DA77ABB)

从API version 8开始支持，从API version 9开始废弃，建议使用[scrollSearch9+](#scrollsearch9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[UiComponent](#uicomponentdeprecated)\> | Promise对象，返回目标控件对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let scrollBar: UiComponent = await driver.findComponent(BY.type('Scroll'));
  let button = await scrollBar.scrollSearch(BY.text('next page'));
}
```

#### UiDriver(deprecated)

UiDriver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等API。

该类提供的方法除UiDriver.create()以外的所有方法都使用Promise方式作为异步方法，需使用await调用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/5eViBMpORe-OYDxWX5ULXg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=7DD58C58FB32D5FFB06B9135B874F9DCC91CE6EEFA804B266AD8B8880498FF2F)

从API version 8开始支持，从API version 9开始废弃，建议使用[Driver9+](#driver9)替代。

#### \[h2\]create(deprecated)

static create(): UiDriver

静态方法，构造一个UiDriver对象，并返回该对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/EqSvEWmhRh68w8Ulicrv-w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=D288D0498473DB35F73778C9B9AC016B2949D28E55A594547CB5B16DC05181F6)

从API version 8开始支持，从API version 9开始废弃，建议使用[create9+](#create9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| UiDriver | 返回构造的UiDriver对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
}
```

#### \[h2\]delayMs(deprecated)

delayMs(duration: number): Promise<void>

UiDriver对象在给定的时间内延时。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/BMJ1-zG7R9C3qZQFEFrTtw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=A5A8BFC2E7FE35FFD55093033862A444968EA577D6B702996608DBA4869D593A)

从API version 8开始支持，从API version 9开始废弃，建议使用[delayMs9+](#delayms9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| duration | number | 是 | 给定的时间。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.delayMs(1000);
}
```

#### \[h2\]findComponent(deprecated)

findComponent(by: By): Promise<UiComponent>

在UiDriver对象中，根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/iOS1BjB9TROMy8sCU4bSGQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=0087BAC56AEA9BF2191489EDCDFE01AE035ACDDE2869A663E814242641864CA8)

从API version 8开始支持，从API version 9开始废弃，建议使用[findComponent9+](#findcomponent9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[UiComponent](#uicomponentdeprecated)\> | Promise对象，返回控件对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let button: UiComponent = await driver.findComponent(BY.text('next page'));
}
```

#### \[h2\]findComponents(deprecated)

findComponents(by: By): Promise<Array<UiComponent>>

在UiDriver对象中，根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/GWKk5HiqRKm8LeE4uWk-gA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=EE088960EF788CA8B89792FA2550A5F7A50E081E42FA73C1B20233032C56A59A)

从API version 8开始支持，从API version 9开始废弃，建议使用[findComponents9+](#findcomponents9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[UiComponent](#uicomponentdeprecated)\>> | Promise对象，返回控件对象的列表。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY, UiComponent } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  let buttonList: Array<UiComponent> = await driver.findComponents(BY.text('next page'));
}
```

#### \[h2\]assertComponentExist(deprecated)

assertComponentExist(by: By): Promise<void>

断言API，用于断言当前界面存在满足给出的目标控件属性的控件; 如果控件不存在，该API将抛出JS异常，使当前测试用例失败。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/kU2OfRHvR1-qZp_aVhISgg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=F5D515822E00F7CED4736190DCE21C237D28A8D48085A0065A05B0A02E59054F)

从API version 8开始支持，从API version 9开始废弃，建议使用[assertComponentExist9+](#assertcomponentexist9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| by | [By](#bydeprecated) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-uitest)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | if the input parameters are invalid. |
| 17000002 | if the async function was not called with await. |
| 17000003 | if the assertion failed. |

**示例：**

```ts
// xxx.test.ets
import { UiDriver, BY } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.assertComponentExist(BY.text('next page'));
}
```

#### \[h2\]pressBack(deprecated)

pressBack(): Promise<void>

UiDriver对象进行点击BACK键的操作。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/X6dTWiSSQp6GDq4qzm536Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=D3D55D245711C58F181A13CB44CF721259751E5090D0D9090F89A8B7D2BB11BE)

从API version 8开始支持，从API version 9开始废弃，建议使用[pressBack9+](#pressback9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.pressBack();
}
```

#### \[h2\]triggerKey(deprecated)

triggerKey(keyCode: number): Promise<void>

UiDriver对象采取如下操作：通过key值找到对应键并点击。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/DFFrCONoR0eKt0TAihnoVg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=5E867DBB33139860FC2DF3008AAF21A61F60110F775DA3237BDABD6D9B636E01)

从API version 8开始支持，从API version 9开始废弃，建议使用[triggerKey9+](#triggerkey9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| keyCode | number | 是 | 指定的key值，取值大于等于0的整数，取值范围：[KeyCode键码值](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-keycode#keycode)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { Driver, UiDriver } from '@kit.TestKit';
import { KeyCode } from '@kit.InputKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.triggerKey(KeyCode.KEYCODE_BACK); // 返回键
}
```

#### \[h2\]click(deprecated)

click(x: number, y: number): Promise<void>

UiDriver对象采取如下操作：在目标坐标点单击。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/6BBbm__DQa-0cW4rxueJyg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=C4B2C95C671D0190FDA28294DC66AD2BDF243B97A6F0AC14B7EA107CA898F895)

从API version 8开始支持，从API version 9开始废弃，建议使用[click9+](#click9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.click(100, 100);
}
```

#### \[h2\]doubleClick(deprecated)

doubleClick(x: number, y: number): Promise<void>

UiDriver对象采取如下操作：在目标坐标点双击。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/UvonBAEUSz-5wKYup7tOZg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=D96BF5147C638F6A485D92DFC495CBDC541B2447A8179744AB82380D8389E8E8)

从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick9+](#doubleclick9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.doubleClick(100, 100);
}
```

#### \[h2\]longClick(deprecated)

longClick(x: number, y: number): Promise<void>

UiDriver对象采取如下操作：在目标坐标点长按下鼠标左键。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/2yYboNYmSfi6xYKGAiGg3w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=A0482BFF1BC4B119CA46C915F8E9A0D229D6C8D6FC8284ABA477BC8EA4D13210)

从API version 8开始支持，从API version 9开始废弃，建议使用[longClick9+](#longclick9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.longClick(100, 100);
}
```

#### \[h2\]swipe(deprecated)

swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>

UiDriver对象采取如下操作：从给出的起始坐标点滑向给出的目的坐标点。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/OQl-a88gQsmWQlsYyJMQtQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=A62D3165B893233D85F2F5FC25FE466735B872063CF6DB458D96967348B78498)

从API version 8开始支持，从API version 9开始废弃，建议使用[swipe9+](#swipe9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.swipe(100, 100, 200, 200);
}
```

#### \[h2\]screenCap(deprecated)

screenCap(savePath: string): Promise<boolean>

UiDriver对象采取如下操作：捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/6DSeMk6FRsO15XSEGqfpHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014837Z&HW-CC-Expire=86400&HW-CC-Sign=1D82F812571767A81C86D4A695DD985245DE41E214E0AB1699FE69E1E0E56B02)

从API version 8开始支持，从API version 9开始废弃，建议使用[screenCap9+](#screencap9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| savePath | string | 是 | 文件保存路径。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：成功完成，false：未成功完成。 |

**示例：**

```ts
// xxx.test.ets
import { UiDriver } from '@kit.TestKit';

async function demo() {
  let driver: UiDriver = UiDriver.create();
  await driver.screenCap('/data/storage/el2/base/cache/1.png');
}
```
