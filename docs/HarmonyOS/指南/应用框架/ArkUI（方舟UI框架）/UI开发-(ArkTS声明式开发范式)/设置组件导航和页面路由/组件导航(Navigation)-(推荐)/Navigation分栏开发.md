---
title: "Navigation分栏开发"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-split-mode"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "设置组件导航和页面路由"
  - "组件导航(Navigation) (推荐)"
  - "Navigation分栏开发"
captured_at: "2026-04-17T01:35:37.312Z"
---

# Navigation分栏开发

[Navigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation)作为一个容器组件，提供了两种布局样式：单栏布局、分栏布局。分栏布局一般适用于宽屏设备，在分栏布局下，导航栏（navBar）会固定显示， 子页面（NavDestination）通过导航控制器（NavPathStack）切换显示， 在导航栏和子页面之间有一条分割线， 可以通过分割线拖拽控制左右显示的比例。架构图详见[Navigation基础架构介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-architecture)。

#### 分栏相关接口介绍

#### \[h2\]mode

[mode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#mode9)属性用于控制Navigation的显示模式，有三种模式：单栏，分栏，自适应。

**图1** 单栏（NavigationMode.Stack）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/z8-DS954QSyx34VPT8oo6A/zh-cn_image_0000002538018608.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3BCFBA9AC58B30B665FBE79FB58B4D12879E976362E19C10FE3C5B4BF6E45C31)

**图2** 分栏（NavigationMode.Split）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/NF9cMgY1SUqxCnCjTQTOhA/zh-cn_image_0000002538178534.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=C502ACDB03AF2CACE35911E1AD65DCFA7203A6651EDA80FA3B399FEE9006BE61)

**图3** 自适应（NavigationMode.Auto）效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/qml1oUkxSYi_rWDwE9D2EA/zh-cn_image_0000002569018323.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=DCBB4618136527326767C9B530553426008085420EAB3D33DD7498D67F7C4019)

#### \[h2\]navBarPosition

[navBarPosition](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navbarposition9)用于控制导航栏显示的位置，用navBarPosition控制导航栏显示位置时，会被系统语言所影响。比如，在以汉语、英语为代表的LTR语言体系下，NavBarPosition.Start指代的是导航栏出现在左侧，而在以阿拉伯语为代表的RTL语言体系下，NavBarPosition.Start则指代导航栏出现在右侧。类似的效果也出现在NavBarPosition.End上。

**NavBarPosition.Start**

**图4** 系统语言为LTR时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/oMTBDpJ3TDm9kwYNV_5aIQ/zh-cn_image_0000002568898315.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=5D8011F8F0D1CFE6FE014F2FBCFFFAC05E999ED6FEA49E1DF34AD2BF4034D0EA)

**图5** 系统语言为RTL时NavBarPosition.Start效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/LZjuFaKbRwKRXE9KrWUUuQ/zh-cn_image_0000002538018610.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=9C77A985A2DDB6E709331E19B40D934864463E2F8F4BBDBDFA009FF635A4000A)

**NavBarPosition.End**

**图6** 系统语言为LTR时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/CjdJkrBvRuWyNTbzBn5u7Q/zh-cn_image_0000002538178536.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=98756AE48AEAE344EA1FAD68C6C9C122BA497B4A7DFE040616DB0D1D06B0B083)

**图7** 系统语言为RTL时NavBarPosition.End效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/t9TjQi1mQLqwJSbdqsJPyw/zh-cn_image_0000002569018325.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=E23D587E9570DCE1479FE78AF4C185AB0CA68A4FE1E9F49F75C141A14A62B327)

#### \[h2\]enableDragBar

[enableDragBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#enabledragbar14)用于控制是否显示分栏的拖动按钮。

**图8** enableDragBar为false效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/VwF_A6t5Q8GDNJwFbGJkpg/zh-cn_image_0000002568898317.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3C9E3BE05C24AF9AA0A8E388E6AC5A9E80BF39D8316F92241CA29EAA9BD405C5)

**图9** enableDragBar为true

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/iMVe8BPuTUuJ3-2VpCOuyQ/zh-cn_image_0000002538018612.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=AC68534A03E3D9A21FD60DF5F1CCE90527F6FCBDFF13E0E3F624791B26E53922)

#### \[h2\]navBarWidth

[navBarWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navbarwidth9)用于控制导航栏的宽度。

#### \[h2\]navBarWidthRange

[navBarWidthRange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#navbarwidthrange10)用于设置导航栏宽度可调整的范围。

#### \[h2\]minContentWidth

[minContentWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#mincontentwidth10)用于控制分栏子页的最小宽度；分栏模式导航栏和子页中间会有一个分割线，在可调范围内，用户可以通过拖动分割线来调整导航栏和子页的显示大小。

#### \[h2\]hideNavBar

[hideNavBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#hidenavbar9)用于控制导航栏的显示状态，默认值为false。如果同时将mode配置为NavigationMode.Split且hideNavBar设置为true，则实际效果会显示为单栏。

#### \[h2\]enableModeChangeAnimation

[enableModeChangeAnimation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#enablemodechangeanimation15)用于控制是否开启单双栏切换的动画，默认开启。

#### \[h2\]splitPlaceholder

[splitPlaceholder](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-navigation#splitplaceholder20)用于设置分栏模式下内容区的默认占位页。分栏模式在默认情况下，栈中没有页面时内容区展示空白，可使用此接口设置此区域的UI布局。

需要注意的是，占位页仅作为UI展示页，仅分栏模式空栈的情况下才展示，不受路由栈管理也不可获焦和响应事件。

#### 分栏开发示例

以开发一个新闻app的demo来演示如何使用Navigation分栏相关接口。

1.  新闻主页内容会放到左侧NavBar中，其中内容是一个新闻列表，用户点击每一条新闻标题时，右边会push一个详情页，用来展示新闻的信息。
    
2.  给左侧NavBar设置一个宽度范围，右侧子页区域也设置一个最小宽度。
    

配置的路由表：

```json
{
  "routerMap": [
    {
      "name": "NewsDetail",
      "pageSourceFile": "src/main/ets/pages/navigation/splitmode/NewsDetail.ets",
      "buildFunction": "NewsDetailPageBuilder",
      "data": {
        "description": "this is DetailPageA"
      }
    }
  ]
}
```

子页代码：

// 自定义的参数类型，用于在push页面时给子页传递参数
export class NewsItem {
  public title: string;
  public overview: string;
  public content: string;

  constructor(title: string, overview: string, content: string) {
    this.title = title;
    this.overview = overview;
    this.content = content;
  }
}

@Builder
export function NewsDetailPageBuilder() {
  NewsDetail()
}

@Component
struct NewsDetail {
  @State title: string = '';
  @State content: string = '';

  build() {
    NavDestination() {
      Column() {
        Text(this.content)
      }
    }
    .title(this.title)
    .backgroundColor('#fff6e3c8')
    .onReady((ctx: NavDestinationContext) => {
      // 在onReady生命周期拿到传来的页面参数
      let param = ctx.pathInfo.param as NewsItem;
      this.title = param?.title;
      this.content = param?.content;
    })
  }
}

主页代码：

import { NewsItem } from './NewsDetail'

@Component
struct NewsHome {
  private newsItemArray: Array<NewsItem> = \[\];
  private stack: NavPathStack | undefined = undefined;

  aboutToAppear(): void {
    // 这里省略了从网络获取新闻信息的过程
    for (let i = 0; i < 50; i++) {
      this.newsItemArray.push(new NewsItem(\`新闻标题${i + 1}\`, \`新闻概述${i + 1}\`, \`新闻详情${i + 1}\`))
    }
    let info = this.queryNavigationInfo();
    this.stack = info?.pathStack;
  }

  build() {
    List() {
      ForEach(this.newsItemArray, (item: NewsItem, index: number) => {
        ListItem() {
          Column() {
            Text(\`${item.title}\`).margin(15).fontSize(25).fontColor(Color.Black)
            Text(\`${item.overview}\`).fontSize(13).fontColor(Color.Gray)
          }.margin({bottom: 15}).backgroundColor('#eeeeee').width('100%')
          .borderRadius(15).height(120).onClick(() => {
            // 用户点击某一个新闻标签时，就在右侧子页区域push一个NavDestination页面，用来展示新闻详情
            this.stack?.pushPath({name: 'NewsDetail', param: item})
          })
        }.width('100%')
      }, (item: NewsItem, index: number) => {
        return item.title;
      })
    }.width('100%').height('100%').padding(15)
  }
}

@Entry
@Component
struct Index {
  private stack: NavPathStack = new NavPathStack();
  @State navWidth: number = 100;

  build() {
    RelativeContainer() {
      Navigation(this.stack) {
        NewsHome().width('100%').height('100%')
      }
      .mode(NavigationMode.Split)
      .enableDragBar(true)
      .hideNavBar(false)
      .navBarWidthRange(\[100, 700\]) // 指定NavBar区域的宽度范围
      .minContentWidth(100) // 指定子页区域的最小宽度
      .hideTitleBar(true)
      .hideToolBar(true)
      .height('100%')
      .width(\`${this.navWidth}%\`)
      .alignRules({
        top: { anchor: '\_\_container\_\_', align: VerticalAlign.Top },
        left: { anchor: '\_\_container\_\_', align: HorizontalAlign.Start }
      })
    }
  }
}

**图10** 运行效果

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/lbCCgf0JTVyRg_vGKJPmIw/zh-cn_image_0000002538178538.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=E70AA0CCA1FE78CF1CBE9B036BAED69A5ADE16D0AD3C8911AF4ADE3A1C0E2817)
