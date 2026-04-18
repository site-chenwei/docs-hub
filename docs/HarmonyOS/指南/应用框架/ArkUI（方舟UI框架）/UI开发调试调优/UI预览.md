---
title: "UI预览"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-ide-previewer"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发调试调优"
  - "UI预览"
captured_at: "2026-04-17T01:35:41.224Z"
---

# UI预览

DevEco Studio为开发者提供了UI预览功能，方便查看UI效果并随时调整页面布局。预览支持页面预览和组件预览。图1中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/dRzq6j8FSHqrguU-fETkxA/zh-cn_image_0000002568898785.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=F4CF177927B77ECB44448D7C9BB2AD839D68271FE8299977950CFDDB8AAC0531)表示页面预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/o3eTZ0HvTYOvSV8ZsokZwg/zh-cn_image_0000002538019080.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=5C00A3526BF61A9FA32E3AB3698F7A5DA3A551E10F6B8594E4AAD056780A89F2)表示组件预览。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/-wMI7kglQ0ygZLNglIdciw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=1874A660B3A7840B4F2A9B04FF89ABC091E7298BD425D07A31AE64A92F4B2BC4)

操作系统和真机设备的差异可能导致预览效果与真机效果不同。预览效果仅作参考，实际效果以真机为准。

**图1** 预览图标

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/95x2nCcoQtS75EZyq96pzQ/zh-cn_image_0000002538179008.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=1DC8D098954A94DA1D80406FF94C0CD05FDCA4365D80E541D8B5A1254DA7E1DA)

#### 页面预览

ArkTS应用/元服务均支持页面预览。页面预览通过在工程的ets文件中，给自定义组件添加[@Entry](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-create-custom-components#entry)装饰器，即可以查看当前UI页面效果。

-   启动方式：选中需要预览的ets页面，点击右侧侧边栏的Previewer按钮，启动页面预览。
    
-   热加载：在启动页面预览的前提下，添加、删除或修改UI组件后，通过Ctrl+S保存，预览器会同步刷新预览效果，无需重新启动预览。
    
-   路由能力：支持通过路由能力进行页面切换查看其它页面预览效果。
    

在页面预览的基础上，提供了极速预览和Inspector双向预览两种特性。下面将详细说明这两种特性。

#### \[h2\]极速预览

支持在修改组件的属性时，无需使用Ctrl+S进行保存，可以直接观察到修改后的预览效果。极速预览默认开启，若需关闭，点击预览器右上角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/xRukIJ1SRxqOJ93Y4GLwSA/zh-cn_image_0000002569018797.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=FC454E4D882CA72EA358EC4898DAC940526D7EA30FDF90C4DAAFF839BBC02890)即可。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/AmaxUQRNSXiGaE7FMaOCiA/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=D10F13F5A5FA7C8DAFAB540C5EDA4F15E5DF8DE89EA890C3D4B74FA2E05F179C)

部分应用场景不支持极速预览：

-   不显示的组件。
-   新增或删除组件。
-   包含private变量或无类型的controller的组件。
-   使用了[@Builder](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builder)、[@Style](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-style)、[@Extend](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-extend)等装饰器的组件。
-   修改使用import导入外部组件/模块的组件。
-   修改状态变量。

效果如图2所示：

**图2** 极速预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/3iSi_pdrQvaDUsHRIsWEaA/zh-cn_image_0000002568898787.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=333959C15264AD5F1201C152AB2F0C9FE470C43B851AB3D669C51E5313800780)

#### \[h2\]inspector双向预览

支持ets文件与预览器的双向预览。使用时，点击预览器界面图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/gcdoSJzDQ_Kt7-8tEiK9mw/zh-cn_image_0000002538019082.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=84CBB53D04563EC8CC6650A640AFCFBF23F0657A3EB0F85B3D9AA1E0F50F2153)开启双向预览功能。

开启双向预览功能后，支持代码编辑器、UI界面和组件树之间的联动：

1.  选中预览器界面中的组件，组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
    
2.  选中布局文件中的代码块，预览器界面将高亮显示，组件树上的组件节点将呈现被选中的状态。
    
3.  选中组件树中的组件，对应的代码块和预览器界面将高亮显示。
    
4.  在预览界面，通过组件的属性面板修改可修改的属性或样式。预览界面的修改会自动同步到代码编辑器中，并实时刷新预览器界面。代码编辑器中的源码修改也会实时刷新预览器界面，并更新组件树信息及组件属性。
    

效果如图3所示：

**图3** inspector双向预览演示图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/f4AB5YkUTSuWdZ6IrucxXw/zh-cn_image_0000002538179010.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=3CCC9422066C5135408EA5B0DEAC621CBD928730D6552ED52ACC21042FD1F607)

#### 组件预览

ArkTS应用/元服务支持组件预览功能。组件预览通过在自定义组件前添加[@Preview](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-previewer#preview装饰器)装饰器实现。在单个源文件中，最多可以使用10个@Preview装饰自定义组件。启动方式：

-   当组件被@Entry和@Preview装饰时，点击右侧侧边栏的Previewer按钮，启动页面预览，页面加载成功后，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/b30H8BOSQt-UmfTeFB3ReA/zh-cn_image_0000002538019080.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=E08F68EACCDDBEDF2883E96EBD85278EEAB0855864328CD0E44B34C41611B745)，切换到组件预览。
-   当组件仅被@Preview装饰时，点击右侧侧边栏的Previewer按钮，则默认为组件预览。

组件预览时，使用@Preview装饰器的默认属性（请参考[PreviewParams](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-component-previewer#previewparams9)）进行效果显示。可以通过设置@Preview的参数，指定预览设备的相关属性，包括设备类型、屏幕形状等。

@Preview的使用参考如下示例：

```ts
@Entry
@Preview
@Component
struct ComponentPreviewOne {
  build() {
    Column() {
      Text('this is component previewer One')
        .height(80)
        .fontSize(30)
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
      Image($r('app.media.startIcon'))
        .height(300)
        .width(300)
    }
  }
}

@Preview
@Component
struct ComponentPreviewTwo {
  build() {
    Column() {
      Text('this is component previewer Two')
        .height(80)
        .fontSize(30)
        .fontColor(Color.Pink)
      // $r('app.media.startIcon')需要替换为开发者所需的图像资源文件
      Image($r('app.media.startIcon'))
        .height(300)
        .width(300)
    }
  }
}
```

效果如图4所示：

**图4** 组件预览效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/H-PjBUpISZ28P-wyAp9ofA/zh-cn_image_0000002569018799.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=18BEE7A4474A32272BFE3BADB85A2AB723A8D55D719D074B3B3CFA280E51B161)

#### 动态修改分辨率

同一个应用/元服务可以运行在多个设备上，因不同设备的屏幕分辨率、形状、大小等不同，开发者需要在不同的设备上查看应用/元服务的UI布局和交互效果。预览支持动态修改分辨率，方便开发者随时查看不同设备上的页面显示效果。启动方式：启动页面预览后，点击右上角![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/vvzs-nKySdOsR-eJt2-qlA/zh-cn_image_0000002568898789.png?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=2CF33971EA085FC8A4F1E537D7A489016DBDC427746BBD437B16DE1C740DF046)，即可拖动页面选中框动态修改当前设备的屏幕大小。

效果如图5所示：

**图5** 动态修改分辨率效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/xDaCjmQxQ729baowpY1tVw/zh-cn_image_0000002538019084.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013542Z&HW-CC-Expire=86400&HW-CC-Sign=5F4235F3A1333B363FD0CEA975CFFF5A56CA1D8A49586074599A1BBD33AC0964)
