---
title: "选项卡 (Tabs)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-tabs"
menu_path:
  - "指南"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "UI开发 (ArkTS声明式开发范式)"
  - "组件布局"
  - "构建布局"
  - "选项卡 (Tabs)"
captured_at: "2026-04-17T01:35:37.482Z"
---

# 选项卡 (Tabs)

当页面信息较多时，为了让用户能够聚焦于当前显示的内容，需要对页面内容进行分类，提高页面空间利用率。[Tabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs)组件可以在一个页面内快速实现视图内容的切换，一方面提升查找信息的效率，另一方面精简用户单次获取到的信息量。

#### 基本布局

Tabs组件的页面组成包含两个部分，分别是[TabContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent)和[TabBar](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#tabbar)。TabContent是内容页，TabBar是导航页签栏，页面结构如下图所示，根据不同的导航类型，布局会有区别，可以分为底部导航、顶部导航、侧边导航，其导航栏分别位于底部、顶部和侧边。

**图1** Tabs组件布局示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/WF3YtSEfTu-O83tgb1WIQQ/zh-cn_image_0000002538018670.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=44EED9F460C5E2E02474AB2AC3308605C2851C67139EB42E41AA1ECDDA462080)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/76x5aLvOS3mwJNbKPq_JtA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=59AEAD69BC20BB475BF73D61DBB7B6672B812373F5A33F7FC3E3F28FD0D5A088)

-   TabContent组件不支持设置通用宽度属性，其宽度默认撑满Tabs父组件。
    
-   TabContent组件不支持设置通用高度属性，其高度由Tabs父组件高度与TabBar组件高度决定。
    

Tabs使用花括号包裹TabContent，如图2，其中TabContent显示相应的内容页。

**图2** Tabs与TabContent使用

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/B07HtcyzTCeWKXMakVdwHQ/zh-cn_image_0000002538178598.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=AE824E968A2E7595CA3236FEC6597314FD8D2C05B4BC7710FC53D7EF4D42D8A2)

每一个TabContent对应的内容需要有一个页签，可以通过TabContent的tabBar属性进行配置。在如下TabContent组件上设置tabBar属性，可以设置其对应页签中的内容，tabBar作为内容的页签。

TabContent() {
  // app.string.homepage\_content资源文件中的value值为“首页的内容”
  Text($r('app.string.homepage\_content'))
    .fontSize(30)
}
// app.string.homepage资源文件中的value值为“首页”
.tabBar($r('app.string.homepage'))

设置多个内容时，需在Tabs内按照顺序放置。

Tabs() {
  TabContent() {
    // app.string.homepage\_content资源文件中的value值为“首页的内容”
    Text($r('app.string.homepage\_content'))
      .fontSize(30)
  }
  // app.string.homepage资源文件中的value值为“首页”
  .tabBar($r('app.string.homepage'))

  TabContent() {
    // app.string.recommend\_content资源文件中的value值为“推荐的内容”
    Text($r('app.string.recommend\_content'))
      .fontSize(30)
  }
  // app.string.recommend资源文件中的value值为“推荐”
  .tabBar($r('app.string.recommend'))

  TabContent() {
    // app.string.discover\_content资源文件中的value值为“发现的内容”
    Text($r('app.string.discover\_content'))
      .fontSize(30)
  }
  // app.string.discover资源文件中的value值为“发现”
  .tabBar($r('app.string.discover'))

  TabContent() {
    // app.string.mine\_content资源文件中的value值为“我的内容”
    Text($r('app.string.mine\_content'))
      .fontSize(30)
  }
  // app.string.mine\_content资源文件中的value值为“我的”
  .tabBar($r('app.string.mine'))
}

#### 底部导航

底部导航是应用中最常见的一种导航方式。底部导航位于应用一级页面的底部，用户打开应用，能够分清整个应用的功能分类，以及页签对应的内容，并且其位于底部更加方便用户单手操作。底部导航一般作为应用的主导航形式存在，其作用是将用户关心的内容按照功能进行分类，迎合用户使用习惯，方便在不同模块间的内容切换。

**图3** 底部导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/7QIfXVnySWiodeoV5rqEFg/zh-cn_image_0000002569018385.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=726125D68600E408135A3B10A7C4775C0B4FE5B837CE666FF5F2A75F102C763C)

导航栏位置使用Tabs的barPosition参数进行设置。默认情况下，导航栏位于顶部，此时，barPosition为BarPosition.Start。设置为底部导航时，需要将barPosition设置为BarPosition.End。

Tabs({ barPosition: BarPosition.End }) {
  // TabContent的内容：首页、发现、推荐、我的
  // ···
}

底部导航栏可通过设置TabContent的[BottomTabBarStyle](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#bottomtabbarstyle9)来实现底部页签样式，详细示例请参考：[示例9（设置底部页签使用symbol图标）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabcontent#示例9设置底部页签使用symbol图标)。

#### 顶部导航

当内容分类较多，用户对不同内容的浏览概率相差不大，需要经常快速切换时，一般采用顶部导航模式进行设计，作为对底部导航内容的进一步划分，常见一些资讯类应用对内容的分类为关注、视频、数码，或者主题应用中对主题进行进一步划分为图片、视频、字体等。

**图4** 顶部导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/wIBshAMyTXOvnGZvJxj7bA/zh-cn_image_0000002568898377.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=1E6128F386D9EA2E771A0EEC6831856F92E1A028A6921C410702E2DB8ADAA95D)

Tabs({ barPosition: BarPosition.Start }) {
  // TabContent的内容:关注、视频、游戏、数码、科技、体育、影视
  // ···
}

#### 侧边导航

侧边导航是应用较为少见的一种导航模式，更多适用于横屏界面，用于对应用进行导航操作，由于用户的视觉习惯是从左到右，侧边导航栏默认为左侧侧边栏。

**图5** 侧边导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/uuTT8WYtQo-8jUErD4mRuQ/zh-cn_image_0000002538018672.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=AD3366BAAAB70A141B1A0ABFDE04E22C43119A29A23BDEFA6CF6E23F61093BF3)

实现侧边导航栏需要将Tabs的[vertical](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#vertical)属性设置为true，vertical默认值为false，表明内容页和导航栏垂直方向排列。

  Tabs({ barPosition: BarPosition.Start }) {
    // TabContent的内容:首页、发现、推荐、我的
    // ···
  }
// ···
  .vertical(true)
  .barWidth(100)
  .barHeight(200)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/uu9ZlP9cQfqpEdq7gTSTcQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=A1C68F762AD73DDEE9D7F6538A93A55348AFBCDEF9D23E6116930654569DCDDA)

-   vertical为false时，tabbar的宽度默认为撑满屏幕的宽度，需要设置[barWidth](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#barwidth)为合适值。
    
-   vertical为true时，tabbar的高度默认为实际内容的高度，需要设置[barHeight](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#barheight)为合适值。
    

#### 限制导航栏的滑动切换

默认情况下，导航栏都支持滑动切换，在一些内容信息量需要进行多级分类的页面，如支持底部导航+顶部导航组合的情况下，底部导航栏的滑动效果与顶部导航出现冲突，此时需要限制底部导航的滑动，避免引起不好的用户体验。

**图6** 限制底部导航栏滑动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/u-rm06Q4T0qVWiXcO6X5_w/zh-cn_image_0000002538178600.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=B594309984AA80A0A0C56ED24AB3E0F530DB3DFB625925D94AAB9DEC24786A91)

控制滑动切换的属性为scrollable，默认值为true，表示可以滑动，若要限制滑动切换页签则需要设置为false。

  Tabs({ barPosition: BarPosition.End }) {
    TabContent() {
      Column() {
        Tabs() {
          // 顶部导航栏内容
        // ···
        }
      }
      .backgroundColor('#ff08a8f1')
      .width('100%')
    }
    // app.string.homepage资源文件中的value值为“首页”
    .tabBar($r('app.string.homepage'))

    // 其他TabContent内容：发现、推荐、我的
    // ···
  }
// ···
  .scrollable(false)

#### 固定导航栏

当内容分类较为固定且不具有拓展性时，例如底部导航内容分类一般固定，分类数量一般在3-5个，此时使用固定导航栏。固定导航栏不可滚动，无法被拖拽滚动，内容均分tabBar的宽度。

**图7** 固定导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/ET8iLvCpSzC-eBIqe6Pong/zh-cn_image_0000002569018387.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=7C0D65E6D7431CFBFB80BBE20E87D21E90F18EA6AE40EF1C7A3B1DC982BA3272)

Tabs的[barMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#barmode10)属性用于控制导航栏是否可以滚动，默认值为BarMode.Fixed。

Tabs({ barPosition: BarPosition.End }) {
  // TabContent的内容：首页、发现、推荐、我的
  // ···
}
.barMode(BarMode.Fixed)

#### 滚动导航栏

滚动导航栏可以用于顶部导航栏或者侧边导航栏的设置，内容分类较多，屏幕宽度无法容纳所有分类页签的情况下，需要使用可滚动的导航栏，支持用户点击和滑动来加载隐藏的页签内容。

**图8** 可滚动导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/3HKAqJQ0TYufsgwNOueZ_A/zh-cn_image_0000002568898379.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=BC69B3C1752384DCD21BC9A83DA838EED793E883114FD67CDA22CCDC67367A8F)

滚动导航栏需要设置Tabs组件的barMode属性，默认值为BarMode.Fixed表示为固定导航栏，BarMode.Scrollable表示可滚动导航栏。

Tabs({ barPosition: BarPosition.Start }) {
  // TabContent的内容：关注、视频、游戏、数码、科技、体育、影视、人文、艺术、自然、军事
  // ···
}
.barMode(BarMode.Scrollable)

#### 自定义导航栏

对于底部导航栏，一般作为应用主页面功能区分，为了更好的用户体验，会组合文字以及对应语义图标表示页签内容，这种情况下，需要自定义导航页签的样式。

**图9** 自定义导航栏

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/cFtY5kynTo2mrAG7c55lHQ/zh-cn_image_0000002538018674.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=636D5BE4A12DFBE02411C8419129BBEF96B9F7C41BF7D32E23CBAA66F86C9627)

系统默认情况下采用了下划线标识当前活跃的页签，而自定义导航栏需要自行实现相应的样式，用于区分当前活跃页签和未活跃页签。

设置自定义导航栏需要使用tabBar的参数，以其支持的CustomBuilder的方式传入自定义的函数组件样式。例如这里声明tabBuilder的自定义函数组件，传入参数包括页签文字title，对应位置index，以及选中状态和未选中状态的图片资源。通过当前活跃的currentIndex和页签对应的targetIndex匹配与否，决定UI显示的样式。

@State currentIndex: number = 0;

@Builder
tabBuilder(title: ResourceStr, targetIndex: number, selectedImg: Resource, normalImg: Resource) {
  Column() {
    Image(this.currentIndex === targetIndex ? selectedImg : normalImg)
      .size({ width: 25, height: 25 })
    Text(title)
      .fontColor(this.currentIndex === targetIndex ? '#1698CE' : '#6B6B6B')
  }
  .width('100%')
  .height(50)
  .justifyContent(FlexAlign.Center)
}

在TabContent对应tabBar属性中传入自定义函数组件，并传递相应的参数。

TabContent() {
  Column() {
    // app.string.mine\_content资源文件中的value值为“我的内容”
    Text($r('app.string.mine\_content'))
  }
  .width('100%')
  .height('100%')
  .backgroundColor('#007DFF')
}
// app.string.mine资源文件中的value值为“我的”
.tabBar(this.tabBuilder($r('app.string.mine'), 0, $r('app.media.mine\_selected'), $r('app.media.mine\_normal')))

#### 切换至指定页签

在不使用自定义导航栏时，默认的Tabs会实现切换逻辑。在使用了自定义导航栏后，默认的Tabs仅实现滑动内容页和点击页签时内容页的切换逻辑，页签切换逻辑需要自行实现。即用户滑动内容页和点击页签时，页签栏需要同步切换至内容页对应的页签。

**图10** 内容页和页签不联动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/uT9qgIX0T4yHsU02BSGTvA/zh-cn_image_0000002538178602.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3B2216E9396DD70A088CB3B454EDC2AD0DAAC74B84DB4DF297561A8B3A08E1D5)

从API version 18开始，支持使用Tabs提供的[onSelected](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#onselected18)事件方法，监听索引index的变化，并将选中元素的index值传递给selectIndex，实现页签的切换。

// 如需作为页面入口，请取消@Entry的注释并删除export关键字
// @Entry
@Component
export struct ContentPageNoAndTabLinkage {

  @State selectIndex: number = 0;
  @Builder tabBuilder(title: Resource, targetIndex: number) {
    Column() {
      Text(title)
        .fontColor(this.selectIndex === targetIndex ? '#1698CE' : '#6B6B6B')
    }
  }
  build() {
    NavDestination() {
      Column({ space: 12 }) {
        // ...
          Tabs({ barPosition: BarPosition.End }) {
            TabContent() {
              // app.string.homepage\_content资源文件中的value值为“首页内容”
              Text($r('app.string.homepage\_content')).width('100%').height('100%').backgroundColor('rgb(213,213,213)')
                .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
            // app.string.homepage资源文件中的value值为“首页”
            }.tabBar(this.tabBuilder($r('app.string.homepage'), 0))

            TabContent() {
              // app.string.discover\_content资源文件中的value值为“发现内容”
              Text($r('app.string.discover\_content')).width('100%').height('100%').backgroundColor('rgb(112,112,112)')
                .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
            // app.string.discover资源文件中的value值为“发现”
            }.tabBar(this.tabBuilder($r('app.string.discover'), 1))

            TabContent() {
              // app.string.recommend\_content资源文件中的value值为“推荐内容”
              Text($r('app.string.recommend\_content')).width('100%').height('100%').backgroundColor('rgb(39,135,217)')
                .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
            // app.string.recommend资源文件中的value值为“推荐”
            }.tabBar(this.tabBuilder($r('app.string.recommend'), 2))

            TabContent() {
              // app.string.mine\_content资源文件中的value值为“我的内容”
              Text($r('app.string.mine\_content')).width('100%').height('100%').backgroundColor('rgb(0,74,175)')
                .fontSize(40).fontColor(Color.Black).textAlign(TextAlign.Center)
            }
            // app.string.mine资源文件中的value值为“我的”
            .tabBar(this.tabBuilder($r('app.string.mine'), 3))
          }
          .animationDuration(0)
          .backgroundColor('#F1F3F5')
          .onSelected((index: number) => {
            this.selectIndex = index;
          })
        // ...
      }
      .width('100%')
      // ...
    }
    // ...
  }
}

**图11** 内容页和页签联动

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/AizCvmPLQ7e0qo-UrE4l2w/zh-cn_image_0000002569018389.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=221249CD815652C8BA85660E64547EF717A3575C61C70B77AD85E4F7187EAFC0)

若希望不滑动内容页和点击页签也能实现内容页和页签的切换，可以将currentIndex传给Tabs的index参数，通过改变currentIndex来实现跳转至指定索引值对应的TabContent内容。也可以使用[TabsController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabscontroller)，TabsController是Tabs组件的控制器，用于控制Tabs组件进行内容页切换。通过TabsController的changeIndex方法来实现跳转至指定索引值对应的TabContent内容。

// ...
  @State currentIndex: number = 2;
  @State currentAnimationMode: AnimationMode = AnimationMode.CONTENT\_FIRST;
  private controller: TabsController = new TabsController();

  // ...
              Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controller }) {
                // ...
              }
              .animationDuration(0)
              .height(300)
              .animationMode(this.currentAnimationMode)
              .onChange((index: number) => {
                this.currentIndex = index;
              })

              // app.string.ContentWillChange\_animationMode资源文件中的value值为“动态修改animationMode”
              Button($r('app.string.ContentWillChange\_animationMode')).width('50%').margin({ top: 20 })
                .onClick(()=>{
                  if (this.currentAnimationMode === AnimationMode.CONTENT\_FIRST) {
                    this.currentAnimationMode = AnimationMode.ACTION\_FIRST;
                  } else if (this.currentAnimationMode === AnimationMode.ACTION\_FIRST) {
                    this.currentAnimationMode = AnimationMode.NO\_ANIMATION;
                  } else if (this.currentAnimationMode === AnimationMode.NO\_ANIMATION) {
                    this.currentAnimationMode = AnimationMode.CONTENT\_FIRST\_WITH\_JUMP;
                  } else if (this.currentAnimationMode === AnimationMode.CONTENT\_FIRST\_WITH\_JUMP) {
                    this.currentAnimationMode = AnimationMode.ACTION\_FIRST\_WITH\_JUMP;
                  } else if (this.currentAnimationMode === AnimationMode.ACTION\_FIRST\_WITH\_JUMP) {
                    this.currentAnimationMode = AnimationMode.CONTENT\_FIRST;
                  }
                })

              // app.string.ContentWillChange\_changeIndex资源文件中的value值为“动态修改index”
              Button($r('app.string.ContentWillChange\_changeIndex')).width('50%').margin({ top: 20 })
                .onClick(() => {
                  this.currentIndex = (this.currentIndex + 1) % 4;
                })

              Button('changeIndex').width('50%').margin({ top: 20 })
                .onClick(() => {
                  let index = (this.currentIndex + 1) % 4;
                  this.controller.changeIndex(index);
                })

**图12** 切换指定页签

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/pFcjr9-sRuyOj_cUJAxL_A/zh-cn_image_0000002568898381.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=B47451C5040AE8256EE80D175EADB50C26412BEFA1BC1FCB4DADB92B4C23DC11)

开发者可以通过Tabs组件的[onContentWillChange](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#oncontentwillchange12)接口，设置自定义拦截回调函数。拦截回调函数在下一个页面即将展示时被调用，如果回调返回true，新页面可以展示；如果回调返回false，新页面不会展示，仍显示原来页面。

Tabs({ barPosition: BarPosition.End, index: this.currentIndex, controller: this.controllerTwo }) {
  // ...
}
// ...
.onContentWillChange((currentIndex, comingIndex) => {
  if (comingIndex === 2) {
    return false;
  }
  return true;
})

**图13** 支持开发者自定义页面切换拦截事件

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/x5f1YE3bS6KTiF14GqXX0Q/zh-cn_image_0000002538018676.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=18841B6BD8FEFF220FBCF63EAB11F816108F5AA1A2C959D8EB7C307D8133F75D)

#### 支持适老化

在适老化大字体场景下，底部页签提供大字体弹窗显示内容。当组件识别到大字体时，基于设置的文字和图标等内容，构建长按提示弹窗。当用户长按弹窗后，滑动到下一个页签位置时，使用新页签的弹窗提示内容替换上一个页签提示内容，抬手关闭弹窗并切换到对应TabContent内容页。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/P5sJj82VRaSQPz6v1R9SAA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=3A82772391C90D33A62355AAFF64E4D308EEC7AF6BC8FDEB737382736E52BD0C)

弹窗只适用于底部页签BottomTabBarStyle。

**图14** 在适老化场景下通过长按底部页签显示适老化弹窗。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/BZ0ywPQbSEGih2GB9jCYXw/zh-cn_image_0000002538178604.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=8EBCEC1A1BC96E2C31F057775D72340FA95BA4E582ECF5E0884BBDE2C15DB553)

// 如需作为页面入口，请取消@Entry的注释并删除export关键字
// @Entry
@Component
export struct AgeFriendlyTabs {
 
  build() {
    NavDestination() {
      Column() {
        Tabs({ barPosition: BarPosition.End }) {
          TabContent() {
            Column().width('100%').height('100%').backgroundColor(Color.Pink)
          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos\_app\_icon'), 'OverLength'))
 
          TabContent() {
            Column().width('100%').height('100%').backgroundColor(Color.Yellow)
          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos\_app\_icon'), 'SixLine'))
 
          TabContent() {
            Column().width('100%').height('100%').backgroundColor(Color.Blue)
          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos\_app\_icon'), 'Blue'))
 
          TabContent() {
            Column().width('100%').height('100%').backgroundColor(Color.Green)
          }.tabBar(new BottomTabBarStyle($r('sys.media.ohos\_app\_icon'), 'Green'))
        }
        .vertical(false)
        .scrollable(true)
        .barMode(BarMode.Fixed)
        .width('100%')
        .backgroundColor(0xF1F3F5)
      }.width('80%').height(200)
      .margin({ top: 200 })
    }
  }
}

#### 控制页面缓存数

从API version 19开始，开发者可以通过[cachedMaxCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#cachedmaxcount19)接口，设置子组件的最大缓存个数和缓存模式。默认情况下Tabs创建时会一次性预加载所有TabContent，而且已加载的页面不会释放，可能会带来性能内存问题。此时可以设置[cachedMaxCount](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#cachedmaxcount19)属性控制缓存的页面数量，设置此属性后不会进行页面预加载，使用懒加载机制(仅切换到页面时才加载)，当切换页面时根据所设置的[TabsCacheMode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-tabs#tabscachemode19枚举说明)决定保留缓存或者释放页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/_g3FrRM4TQm26jm0JyGgvA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=64E37A66972510742CB247F6372DA816CFCCCFDF8EB80070D63687F33350F164)

-   TabsCacheMode枚举值为CACHE\_BOTH\_SIDE时，缓存当前显示的子组件和其两侧的子组件。
    
-   TabsCacheMode枚举值为CACHE\_LATEST\_SWITCHED时，缓存当前显示的子组件和最近切换过的子组件。
    
-   存在翻页动画时，从页面1直接切换到页面3，翻页动画会包含页面2，页面2也会被加载，如果此时页面2不在缓存范围内，页面切换完成后会立马释放。
    

**图15** 在页面缓存场景下通过点击yellow按键切换界面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/ezPYmhQQThOkpEFrEsCeNw/zh-cn_image_0000002569018391.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=2A0CBF586B1E7471BFC6A69F531D3BF4346D85F21C09778487012ADAAF443708)

// 如需作为页面入口，请取消@Entry的注释并删除export关键字
// @Entry
@Component
export struct NumberOfCachesTabBar {
  build() {
    // ...
          Tabs({ barPosition: BarPosition.Start }) {
            TabContent() {
              MyComponent({ color: '#00CB87' })
            }.tabBar(SubTabBarStyle.of('green'))

            TabContent() {
              MyComponent({ color: '#007DFF' })
            }.tabBar(SubTabBarStyle.of('blue'))

            TabContent() {
              MyComponent({ color: '#FFBF00' })
            }.tabBar(SubTabBarStyle.of('yellow'))

            TabContent() {
              MyComponent({ color: '#E67C92' })
            }.tabBar(SubTabBarStyle.of('pink'))

            TabContent() {
              MyComponent({ color: '#FF0000' })
            }.tabBar(SubTabBarStyle.of('red'))
          }
          .width(360)
          .height(296)
          .backgroundColor('#F1F3F5')
          .cachedMaxCount(1, TabsCacheMode.CACHE\_BOTH\_SIDE)
          // ...
  }
}

@Component
struct MyComponent {
  private color: string = '';

  aboutToAppear(): void {
    console.info('aboutToAppear backgroundColor:' + this.color);
  }

  aboutToDisappear(): void {
    console.info('aboutToDisappear backgroundColor:' + this.color);
  }

  build() {
    Column()
      .width('100%')
      .height('100%')
      .backgroundColor(this.color)
  }
}

基于以上示例代码为例，不同场景下的缓存策略如下：

1.  如图16所示，使用默认翻页动画，CACHE\_BOTH\_SIDE模式，n设置为2，点击TabBar切换到yellow页，TabContent1~3被缓存。再切换到red页，TabContent1、2释放，TabContent3~5被缓存。
    
    **图16** 默认翻页动画，CACHE\_BOTH\_SIDE模式示意图
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/a1XlFlXATZq9jmmBf0ZzCQ/zh-cn_image_0000002568898383.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=51AC27F6E1B088C5F7656156D4E062C8FEA0C84FA97DFD50A02F469BB60C1A29)
    
2.  如图17所示，使用默认翻页动画，CACHE\_LATEST\_SWITCHED模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存，TabContent2释放。再切换到red页，TabContent1、3、5被缓存，TabContent4释放。
    
    **图17** 默认翻页动画，CACHE\_LATEST\_SWITCHED模式示意图
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/ey9-jeFHStSt0VH8-DAuoQ/zh-cn_image_0000002538018678.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=30FA0AC610A64461A72C8D038E260D37A1683D7FDDBB2FD3AAAE513B0C5F6E00)
    
3.  如图18所示，关闭翻页动画，CACHE\_BOTH\_SIDE模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存。再切换到red页，TabContent3、5被缓存，TabContent1释放。
    
    **图18** 关闭翻页动画，CACHE\_BOTH\_SIDE模式示意图
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/znEJH5jfRZ6_6NAEVUqY1Q/zh-cn_image_0000002538178606.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=412452EF1CF5E4B231910598A8581D2C5F11386BEC7177F5D36B903FB40D602D)
    
4.  如图19所示，关闭翻页动画，CACHE\_LATEST\_SWITCHED模式，n设置为2，点击TabBar切换到yellow页，TabContent1、3被缓存。再切换到red页，TabContent1、3、5被缓存。
    
    **图19** 关闭翻页动画，CACHE\_LATEST\_SWITCHED模式示意图
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/DIDmaqlDS3mwZva5ygWP8g/zh-cn_image_0000002569018393.png?HW-CC-KV=V1&HW-CC-Date=20260417T013538Z&HW-CC-Expire=86400&HW-CC-Sign=54F5D649122E10FC8F8A938357BE11E958A6BDE21C0B5A0B7CE6E5FCE21EBD2D)
    

#### 示例代码

-   [基于Tabs组件实现常见导航样式](https://gitcode.com/HarmonyOS_Samples/multi-tab-navigation)
-   [基于Tab组件实现增删Tab的功能](https://gitcode.com/HarmonyOS_Samples/handle-tabs)
