# HarmonyOS UI 设计布局小白指南

本文面向刚开始写 HarmonyOS / ArkUI 界面的开发者，目标是把页面结构、HDS 导航、底部 TAB、二级页面、Scroll 与 Column 的关系、资源 token、深浅色和常见布局问题整理成一套可以直接复用的 UI 布局指南。

本文不是 DNSHelper 专用。当前应用里的 `Index.ets`、`SettingsTab.ets`、`ConfigTab.ets`、`SecondaryPageScaffold.ets`、`SettingsItem.ets` 是一套已经落地的参考结构，本文会把这些经验抽成通用模板。

相关文档分工：

| 文档 | 负责什么 |
| --- | --- |
| `docs/ArkTS开发小白指南.md` | ArkTS 语言、状态、异步、错误处理、资源和工程分层 |
| `docs/HarmonyOS界面设计布局小白指南.md` | ArkUI 页面结构、布局、组件、导航、TAB、二级页、响应式和视觉规则 |
| `docs/HarmonyOS沉浸光感适配小白指南.md` | 沉浸式窗口、安全区、HDS 沉浸光感、标题栏材质和底部悬浮 TAB |

## 1. UI 先看结构，不要先堆组件

一个 HarmonyOS 应用的常见 UI 结构可以拆成四层：

```text
窗口层 EntryAbility
  -> 根导航 HdsNavigation / Navigation
    -> 根内容 HdsTabs / 首页内容
      -> TAB 页面 Scroll -> Column
    -> 二级页 HdsNavDestination
      -> Scroll -> Column
```

每层只做自己的事：

| 层级 | 负责什么 |
| --- | --- |
| `EntryAbility` | 窗口、安全区、深浅色策略、加载入口页面 |
| 根 `HdsNavigation` | 全局标题栏、导航栈、根页面背景 |
| `HdsTabs` | 根级 TAB 切换、底部悬浮页签 |
| TAB 页面 | 展示当前 TAB 内容，接收外部 `Scroller` 和底部 padding |
| `HdsNavDestination` | 二级页面标题栏、返回、滚动绑定 |
| `Scroll -> Column` | 页面内容滚动、从上往下排版、撑满短页面 |
| 业务组件 | 设置项、表单项、卡片、提示、按钮 |

新手最常见的问题，是把这些职责混在一个页面里：页面自己读窗口安全区、自己造标题栏、自己写底部栏、自己写业务、自己处理数据库。短期能跑，后期会很难统一风格。

## 2. 布局组件怎么选

| 组件 | 方向 | 适合场景 |
| --- | --- | --- |
| `Column` | 垂直 | 页面主内容、表单、设置组、卡片内部上下排列 |
| `Row` | 水平 | 设置项、标题 + 值、图标 + 文本、按钮组 |
| `Stack` | 叠放 | 头像角标、播放按钮覆盖、状态动效覆盖 |
| `Scroll` | 滚动 | 页面内容可能超过一屏 |
| `List` | 列表 | 大量同类行，需要列表能力 |
| `ForEach` | 重复渲染 | 少量或中等数量数组数据 |
| `LazyForEach` | 懒加载 | 大量数据或复杂列表 |
| `HdsNavigation` | 根导航 | 根页面标题栏、导航栈 |
| `HdsNavDestination` | 二级页 | 详情页、编辑页、设置子页 |
| `HdsTabs` | 页签 | 底部 TAB、顶部 TAB |

简单判断：

1. 只有上下排列，先用 `Column`。
2. 只有左右排列，先用 `Row`。
3. 要滚动，外面套 `Scroll`，里面用 `Column`。
4. 页面级导航，用 HDS 导航组件。
5. 大列表再考虑 `List` 或 `LazyForEach`。

## 3. 推荐尺寸和资源 token

不要在页面里散落 `16`、`24`、`#FFFFFF`、`#132022`。推荐把它们放进资源和常量。

### 3.1 尺寸 token

`entry/src/main/resources/base/element/float.json`：

```json
{
  "float": [
    {
      "name": "text_size_display",
      "value": "28fp"
    },
    {
      "name": "text_size_title",
      "value": "16fp"
    },
    {
      "name": "text_size_body",
      "value": "14fp"
    },
    {
      "name": "text_size_caption",
      "value": "12fp"
    },
    {
      "name": "space_xs",
      "value": "4vp"
    },
    {
      "name": "space_sm",
      "value": "8vp"
    },
    {
      "name": "space_lg",
      "value": "16vp"
    },
    {
      "name": "space_xl",
      "value": "24vp"
    },
    {
      "name": "radius_sm",
      "value": "8vp"
    },
    {
      "name": "list_item_height",
      "value": "52vp"
    }
  ]
}
```

页面使用：

```ts
Text($r('app.string.settings_about'))
  .fontSize($r('app.float.text_size_title'))
  .fontColor($r('app.color.text_primary'))
```

### 3.2 颜色 token

浅色资源：

```json
{
  "color": [
    {
      "name": "start_window_background",
      "value": "#F4F8F7"
    },
    {
      "name": "card_background",
      "value": "#FFFFFF"
    },
    {
      "name": "text_primary",
      "value": "#132022"
    },
    {
      "name": "text_secondary",
      "value": "#54666B"
    },
    {
      "name": "divider_color",
      "value": "#DFE8EA"
    },
    {
      "name": "transparent",
      "value": "#00000000"
    }
  ]
}
```

深色资源：

```json
{
  "color": [
    {
      "name": "start_window_background",
      "value": "#0F1417"
    },
    {
      "name": "card_background",
      "value": "#171E22"
    },
    {
      "name": "text_primary",
      "value": "#EAF3F1"
    },
    {
      "name": "text_secondary",
      "value": "#A8B8B8"
    },
    {
      "name": "divider_color",
      "value": "#2A353A"
    },
    {
      "name": "transparent",
      "value": "#00000000"
    }
  ]
}
```

规则：

1. 新增一个浅色 token，就同步新增一个深色 token。
2. 页面只引用语义色，不写具体十六进制颜色。
3. 透明背景统一用 `transparent`，不要到处写 `'#00000000'`。

## 4. 根页面结构

根页面建议只放全局导航、TAB 和路径栈，不要塞大量业务代码。

推荐结构：

```ts
@Entry
@ComponentV2
struct Index {
  @Local currentIndex: number = 0;
  @Provider('navStack') navStack: NavPathStack = new NavPathStack();
  private readonly tabScrollers: Scroller[] = [new Scroller(), new Scroller()];

  build() {
    HdsNavigation(this.navStack) {
      HdsTabs({ index: this.currentIndex }) {
        TabContent() {
          HomeTab({
            scroller: this.tabScrollers[0],
            bottomContentPadding: this.resolveTabContentBottomPadding()
          })
        }
        .tabBar(this.buildTabBar(0))

        TabContent() {
          SettingsTab({
            scroller: this.tabScrollers[1],
            bottomContentPadding: this.resolveTabContentBottomPadding()
          })
        }
        .tabBar(this.buildTabBar(1))
      }
      .barPosition(BarPosition.End)
      .barOverlap(true)
      .scrollable(false)
      .onChange((index: number) => {
        this.currentIndex = index;
      })
    }
    .titleBar(this.resolveRootTitleBar())
    .titleMode(HdsNavigationTitleMode.MINI)
    .hideBackButton(true)
    .bindToScrollable([this.resolveActiveScroller()])
    .width('100%')
    .height('100%')
    .backgroundColor($r('app.color.start_window_background'))
  }

  private resolveTabContentBottomPadding(): number {
    return 96;
  }

  private resolveActiveScroller(): Scroller {
    return this.tabScrollers[this.currentIndex] ?? this.tabScrollers[0];
  }
}
```

关键点：

1. `NavPathStack` 在根页面只创建一次。
2. 每个 TAB 一个 `Scroller`。
3. 根导航的 `bindToScrollable()` 绑定当前 TAB 的 `Scroller`。
4. TAB 页面不要自己创建根导航。
5. 页面背景放在根容器和内容容器上，避免滚动时露底。

## 5. TAB 内容页面结构

根 TAB 页面推荐统一写成：

```text
Scroll(scroller)
  -> Column(minHeight 100%)
    -> Column(maxWidth)
      -> 页面真实内容
```

可直接复用的 TAB 内容脚手架：

```ts
import { AppState } from '../model/AppState';
import { Constants } from '../utils/Constants';

@ComponentV2
export struct RootTabContentScaffold {
  @Local appState: AppState = AppState.getInstance();
  @Param scroller: Scroller = new Scroller();
  @Param bottomContentPadding: number = 24;
  @Param pageBackgroundColor: ResourceColor = $r('app.color.start_window_background');
  @BuilderParam content: () => void = this.EmptyContent;

  @Builder
  private EmptyContent(): void {
  }

  build() {
    Scroll(this.scroller) {
      Column() {
        Column() {
          this.content();
        }
        .width('100%')
        .constraintSize({ maxWidth: Constants.TAB_PAGE_MAX_WIDTH })
      }
      .constraintSize({ minHeight: '100%' })
      .width('100%')
      .alignItems(HorizontalAlign.Center)
      .padding({
        left: Constants.TAB_PAGE_HORIZONTAL_PADDING,
        right: Constants.TAB_PAGE_HORIZONTAL_PADDING,
        top: Constants.TAB_PAGE_TOP_PADDING,
        bottom: this.bottomContentPadding
      })
    }
    .width('100%')
    .height('100%')
    .edgeEffect(EdgeEffect.Spring)
    .scrollBar(BarState.Off)
    .backgroundColor(this.pageBackgroundColor)
  }
}
```

业务 TAB：

```ts
@ComponentV2
export default struct SettingsTab {
  @Param scroller: Scroller = new Scroller();
  @Param bottomContentPadding: number = 24;

  build() {
    RootTabContentScaffold({
      scroller: this.scroller,
      bottomContentPadding: this.bottomContentPadding
    }) {
      Column({ space: 12 }) {
        SettingsItem({
          title: $r('app.string.settings_about'),
          onClickHandler: () => {
            // push page
          }
        })
      }
      .width('100%')
    }
  }
}
```

为什么要这样写：

1. `Scroll` 负责滚动。
2. 外层 `Column` 负责撑满一屏和水平居中。
3. 内层 `Column` 负责最大宽度，避免平板或折叠屏上内容拉太宽。
4. `bottomContentPadding` 由根页面计算，避免被底部 TAB 遮挡。

## 6. 二级页面结构

二级页面推荐统一用 `HdsNavDestination -> Scroll -> Column`。

```text
HdsNavDestination
  -> Scroll(scroller)
    -> Column.constraintSize({ minHeight: '100%' })
             .justifyContent(FlexAlign.Start)
      -> 页面真实内容
```

这不是只为了代码好看，而是为了滚动高度、短页面高度、内容顺序和沉浸式背景都稳定。

### 6.1 `Column.constraintSize({ minHeight: '100%' })` 的作用

`Column` 是垂直方向线性布局容器。放在 `Scroll` 内部时，它负责承载页面真实内容。

推荐写：

```ts
Scroll(this.scroller) {
  Column() {
    this.content();
  }
  .width('100%')
  .constraintSize({ minHeight: '100%' })
  .justifyContent(FlexAlign.Start)
}
```

作用：

1. 短内容至少撑满一屏，页面背景不会只包住内容。
2. 长内容可以自然增长，`Scroll` 能拿到正确滚动高度。
3. 内容默认从上往下排，符合表单、设置、详情页的阅读顺序。
4. 后续加空状态、加载态、底部操作区时，不容易把布局挤乱。

不要写：

```ts
Scroll(this.scroller) {
  Column() {
    this.content();
  }
  .height('100%')
}
```

`height('100%')` 会把 `Scroll` 内部内容容器锁在可视区域高度。内容一多，就可能出现：

1. 内部内容被迫挤在一屏里。
2. 表单项、卡片、说明文字之间的间距被压缩。
3. `Scroll` 计算到的内容高度不是真实内容高度。
4. 底部内容可能滚不到，或被底部安全区、悬浮栏遮挡。

### 6.2 二级页内容默认从上往下

二级页通常是编辑页、详情页、设置子页、导入页，默认应从顶部开始布局。

推荐显式写：

```ts
.justifyContent(FlexAlign.Start)
```

不建议作为二级页默认值：

```ts
.justifyContent(FlexAlign.Center)
.justifyContent(FlexAlign.End)
.justifyContent(FlexAlign.SpaceBetween)
.justifyContent(FlexAlign.SpaceAround)
.justifyContent(FlexAlign.SpaceEvenly)
```

这些只适合特殊页面，例如空状态页、登录页、引导页。普通二级业务页默认这样写，容易出现大空白、上下被拉开、内容被挤压等问题。

### 6.3 可直接复用的二级页 scaffold

```ts
import {
  HdsNavDestination,
  HdsNavDestinationTitleMode,
  HdsNavigationMenuContentOptions,
  HdsNavigationTitle
} from '@kit.UIDesignKit';
import { AppState } from '../model/AppState';
import { buildImmersiveTitleBarOptions, resolveImmersiveTopInset } from '../utils/ImmersiveNavigation';

@ComponentV2
export struct SecondaryPageScaffold {
  @Local appState: AppState = AppState.getInstance();
  @Param title: HdsNavigationTitle = { mainTitle: '' };
  @Param menu: HdsNavigationMenuContentOptions = { value: [] };
  @Param scroller: Scroller = new Scroller();
  @Param pageBackgroundColor: ResourceColor = $r('app.color.start_window_background');
  @Event onReadyHandler: (context: NavDestinationContext) => void = (_context: NavDestinationContext): void => {};
  @BuilderParam content: () => void = this.EmptyContent;

  @Builder
  private EmptyContent(): void {
  }

  build() {
    HdsNavDestination() {
      Scroll(this.scroller) {
        Column() {
          this.content();
        }
        .width('100%')
        .constraintSize({ minHeight: '100%' })
        .justifyContent(FlexAlign.Start)
        .padding({
          top: resolveImmersiveTopInset(this.appState.topSafeHeight),
          bottom: this.appState.bottomSafeHeight
        })
        .backgroundColor(this.pageBackgroundColor)
      }
      .width('100%')
      .height('100%')
      .edgeEffect(EdgeEffect.Spring)
      .scrollBar(BarState.Off)
      .backgroundColor(this.pageBackgroundColor)
    }
    .titleBar(buildImmersiveTitleBarOptions(this.title, this.resolveMenu()))
    .titleMode(HdsNavDestinationTitleMode.MINI)
    .hideToolBar(true)
    .bindToScrollable([this.scroller])
    .onReady((context: NavDestinationContext): void => {
      this.onReadyHandler(context);
    })
    .width('100%')
    .height('100%')
    .backgroundColor(this.pageBackgroundColor)
  }

  private resolveMenu(): HdsNavigationMenuContentOptions | undefined {
    const menuItems = this.menu.value ?? [];
    if (menuItems.length === 0) {
      return undefined;
    }
    return { value: menuItems };
  }
}
```

业务页面使用：

```ts
@ComponentV2
struct EditPage {
  @Local pathStack: NavPathStack = new NavPathStack();
  private readonly contentScroller: Scroller = new Scroller();

  @Builder
  private PageContent(): void {
    Column({ space: 12 }) {
      InputCell({
        title: $r('app.string.common_name'),
        value: this.name,
        $value: (val: string) => {
          this.name = val;
        }
      })
    }
    .width('100%')
    .constraintSize({ minHeight: '100%' })
    .justifyContent(FlexAlign.Start)
    .padding({
      left: $r('app.float.space_lg'),
      right: $r('app.float.space_lg'),
      top: $r('app.float.space_lg'),
      bottom: $r('app.float.space_lg')
    })
  }

  build() {
    SecondaryPageScaffold({
      title: { mainTitle: $r('app.string.common_edit') },
      scroller: this.contentScroller,
      onReadyHandler: (context: NavDestinationContext): void => {
        this.pathStack = context.pathStack;
      },
      content: (): void => {
        this.PageContent();
      }
    })
  }
}
```

## 7. 设置项和表单布局

设置页通常是一组一组的纵向信息。推荐结构：

```text
Column(space 24)
  -> Column(space 12)
    -> SectionHeader
    -> SettingsItem
    -> HelperText
  -> Column(space 12)
    -> SectionHeader
    -> SettingsItem
```

设置项组件：

```ts
@ComponentV2
export struct SettingsItem {
  @Param title: ResourceStr = '';
  @Param value: string = '';
  @Param showArrow: boolean = true;
  @Event onClickHandler: () => void = () => {};

  build() {
    Row() {
      Text(this.title)
        .fontSize($r('app.float.text_size_title'))
        .fontColor($r('app.color.text_primary'))
        .layoutWeight(1)

      if (this.value.length > 0) {
        Text(this.value)
          .fontSize($r('app.float.text_size_body'))
          .fontColor($r('app.color.text_secondary'))
          .margin({ right: $r('app.float.space_xs') })
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .constraintSize({ maxWidth: '50%' })
      }

      if (this.showArrow) {
        Image($r('app.media.ic_arrow_right'))
          .width($r('app.float.icon_size_secondary'))
          .height($r('app.float.icon_size_secondary'))
          .fillColor($r('app.color.icon_tertiary'))
      }
    }
    .width('100%')
    .height($r('app.float.list_item_height'))
    .padding({
      left: $r('app.float.space_lg'),
      right: $r('app.float.space_lg')
    })
    .backgroundColor($r('app.color.card_background'))
    .borderRadius($r('app.float.radius_sm'))
    .onClick(() => {
      this.onClickHandler();
    })
  }
}
```

表单页建议：

1. 一组输入项放在同一个 `Column`。
2. 输入项之间用 `Divider`。
3. 外层卡片负责背景、圆角、阴影。
4. 保存按钮放标题栏 menu 或页面底部固定区域，不要藏在很长内容中间。
5. 文案过长时用 `maxLines` 和 `textOverflow`。

## 8. 卡片和分组

卡片适合承载一个独立对象、状态摘要或操作组。不要为了装饰把所有内容都套卡片。

推荐用卡片的场景：

| 场景 | 是否适合卡片 |
| --- | --- |
| DNS 服务项、账户项、设备项 | 适合 |
| 当前运行状态摘要 | 适合 |
| 一组设置项的容器 | 适合 |
| 整个页面外层 | 不建议 |
| 页面 section 外层再套一层大卡片 | 不建议 |

卡片模板：

```ts
Column({ space: 8 }) {
  Text(title)
    .fontSize($r('app.float.text_size_title'))
    .fontColor($r('app.color.text_primary'))

  Text(summary)
    .fontSize($r('app.float.text_size_body'))
    .fontColor($r('app.color.text_secondary'))
}
.width('100%')
.padding($r('app.float.space_lg'))
.borderRadius($r('app.float.radius_sm'))
.backgroundColor($r('app.color.card_background'))
.shadow({
  radius: 8,
  color: $r('app.color.shadow_sm'),
  offsetY: 2
})
```

注意：卡片圆角不要无限放大。普通设置、表单、管理工具里，`8vp` 到 `14vp` 通常更稳。

## 9. 文本和按钮

### 9.1 文本

推荐层级：

| 类型 | 建议 token |
| --- | --- |
| 大数字、核心状态 | `text_size_display` |
| 页面内标题 | `text_size_headline` 或 `text_size_title` |
| 正文 | `text_size_body` |
| 说明、辅助信息 | `text_size_caption` |

通用写法：

```ts
Text($r('app.string.settings_background_run_desc'))
  .fontSize($r('app.float.text_size_caption'))
  .fontColor($r('app.color.text_secondary'))
  .maxLines(2)
  .textOverflow({ overflow: TextOverflow.Ellipsis })
```

### 9.2 图标按钮

如果是明确动作，优先用图标加可访问 label。例如标题栏的新增、导入、保存。

```ts
{
  content: {
    label: $r('app.string.common_done'),
    icon: $r('app.media.ic_save'),
    isEnabled: true,
    action: () => {
      this.save();
    }
  }
}
```

不建议把工具类动作都写成大号文字按钮。保存、添加、导入、返回这类动作在 HDS 标题栏里用 icon 更符合移动端习惯。

## 10. 响应式和多设备

不要假设只有一台手机、一种宽度。

推荐：

```ts
Column() {
  this.content();
}
.width('100%')
.constraintSize({ maxWidth: 760 })
```

外层：

```ts
Column() {
  Column() {
    this.content();
  }
  .constraintSize({ maxWidth: Constants.TAB_PAGE_MAX_WIDTH })
}
.width('100%')
.alignItems(HorizontalAlign.Center)
```

这样手机上占满宽度，平板和折叠屏上内容不会被拉得太散。

常见响应式规则：

1. 页面宽度 `100%`，内容最大宽度单独限制。
2. 列表、表单、设置页默认单列。
3. 只有数据密集页面才考虑双列。
4. 不用 viewport 宽度直接缩放字体。
5. 长文本必须 `maxLines`、`textOverflow` 或换行。

## 11. 安全区和沉浸布局

如果页面启用了沉浸式窗口，背景可以进入状态栏和底部导航区，但内容要避让。

沉浸适配详情见 `docs/HarmonyOS沉浸光感适配小白指南.md`。这里先记住两个原则：

1. 根容器可以忽略系统安全区，让背景铺满。
2. 内容容器要加顶部和底部 padding，避免被状态栏、标题栏、底部手势条和悬浮 TAB 遮挡。

TAB 内容常见 padding：

```ts
.padding({
  top: this.appState.topSafeHeight + Constants.ROOT_MINI_TITLE_BAR_HEIGHT,
  bottom: this.appState.bottomSafeHeight
})
```

底部悬浮 TAB 内容避让：

```ts
private resolveTabContentBottomPadding(): number {
  return this.tabBarHeight + this.appState.bottomSafeHeight + this.floatingBarMargin * 2;
}
```

## 12. HDS 沉浸光感和普通布局的边界

`HdsNavigation`、`HdsNavDestination`、`HdsTabs` 解决的是导航、标题栏、页签和材质体验。它们不会自动帮你解决所有内容布局问题。

你仍然需要自己处理：

1. `Scroll` 内部内容容器。
2. `Column` 的最小高度。
3. 内容从上往下排列。
4. 底部 padding。
5. 背景颜色。
6. 文本溢出。
7. 横向最大宽度。

所以不要以为用了 HDS 就不用写 `Column.constraintSize({ minHeight: '100%' })`。这个约束依然是页面内容布局稳定的关键。

## 13. 页面检查清单

每写一个页面，都按下面检查：

| 检查项 | 期待结果 |
| --- | --- |
| 根容器 | `.width('100%').height('100%')` |
| 可滚动页面 | `Scroll -> Column.constraintSize({ minHeight: '100%' })` |
| 二级页内容 | 默认 `justifyContent(FlexAlign.Start)` |
| 背景 | 页面和滚动容器都有明确背景色 |
| 左右边距 | 使用 token 或常量，不到处写散值 |
| 最大宽度 | 平板/折叠屏内容不拉满 |
| 底部避让 | 底部内容不被 TAB 或手势条遮挡 |
| 文本溢出 | 长文本有 `maxLines` 和 `textOverflow` |
| 资源 | 文案、颜色、字号走 `$r(...)` |
| 列表 key | `ForEach` 使用稳定业务 key |

## 14. 常见布局错误

### 错误 1：`Scroll` 里直接塞很多组件

不推荐：

```ts
Scroll() {
  Text('标题')
  Text('内容')
}
```

推荐：

```ts
Scroll() {
  Column({ space: 12 }) {
    Text('标题')
    Text('内容')
  }
  .constraintSize({ minHeight: '100%' })
  .justifyContent(FlexAlign.Start)
}
```

### 错误 2：用 `height('100%')` 锁死滚动内容

修法：改成 `constraintSize({ minHeight: '100%' })`。

### 错误 3：普通详情页默认居中

修法：普通二级页使用 `justifyContent(FlexAlign.Start)`，只有明确的空状态或引导页才居中。

### 错误 4：底部悬浮 TAB 挡住最后一项

修法：根页面计算 `bottomContentPadding`，传给每个 TAB 内容。

### 错误 5：平板上内容被拉太宽

修法：内容内层加 `constraintSize({ maxWidth: Constants.TAB_PAGE_MAX_WIDTH })`。

### 错误 6：浅深色只做了一套颜色

修法：`base/element/color.json` 和 `dark/element/color.json` 同名 token 成对维护。

### 错误 7：设置项右侧长文本把箭头挤掉

修法：右侧值加 `constraintSize({ maxWidth: '50%' })`、`maxLines(1)` 和 `textOverflow`。

## 15. 官方依据

本文依据本地 DocsHub 中的 HarmonyOS 官方文档快照整理，关键资料包括：

| 主题 | 官方文档 |
| --- | --- |
| 布局选择 | [布局概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-overview) |
| Row/Column | [线性布局 (Row/Column)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-linear) |
| Column API | [Column](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-column) |
| Row API | [Row](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-row) |
| constraintSize | [基础类型定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types) |
| ForEach/LazyForEach | [LazyForEach：数据懒加载](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-rendering-control-lazyforeach) |
| Navigation | [Navigation基础架构介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-architecture) |
| HdsNavigation | [HdsNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation) |
| HdsNavDestination | [HdsNavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavdestination) |
| HdsTabs | [HdsTabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdstabs) |
| HDS 沉浸光感 | [沉浸光感](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-component-material) |
| 安全区 | [安全区域](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area) |
| 深浅色 | [应用深浅色适配](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-dark-light-color-adaptation) |
