# HarmonyOS 沉浸光感适配小白指南

本文面向刚接触 HarmonyOS / ArkTS 的开发者，目标是把沉浸式窗口、HDS 标题栏、底部页签、二级页面、安全区、深浅色资源和主题色适配串成一套可复制的工程方案。

本文职责只聚焦“沉浸光感适配”：窗口如何进入沉浸式、背景如何铺进系统区域、标题栏和底部页签如何启用 HDS 光感材质、内容如何避开状态栏和底部手势区、二级页在沉浸场景下如何保持正确滚动和布局。

通用 ArkTS 语言、状态管理、异步错误处理、资源组织请看 `docs/ArkTS开发小白指南.md`；通用 ArkUI 页面结构、Row/Column/Scroll、设置项、卡片、响应式布局请看 `docs/HarmonyOS界面设计布局小白指南.md`。本文会保留 `HdsNavDestination -> Scroll -> Column.constraintSize({ minHeight: '100%' })` 和 `justifyContent(FlexAlign.Start)` 的说明，因为它直接影响沉浸二级页的滚动高度、内容避让和背景铺满效果。

这里说的“沉浸光感”不是一个单独开关，而是两层能力叠加：

1. **沉浸式布局**：应用内容和背景可以延伸到状态栏、底部导航条所在区域，避免顶部或底部出现割裂的系统底色。
2. **HDS 沉浸光感材质**：HDS 标题栏按钮和 HDS 底部页签可以使用 `systemMaterialEffect`，让系统按设备能力自适应选择材质和光感效果。

一个完整的 HarmonyOS 沉浸光感实现，通常可以按下面这些工程落点组织：

| 层级 | 推荐文件或组件 | 做什么 |
| --- | --- | --- |
| 窗口层 | `entry/src/main/ets/entryability/EntryAbility.ets` | 设置主窗口沉浸式布局，读取顶部/底部避让区高度，设置应用深浅色跟随系统 |
| 全局状态 | `AppState.ets` / `UiState.ets` | 保存 `topSafeHeight`、`bottomSafeHeight`、主题配置和派生 palette |
| 标题栏封装 | `ImmersiveNavigation.ets` / `ImmersiveShell.ets` | 统一构造 HDS 沉浸光感标题栏参数 |
| 根导航和 TAB | `entry/src/main/ets/pages/Index.ets` | 使用 `HdsNavigation` + `HdsTabs`，根容器忽略顶部/底部系统安全区，底部悬浮页签叠加光感材质 |
| 根 TAB 内容 | `HomeTab.ets`、`SettingsTab.ets` 等 | 每个 TAB 接收外部 `Scroller` 和底部 padding，内容避开标题栏和底部悬浮 TAB |
| 二级页面 | `SecondaryPageScaffold.ets` | 使用 `HdsNavDestination`，统一二级页标题栏、滚动绑定、安全区和背景 |
| 颜色资源 | `entry/src/main/resources/base/element/color.json`、`entry/src/main/resources/dark/element/color.json` | 浅色/深色成对定义窗口背景、卡片背景、文字色、TAB 色等 |
| 自定义主题基础 | `ThemeModels.ets`、`ThemeColorEngine.ets`、`ThemeSafetyGate.ets`、`ThemePreferenceService.ets` | 从用户输入色值派生浅色/深色 palette，并做对比度和语义色安全校验 |

## 1. 先理解几个概念

### 1.1 状态栏、导航条、安全区、避让区

屏幕顶部状态栏和底部导航条属于系统区域。默认情况下，应用内容会被限制在安全区内，不会和这些系统区域重叠。

做沉浸式后，应用背景会铺满屏幕，视觉上进入状态栏和底部导航条区域。但文字、按钮、列表项仍然要避开这些区域，否则会被系统图标、手势条遮挡。

记住一句话：**背景可以延伸，内容要避让。**

### 1.2 `expandSafeArea` 和 `ignoreLayoutSafeArea` 的区别

官方文档里的核心区别可以这样理解：

| API | 影响什么 | 适合什么场景 |
| --- | --- | --- |
| `expandSafeArea` | 扩展组件的绘制区域，不重新布局子组件 | 让背景色、背景图、底部栏背景延伸到系统区域 |
| `ignoreLayoutSafeArea` | 让组件布局范围进入非安全区，子组件位置也会受影响 | 根 `Navigation`、`HdsNavigation`、`NavDestination` 需要真正铺满全屏时 |

推荐根导航和二级页使用：

```ts
.ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
```

这表示根容器布局范围进入顶部状态栏和底部导航区域。随后页面内部再通过 `topSafeHeight`、`bottomSafeHeight` 和标题栏高度给内容补 padding。

### 1.3 HDS 沉浸光感材质

官方 `沉浸光感` 文档说明，从 HarmonyOS `6.1.0(23)` 起，HDS 支持标题栏和底部页签的沉浸光感材质：

- `HdsNavigation`：在 `TitleBarStyleOptions.systemMaterialEffect` 中配置。
- `HdsTabs`：在 `HdsTabsFloatingStyle.systemMaterialEffect` 中配置。

推荐优先使用：

```ts
{
  materialType: hdsMaterial.MaterialType.ADAPTIVE,
  materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
}
```

这样系统会根据设备性能选择材质策略。不要一上来固定用最高档材质；官方建议如果不用自适应，应先通过 `hdsMaterial.getSystemMaterialTypes()` 查询设备是否支持 `IMMERSIVE`，不支持时使用更轻的 `SMOOTH`。

## 2. 官方依据和推荐选择

| 主题 | 官方依据 | 推荐选择 |
| --- | --- | --- |
| 窗口沉浸式 | [管理应用窗口（Stage模型）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-window-stage) | 在 `EntryAbility.onWindowStageCreate()` 获取主窗口并调用 `setWindowLayoutFullScreen(true)` |
| 安全区 | [开发应用沉浸式效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-develop-apply-immersive-effects)、[安全区域](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-expand-safe-area) | 根容器忽略系统安全区，内容层手动补顶部/底部 padding |
| HDS 沉浸光感 | [沉浸光感](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-design-hds-component-material) | 标题栏和底部悬浮 TAB 使用 `hdsMaterial.MaterialType.ADAPTIVE` |
| HDS 标题栏 | [HdsNavigation](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavigation)、[HdsNavDestination](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsnavdestination) | 根页用 `HdsNavigation`，二级页用 `HdsNavDestination`，标题栏参数统一由 `buildImmersiveTitleBarOptions()` 生成 |
| HDS 底部页签 | [HdsTabs](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdstabs) | `HdsTabs.barFloatingStyle()` 配置悬浮页签和光感材质 |
| 深浅色 | [获取/设置环境变量](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/subscribe-system-environment-variable-changes)、[设置应用内主题换肤](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/theme_skinning) | `EntryAbility` 使用 `COLOR_MODE_NOT_SET` 让应用跟随系统；资源目录有 `base` 与 `dark` 两套颜色 |
| 材质能力查询 | [hdsMaterial](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ui-design-hdsmaterial) | 默认使用系统自适应；如要自定义材质档位，应先查询设备能力 |

## 3. 推荐工程分层

不要在每个页面里到处调用窗口 API、写安全区公式、写标题栏材质。推荐固定成下面几层：

| 层 | 只做这些事 | 不应该做 |
| --- | --- | --- |
| `EntryAbility` 窗口层 | 全屏沉浸、读取避让区、设置应用深浅色策略 | 不写页面布局，不写页面标题 |
| `AppState` 状态层 | 保存安全区、主题配置、palette | 不直接读取窗口对象 |
| `ImmersiveNavigation` 工具层 | 统一构造标题栏、统一高度公式 | 不关心具体业务页面 |
| 根 `Index` | 拼装 `HdsNavigation`、`HdsTabs`、全局 `NavPathStack` | 不在每个 TAB 内重复创建根导航 |
| 根 TAB 内容脚手架 | 统一滚动、顶部/底部 padding、最大宽度 | 不再单个页面手写安全区公式 |
| 二级页脚手架 | 统一 `HdsNavDestination`、标题栏、滚动绑定、返回栈 | 不让二级页自己处理根级沉浸 |
| 资源和主题 token | 成对维护浅色/深色语义色 | 不在页面里写散落的十六进制颜色 |

## 4. 窗口层适配

### 4.1 窗口层应该做什么

推荐在 `EntryAbility.onWindowStageCreate()` 里做三件关键事：

1. `windowStage.getMainWindow()` 获取主窗口。
2. `mainWindow.setWindowLayoutFullScreen(true)` 让主窗口进入沉浸式布局。
3. `getWindowAvoidArea()` 读取顶部状态栏、底部导航指示区高度，再除以屏幕密度，保存到 `AppState` 的 `topSafeHeight` 和 `bottomSafeHeight`。

推荐在 `onCreate()` 里设置：

```ts
this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
```

这表示应用深浅色模式不强制为浅色或深色，而是跟随系统。

### 4.2 可直接复用：窗口沉浸初始化

下面代码可以直接放到新项目的 `EntryAbility.ets`，再按项目名调整 import 路径。

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { display, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import { AppState } from '../model/AppState';
import { LogUtils } from '../utils/LogUtils';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      // 跟随系统深浅色。不要在这里强制 DARK/LIGHT，除非产品明确要求。
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      LogUtils.error('EntryAbility', 'Failed to set colorMode: ' + JSON.stringify(err));
    }
  }

  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
    try {
      const mainWindow = await windowStage.getMainWindow();

      // 让主窗口进入沉浸式布局。背景和根容器可以铺进状态栏/导航条区域。
      await mainWindow.setWindowLayoutFullScreen(true);

      const systemAvoidArea = mainWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_SYSTEM);
      const navigationAvoidArea = mainWindow.getWindowAvoidArea(window.AvoidAreaType.TYPE_NAVIGATION_INDICATOR);
      const density = display.getDefaultDisplaySync().densityPixels;

      AppState.getInstance().topSafeHeight = systemAvoidArea.topRect.height / density;
      AppState.getInstance().bottomSafeHeight = navigationAvoidArea.bottomRect.height / density;
    } catch (err) {
      LogUtils.error('EntryAbility', 'Failed to setup immersive window: ' + JSON.stringify(err));
    }

    windowStage.loadContent('pages/Index', (err: BusinessError) => {
      if (err && err.code) {
        LogUtils.error('EntryAbility', 'Failed to load content: ' + JSON.stringify(err));
      }
    });
  }
}
```

### 4.3 什么时候需要补系统栏文字颜色

官方文档说明 `setWindowSystemBarProperties()` 可以设置状态栏/导航栏背景色和内容色。如果项目主要依赖 HDS 标题栏与浅深色资源，但真机上出现下面问题，就应补上系统栏内容色：

- 深色模式下状态栏文字仍是黑色，看不清。
- 浅色模式下状态栏文字过亮，看不清。
- 页面背景和系统栏内容对比度不足。

可复用示例：

```ts
private async applySystemBarForMode(mainWindow: window.Window, isDarkMode: boolean): Promise<void> {
  const contentColor = isDarkMode ? '#E5FFFFFF' : '#E5000000';
  const props: window.SystemBarProperties = {
    statusBarColor: '#00000000',
    navigationBarColor: '#00000000',
    statusBarContentColor: contentColor,
    navigationBarContentColor: contentColor
  };
  await mainWindow.setWindowSystemBarProperties(props);
}
```

注意：`statusBarContentColor` 设置后，`isStatusBarLightIcon` 这类高亮属性会失效，以内容色为准。

## 5. 全局状态层

推荐用 `AppState` 或同类全局 UI 状态对象保存安全区高度：

```ts
@ObservedV2
export class AppState {
  private static instance: AppState;

  @Trace topSafeHeight: number = 0;
  @Trace bottomSafeHeight: number = 0;

  public static getInstance(): AppState {
    if (!AppState.instance) {
      AppState.instance = new AppState();
    }
    return AppState.instance;
  }
}
```

这样做的好处是：窗口 API 只在 `EntryAbility` 调一次，页面只读 `AppState`，不会把窗口对象传得到处都是。

新项目可以直接照这个思路做，命名可以换成 `UiState`、`ShellState` 或 `AppState`。

## 6. 标题栏沉浸光感封装

### 6.1 推荐封装

建议创建 `entry/src/main/ets/utils/ImmersiveNavigation.ets`，统一生成标题栏配置：

```ts
export function buildImmersiveTitleBarOptions(
  title: HdsNavigationTitle,
  menu?: HdsNavigationMenuContentOptions
): HdsNavigationTitleBarOptions {
  const scrollEffectOpts: ScrollEffectOptions = {
    enableScrollEffect: false,
    scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
  };
  const systemMaterialEffect: SystemMaterialParams = {
    materialType: hdsMaterial.MaterialType.ADAPTIVE,
    materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
  };
  const style: TitleBarStyleOptions = {
    scrollEffectOpts,
    originalStyle: {
      backgroundStyle: {
        backgroundColor: $r('app.color.transparent')
      }
    },
    systemMaterialEffect,
  };
  const content: TitleBarContentOptions = {
    title,
    menu
  };
  return {
    style,
    avoidLayoutSafeArea: true,
    enableComponentSafeArea: false,
    content,
  };
}
```

这段代码里最关键的是：

- `systemMaterialEffect`：给标题栏按钮启用 HDS 沉浸光感。
- `originalStyle.backgroundStyle.backgroundColor = transparent`：避免标题栏背景退回默认灰底。
- `avoidLayoutSafeArea: true`：标题栏主动避开顶部系统区域。
- `enableComponentSafeArea: false`：不把标题栏设置为组件级安全区，页面内容自己通过 padding 避让。

### 6.2 可直接复用：完整工具文件

```ts
import {
  hdsMaterial,
  HdsNavigationMenuContentOptions,
  HdsNavigationTitle,
  HdsNavigationTitleBarOptions,
  ScrollEffectOptions,
  ScrollEffectType,
  SystemMaterialParams,
  TitleBarContentOptions,
  TitleBarStyleOptions
} from '@kit.UIDesignKit';
import { Constants } from './Constants';

export function buildImmersiveTitleBarOptions(
  title: HdsNavigationTitle,
  menu?: HdsNavigationMenuContentOptions
): HdsNavigationTitleBarOptions {
  const scrollEffectOpts: ScrollEffectOptions = {
    enableScrollEffect: false,
    scrollEffectType: ScrollEffectType.GRADIENT_BLUR,
  };
  const systemMaterialEffect: SystemMaterialParams = {
    materialType: hdsMaterial.MaterialType.ADAPTIVE,
    materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
  };
  const style: TitleBarStyleOptions = {
    scrollEffectOpts,
    originalStyle: {
      backgroundStyle: {
        backgroundColor: $r('app.color.transparent')
      }
    },
    systemMaterialEffect,
  };
  const content: TitleBarContentOptions = {
    title,
    menu
  };
  return {
    style,
    avoidLayoutSafeArea: true,
    enableComponentSafeArea: false,
    content,
  };
}

export function resolveImmersiveTopInset(topAvoidAreaVp: number): number {
  return topAvoidAreaVp + Constants.ROOT_MINI_TITLE_BAR_HEIGHT;
}

export function resolveImmersiveContentTopPadding(): number {
  return Constants.TAB_PAGE_TOP_PADDING;
}
```

配套 `Constants` 至少要有：

```ts
export class Constants {
  static readonly ROOT_MINI_TITLE_BAR_HEIGHT = 56;
  static readonly TAB_PAGE_HORIZONTAL_PADDING = 20;
  static readonly TAB_PAGE_TOP_PADDING = 28;
  static readonly TAB_PAGE_MAX_WIDTH = 760;
  static readonly TAB_BAR_HEIGHT = 48;
}
```

## 7. 根 HdsNavigation + HdsTabs 适配

### 7.1 推荐结构

根页面通常放在 `Index.ets`，核心结构建议是：

```ts
HdsNavigation(this.navStack) {
  HdsTabs({ index: this.currentIndex }) {
    TabContent() { StartTab(...) }.tabBar(...)
    TabContent() { ConfigTab(...) }.tabBar(...)
    TabContent() { DebugTab(...) }.tabBar(...)
    TabContent() { SettingsTab(...) }.tabBar(...)
  }
  .barPosition(BarPosition.End)
  .barOverlap(true)
  .barFloatingStyle({
    barBottomMargin: this.floatingBarMargin + this.appState.bottomSafeHeight,
    systemMaterialEffect: {
      materialType: hdsMaterial.MaterialType.ADAPTIVE
    }
  })
}
.titleBar(this.resolveRootTitleBar())
.titleMode(HdsNavigationTitleMode.MINI)
.bindToScrollable([this.resolveActiveScroller()])
.ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
```

根页面有几个关键点：

- `navStack` 只创建一次，并通过 `@Provider('navStack')` 给子页面使用。
- 每个 TAB 都接收一个独立 `Scroller`，根 `HdsNavigation.bindToScrollable()` 绑定当前 TAB 的滚动容器。
- `HdsTabs.barOverlap(true)` 让页签栏叠加在内容上方。
- `barBottomMargin` 要加 `bottomSafeHeight`，否则悬浮 TAB 可能贴到手势条。
- 内容页要接收 `bottomContentPadding`，否则列表底部会被悬浮 TAB 挡住。

### 7.2 可直接复用：根 TAB scaffold

下面是通用根 TAB 模板。实际项目只需要替换 `TabA`、`TabB`、图标和标题。

```ts
import {
  hdsMaterial,
  HdsNavigation,
  HdsNavigationMenuContentOptions,
  HdsNavigationTitle,
  HdsNavigationTitleBarOptions,
  HdsNavigationTitleMode,
  HdsTabs
} from '@kit.UIDesignKit';
import { AppState } from '../model/AppState';
import { Constants } from '../utils/Constants';
import { buildImmersiveTitleBarOptions } from '../utils/ImmersiveNavigation';
import TabA from './TabA';
import TabB from './TabB';

class RootTabItem {
  icon: Resource = $r('app.media.ic_home');
  label: ResourceStr = '';
}

@Entry
@ComponentV2
struct Index {
  @Local currentIndex: number = 0;
  @Provider('navStack') navStack: NavPathStack = new NavPathStack();

  private appState: AppState = AppState.getInstance();
  private readonly tabBarHeight: number = Constants.TAB_BAR_HEIGHT + 12;
  private readonly floatingBarMargin: number = 16;
  private readonly tabScrollers: Scroller[] = [new Scroller(), new Scroller()];
  private readonly tabs: RootTabItem[] = [
    { icon: $r('app.media.ic_home'), label: '首页' } as RootTabItem,
    { icon: $r('app.media.ic_settings'), label: '设置' } as RootTabItem
  ];

  @Builder
  private buildTabBar(index: number) {
    Column({ space: 4 }) {
      Image(this.tabs[index].icon)
        .width(20)
        .height(20)
        .fillColor(this.currentIndex === index ? $r('app.color.tab_item_active') : $r('app.color.tab_item_inactive'))

      Text(this.tabs[index].label)
        .fontSize(12)
        .fontColor(this.currentIndex === index ? $r('app.color.tab_item_active') : $r('app.color.tab_item_inactive'))
        .maxLines(1)
        .maxFontScale(1.2)
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%')
    .backgroundColor($r('app.color.transparent'))
  }

  build() {
    HdsNavigation(this.navStack) {
      HdsTabs({ index: this.currentIndex }) {
        TabContent() {
          TabA({
            scroller: this.tabScrollers[0],
            bottomContentPadding: this.resolveTabContentBottomPadding()
          })
        }
        .tabBar(this.buildTabBar(0))

        TabContent() {
          TabB({
            scroller: this.tabScrollers[1],
            bottomContentPadding: this.resolveTabContentBottomPadding()
          })
        }
        .tabBar(this.buildTabBar(1))
      }
      .barPosition(BarPosition.End)
      .vertical(false)
      .barOverlap(true)
      .scrollable(false)
      .barHeight(this.tabBarHeight)
      .barBackgroundColor($r('app.color.transparent'))
      .barFloatingStyle({
        barSideMargin: this.floatingBarMargin,
        barBottomMargin: this.floatingBarMargin + this.appState.bottomSafeHeight,
        gradientMask: {
          maskColor: '#00FFFFFF',
          maskHeight: 0
        },
        systemMaterialEffect: {
          materialType: hdsMaterial.MaterialType.ADAPTIVE,
          materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
        }
      })
      .backgroundColor($r('app.color.start_window_background'))
      .onChange((index: number) => {
        this.currentIndex = index;
      })
    }
    .titleBar(this.resolveRootTitleBar())
    .titleMode(HdsNavigationTitleMode.MINI)
    .hideBackButton(true)
    .bindToScrollable([this.resolveActiveScroller()])
    .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
    .width('100%')
    .height('100%')
    .backgroundColor($r('app.color.start_window_background'))
  }

  private resolveTabContentBottomPadding(): number {
    return this.tabBarHeight + this.appState.bottomSafeHeight + this.floatingBarMargin * 2;
  }

  private resolveRootTitleBar(): HdsNavigationTitleBarOptions {
    return buildImmersiveTitleBarOptions(this.resolveRootTitle(), this.resolveRootMenu());
  }

  private resolveRootTitle(): HdsNavigationTitle {
    if (this.currentIndex === 1) {
      return { mainTitle: '设置' };
    }
    return { mainTitle: '首页' };
  }

  private resolveRootMenu(): HdsNavigationMenuContentOptions | undefined {
    return undefined;
  }

  private resolveActiveScroller(): Scroller {
    return this.tabScrollers[this.currentIndex] ?? this.tabScrollers[0];
  }
}
```

## 8. 根 TAB 内容适配

根 TAB 页面建议遵循同一模式：

1. 外部传入 `Scroller`。
2. 外部传入 `bottomContentPadding`。
3. `Scroll` 顶部 padding = `topSafeHeight + ROOT_MINI_TITLE_BAR_HEIGHT`。
4. 内容 Column 顶部再加业务留白 `TAB_PAGE_TOP_PADDING`。
5. 内容 Column 底部 padding = `bottomContentPadding`，避免被悬浮 TAB 遮挡。
6. 页面背景统一用 `$r('app.color.start_window_background')`。

### 8.1 可直接复用：根 TAB 内容脚手架

如果每个 TAB 内部都重复写这套逻辑，可以抽成组件：

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
    .padding({
      top: this.appState.topSafeHeight + Constants.ROOT_MINI_TITLE_BAR_HEIGHT,
      bottom: this.appState.bottomSafeHeight
    })
    .edgeEffect(EdgeEffect.Spring)
    .scrollBar(BarState.Off)
    .align(Alignment.TopStart)
    .backgroundColor(this.pageBackgroundColor)
  }
}
```

业务 TAB 使用方式：

```ts
@ComponentV2
export default struct ConfigTab {
  @Param scroller: Scroller = new Scroller();
  @Param bottomContentPadding: number = 24;

  build() {
    RootTabContentScaffold({
      scroller: this.scroller,
      bottomContentPadding: this.bottomContentPadding
    }) {
      Text('这里放业务内容')
        .fontSize(16)
        .fontColor($r('app.color.text_primary'))
    }
  }
}
```

这样新 TAB 不需要知道状态栏高度、标题栏高度、底部手势条高度和悬浮 TAB 高度怎么计算。

## 9. 二级页面适配

### 9.1 推荐二级页脚手架

推荐把 `SecondaryPageScaffold.ets` 作为可复用封装：

```ts
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
  }
}
.titleBar(buildImmersiveTitleBarOptions(this.title, this.resolveMenu()))
.titleMode(HdsNavDestinationTitleMode.MINI)
.hideToolBar(true)
.bindToScrollable([this.scroller])
.ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
```

关键点：

- 二级页用 `HdsNavDestination`，不要再套一层根 `HdsNavigation`。
- 二级页自己的 `Scroll` 绑定给 `HdsNavDestination.bindToScrollable()`，让标题栏能感知滚动。
- `Scroll` 内部推荐再放一层 `Column().constraintSize({ minHeight: '100%' })`，让滚动内容至少撑满一屏，但内容超过一屏时仍然可以继续自然长高。
- 这层 `Column` 内部的业务内容应默认从上往下布局；建议显式写 `justifyContent(FlexAlign.Start)`，不要默认做居中、尾部对齐或上下均分。
- 二级页也要忽略顶部和底部系统安全区，否则背景不会铺满。
- 内容 padding 顶部 = 状态栏高度 + MINI 标题栏高度。
- 内容 padding 底部 = 底部导航指示区高度。

### 9.2 为什么要写 `Scroll -> Column.constraintSize({ minHeight: '100%' })`

二级页面最稳的结构是：

```text
HdsNavDestination
  -> Scroll
    -> Column.constraintSize({ minHeight: '100%' })
             .justifyContent(FlexAlign.Start)
      -> 页面真实内容
```

官方 `Column` 文档说明它是“沿垂直方向布局的容器”，线性布局指南也说明 `Column` 容器内子元素按垂直方向排列，`justifyContent(FlexAlign.Start)` 是垂直方向首端对齐的默认方式。放在二级页 `Scroll` 里时，推荐把这件事显式写出来，降低后续维护时被误改的概率。

这层 `Column` 的作用有四个：

1. **给滚动内容一个稳定的内容容器。** `Scroll` 负责滚动，内部 `Column` 负责承载页面内容、统一 padding、统一最大宽度和统一背景。
2. **短内容也能撑满一屏。** `constraintSize({ minHeight: '100%' })` 表示“至少等于 Scroll 可视区域高度”。详情页、空状态页、设置页这种内容不多的页面，不会只在顶部占一小块，背景和布局仍然能铺满整屏。
3. **长内容不会被锁死。** `minHeight` 只设置最小高度，不设置最大高度；当表单、列表、卡片很多时，`Column` 会按真实内容继续变高，`Scroll` 才有正确的滚动高度。
4. **业务内容按自然阅读顺序排列。** 二级页通常是表单、说明、详情、设置组或列表摘要，应从顶部开始一块一块向下排；这符合用户阅读顺序，也避免内容被人为分散到屏幕中间或底部。

不要把内容容器默认写成这些布局：

```ts
.justifyContent(FlexAlign.Center)       // 不推荐作为二级页默认值
.justifyContent(FlexAlign.End)          // 不推荐作为二级页默认值
.justifyContent(FlexAlign.SpaceBetween) // 不推荐作为二级页默认值
.justifyContent(FlexAlign.SpaceAround)  // 不推荐作为二级页默认值
.justifyContent(FlexAlign.SpaceEvenly)  // 不推荐作为二级页默认值
```

这些对齐方式只适合明确的特殊页面。例如登录页、空状态页、引导页可能需要居中；但普通二级业务页不应该默认这样做。否则容易出现：

- 短内容被推到屏幕中间或底部，和标题栏之间出现不自然的大空白。
- 多个设置项或表单组被强行均分到整屏，视觉节奏不稳定。
- 内容变多后，均分间距突然变化，滚动前后的布局感不一致。
- 配合错误的 `height('100%')` 时，内容更容易被压缩、挤压或遮挡。

不要把这里写成：

```ts
Scroll(this.scroller) {
  Column() {
    this.content();
  }
  .height('100%') // 不推荐
}
```

`height('100%')` 会把 Scroll 内部内容容器限定在可视区域高度。内容少时看不出问题，但内容多时很容易出现这些异常：

- `Column` 高度被限制在屏幕高度，内部内容被迫挤在一屏里。
- 使用 `justifyContent(FlexAlign.SpaceBetween)`、大卡片、表单组时，间距会被压缩或布局变形。
- Scroll 计算到的内容高度不符合真实内容高度，可能出现底部内容滚不到、被底部安全区或悬浮栏挡住的现象。
- 页面背景、空状态、加载态无法稳定铺满整屏。

所以二级页内容容器推荐使用：

```ts
.constraintSize({ minHeight: '100%' })
.justifyContent(FlexAlign.Start)
```

而不是：

```ts
.height('100%')
```

### 9.3 可直接复用：二级页 scaffold

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
  @Event onReadyHandler: (context: NavDestinationContext) => void = (_context: NavDestinationContext): void => {
  };
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
      .backgroundColor(this.pageBackgroundColor)
      .width('100%')
      .height('100%')
      .edgeEffect(EdgeEffect.Spring)
      .scrollBar(BarState.Off)
    }
    .titleBar(buildImmersiveTitleBarOptions(this.title, this.resolveMenu()))
    .titleMode(HdsNavDestinationTitleMode.MINI)
    .hideToolBar(true)
    .bindToScrollable([this.scroller])
    .ignoreLayoutSafeArea([LayoutSafeAreaType.SYSTEM], [LayoutSafeAreaEdge.TOP, LayoutSafeAreaEdge.BOTTOM])
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

二级页面使用方式：

```ts
import { SecondaryPageScaffold } from '../component/SecondaryPageScaffold';
import { resolveImmersiveContentTopPadding } from '../utils/ImmersiveNavigation';

@ComponentV2
export default struct ExampleDetailPage {
  private scroller: Scroller = new Scroller();

  build() {
    SecondaryPageScaffold({
      title: { mainTitle: '详情' },
      scroller: this.scroller
    }) {
      Column({ space: 12 }) {
        Text('详情内容')
          .fontSize(16)
          .fontColor($r('app.color.text_primary'))
      }
      .width('100%')
      .constraintSize({ minHeight: '100%' })
      .justifyContent(FlexAlign.Start)
      .padding({
        left: 20,
        right: 20,
        top: resolveImmersiveContentTopPadding(),
        bottom: 24
      })
    }
  }
}
```

## 10. 颜色、深浅色和自定义主题

### 10.1 推荐资源结构

HarmonyOS 项目建议同时准备浅色和深色资源：

```text
entry/src/main/resources/base/element/color.json
entry/src/main/resources/dark/element/color.json
```

关键 token 成对存在：

| token | 浅色 | 深色 | 用途 |
| --- | --- | --- | --- |
| `start_window_background` | `#F4F8F7` | `#0F1417` | 根窗口和页面背景 |
| `card_background` | `#FFFFFF` | `#171E22` | 卡片背景 |
| `text_primary` | `#132022` | `#EAF3F1` | 主文本 |
| `text_secondary` | `#54666B` | `#A8B8B8` | 次级文本 |
| `tab_item_active` | `#00766D` | `#5DD6C8` | 当前选中 TAB 图标和文字 |
| `tab_item_inactive` | `#5F7177` | `#7D8C8F` | 未选中 TAB |
| `transparent` | `#00000000` | `#00000000` | 标题栏/TAB 透明背景 |

页面里应使用 `$r('app.color.xxx')`，不要直接写颜色：

```ts
Text('HarmonyOS')
  .fontColor($r('app.color.text_primary'))
  .backgroundColor($r('app.color.start_window_background'))
```

### 10.2 可直接复用：浅深色资源示例

`entry/src/main/resources/base/element/color.json`：

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
      "name": "tab_item_active",
      "value": "#00766D"
    },
    {
      "name": "transparent",
      "value": "#00000000"
    }
  ]
}
```

`entry/src/main/resources/dark/element/color.json`：

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
      "name": "tab_item_active",
      "value": "#5DD6C8"
    },
    {
      "name": "transparent",
      "value": "#00000000"
    }
  ]
}
```

注意：如果只写 `base`，没有 `dark` 对应 token，深色模式下就不会得到正确资源值。官方 `WithTheme` 文档也明确提醒，局部深浅色要生效，需要添加深色资源。

### 10.3 自定义主题不要绕过安全门

如果项目要支持用户自定义主题色，建议准备这些基础模块：

- `ThemeColorEngine`：从用户输入的 `#RRGGBB` 派生浅色/深色 palette。
- `ThemeSafetyGate`：校验文本对比度、非文本对比度、语义色冲突。
- `ThemePreferenceService`：保存、恢复、fallback 到默认主题。
- `AppState.applyThemePreference()`：统一更新主题状态。

后续页面如果要消费自定义主题，推荐仍然走统一 token 层，不要在页面里直接读用户输入色值：

```ts
@ObservedV2
export class AppState {
  @Trace themePaletteSet: ThemePaletteSet = createDefaultThemePaletteSet();
  @Trace isCustomTheme: boolean = false;

  public applyThemePreference(config: ThemeConfig, paletteSet: ThemePaletteSet, isCustomTheme: boolean,
    fallbackReason: string, source: string): void {
    this.themePaletteSet = cloneThemePaletteSet(paletteSet);
    this.isCustomTheme = isCustomTheme;
  }
}
```

页面层不要这样写：

```ts
// 不推荐：直接使用用户输入色，绕过对比度和语义校验。
Text('保存')
  .fontColor(this.userInputColor)
```

应改成：

```ts
// 推荐：页面只使用已经校验过的 token。
Text('保存')
  .fontColor($r('app.color.text_primary'))
```

如果后续确实要让资源 token 动态来自 `AppState.themePaletteSet`，也应先集中做一个 resolver，再让页面调用 resolver，避免业务页面重复判断浅色/深色。

## 11. 自定义材质档位

默认建议用 `ADAPTIVE`。只有在产品明确要求某种材质强度时，才需要自定义档位。

可复用代码：

```ts
import { hdsMaterial, SystemMaterialParams } from '@kit.UIDesignKit';
import { BusinessError } from '@kit.BasicServicesKit';

export function resolveSystemMaterialEffect(): SystemMaterialParams {
  try {
    const supportedTypes: Array<hdsMaterial.MaterialType> = hdsMaterial.getSystemMaterialTypes();
    const supportsImmersive = supportedTypes.indexOf(hdsMaterial.MaterialType.IMMERSIVE) >= 0;

    return {
      materialType: hdsMaterial.MaterialType.ADAPTIVE,
      materialLevel: supportsImmersive ? hdsMaterial.MaterialLevel.GENTLE : hdsMaterial.MaterialLevel.SMOOTH
    };
  } catch (err) {
    const error = err as BusinessError;
    console.error(`getSystemMaterialTypes failed, code=${error.code}, message=${error.message}`);
    return {
      materialType: hdsMaterial.MaterialType.ADAPTIVE,
      materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
    };
  }
}
```

一般项目不需要这段，直接用 `ADAPTIVE + ADAPTIVE` 更稳。

## 12. 接入步骤

### 12.1 新项目从零接入

1. 在 `EntryAbility` 设置 `setWindowLayoutFullScreen(true)`。
2. 读取 `TYPE_SYSTEM` 和 `TYPE_NAVIGATION_INDICATOR` 避让区，保存到 `AppState`。
3. 设置 `setColorMode(COLOR_MODE_NOT_SET)`，让应用默认跟随系统深浅色。
4. 创建 `ImmersiveNavigation.ets`，统一封装 `buildImmersiveTitleBarOptions()`。
5. 根页面使用 `HdsNavigation + HdsTabs`，根容器配置 `ignoreLayoutSafeArea([SYSTEM], [TOP, BOTTOM])`。
6. HDS 标题栏和 HDS 悬浮 TAB 都配置 `systemMaterialEffect`。
7. 每个根 TAB 接收外部 `Scroller`，并把当前 TAB 的 `Scroller` 绑定给根 `HdsNavigation`。
8. 根 TAB 内容顶部避让 `topSafeHeight + ROOT_MINI_TITLE_BAR_HEIGHT`。
9. 根 TAB 内容底部避让 `tabBarHeight + bottomSafeHeight + floatingBarMargin * 2`。
10. 二级页面全部使用 `SecondaryPageScaffold`。
11. 颜色只写语义 token，并在 `base` 与 `dark` 资源中成对维护。
12. 真机验证浅色、深色、滚动、底部手势条、二级页返回、横竖屏或不同窗口模式。

### 12.2 既有项目改造

1. 先搜索窗口 API：`rg "setWindowLayoutFullScreen|setWindowSystemBarProperties|getWindowAvoidArea" entry/src/main/ets`。
2. 如果多个页面直接调用窗口 API，先收敛到 `EntryAbility` 或统一窗口服务。
3. 搜索安全区：`rg "expandSafeArea|ignoreLayoutSafeArea|SafeArea|topSafeHeight|bottomSafeHeight" entry/src/main/ets`。
4. 如果页面里到处手写 `56 + 24 + safeArea`，抽成 `ImmersiveNavigation` 或 scaffold。
5. 搜索 HDS 标题栏：`rg "titleBar\\(|HdsNavigation|HdsNavDestination" entry/src/main/ets`。
6. 如果标题栏配置分散，统一改用 `buildImmersiveTitleBarOptions()`。
7. 搜索硬编码颜色：`rg "#[0-9A-Fa-f]{6}|Color\\." entry/src/main/ets`。
8. 将页面硬编码颜色收敛成 `base/dark` 成对资源或主题 token。
9. 先改根页面，再改根 TAB 内容，最后改二级页面。
10. 每改一类页面就跑构建和真机视觉检查，不要一次改完全应用后才验证。

## 13. 验收清单

### 13.1 静态检查

```bash
rg "setWindowLayoutFullScreen|getWindowAvoidArea" entry/src/main/ets
rg "buildImmersiveTitleBarOptions|systemMaterialEffect|barFloatingStyle" entry/src/main/ets
rg "ignoreLayoutSafeArea|expandSafeArea|topSafeHeight|bottomSafeHeight" entry/src/main/ets
rg "#[0-9A-Fa-f]{6}|Color\\." entry/src/main/ets
```

期待结果：

- 窗口 API 集中在 `EntryAbility` 或统一窗口服务。
- 标题栏光感材质集中在 `ImmersiveNavigation`。
- 根 `HdsNavigation` 和二级 `HdsNavDestination` 都能看到 `ignoreLayoutSafeArea`。
- 页面主色来自 `$r('app.color.xxx')` 或统一 token，不是到处写十六进制颜色。

### 13.2 构建检查

文档改动只需 Markdown 检查；代码改动至少跑受影响 Harmony build：

```bash
python3 <harmony-build-skill>/run.py build --repo . --paths entry/src/main/ets/pages/Index.ets entry/src/main/ets/utils/ImmersiveNavigation.ets entry/src/main/ets/component/SecondaryPageScaffold.ets
```

如果改了 `EntryAbility`，把它也加入 `--paths`。

### 13.3 真机视觉检查

沉浸光感最终要以真机为准，尤其是 HDS 光感材质。检查项：

| 场景 | 应该看到 |
| --- | --- |
| 浅色模式首页 | 状态栏区域背景和页面背景连续，状态栏文字清晰 |
| 深色模式首页 | 状态栏区域不发灰、不突兀，状态栏文字清晰 |
| 根 TAB 滚动 | 标题栏不会遮住第一行内容，标题栏按钮有 HDS 材质层次 |
| 底部悬浮 TAB | 不贴住手势条，不挡住列表最后一项 |
| 二级页面 | 顶部标题栏、返回按钮和内容不重叠 |
| 二级页面长列表 | 滚动时标题栏绑定正常，底部内容能完全滚出悬浮区域 |
| 横竖屏/折叠屏窗口 | 背景仍铺满，内容仍在安全区域内 |

官方 UI Design Kit 简介里提到，模拟器不支持部分 HDS 沉浸视效，包括沉浸光感材质。因此模拟器最多用于检查布局，不适合作为最终光感效果证据。

## 14. 常见错误

### 错误 1：只调用 `setWindowLayoutFullScreen(true)`，不处理 padding

现象：内容顶到状态栏下面，第一行文字被系统时间遮住。

修法：背景可以全屏，但内容顶部必须加：

```ts
top: this.appState.topSafeHeight + Constants.ROOT_MINI_TITLE_BAR_HEIGHT
```

### 错误 2：底部悬浮 TAB 没加 `bottomSafeHeight`

现象：底部 TAB 贴着手势条，或者列表最后一项被挡住。

修法：

```ts
barBottomMargin: this.floatingBarMargin + this.appState.bottomSafeHeight
```

内容底部也要加：

```ts
bottomContentPadding = tabBarHeight + bottomSafeHeight + floatingBarMargin * 2
```

### 错误 3：每个页面自己写标题栏

现象：有的标题栏透明，有的灰底；有的带光感，有的不带；二级页和根页不一致。

修法：所有 `HdsNavigation` 和 `HdsNavDestination` 都使用同一个：

```ts
.titleBar(buildImmersiveTitleBarOptions(this.title, this.menu))
```

### 错误 4：深色资源缺 token

现象：深色模式下某些卡片还是白底，文字对比度差。

修法：每新增一个 `base/element/color.json` token，都同步在 `dark/element/color.json` 添加同名 token。

### 错误 5：把用户自定义颜色直接用于文本或状态栏

现象：用户选了很浅或很深的颜色后，文字看不清，错误色/警告色被主题色污染。

修法：所有用户色先经过 `ThemeSafetyGate`，页面只使用校验后的 token。

### 错误 6：用模拟器结论代替真机光感效果

现象：模拟器上看不到 HDS 光感，误以为代码不生效。

修法：模拟器只看布局；HDS 沉浸光感材质必须真机看。

## 15. 最小完成定义

一次沉浸光感适配至少要满足：

1. 主窗口调用 `setWindowLayoutFullScreen(true)`。
2. 顶部/底部避让区被读取并进入全局状态。
3. 根 `HdsNavigation` 或 `Navigation` 背景铺满顶部/底部系统区域。
4. 标题栏统一配置透明背景和 HDS `systemMaterialEffect`。
5. 底部 `HdsTabs` 配置悬浮样式和 HDS `systemMaterialEffect`。
6. 根 TAB 内容顶部不被状态栏/标题栏挡住。
7. 根 TAB 内容底部不被悬浮 TAB/手势条挡住。
8. 二级页统一走 `SecondaryPageScaffold` 或等价封装。
9. 浅色/深色资源成对存在，页面不散落硬编码颜色。
10. 真机检查浅色、深色、滚动、底部手势条、二级页返回都正常。

## 16. 通用维护建议

沉浸光感适配完成后，建议继续收敛两点：

1. 根 TAB 内容可抽出 `RootTabContentScaffold`，减少各个 TAB 页面里的重复 padding 逻辑。
2. 自定义主题色进入页面消费时，应先建立统一 token resolver，再把 `ThemePaletteSet` 映射到页面颜色，避免页面直接使用用户输入色。

这两点不是沉浸式布局的必要前置，但能让沉浸光感、深浅色和自定义主题在长期维护中保持一致。
