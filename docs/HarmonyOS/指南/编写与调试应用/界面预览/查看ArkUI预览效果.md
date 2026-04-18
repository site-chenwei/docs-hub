---
title: "查看ArkUI预览效果"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkui"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "界面预览"
  - "查看ArkUI预览效果"
captured_at: "2026-04-17T01:36:48.718Z"
---

# 查看ArkUI预览效果

ArkUI预览支持页面预览、组件预览和卡片预览，下图中左侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/MzyeE3FVQo2_61jBdgqzhQ/zh-cn_image_0000002561833361.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=ABF47DB642400BE1DD2C0D76676E6CF47E8440ABB51D39367D373171FFAE8583)为页面预览，右侧图标![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/TZIReSONQx6fl5YTYVKfbA/zh-cn_image_0000002530913440.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=47B582A34277CD2C4B51E2A9ABB3D58210C3F78A2D88DB4A7609F2260A13611D)为组件预览，卡片预览在创建卡片文件后可直接预览。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/iItA8nWFS2G8DnkJGBN1Xg/zh-cn_image_0000002561833359.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=10C8B236DEAB3E660820B535B98E985725843324D10C4DBBB53940B5006B4ED2)

#### 页面预览

ArkTS应用/元服务支持页面预览。页面预览通过在工程的ets文件头部添加@Entry实现。

@Entry的使用参考如下示例：

@Entry
@Component
struct Index {
  @State message: string = 'Hello World'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

#### 组件预览

ArkTS应用/元服务支持组件预览。组件预览支持实时预览，不支持动态图和动态预览。组件预览通过在组件前添加注解@Preview实现，在单个源文件中，最多可以使用10个@Preview装饰自定义组件。

@Preview的使用参考如下示例：

@Preview({
  title: 'ContentTable'
})
@Component
struct ContentTablePreview {
  build() {
    Flex() {
      ContentTable({ foodItem: getDefaultFoodData() })
    }
  }
}

以上示例的组件预览效果如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/ZBYfrNK9QxeIlbe5v9d88w/zh-cn_image_0000002530913446.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=2C3B1AA52827DC8090F121E91947E30FCABA0EB435355593E592E38F3829716A "点击放大")

组件预览默认的预览设备为Phone，若您想查看不同的设备，或者不同的屏幕形状，或者不同设备语言等情况下的组件预览效果，可以通过设置@Preview的参数，指定预览设备的相关属性。若不设置@Preview的参数，默认的设备属性如下所示：

@Preview({
  title: 'Component1',  //预览组件的名称
  deviceType: 'phone',  //指定当前组件预览渲染的设备类型，默认为Phone
  width: 1080,  //预览设备的宽度，单位：px
  height: 2340,  //预览设备的长度，单位：px
  colorMode: 'light',  //显示的亮暗模式，当前支持取值为light
  dpi: 480,  //预览设备的屏幕DPI值
  locale: 'zh\_CN',  //预览设备的语言，如zh\_CN、en\_US等
  orientation: 'portrait',  //预览设备的横竖屏状态，取值为portrait或landscape
  roundScreen: false  //设备的屏幕形状是否为圆形
})

请注意，如果被预览的组件是依赖参数注入的组件，建议的预览方式是：定义一个组件片段，在该片段中声明将要预览的组件，以及该组件依赖的入参，并在组件片段上标注@Preview注解，以表明将预览该片段中的内容。例如，要预览如下组件：

@Component
struct Title {
  @Prop context: string; 
  build() {
    Text(this.context)
  }
}

建议按如下方式预览：

@Preview
@Component    //定义组件片段TitlePreview
struct TitlePreview {
  build() {
    Title({ context: 'MyTitle' })    //在该片段中声明将要预览的组件Title，以及该组件依赖的入参 {context: 'MyTitle'}
  }
}

#### 卡片预览

创建卡片并选中卡片文件后，点击右侧边栏**Previewer**按钮即可预览卡片。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/zYjw7h_SQIO1opke0WCkQA/zh-cn_image_0000002530913442.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=1FDEB499F12DDA1CDDA219BD863C77EFDB242A6296176F6C9B3DA908B20C7FB0 "点击放大")
