---
title: "Class (ContextMenuController)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-contextmenucontroller"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "@ohos.arkui.UIContext (UIContext)"
  - "Class (ContextMenuController)"
captured_at: "2026-04-17T01:47:52.728Z"
---

# Class (ContextMenuController)

提供控制菜单关闭的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/zSDFa2ebSfWtikf9dJCsTQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014754Z&HW-CC-Expire=86400&HW-CC-Sign=2B6B57FA3109B93B0331CF64D2594A7F55390525F3E13AD3DA0B2EE6C90B8B78)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   以下API需先使用UIContext中的[getContextMenuController()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getcontextmenucontroller12)方法获取ContextMenuController实例，再通过此实例调用对应方法。
    

#### close12+

close(): void

关闭菜单。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

通过定时器触发，调用ContextMenuController的close方法关闭菜单。

```ts
import { ContextMenuController } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  menu: ContextMenuController = this.getUIContext().getContextMenuController();

  @Builder MenuBuilder() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button('Test ContextMenu1 Close')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('Test ContextMenu2')
      Divider().strokeWidth(2).margin(5).color(Color.Black)
      Button('Test ContextMenu3')
    }
    .width(200)
    .height(160)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
      Button("启动定时器").onClick(()=>
      {
        setTimeout(() => {
          this.menu.close();
        }, 10000);
      })

      Column() {
        Text("Test ContextMenu close")
          .fontSize(20)
          .width('100%')
          .height(500)
          .backgroundColor(0xAFEEEE)
          .textAlign(TextAlign.Center)
      }
      .bindContextMenu(this.MenuBuilder, ResponseType.LongPress)
    }
    .width('100%')
    .height('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/SDiLYoxPRTaqNEQzXC7vvA/zh-cn_image_0000002538020354.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014754Z&HW-CC-Expire=86400&HW-CC-Sign=E790F428452456FE6E9481832CEA79BA91AC6A3E65EC2B91B8F67E15E17156E9)
