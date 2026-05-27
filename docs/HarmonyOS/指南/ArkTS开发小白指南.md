# HarmonyOS ArkTS 开发小白指南

本文面向刚开始写 HarmonyOS 应用的开发者，目标是把 ArkTS 语言规则、ArkUI 声明式组件、状态管理、资源引用、异步错误处理和常见工程分层串成一套可以直接照抄的入门规范。

本文不绑定某一个应用。示例代码会参考当前应用里已经验证过的写法，例如 `AppState`、`SettingsItem`、`SecondaryPageScaffold`、`DnsDataManager` 这类结构，但你可以把命名替换成自己项目的业务名。

相关文档分工：

| 文档 | 负责什么 |
| --- | --- |
| `docs/ArkTS开发小白指南.md` | ArkTS 语言、组件写法、状态、异步、错误处理、资源和工程分层 |
| `docs/HarmonyOS界面设计布局小白指南.md` | 页面结构、Row/Column/Scroll 布局、HDS 导航、TAB、二级页和视觉规则 |
| `docs/HarmonyOS沉浸光感适配小白指南.md` | 沉浸式窗口、安全区、HDS 沉浸光感、标题栏、底部悬浮 TAB 和二级页沉浸适配 |

## 1. 先理解 ArkTS 和 ArkUI 的关系

ArkTS 是 HarmonyOS 应用的主要开发语言。ArkUI 是用 ArkTS 写界面的声明式 UI 框架。

可以这样理解：

| 名称 | 负责什么 | 新手最常接触的内容 |
| --- | --- | --- |
| ArkTS | 业务逻辑、类型、类、接口、异步、模块导入 | `class`、`interface`、`Promise`、`async/await`、`import` |
| ArkUI | 页面和组件声明 | `@ComponentV2`、`build()`、`Column()`、`Row()`、`Text()`、`Scroll()` |
| Kit API | 系统能力 | `@kit.AbilityKit`、`@kit.ArkUI`、`@kit.UIDesignKit`、`@kit.ArkData` |
| resources | 颜色、文字、尺寸、图片 | `$r('app.string.xxx')`、`$r('app.color.xxx')`、`$r('app.float.xxx')` |

一个普通页面通常长这样：

```ts
@ComponentV2
export default struct ExamplePage {
  @Local title: string = 'Hello';

  build() {
    Column({ space: 12 }) {
      Text(this.title)
        .fontSize($r('app.float.text_size_title'))
        .fontColor($r('app.color.text_primary'))
    }
    .width('100%')
    .height('100%')
    .backgroundColor($r('app.color.start_window_background'))
  }
}
```

记住三件事：

1. 页面是 `struct`，用 `@ComponentV2` 装饰。
2. 界面写在 `build()` 里。
3. 会变化的数据要用状态装饰器，例如 `@Local`、`@Param`、`@Trace`。

## 2. 推荐项目目录

新项目可以先按下面结构组织，后续再按业务增长拆分：

```text
entry/src/main/ets/
  entryability/
    EntryAbility.ets
  pages/
    Index.ets
    SettingsPage.ets
  component/
    SettingsItem.ets
    SecondaryPageScaffold.ets
  model/
    AppState.ets
    UserModels.ets
  utils/
    Constants.ets
    LogUtils.ets
    DataManager.ets
  db/
    AppDatabase.ets
entry/src/main/resources/
  base/element/
    string.json
    color.json
    float.json
  dark/element/
    color.json
```

职责建议：

| 目录 | 放什么 | 不建议放什么 |
| --- | --- | --- |
| `pages/` | 页面入口、TAB 页面、二级页面 | 大量业务算法、数据库细节 |
| `component/` | 可复用 UI 组件 | 页面级状态和路由主逻辑 |
| `model/` | 数据模型、全局状态 | 系统 API 调用 |
| `utils/` | 工具、服务、校验器、主题计算 | 大型 UI 组件 |
| `db/` | RDB、DAO、持久化 | 页面展示逻辑 |
| `resources/` | 字符串、颜色、尺寸、图片 | 临时测试数据 |

## 3. ArkTS 类型规则

ArkTS 比普通 TypeScript 更强调静态类型。新手最容易踩的坑是：把 TypeScript 里很灵活的写法直接搬过来。

### 3.1 尽量写清楚类型

推荐：

```ts
let count: number = 0;
let title: string = '设置';
let enabled: boolean = false;
let names: string[] = ['默认 DNS', '备用 DNS'];
```

也可以让编译器推断：

```ts
const defaultTimeoutMs = 10000;
const tag = 'SettingsPage';
```

不推荐：

```ts
let data: any = {};
let result;
```

原因：ArkTS 依赖编译期类型做检查和优化。类型越模糊，越容易在编译或运行时出问题。

### 3.2 用 class 或 interface 描述对象形状

不要把对象类型写成 TypeScript 的匿名对象类型：

```ts
// 不推荐
let user: { id: string, name: string } = {
  id: '1',
  name: 'Tom'
};
```

推荐使用 `class` 或 `interface`：

```ts
export class UserInfo {
  id: string = '';
  name: string = '';
}

let user: UserInfo = new UserInfo();
user.id = '1';
user.name = 'Tom';
```

如果只是函数入参结构，也可以用 `interface`：

```ts
export interface SaveOptions {
  retryCount: number;
  showToast: boolean;
}

function save(options: SaveOptions): void {
  if (options.showToast) {
    // show toast
  }
}
```

### 3.3 空值要显式写出来

ArkTS 默认不允许普通类型为 `null`。如果一个值可能为空，要写联合类型：

```ts
let selectedId: string | null = null;

function findName(id: string): string | null {
  if (id.length === 0) {
    return null;
  }
  return '默认';
}
```

使用前要判断：

```ts
const name = findName('1');
if (name !== null) {
  console.info(name);
}
```

不要为了省事到处写非空断言。非空断言只适合你非常确定对象一定存在的场景。

### 3.4 类型转换先判断再 `as`

`as` 是编译期类型断言，不会在运行时帮你验证对象真的是什么类型。

不推荐：

```ts
const context = value as UIAbilityContext;
context.startAbility(want);
```

推荐：

```ts
if (value instanceof UIAbilityContext) {
  const context = value as UIAbilityContext;
  context.startAbility(want);
}
```

不是所有 Kit 类型都适合 `instanceof`，遇到系统对象时可以用字段存在性、返回值是否为空、错误码等方式做边界判断。

## 4. 组件和状态管理

### 4.1 `@ComponentV2` 组件基本写法

```ts
@ComponentV2
export struct CounterView {
  @Local count: number = 0;

  build() {
    Row({ space: 8 }) {
      Text(`次数：${this.count}`)
        .fontSize($r('app.float.text_size_body'))

      Button('增加')
        .onClick(() => {
          this.count++;
        })
    }
  }
}
```

`@Local` 适合组件自己的内部状态。父组件不需要知道它，也不需要控制它。

### 4.2 `@Param` 和 `@Event`

子组件接收父组件数据，用 `@Param`。子组件通知父组件，用 `@Event`。

可复用的设置项组件：

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

父组件使用：

```ts
SettingsItem({
  title: $r('app.string.settings_about'),
  value: '1.0.0',
  onClickHandler: () => {
    this.navStack.pushPath({ name: 'AboutPage' });
  }
})
```

### 4.3 双向输入用 `@Param + @Event`

输入框这类组件通常需要父子双向同步。推荐显式写 `$value` 回调。

```ts
@ComponentV2
export struct InputCell {
  @Param title: ResourceStr = '';
  @Param value: string = '';
  @Event $value: (value: string) => void = (_value: string): void => {};

  build() {
    Row() {
      Text(this.title)
        .width($r('app.float.input_label_width'))

      TextInput({ text: this.value })
        .layoutWeight(1)
        .onChange((nextValue: string) => {
          this.$value(nextValue);
        })
    }
  }
}
```

页面使用：

```ts
InputCell({
  title: $r('app.string.common_name'),
  value: this.name,
  $value: (val: string) => {
    this.name = val;
  }
})
```

### 4.4 全局状态用 `@ObservedV2 + @Trace`

应用级状态可以集中放到 `AppState`：

```ts
@ObservedV2
export class AppState {
  private static instance: AppState;

  @Trace topSafeHeight: number = 0;
  @Trace bottomSafeHeight: number = 0;
  @Trace isRunning: boolean = false;
  @Trace selectedIds: string[] = [];

  public static getInstance(): AppState {
    if (!AppState.instance) {
      AppState.instance = new AppState();
    }
    return AppState.instance;
  }

  public resetRuntimeStats(): void {
    this.isRunning = false;
  }
}
```

页面读取：

```ts
@ComponentV2
export default struct HomePage {
  @Local appState: AppState = AppState.getInstance();

  build() {
    Text(this.appState.isRunning ? '运行中' : '未运行')
  }
}
```

原则：

| 状态类型 | 推荐位置 |
| --- | --- |
| 只影响当前组件 | `@Local` |
| 父组件传给子组件 | `@Param` |
| 子组件回调父组件 | `@Event` |
| 全局 UI 状态 | `@ObservedV2` 类里的 `@Trace` 字段 |
| 跨层级路由栈 | `@Provider` / `@Consumer` 或 `onReady` 获取 |

### 4.5 监听状态变化用 `@Monitor`

当一个状态变化后需要触发副作用，可以用 `@Monitor`：

```ts
@Monitor('appState.isRunning')
onRunningChange(): void {
  if (this.appState.isRunning) {
    this.startTimer();
    return;
  }
  this.stopTimer();
}
```

注意：`@Monitor` 里不要做太重的同步计算，也不要制造循环更新。它适合启动计时器、刷新派生展示、触发轻量同步。

## 5. 生命周期和资源释放

页面出现时订阅事件，页面消失时必须取消订阅和定时器。

```ts
@ComponentV2
export default struct RuntimePage {
  private timerId: number = -1;

  aboutToAppear(): void {
    this.timerId = setInterval(() => {
      this.refresh();
    }, 1000);
  }

  aboutToDisappear(): void {
    if (this.timerId !== -1) {
      clearInterval(this.timerId);
      this.timerId = -1;
    }
  }

  private refresh(): void {
    // refresh data
  }

  build() {
    Text('运行状态')
  }
}
```

这条规则很重要。页面退出后如果还保留定时器、订阅或异步回调，后续可能出现重复刷新、状态错乱和内存占用增长。

## 6. 异步、错误处理和日志

### 6.1 `async/await` 基本写法

```ts
async function loadData(): Promise<void> {
  const list = await DataManager.getInstance().getList();
  AppState.getInstance().selectedIds = list.map((item: ItemInfo): string => item.id);
}
```

如果函数内部用了 `await`，函数返回类型通常写 `Promise<void>` 或 `Promise<T>`。

### 6.2 `catch` 里先转成可处理类型

不要假设 `catch` 拿到的一定是 `Error`。

```ts
try {
  await this.save();
} catch (err) {
  const message = err instanceof Error ? err.message : JSON.stringify(err);
  LogUtils.error('SettingsPage', `save failed: ${message}`);
  AppState.showToast($r('app.string.toast_save_failed'));
}
```

如果你要继续抛错，优先抛 `Error`：

```ts
function requireName(name: string): void {
  if (name.trim().length === 0) {
    throw new Error('name is empty');
  }
}
```

### 6.3 不要吞掉关键错误

不推荐：

```ts
try {
  await this.save();
} catch (err) {
}
```

推荐：

```ts
try {
  await this.save();
} catch (err) {
  LogUtils.error('EditPage', 'save failed: ' + JSON.stringify(err));
  AppState.showToast($r('app.string.toast_save_failed'));
}
```

只有清理动作可以谨慎吞错，例如关闭 socket、取消订阅、删除临时文件。即便吞错，也建议核心流程已经有日志。

## 7. JSON 和外部输入

### 7.1 `JSON.parse` 要标注返回类型

不推荐：

```ts
let data = JSON.parse(raw);
```

推荐：

```ts
interface ThemePayload {
  baseColor: string;
}

function parseThemePayload(raw: string): ThemePayload {
  const data: ThemePayload = JSON.parse(raw) as ThemePayload;
  if (!isValidHexColor(data.baseColor)) {
    throw new Error('invalid theme color');
  }
  return data;
}
```

### 7.2 外部输入先 normalize 再保存

以颜色输入为例：

```ts
class NormalizeResult {
  ok: boolean = false;
  value: string = '';
  reason: string = '';
}

class ColorParser {
  private static readonly HEX_COLOR_PATTERN: RegExp = /^#?[0-9A-Fa-f]{6}$/;

  static normalize(raw: string): NormalizeResult {
    const result = new NormalizeResult();
    const value = raw.trim();
    if (!ColorParser.HEX_COLOR_PATTERN.test(value)) {
      result.reason = 'invalid_format';
      return result;
    }
    result.ok = true;
    result.value = value.startsWith('#') ? value.toUpperCase() : `#${value.toUpperCase()}`;
    return result;
  }
}
```

页面保存时：

```ts
const normalized = ColorParser.normalize(this.inputColor);
if (!normalized.ok) {
  AppState.showToast($r('app.string.toast_invalid_color'));
  return;
}
await ThemePreferenceService.getInstance().save(normalized.value);
```

原则：用户输入、文件内容、网络响应、路由参数都算外部输入，都要校验。

## 8. 列表渲染和 key

`ForEach` 渲染列表时，建议提供稳定 key。

```ts
ForEach(this.appState.dnsList, (item: DnsInfo) => {
  DnsCardItem({
    item: item,
    isSelected: this.appState.selectedDnsIds.includes(item.id)
  })
}, (item: DnsInfo): string => {
  return `${item.id}_${this.appState.selectedDnsIds.includes(item.id) ? 'selected' : 'unselected'}`;
})
```

稳定 key 的作用：

1. 帮助 ArkUI 判断哪些组件需要复用。
2. 避免列表修改后 UI 不刷新或刷新错位。
3. 让选择态、展开态、动画状态更可控。

如果是非常长的列表，再考虑 `LazyForEach`。普通设置页、少量卡片列表，用 `ForEach` 更简单。

## 9. 资源引用

页面文字、颜色、尺寸尽量走资源。

推荐：

```ts
Text($r('app.string.settings_about'))
  .fontSize($r('app.float.text_size_title'))
  .fontColor($r('app.color.text_primary'))
```

不推荐：

```ts
Text('关于')
  .fontSize(16)
  .fontColor('#132022')
```

常用资源文件：

```text
entry/src/main/resources/base/element/string.json
entry/src/main/resources/base/element/color.json
entry/src/main/resources/base/element/float.json
entry/src/main/resources/dark/element/color.json
```

### 9.1 `ResourceStr` 和 `ResourceColor`

组件参数如果可能接收资源，类型写成资源友好的形式：

```ts
@Param title: ResourceStr = '';
@Param pageBackgroundColor: ResourceColor = $r('app.color.start_window_background');
```

这样调用方既可以传字符串，也可以传 `$r(...)`。

### 9.2 动态字符串用 ResourceManager

有些文案需要根据状态生成，不能直接用 `$r` 嵌套。可以通过 `resourceManager` 获取：

```ts
private getStringByName(name: string): string {
  try {
    const hostContext = this.getUIContext().getHostContext();
    if (!hostContext) {
      return '';
    }
    return hostContext.resourceManager.getStringByNameSync(name);
  } catch (err) {
    return '';
  }
}
```

使用：

```ts
private getEnabledSummary(enabled: boolean): string {
  return enabled ? this.getStringByName('settings_enabled') : this.getStringByName('settings_disabled');
}
```

## 10. 页面、组件、服务的分层

推荐页面只做三件事：

1. 展示状态。
2. 响应用户操作。
3. 调用服务完成真实业务。

不要把数据库、网络、复杂解析逻辑都写在页面里。

### 10.1 页面保存流程模板

```ts
async save(): Promise<void> {
  const name = this.name.trim();
  const address = this.address.trim();

  if (name.length === 0 || address.length === 0) {
    AppState.showToast($r('app.string.toast_fill_complete'));
    return;
  }

  if (!Validator.isValidAddress(address)) {
    AppState.showToast($r('app.string.toast_address_invalid'));
    return;
  }

  try {
    const item = new ServerInfo();
    item.name = name;
    item.address = address;
    await DataManager.getInstance().saveServer(item);
    AppState.showToast($r('app.string.toast_save_success'));
    this.pathStack.pop();
  } catch (err) {
    LogUtils.error('ServerEditPage', 'save failed: ' + JSON.stringify(err));
    AppState.showToast($r('app.string.toast_save_failed'));
  }
}
```

这个模板的顺序是：

1. 读取并清洗输入。
2. 做本地校验。
3. 调服务保存。
4. 成功后提示并返回。
5. 失败时记录日志并提示。

### 10.2 服务类模板

```ts
export class DataManager {
  private static instance: DataManager;

  public static getInstance(): DataManager {
    if (!DataManager.instance) {
      DataManager.instance = new DataManager();
    }
    return DataManager.instance;
  }

  async saveServer(item: ServerInfo): Promise<void> {
    if (item.name.trim().length === 0) {
      throw new Error('server name is empty');
    }
    await AppDatabase.getInstance().serverDao.save(item);
    AppState.getInstance().serverList = await AppDatabase.getInstance().serverDao.list();
  }
}
```

服务层负责业务一致性，页面层负责展示和交互。这样后续同一个保存逻辑可以被多个页面复用。

## 11. 导航和路由基础

普通 HarmonyOS 应用建议用 `Navigation + NavPathStack` 或 HDS 的 `HdsNavigation + HdsNavDestination`。

根页面持有一个栈：

```ts
@Provider('navStack') navStack: NavPathStack = new NavPathStack();
```

子页面或 TAB 消费：

```ts
@Consumer('navStack') navStack: NavPathStack = new NavPathStack();
```

跳转：

```ts
this.navStack.pushPath({ name: 'SettingsPage' });
```

带参数跳转：

```ts
this.navStack.pushPath({
  name: 'EditPage',
  param: new EditPageParam(item.id)
});
```

二级页也可以在 `onReady` 里拿到当前 `pathStack`：

```ts
.onReady((context: NavDestinationContext): void => {
  this.pathStack = context.pathStack;
  const param = context.pathInfo.param as EditPageParam;
  this.initWithParam(param);
})
```

详细布局结构见 `docs/HarmonyOS界面设计布局小白指南.md`。

## 12. 命名和代码风格

推荐规则：

| 内容 | 命名 |
| --- | --- |
| 页面 | `SettingsPage.ets`、`DnsEditPage.ets` |
| TAB | `StartTab.ets`、`SettingsTab.ets` |
| 组件 | `SettingsItem.ets`、`InputCell.ets` |
| 模型 | `DnsInfo.ets`、`ThemeModels.ets` |
| 服务 | `DnsDataManager.ets`、`ThemePreferenceService.ets` |
| 常量 | `Constants.ets` |
| 日志 tag | `const TAG = 'ModuleName';` |

代码风格：

1. ArkTS 源码使用两空格缩进。
2. 字符串默认单引号。
3. import 使用明确相对路径。
4. 组件参数写默认值。
5. 公共逻辑先抽到 `component/` 或 `utils/`，不要复制到每个页面。
6. 注释只写非显而易见的原因，例如平台限制、生命周期边界、异常恢复策略。

## 13. 新手常见错误

### 错误 1：把 TypeScript 对象类型直接搬到 ArkTS

修法：用 `class` 或 `interface`。

### 错误 2：到处用 `any`

修法：为模型、接口返回值、JSON 结果写明确类型。

### 错误 3：页面里直接写数据库逻辑

修法：页面调用 `DataManager`，`DataManager` 再调用 DAO。

### 错误 4：订阅和定时器不释放

修法：`aboutToAppear()` 创建，`aboutToDisappear()` 释放。

### 错误 5：颜色、字号、文案写死

修法：放进 `resources/base/element`，深色颜色同步放进 `resources/dark/element`。

### 错误 6：`ForEach` 不写稳定 key

修法：用业务 id 生成 key，选择态影响 UI 时也纳入 key。

### 错误 7：catch 后没有日志

修法：至少记录模块名、动作和错误对象。

### 错误 8：外部输入不校验

修法：用户输入、文件、网络响应、路由参数都先 normalize 和 validate。

## 14. 最小开发流程

做一个新页面时，按这个顺序：

1. 先定义模型和页面参数。
2. 在 `resources` 里补齐文案、颜色、尺寸。
3. 写页面状态：`@Local`、`@Param`、`@Consumer`。
4. 写静态 UI，先不接业务。
5. 把重复 UI 抽成组件。
6. 写输入校验和保存流程。
7. 调服务层，不直接操作数据库。
8. 给 `ForEach` 加稳定 key。
9. 加错误日志和 toast。
10. 跑构建，真机看关键交互。

## 15. 官方依据

本文依据本地 DocsHub 中的 HarmonyOS 官方文档快照整理，关键资料包括：

| 主题 | 官方文档 |
| --- | --- |
| ArkTS 语言 | [ArkTS语言介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/introduction-to-arkts) |
| TypeScript 到 ArkTS | [从TypeScript到ArkTS的适配规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/typescript-to-arkts-migration-guide) |
| ArkTS 案例 | [适配指导案例](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-more-cases) |
| 状态管理 V2 | [状态管理概述](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview) |
| `@ObservedV2` / `@Trace` | [数据对象状态变量迁移](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-class) |
| `@Param` / `@Event` | [组件内状态变量迁移](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-inner-component) |
| `@Monitor` | [@Monitor装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-monitor) |
| `@BuilderParam` | [@BuilderParam装饰器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-builderparam) |
| Navigation | [Navigation基础架构介绍](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-architecture) |
| 资源类型 | [基础类型定义](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-types) |
| 深浅色资源 | [应用深浅色适配](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ui-dark-light-color-adaptation) |
