---
title: "XComponentNode"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-xcomponentnode"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "XComponentNode"
captured_at: "2026-04-17T01:47:54.167Z"
---

# XComponentNode

提供XComponent节点XComponentNode，表示组件树中的[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)组件，用于[EGL](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/egl)/[OpenGL ES](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/opengles)和媒体数据写入，并支持动态修改节点渲染类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/d755vC3XTEmABZ7R83ffxg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=C660D8921A7F0FE2F073DD0591F92EE6666322B255BB6241CE0FAB5A4E456ABB)

从API version 12开始废弃，建议使用[类型为XComponent的typeNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode#xcomponent12)的方式实现。

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

当前不支持在预览器中使用XComponentNode。

#### 导入模块

```ts
import { XComponentNode } from "@kit.ArkUI";
```

#### XComponentNode(deprecated)

#### \[h2\]constructor(deprecated)

constructor(uiContext: UIContext, options: RenderOptions, id: string, type: XComponentType, libraryName?: string)

XComponentNode的构造函数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/xBSeP6kUT0aDPnzEHgKDIA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=65F7B8BF3873AFE3F91C80803AB6A993E31F338EAAB4C8B79664C6B3F5648C8D)

从API version 11开始支持，从API version 12开始废弃，建议使用[createNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode#createnodexcomponent12)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| uiContext | [UIContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext) | 是 | UI上下文，获取方式可参考[UIContext获取方法](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-node#uicontext获取方法)。 |
| options | [RenderOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-buildernode#renderoptions) | 是 | XComponentNode的构造可选参数。 |
| id | string | 是 | XComponent的唯一标识，支持最大的字符串长度128。详见[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)组件。 |
| type | [XComponentType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-appendix-enums#xcomponenttype10) | 是 | 用于指定XComponent组件类型。详见[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)组件。 |
| libraryName | string | 否 | Native层编译输出动态库名称。详见[XComponent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent)组件。 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/8sme8Zm3S7KVB5IY2e-TeQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=75EDE69432088D803A94350FE98A9E039D1320B3109B0CC4981C059E0DE7FC89)

需要显式指定[RenderOptions](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-buildernode#renderoptions)中的selfIdealSize，否则XComponentNode内容大小为空，不显示任何内容。

#### \[h2\]onCreate(deprecated)

onCreate(event?: Object): void

XComponentNode加载完成时触发该回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/HObPLkEHSDOwcKA3Urw6xQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=E664F8DA494841CCB1B38886A905B355F5CB4A7D671D553C0B37B1996ED4C3F0)

从API version 11开始支持，从API version 12开始废弃，建议使用[onLoad](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent#onload)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| event | Object | 否 | 获取XComponent实例对象的context，context上挂载的方法由开发者在C++层定义。 |

#### \[h2\]onDestroy(deprecated)

onDestroy(): void

XComponentNode销毁时触发该回调。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/RB-haTOdQfmvHVjxzYNQpw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=B16B5CBC7662DB6905DCA749B1EB660D345A2D809B0E54ECC7A16734DD283228)

从API version 11开始支持，从API version 12开始废弃，建议使用[onDestroy](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-xcomponent#ondestroy)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]changeRenderType(deprecated)

changeRenderType(type: NodeRenderType): boolean

修改XComponentNode的渲染类型。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/7nuvUoBlRcu4AyZVbgQ2Nw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=5C0C0592236F33DEC04C7018B303B080B9B724EB6D26F776D3DC04CAAA430001)

从API version 11开始支持，从API version 12开始废弃，建议使用[appendChild](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode#appendchild12)替代。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| type | [NodeRenderType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-buildernode#noderendertype) | 是 | 需要修改的渲染类型。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| boolean | 
修改渲染类型是否成功。

true：修改渲染类型成功；false：修改渲染类型失败。

 |

#### 示例

```ts
import { NodeController, FrameNode, XComponentNode, NodeRenderType, UIContext} from '@kit.ArkUI'

class XComponentNodeController extends NodeController {
  private xComponentNode: MyXComponentNode | null = null;
  private soName: string = "tetrahedron_napi" // 该 so 由开发者通过 NAPI 编写并生成

  constructor() {
    super();
  }

  makeNode(context: UIContext): FrameNode | null {
    this.xComponentNode = new MyXComponentNode(context, {
      selfIdealSize: { width: 200, height: 200 }
    }, "xComponentId", XComponentType.SURFACE, this.soName);
    return this.xComponentNode;
  }

  changeRenderType(renderType: NodeRenderType): void {
    if (this.xComponentNode) {
      this.xComponentNode.changeRenderType(renderType);
    }
  }
}

class MyXComponentNode extends XComponentNode {
  onCreate(event: Object) {
    // do something when XComponentNode has created
  }

  onDestroy() {
    // do something when XComponentNode is destroying
  }
}

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        NodeContainer(new XComponentNodeController())
      }
      .width('100%')
      .height('100%')
    }
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/iLUTsxFHSqabgROrKc6v0Q/zh-cn_image_0000002568900115.jpg?HW-CC-KV=V1&HW-CC-Date=20260417T014756Z&HW-CC-Expire=86400&HW-CC-Sign=0C64A3C6733071DBEAE3EBE7265D811D3E322606497C62BFCFEDED2C2E13E4A7)
