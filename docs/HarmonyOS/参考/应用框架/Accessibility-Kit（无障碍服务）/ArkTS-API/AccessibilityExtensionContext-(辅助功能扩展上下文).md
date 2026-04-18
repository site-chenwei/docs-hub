---
title: "AccessibilityExtensionContext (辅助功能扩展上下文)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/is-inner-application-accessibilityextensioncontext"
menu_path:
  - "参考"
  - "应用框架"
  - "Accessibility Kit（无障碍服务）"
  - "ArkTS API"
  - "AccessibilityExtensionContext (辅助功能扩展上下文)"
captured_at: "2026-04-17T01:47:49.121Z"
---

# AccessibilityExtensionContext (辅助功能扩展上下文)

AccessibilityExtensionContext是AccessibilityExtensionAbility上下文环境，继承自ExtensionContext。

辅助功能扩展上下文模块提供辅助功能扩展的上下文环境的能力，包括允许配置辅助应用关注信息类型、查询节点信息、手势注入等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/1UIE15jIQcK2pjeOi0TXbA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=C163D9BB162D85EFAD4B85625CF76F6800D32EE4020D86396E6604F12BB1B702)

-   本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 使用说明

在使用AccessibilityExtensionContext的功能前，需要通过AccessibilityExtensionAbility子类实例获取AccessibilityExtensionContext的实例。

```ts
import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

class EntryAbility extends AccessibilityExtensionAbility {
  onConnect(): void {
    let axContext = this.context;
  }
}
```

#### ElementAttributeValues

节点元素具备的属性名称及属性值类型信息。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

#### \[h2\]属性

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| accessibilityFocused | boolean | 否 | 否 | 表示元素是否处于无障碍焦点状态。true表示元素当前处于无障碍焦点状态，false表示元素当前不处于无障碍焦点状态，默认值为false。 |
| accessibilityText12+ | string | 否 | 否 | 元素的无障碍文本信息。 |
| bundleName | string | 否 | 否 | 应用包名。 |
| checkable | boolean | 否 | 否 | 表示元素是否支持点击操作。true表示元素支持点击操作，false表示元素不支持点击操作，默认值为false。 |
| checked | boolean | 否 | 否 | 表示元素当前的可点击状态。true表示元素当前是可点击的，false表示元素当前是不可点击的，默认值为false。 |
| children | Array<[AccessibilityElement](#accessibilityelement)\> | 否 | 否 | 所有子元素。 |
| clickable | boolean | 否 | 否 | 表示元素是否可点击。true表示元素可点击，false表示元素不可点击，默认值为false。 |
| componentId | number | 否 | 否 | 元素所属的组件ID。默认值为-1。 |
| componentType | string | 否 | 否 | 应与元素所属的组件类型所对应，如：按钮Button类型->'Button'、图像Image类型->'Image'。 |
| contents | Array<string> | 否 | 否 | 内容列表。根据实际场景设置，无特殊限制。 |
| currentIndex | number | 否 | 否 | 当前项的索引。默认值为0。 |
| description | string | 否 | 否 | 元素的描述信息。根据实际场景设置，无特殊限制。 |
| editable | boolean | 否 | 否 | 表示元素是否可编辑。true表示元素可编辑，false表示元素不可编辑，默认值为false。 |
| endIndex | number | 否 | 否 | 屏幕最后显示项的列表索引。默认值为0。 |
| error | string | 否 | 否 | 错误状态字符串。 |
| focusable | boolean | 否 | 否 | 表示元素是否可聚焦。true表示元素可聚焦，false表示元素不可聚焦，默认值为false。 |
| hintText | string | 否 | 否 | 提示文本。 |
| inputType | number | 否 | 否 | 输入文本的类型。默认值为0。 |
| inspectorKey | string | 否 | 否 | 检查键。 |
| isActive | boolean | 否 | 否 | 表示元素是否处于活动状态。true表示元素处于活动状态，false表示元素不处于活动状态，默认值为true。 |
| isEnable | boolean | 否 | 否 | 表示元素是否启用。true表示元素已启用，false表示元素未启用，默认值为false。 |
| isHint | boolean | 否 | 否 | 表示元素是否为提示状态。true表示元素处于提示状态，false表示元素不处于提示状态，默认值为false。 |
| isFocused | boolean | 否 | 否 | 表示元素是否聚焦。true表示元素处于聚焦状态，false表示元素不处于聚焦状态，默认值为false。 |
| isPassword | boolean | 否 | 否 | 表示元素是否为密码。true表示元素为密码，false表示元素不为密码，默认值为false。 |
| isVisible | boolean | 否 | 否 | 表示元素是否可见。true表示元素可见，false表示元素不可见，默认值为false。 |
| itemCount | number | 否 | 否 | 项目的总数。默认值为0。 |
| lastContent | string | 否 | 否 | 最后的内容。 |
| layer | number | 否 | 否 | 该元素的显示层。 |
| longClickable | boolean | 否 | 否 | 表示元素是否可长单击。true表示元素可长单击，false表示元素不可长单击，默认值为false。 |
| pageId | number | 否 | 否 | 页码id。默认值为-1。 |
| parent | [AccessibilityElement](#accessibilityelement) | 否 | 否 | 元素的父元素。 |
| pluralLineSupported | boolean | 否 | 否 | 表示元素是否支持多行文本。true表示元素支持多行文本，false表示元素不支持多行文本，默认值为false。 |
| rect | [Rect](#rect) | 否 | 否 | 元素的面积。 |
| resourceName | string | 否 | 否 | 元素的资源名称。 |
| rootElement | [AccessibilityElement](#accessibilityelement) | 否 | 否 | 窗口元素的根元素。 |
| screenRect | [Rect](#rect) | 否 | 否 | 元素的显示区域。 |
| scrollable | boolean | 否 | 否 | 表示元素是否可滚动。true表示元素可滚动，false表示元素不可滚动，默认值为false。 |
| selected | boolean | 否 | 否 | 表示元素是否被选中。true表示元素被选中，false表示元素未被选中，默认值为false。 |
| startIndex | number | 否 | 否 | 在屏幕上的第一个项目的列表索引。默认值为0。 |
| text | string | 否 | 否 | 元素的文本。 |
| textLengthLimit | number | 否 | 否 | 元素文本的最大长度限制。 |
| textMoveUnit | [accessibility.TextMoveUnit](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility#textmoveunit) | 否 | 否 | 文本被读取时的移动单位。 |
| triggerAction | [accessibility.Action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility#action) | 否 | 否 | 触发元素事件的动作。 |
| type | [WindowType](#windowtype) | 否 | 否 | 元素的窗口类型。 |
| valueMax | number | 否 | 否 | 最大值。默认值为0。 |
| valueMin | number | 否 | 否 | 最小值。默认值为0。 |
| valueNow | number | 否 | 否 | 当前值。默认值为0。 |
| windowId | number | 否 | 否 | 窗口ID。默认值为-1。 |
| textType12+ | string | 否 | 否 | 元素的无障碍文本类型，由组件accessibilityTextHint属性配置。 |
| offset12+ | number | 否 | 否 | 对于可滚动类控件，如List、Grid，内容区相对控件的顶部坐标滚动的像素偏移量。默认值为0。 |
| hotArea12+ | [Rect](#rect) | 否 | 否 | 元素的可触摸区域。 |
| customComponentType18+ | string | 否 | 是 | 自定义组件类型。 |
| accessibilityNextFocusId18+ | number | 否 | 是 | 下一个要聚焦的组件ID。通过findElement('elementId')查询到的AccessibilityElementInfo对象中可获取到用户在控件上设置的该属性值。默认值为-1。 |
| accessibilityPreviousFocusId18+ | number | 否 | 是 | 上一个聚焦的组件ID。通过findElement('elementId')查询到的AccessibilityElementInfo对象中可获取到用户在控件上设置的该属性值。默认值为-1。 |
| extraInfo18+ | string | 否 | 是 | 
扩展属性，用于定义一些特定组件的属性，包含：

\- CheckboxGroupSelectedStatus：表示CheckboxGroup组件的选中状态，其中取值0表示已选中，取值1表示部分选中，取值2表示未选中。

\- Row：Grid组件中聚焦item的行信息，表示该item在第几行。

\- Column：Grid组件中聚焦的item的列，表示该item在第几列。

\- ListItemIndex：List组件中聚焦item的行信息，表示当前该item在第几行。

\- SideBarContainerStates：表示可展开类组件（SideBarContainer、Select）的展开状态，其中取值0表示收起态，取值1表示展开态。

\- ToggleType：表示Toggle组件的具体类型，其中取值0表示Checkbox，取值1表示Switch，取值2表示Button。

\- BindSheet：表示BindSheet组件的状态，其中取值0表示状态高，取值1表示状态中，取值2表示状态低。

\- hasRegisteredHover：表示组件是否注册了onAccessibilityHover事件回调，取值为1表示组件注册了事件回调，若未注册不会使用该字段。

\- direction：表示list组件的布局方向，其中取值"vertical"表示竖向，取值"horizontal"表示横向。

\- expandedState：表示list组件中listItem的展开状态，其中取值"expanded"表示展开态，取值"collapsed"表示收起态。

\- componentTypeDescription：组件类型详细信息，对componentType的补充描述。

 |
| accessibilityScrollable18+ | boolean | 否 | 是 | 表示无障碍模式下元素是否滚动，优先级高于scrollable。其中，true表示可滚动，false表示不可滚动，默认值为true。 |

#### FocusDirection

type FocusDirection = 'up' | 'down' | 'left' | 'right' | 'forward' | 'backward'

表示查询下一焦点元素的方向。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| :-- | :-- |
| 'up' | 表示向上查询。 |
| 'down' | 表示向下查询。 |
| 'left' | 表示向左查询。 |
| 'right' | 表示向右查询。 |
| 'forward' | 表示向前查询。 |
| 'backward' | 表示向后查询。 |

#### FocusType

type FocusType = 'accessibility' | 'normal'

表示查询焦点元素的类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| :-- | :-- |
| 'accessibility' | 表示无障碍的焦点类型。 |
| 'normal' | 表示普通的焦点类型。 |

#### Rect

表示矩形区域。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| left | number | 否 | 否 | 矩形区域的左边界。 |
| top | number | 否 | 否 | 矩形区域的上边界。 |
| width | number | 否 | 否 | 矩形区域的宽度。 |
| height | number | 否 | 否 | 矩形区域的高度。 |

#### WindowType

type WindowType = 'application' | 'system'

表示窗口的类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| :-- | :-- |
| 'application' | 表示应用窗口类型。 |
| 'system' | 表示系统窗口类型。 |

#### AccessibilityExtensionContext.setTargetBundleName(deprecated)

setTargetBundleName(targetNames: Array<string>): Promise<void>;

设置关注的目标包名，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/E9Pn2vlaTNG5iXSClaPcEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=8C204E05AF5044A5AF91249B8B260536A554501EDB6E19537D2FD982216BF1FD)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| targetNames | Array<string> | 是 | 设置关注应用的包名，服务接收关注应用的无障碍事件，默认接收所有应用的无障碍事件，取消关注应用则传空数组。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let targetNames = ['com.ohos.xyz'];
axContext.setTargetBundleName(targetNames).then(() => {
  console.info(`Succeeded in set target bundle names, targetNames is ${targetNames}`);
}).catch((err: BusinessError) => {
  console.error(`failed to set target bundle names, Code is ${err.code}, message is ${err.message}`);
})
```

#### AccessibilityExtensionContext.setTargetBundleName(deprecated)

setTargetBundleName(targetNames: Array<string>, callback: AsyncCallback<void>): void;

设置关注的目标包名，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/gychSLGOTsuuIwcV9sqHsg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=166C88BB221F6B34A085DB70BF21EFA1FF955D60F9A8067D1E7B28943139F3FF)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| targetNames | Array<string> | 是 | 设置关注应用的包名，服务接收关注应用的无障碍事件，默认接收所有应用的无障碍事件，取消关注应用则传空数组。 |
| callback | AsyncCallback<void> | 是 | 回调函数，如果设置关注的目标包名失败，则AsyncCallback中err有数据返回。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let targetNames = ['com.ohos.xyz'];
try {
  axContext.setTargetBundleName(targetNames, (err: BusinessError) => {
    if (err && err.code) {
      console.error(`failed to set target bundle names, Code is ${err.code}, message is ${err.message}`);
      return;
    }
    console.info(`Succeeded in set target bundle names, targetNames is ${targetNames}`);
  });
} catch (error) {
  console.error(`failed to set target bundle names, Because ${JSON.stringify(error)}`);
}
```

#### AccessibilityExtensionContext.getFocusElement(deprecated)

getFocusElement(isAccessibilityFocus?: boolean): Promise<AccessibilityElement>;

获取焦点元素, 使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/jMDeoXmuSnG7tEKjoqcxhQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=B6CE6ED8AA26E5E0BB9E30EBB18D86C9747628455BE6BBEC1FE6988D0865F8AF)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isAccessibilityFocus | boolean | 否 | 获取的是否是无障碍焦点元素，true表示是，false表示否，默认为否。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AccessibilityElement](#accessibilityelement)\> | Promise对象，返回当前对应的焦点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getFocusElement().then((data: AccessibilityElement) => {
  rootElement = data;
  console.info(`Succeeded in get focus element,${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get focus element, Code is ${err.code}, message is ${err.message}`);
})
```

#### AccessibilityExtensionContext.getFocusElement(deprecated)

getFocusElement(callback: AsyncCallback<AccessibilityElement>): void;

获取焦点元素, 使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-n5l-5TMQUq3BCBgb8VEAg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=0689A39156312C9F19AEF392ECAC33707ADEE4B358660C637EF141E9A2B08BC2)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | 是 | 回调函数，返回当前对应的焦点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getFocusElement((err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(`failed to get focus element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  rootElement = data;
  console.info(`Succeeded in get focus element, ${JSON.stringify(data)}`);
});
```

#### AccessibilityExtensionContext.getFocusElement(deprecated)

getFocusElement(isAccessibilityFocus: boolean, callback: AsyncCallback<AccessibilityElement>): void;

获取焦点元素, 使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/QrwXylvHQdW3_bX2mgr6iA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=B9D5D5AAD5E5DB4F0EA52622867A632BA31CA91D3E5B0E130A7252CC8882A9B7)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| isAccessibilityFocus | boolean | 是 | 获取的是否是无障碍焦点元素，True表示是，False表示否。 |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | 是 | 回调函数，返回当前对应的焦点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let isAccessibilityFocus = true;
let rootElement: AccessibilityElement;

axContext.getFocusElement(isAccessibilityFocus, (err: BusinessError, data: AccessibilityElement)=> {
  if (err && err.code) {
    console.error(`failed to get focus element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  rootElement = data;
  console.info(`Succeeded in get focus element, ${JSON.stringify(data)}`);
});
```

#### AccessibilityExtensionContext.getWindowRootElement(deprecated)

getWindowRootElement(windowId?: number): Promise<AccessibilityElement>;

获取指定窗口的根节点元素, 使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/UfAKN1gQQzqVhoh7p6R4Rw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=6D79D41382281DBA6BC723CDD88C4C22DC276389757F30B49DAF538D9687B454)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 否 | 指定窗口的编号，未指定则从当前活跃窗口获取。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AccessibilityElement](#accessibilityelement)\> | Promise对象，返回指定窗口的根节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getWindowRootElement().then((data: AccessibilityElement) => {
  rootElement = data;
  console.info(`Succeeded in get root element of the window, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get root element of the window, Code is ${err.code}, message is ${err.message}`);
});
```

#### AccessibilityExtensionContext.getWindowRootElement(deprecated)

getWindowRootElement(callback: AsyncCallback<AccessibilityElement>): void;

获取指定窗口的根节点元素, 使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/RO2Riry7SRy60xLe7Mj8sw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=F4E84D402A9DD625A383D96053A655A055CBE7E401B6D66DF87072074CF3C7E8)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | 是 | 回调函数，返回指定窗口的根节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rootElement: AccessibilityElement;

axContext.getWindowRootElement((err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(`failed to get root element of the window, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  rootElement = data;
  console.info(`Succeeded in get root element of the window, ${JSON.stringify(data)}`);
});
```

#### AccessibilityExtensionContext.getWindowRootElement(deprecated)

getWindowRootElement(windowId: number, callback: AsyncCallback<AccessibilityElement>): void;

获取指定窗口的根节点元素, 使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/amtHks5OSdGyubXA9TmzjQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=0907A37BB4D1D448107DDB5F25243A145A9BFBBC05CB63702B7975F71B1F56E0)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| windowId | number | 是 | 指定窗口的编号，未指定则从当前活跃窗口获取。 |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | 是 | 回调函数，返回指定窗口的根节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let windowId = 10;
let rootElement: AccessibilityElement;

axContext.getWindowRootElement(windowId, (err: BusinessError, data: AccessibilityElement) => {
  if (err && err.code) {
    console.error(`failed to get root element of the window, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  rootElement = data;
  console.info(`Succeeded in get root element of the window, ${JSON.stringify(data)}`);
});
```

#### AccessibilityExtensionContext.getWindows(deprecated)

getWindows(displayId?: number): Promise<Array<AccessibilityElement>>;

获取指定屏幕中的所有窗口，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/FjeySpM8QpS_--IMHdGR7A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=307D5865241D59C45BA8F2C51962AA3F5FB4B6558399DBDFC356BFF3B3AFC89D)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 否 | 指定的屏幕编号，未指定则从默认主屏幕获取。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AccessibilityElement](#accessibilityelement)\>> | Promise对象，返回指定屏幕的所有窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

axContext.getWindows().then((data: AccessibilityElement[]) => {
  console.info(`Succeeded in get windows, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get windows, Code is ${err.code}, message is ${err.message}`);
});
```

#### AccessibilityExtensionContext.getWindows(deprecated)

getWindows(callback: AsyncCallback<Array<AccessibilityElement>>): void;

获取指定屏幕中的所有窗口，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/WfvKm7rfRmWR4Ou_Y-cqkA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=87A2B5A1E6A460CEFC268E5E729C98088F3400BD512F5B31BEE59E61910D0B9D)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[AccessibilityElement](#accessibilityelement)\>> | 是 | 回调函数，返回指定屏幕的所有窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

axContext.getWindows((err: BusinessError, data: AccessibilityElement[]) => {
  if (err && err.code) {
    console.error(`failed to get windows, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get windows, ${JSON.stringify(data)}`);
});
```

#### AccessibilityExtensionContext.getWindows(deprecated)

getWindows(displayId: number, callback: AsyncCallback<Array<AccessibilityElement>>): void;

获取指定屏幕中的所有窗口，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/h9zk3IM0T6WuQLpMzd3Xgw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=38EB838CCCCB883742615A7DE9A817DEDBF6B977DDAF063004E26FF1471FC6C3)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| displayId | number | 是 | 指定的屏幕编号，未指定则从默认主屏幕获取。 |
| callback | AsyncCallback<Array<[AccessibilityElement](#accessibilityelement)\>> | 是 | 回调函数，返回指定屏幕的所有窗口。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { AccessibilityElement } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let displayId = 10;
axContext.getWindows(displayId, (err: BusinessError, data: AccessibilityElement[]) => {
  if (err && err.code) {
    console.error(`failed to get windows, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get windows, ${JSON.stringify(data)}`);
});
```

#### AccessibilityExtensionContext.injectGesture(deprecated)

injectGesture(gesturePath: GesturePath): Promise<void>;

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/rbwGloYERqu2NXAKHXh__g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=1F619FABF683001F8090654571493238817CFCC4CA6946EC22EBC28A1021B750)

从API version 9开始支持，从API version 10开始废弃，建议使用[AccessibilityExtensionContext.injectGestureSync](#accessibilityextensioncontextinjectgesturesyncdeprecated)替代。

注入手势，使用Promise异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| gesturePath | [GesturePath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepath#gesturepath) | 是 | 表示手势的路径信息。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gesturePath: GesturePath = new GesturePath(100);

for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i * 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGesture(gesturePath).then(() => {
  console.info(`Succeeded in inject gesture,gesturePath is ${gesturePath}`);
}).catch((err: BusinessError) => {
  console.error(`failed to inject gesture, Code is ${err.code}, message is ${err.message}`);
});
```

#### AccessibilityExtensionContext.injectGesture(deprecated)

injectGesture(gesturePath: GesturePath, callback: AsyncCallback<void>): void

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Vla6SXRUQq6ifQ5K0xVF0Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=6985B44D0F44E34ACCC663E376C41153FAFA9EB9F7E999101666A061E8035349)

从API version 9开始支持，从API version 10开始废弃，建议使用[AccessibilityExtensionContext.injectGestureSync](#accessibilityextensioncontextinjectgesturesyncdeprecated)替代。

注入手势，使用callback异步回调。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| gesturePath | [GesturePath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepath#gesturepath) | 是 | 表示手势的路径信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，表示注入手势执行结果的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let gesturePath: GesturePath = new GesturePath(100);
for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i * 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGesture(gesturePath, (err: BusinessError) => {
  if (err) {
    console.error(`failed to inject gesture, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in inject gesture,gesturePath is ${gesturePath}`);
});
```

#### AccessibilityExtensionContext.injectGestureSync(deprecated)

injectGestureSync(gesturePath: GesturePath): void

注入手势。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/4X_o4VbMQPiikWvopYMvsg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=4EE157569A7859FDA24300694A8CF243D1B4C02F244D5AF5EAD082BF05774120)

从API version 10开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| gesturePath | [GesturePath](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility-gesturepath#gesturepath) | 是 | 表示手势的路径信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300003 | No accessibility permission to perform the operation. |

**示例：**

```ts
import { GesturePath, GesturePoint } from '@kit.AccessibilityKit';

let gesturePath: GesturePath = new GesturePath(100);
for (let i = 0; i < 10; i++) {
  let gesturePoint = new GesturePoint(100, i * 200);
  gesturePath.points.push(gesturePoint);
}
axContext.injectGestureSync(gesturePath);
```

#### AccessibilityElement

无障碍节点元素, 在调用AccessibilityElement的方法前，需要先通过[AccessibilityExtensionContext.getFocusElement()](#accessibilityextensioncontextgetfocuselementdeprecated) 或者[AccessibilityExtensionContext.getWindowRootElement()](#accessibilityextensioncontextgetwindowrootelementdeprecated) 获取AccessibilityElement实例。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

#### \[h2\]attributeNames(deprecated)

attributeNames<T extends keyof ElementAttributeValues>() : Promise<Array<T>>;

获取节点元素的所有属性名称，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/jG0mO4R_RTqzGKI5HEOPcQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=FDEA1577A50B2B5283A152739D1FD08985D91D4DB1BA9D4B8F1389194274AA16)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<T>> | Promise对象，返回节点元素的所有属性名称。 |

**示例：**

```ts
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例
rootElement.attributeNames().then((data: ElementAttributeKeys[]) => {
  console.info(`Succeeded in get attribute names, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get attribute names, Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]attributeNames(deprecated)

attributeNames<T extends keyof ElementAttributeValues>(callback: AsyncCallback<Array<T>>): void;

获取节点元素的所有属性名称，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/uGbRlPMHTUG244b7LQRImQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=1D191265E324595301614E5A9D026E4B12CE26DF528F0C97BFBAD2BF8312F489)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<T>> | 是 | 回调函数，返回节点元素的所有属性名称。 |

**示例：**

```ts
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例
rootElement.attributeNames((err: BusinessError, data: ElementAttributeKeys[]) => {
  if (err && err.code) {
    console.error(`failed to get attribute names, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get attribute names, ${JSON.stringify(data)}`);
});
```

#### \[h2\]attributeValue(deprecated)

attributeValue<T extends keyof ElementAttributeValues>(attributeName: T): Promise<ElementAttributeValues\[T\]>;

根据属性名称获取属性值，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/sMMOzFU-SN-ePIIq42rG4A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=583E07DC10A4414DD58ACE660EEA6CFD85F897DAA42FE056E80D39BBF2983938)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| attributeName | ElementAttributeKeys | 是 | 表示属性的名称。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<ElementAttributeValues\[T\]> | Promise对象，返回根据节点属性名称获取的属性值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300004 | This property does not exist. |

**示例：**

```ts
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let attributeName: ElementAttributeKeys = 'bundleName';

// rootElement是AccessibilityElement的实例
rootElement.attributeValue(attributeName).then((data: string) => {
  console.info(`Succeeded in get attribute value by name, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get attribute value, Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]attributeValue(deprecated)

attributeValue<T extends keyof ElementAttributeValues>(attributeName: T, callback: AsyncCallback<ElementAttributeValues\[T\]>): void

根据属性名称获取属性值。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/5gL9fLowSUezxWyg2pRfcg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=FE1125092A08D6D00E830133366E46EFAA42214DCA5C14658E5E95A15C6AB914)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| attributeName | ElementAttributeKeys | 是 | 表示属性的名称。 |
| callback | AsyncCallback<ElementAttributeValues\[T\]> | 是 | 回调函数，返回根据节点属性名称获取的属性值。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300004 | This property does not exist. |

**示例：**

```ts
import { ElementAttributeKeys } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let attributeName: ElementAttributeKeys = 'bundleName';

// rootElement是AccessibilityElement的实例
rootElement.attributeValue(attributeName, (err: BusinessError, data: string) => {
  if (err && err.code) {
    console.error(`failed to get attribute value, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get attribute value, ${JSON.stringify(data)}`);
});
```

#### \[h2\]actionNames(deprecated)

actionNames(): Promise<Array<string>>;

获取节点元素支持的所有操作名称，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/_PTVe7p5SUKvSx7BIoykAA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=F19C7350D3053294FBE60E35069D770800AFF515FE34A2F48EAE64891AB13E46)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<string>> | Promise对象，返回节点元素支持的所有操作名称。 |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例
rootElement.actionNames().then((data: string[]) => {
  console.info(`Succeeded in get action names, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to get action names, Code is ${err.code}, message is ${err.message}`);
})
```

#### \[h2\]actionNames(deprecated)

actionNames(callback: AsyncCallback<Array<string>>): void;

获取节点元素支持的所有操作名称，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/Qy2MxVzKRmC59nzGOAftCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=D4CB8485FB1C757BECCEB7B8B6BDF1326C7C07FC4EEA690AF40485400F01DF54)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | 是 | 回调函数，返回节点元素支持的所有操作名称。 |

**示例：**

```ts
// rootElement是AccessibilityElement的实例
rootElement.actionNames((err: BusinessError, data: string[]) => {
  if (err && err.code) {
    console.error(`failed to get action names, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in get action names, ${JSON.stringify(data)}`);
})
```

#### \[h2\]performAction(deprecated)

performAction(actionName: string, parameters?: object): Promise<void>;

根据操作名称执行某个操作，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/W8G6TCDjSceukpWD5mIXwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=CD9DC994C29260193EF1894CCEB5C491E2F26B0167781F66AD0F54793B81C31B)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| actionName | string | 是 | 表示属性的名称，取值参考[Action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility#action)。 |
| parameters | object | 否 | 表示执行操作时所需要的参数；默认为空。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300005 | This action is not supported. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';

// rootElement是AccessibilityElement的实例
rootElement.performAction(actionName).then(() => {
  console.info(`Succeeded in perform action,actionName is ${actionName}`);
}).catch((err: BusinessError) => {
  console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
});
```

**无参数Action示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例
// Action描述中无明确要求的，均为无参数Action
rootElement.performAction('click').then(() => {
  console.info(`Succeeded in perform action.`);
}).catch((err: BusinessError) => {
  console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
});
```

**有参数Action示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例
// setSelection示例代码
rootElement.performAction('setSelection', {
  selectTextBegin: '0', // 表示选择起始位置
  selectTextEnd: '8',   // 表示选择结束位置
  selectTextInForWard: true   // true表示为前光标，false表示为后光标
}).then(() => {
  console.info(`Succeeded in perform action`);
}).catch((err: BusinessError) => {
  console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
});
```

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// rootElement是AccessibilityElement的实例
// setCursorPosition示例代码
rootElement.performAction('setCursorPosition', {
  offset: '1'   // 表示光标的设置位置
}).then(() => {
  console.info(`Succeeded in perform action`);
}).catch((err: BusinessError) => {
  console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]performAction(deprecated)

performAction(actionName: string, callback: AsyncCallback<void>): void;

根据操作名称执行某个操作，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/KLqfhF6rT06vFt5Y8UOLHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=8852C8C78D61806753AEFA9359B90A81FCA944D4CD46693BC57EC1D092C0FEEA)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| actionName | string | 是 | 表示属性的名称，取值参考[Action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility#action)。 |
| callback | AsyncCallback<void> | 是 | 回调函数，表示执行指定操作的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300005 | This action is not supported. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';

// rootElement是AccessibilityElement的实例
rootElement.performAction(actionName, (err: BusinessError) => {
  if (err && err.code) {
    console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in perform action, actionName is ${actionName}`);
});
```

#### \[h2\]performAction(deprecated)

performAction(actionName: string, parameters: object, callback: AsyncCallback<void>): void;

根据操作名称执行某个操作，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/39aewmwuQzK_UZC3u4blxA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=1A166C1AFE0001F36E78CA47552B029E34328F5D594C84343CAC958592B3502A)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| actionName | string | 是 | 表示属性的名称，取值参考[Action](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-accessibility#action)。 |
| parameters | object | 是 | 表示执行操作时所需要的参数；默认为空。 |
| callback | AsyncCallback<void> | 是 | 回调函数，表示执行指定操作的回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)和[无障碍子系统错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-accessibility)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 9300005 | This action is not supported. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let actionName = 'action';
let parameters: object = [];

// rootElement是AccessibilityElement的实例
rootElement.performAction(actionName, parameters, (err: BusinessError) => {
  if (err && err.code) {
    console.error(`failed to perform action, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in perform action,actionName is ${actionName}, parameters is ${parameters}`);
});
```

#### \[h2\]findElement('content')(deprecated)

findElement(type: 'content', condition: string): Promise<Array<AccessibilityElement>>;

根据节点内容查询所有节点元素，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/68WI7WmJTaKVUCaFbJbbuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=09BE817BDAEB5A5175352856E29A01D6BA007C7E8AEC3A5EA04EF107EAD4720B)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定为'content', 表示查找的类型为节点元素内容。 |
| condition | string | 是 | 表示查找的条件。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<Array<[AccessibilityElement](#accessibilityelement)\>> | Promise对象，返回满足指定查询关键字的所有节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let condition = 'keyword';

// rootElement是AccessibilityElement的实例
rootElement.findElement('content', condition).then((data: AccessibilityElement[]) => {
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]findElement('content')(deprecated)

findElement(type: 'content', condition: string, callback: AsyncCallback<Array<AccessibilityElement>>): void;

根据节点内容查询所有节点元素。使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/m2Vg_aJKQpql7gRwZJIqHA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=704A3A7E1EF046CD015CB94C5854CFC4F43B96BC80401D2ACF40313ACA9696C6)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定为'content',表示查找的类型为节点元素内容。 |
| condition | string | 是 | 表示查找的条件。 |
| callback | AsyncCallback<Array<[AccessibilityElement](#accessibilityelement)\>> | 是 | 回调函数，返回满足指定查询关键字的所有节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let condition = 'keyword';

// rootElement是AccessibilityElement的实例
rootElement.findElement('content', condition, (err: BusinessError, data: AccessibilityElement[])=>{
  if (err && err.code) {
    console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
});
```

#### \[h2\]findElement('focusType')(deprecated)

findElement(type: 'focusType', condition: FocusType): Promise<AccessibilityElement>;

根据焦点元素类型查询节点元素，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/tf2dI1-rSgmZrto5mD9Qnw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=DB0B280DFE1B292775B11896D700134F8EF5A8D0A49F78389B0B6330837FE964)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定为'focusType'，表示查询的类型为节点的焦点元素类型。 |
| condition | [FocusType](#focustype) | 是 | 表示查询焦点元素的类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AccessibilityElement](#accessibilityelement)\> | Promise对象，返回满足指定查询焦点元素类型的节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { FocusType } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusType = 'normal';

// rootElement是AccessibilityElement的实例
rootElement.findElement('focusType', condition).then((data: AccessibilityElement) => {
  console.info(`Succeeded in find element,${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]findElement('focusType')(deprecated)

findElement(type: 'focusType', condition: FocusType, callback: AsyncCallback<AccessibilityElement>): void;

根据焦点元素类型查询节点元素，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/VR9zLystT365RnxfKdPgvw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=FB742D47D2E0A6A04D35348B8C03A696F5DDC36B2EE73972AC9963EF7826D994)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定为'focusType'，表示查询的类型为节点的焦点元素类型。 |
| condition | [FocusType](#focustype) | 是 | 表示查询焦点元素的类型。 |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | 是 | 回调函数，返回满足指定查询焦点元素类型的节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { FocusType } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusType = 'normal';

// rootElement是AccessibilityElement的实例
rootElement.findElement('focusType', condition, (err: BusinessError, data: AccessibilityElement)=>{
  if (err && err.code) {
    console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
});
```

#### \[h2\]findElement('focusDirection')(deprecated)

findElement(type: 'focusDirection', condition: FocusDirection): Promise<AccessibilityElement>;

根据下一焦点元素方向查询节点元素，使用Promise异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/-pHrQr1ESU2NCUBafgmKDg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=D3AC5C3F0428CE1E4940A9DA65883468294E64EB06B7A8BF3E39861DE581BBDE)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定为'focusDirection'，表示查询的类型为节点的下一焦点元素方向。 |
| condition | [FocusDirection](#focusdirection) | 是 | 表示查询下一焦点元素的方向。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<[AccessibilityElement](#accessibilityelement)\> | Promise对象，返回满足指定查询下一焦点元素方向的节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { FocusDirection } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusDirection = 'up';

// rootElement是AccessibilityElement的实例
rootElement.findElement('focusDirection', condition).then((data: AccessibilityElement) => {
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
  console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
});
```

#### \[h2\]findElement('focusDirection')(deprecated)

findElement(type: 'focusDirection', condition: FocusDirection, callback: AsyncCallback<AccessibilityElement>): void;

根据下一焦点元素方向查询节点元素，使用callback异步回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/87VdaPn9Qb2zSzc4rFDBeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=82C11C33D7A55C6D2B8CBB6AE965F585F7FA3D89BD24740FF295E98F1534C6A8)

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | string | 是 | 固定为'focusDirection', 表示查询的类型为节点的下一焦点元素方向。 |
| condition | [FocusDirection](#focusdirection) | 是 | 表示下一查询焦点元素的方向。 |
| callback | AsyncCallback<[AccessibilityElement](#accessibilityelement)\> | 是 | 回调函数，返回满足指定查询下一焦点元素方向的节点元素。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-universal)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```ts
import { FocusDirection } from '@kit.AccessibilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let condition: FocusDirection = 'up';

// rootElement是AccessibilityElement的实例
rootElement.findElement('focusDirection', condition, (err: BusinessError, data: AccessibilityElement) =>{
  if (err && err.code) {
    console.error(`failed to find element, Code is ${err.code}, message is ${err.message}`);
    return;
  }
  console.info(`Succeeded in find element, ${JSON.stringify(data)}`);
});
```
