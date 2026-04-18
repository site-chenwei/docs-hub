---
title: "NodeContent"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-nodecontent"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "arkui"
  - "NodeContent"
captured_at: "2026-04-17T01:47:53.534Z"
---

# NodeContent

NodeContent是ArkUI提供的[ContentSlot](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-components-contentslot)的管理器。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/b1GXDVs8SKKOErukoSB2xw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014755Z&HW-CC-Expire=86400&HW-CC-Sign=3CC6F377EF05E3741418C4CE2F9A02B988A4D9457E9869017F41E1AFC51AED1A)

-   本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   NodeContent对象不支持使用JSON序列化。
    

#### 导入模块

```ts
import { NodeContent } from '@kit.ArkUI';
```

#### NodeContent

NodeContent是节点内容的实体封装。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor

constructor()

节点内容的实体封装。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
import { nativeNode } from 'libNativeNode.so'; // 开发者自己实现的so
import { NodeContent } from '@kit.ArkUI';

@Component
struct Parent {
  private nodeContent: Content = new NodeContent();

  aboutToAppear() {
    // 通过C-API创建节点，并添加到管理器nodeContent上
    nativeNode.createNativeNode(this.nodeContent);
  }

  build() {
    Column() {
      // 显示nodeContent管理器里存放的Native侧的组件
      ContentSlot(this.nodeContent)
    }
  }
}
```

上述代码中so的实现可参考[Native XComponent](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/ArkUISample/NativeXComponentSample)。

#### \[h2\]addFrameNode12+

addFrameNode(node: FrameNode): void

根据参数将FrameNode添加到NodeContent中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| node | [FrameNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode) | 是 | 需要添加的FrameNode。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-node)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: it cannot be adopted." |

#### \[h2\]removeFrameNode12+

removeFrameNode(node: FrameNode): void

根据参数将FrameNode从NodeContent中删除。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| node | [FrameNode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-framenode) | 是 | 需要删除的FrameNode。 |

**示例：**

添加删除NodeContent中的FrameNode节点。

```ts
// xxx.ets
import { NodeContent, typeNode } from '@kit.ArkUI';

class NodeContentCtrl {
  content: NodeContent;
  textNode: Array<typeNode.Text> = new Array();
  uiContext: UIContext;
  width: number;

  constructor(uiContext: UIContext) {
    this.content = new NodeContent();
    this.uiContext = uiContext;
    this.width = Infinity;
  }

  AddNode() {
    let node = typeNode.createNode(this.uiContext, "Text");
    node.initialize("ContentText:" + this.textNode.length).fontSize(20);
    this.textNode.push(node);
    this.content.addFrameNode(node);
  }

  RemoveNode() {
    let node = this.textNode.pop();
    this.content.removeFrameNode(node);
  }

  RemoveFront() {
    let node = this.textNode.shift();
    this.content.removeFrameNode(node);
  }

  GetContent(): NodeContent {
    return this.content;
  }
}

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';
  controller = new NodeContentCtrl(this.getUIContext());

  build() {
    Row() {
      Column() {
        ContentSlot(this.controller.GetContent())
        Button("AddToSlot")
          .onClick(() => {
            this.controller.AddNode();
          })
        Button("RemoveBack")
          .onClick(() => {
            this.controller.RemoveNode();
          })
        Button("RemoveFront")
          .onClick(() => {
            this.controller.RemoveFront();
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
