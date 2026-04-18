---
title: "跨设备互通（RichEditor控件）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-richeditor-title"
menu_path:
  - "指南"
  - "系统"
  - "网络"
  - "Service Collaboration Kit（协同服务）"
  - "跨设备互通（RichEditor控件）"
captured_at: "2026-04-17T01:35:54.570Z"
---

# 跨设备互通（RichEditor控件）

富文本控件[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)已集成跨设备互通能力。在平板或2in1设备上，用户可通过其右键菜单调用手机的相机、扫描及图库（访问图片）功能。

#### 场景介绍

您通过此能力实现跨设备交互，可以使用其他设备的相机、扫描和图库功能。

#### 约束与限制

需同时满足以下条件，才能使用该功能：

-   **设备限制**
    
    -   本端设备：HarmonyOS版本为HarmonyOS NEXT及以上的平板或2in1设备。
    -   远端设备：HarmonyOS版本为HarmonyOS NEXT及以上、具有相机能力的手机或平板设备。
-   **使用限制**
    
    -   双端设备需要登录同一华为账号。
    -   跨设备互通API支持根据特定调用策略调用设备。调用策略：2in1设备可以调用平板和手机，平板可以调用手机，同类型设备不可调用。
    -   双端设备需要打开WLAN和蓝牙开关。
        
        条件允许时，建议双端设备接入同一个局域网，可提升唤醒相机的速度。
        

#### 开发步骤

添加[RichEditor](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-richeditor)富文本组件，即可在富文本组件中右键中选择其他设备进行导入，通过onWillChange属性对回传的照片进行处理。

```typescript
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController()
  options: RichEditorOptions = { controller: this.controller }

  build() {
    Column() {
      Column() {
        RichEditor(this.options)
          .onWillChange((value: RichEditorChangeValue) => {
            if (value?.replacedImageSpans[0]?.imageStyle?.objectFit != 0) {
              return true;
            }
            for(let item of value.replacedImageSpans) {
              this.controller.addImageSpan(item.valuePixelMap, {
                imageStyle: {
                  size: ["500px", "500px"],
                  layoutStyle: {
                    borderRadius: '10px',
                  }
                }
              })
            }
            return false;
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("100%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }
  }
}
```

富文本组件使用流程如下：

1.在富文本区域右键。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/c9sPWsmBQLmhP0fvLS_NYQ/zh-cn_image_0000002569019099.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=79D260A30EEAFAD465A285468712FDEE0CDFF7C8C8C91B5BC9F970495799C86E)

2.选择想要使用的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/bqD1jhOsR9Cj-fbypUw4zA/zh-cn_image_0000002568899089.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=EDFEB5C0AFB6D1E47FEB561B10E53DC8E227BB5E11F9BB7198395A5C3F3459B2)

3.等待对端设备拍照回传。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/cnk-dEtAQ6yokNSNwsm9ug/zh-cn_image_0000002538019384.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=DC5DF05DCCDCA7ADD5EEFF980A04C2D85342EA090C00284412B069C9459BDEC2)

4.图片回传后，在光标后面已嵌入一张图片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/XeMEkBWmTOeb41AVcEXGKA/zh-cn_image_0000002538179314.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=133DD4595C2DDD628272FEA672A42E8198109031BC872ABC04E630693C796045)

#### 关闭富文本跨设备互通能力

如果需要关闭富文本右键菜单跨设备互通能力，可通过editMenuOptions属性自定义菜单内容去除跨设备互通菜单项，示例如下：

```typescript
@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController()
  options: RichEditorOptions = { controller: this.controller }

  build() {
    Column() {
      Column() {
        RichEditor(this.options)
          .editMenuOptions({
            onCreateMenu: (menuItems: Array<TextMenuItem>) => {
              if (menuItems.length === 0) {
                return menuItems;
              }
              let newMenuItems: TextMenuItem[] = [];
              menuItems.forEach((item, index) => {
                if(!item.id.equals(TextMenuItemId.COLLABORATION_SERVICE)) {
                  newMenuItems.push(item);
                }
              })
              return newMenuItems;
            },
            onMenuItemClick: (menuItem: TextMenuItem, textRange: TextRange) => {
              return false;
            }
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width("100%")
          .height("100%")
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width("100%")
      .height("70%")
    }
  }
}
```
