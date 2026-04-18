---
title: "Class (CursorController)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-cursorcontroller"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "@ohos.arkui.UIContext (UIContext)"
  - "Class (CursorController)"
captured_at: "2026-04-17T01:47:52.739Z"
---

# Class (CursorController)

提供光标样式设置的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/UNv1crTVTvyH24zVdxIveA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014754Z&HW-CC-Expire=86400&HW-CC-Sign=2112FAF0C0A50BD9EA3124B2A8971FBD3F71C2E7A5813CC7E31A547407EFEA61)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本Class首批接口从API version 12开始支持。
    
-   以下API需先使用UIContext中的[getCursorController()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getcursorcontroller12)方法获取CursorController实例，再通过此实例调用对应方法。
    

#### restoreDefault12+

restoreDefault(): void

恢复默认的光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

当光标移出绿框时，通过CursorController的restoreDefault方法恢复默认光标样式。

```ts
import { pointer } from '@kit.InputKit';
import { UIContext, CursorController } from '@kit.ArkUI';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  cursorCustom: CursorController = this.getUIContext().getCursorController();

  build() {
    Column() {
      Row().height(200).width(200).backgroundColor(Color.Green).position({x: 150 ,y:70})
        .onHover((flag) => {
          if (flag) {
            this.cursorCustom.setCursor(pointer.PointerStyle.EAST);
          } else {
            console.info("restoreDefault");
            this.cursorCustom.restoreDefault();
          }
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/y4-A698aS5WnqI3sUyZ2Yw/zh-cn_image_0000002538180280.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014754Z&HW-CC-Expire=86400&HW-CC-Sign=FB8C2A67451BD3E0A251DD599D510AD21578C55DB7FA3AF0F3720C8AC1D2411E)

#### setCursor12+

setCursor(value: PointerStyle): void

更改当前的鼠标光标样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/mf-NpuHLTgqtGBieUWGQuQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014754Z&HW-CC-Expire=86400&HW-CC-Sign=4D420CD4E79965042B0A7A373D5227713DDB663FECDFB30A48B8CC63FACDCB75)

该接口调用后不会立即生效，而是在下一帧改变鼠标光标样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| value | [PointerStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-t#pointerstyle12) | 是 | 光标样式。 |

**示例：**

当光标进入蓝框时，通过CursorController的setCursor方法修改光标样式为PointerStyle.WEST。

```ts
import { pointer } from '@kit.InputKit';
import { UIContext, CursorController } from '@kit.ArkUI';

@Entry
@Component
struct CursorControlExample {
  @State text: string = '';
  cursorCustom: CursorController = this.getUIContext().getCursorController();

  build() {
    Column() {
      Row().height(200).width(200).backgroundColor(Color.Blue).position({x: 100 ,y:70})
        .onHover((flag) => {
          if (flag) {
            this.cursorCustom.setCursor(pointer.PointerStyle.WEST);
          } else {
            this.cursorCustom.restoreDefault();
          }
        })
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/TUJhBYBZRP67nSMSVnXm9g/zh-cn_image_0000002569020069.gif?HW-CC-KV=V1&HW-CC-Date=20260417T014754Z&HW-CC-Expire=86400&HW-CC-Sign=58597EBD68C25F61DBDCD7B70FF6A6138E1C11A0EAFF9DCD755574314F95E255)
