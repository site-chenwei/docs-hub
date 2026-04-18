---
title: "ReadPageComponent（阅读页组件）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-api-readpagecomponent"
menu_path:
  - "参考"
  - "应用服务"
  - "Reader Kit（阅读服务）"
  - "ArkTS组件"
  - "ReadPageComponent（阅读页组件）"
captured_at: "2026-04-17T01:49:03.846Z"
---

# ReadPageComponent（阅读页组件）

本模块提供ReadPageComponent组件，HarmonyOS应用通过集成该组件可快速构建书籍阅读功能。

**起始版本：** 5.0.4(16)

#### 导入模块

```typescript
import { ReadPageComponent } from '@kit.ReaderKit';
```

#### ReadPageComponent

阅读页组件，支持对书籍排版内容的显示、多种翻页交互和翻页动效，以及翻页阅读过程中阅读器所需要的进度、行为感知能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/uOIK2HaNRRWncEU0oXB7xg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014904Z&HW-CC-Expire=86400&HW-CC-Sign=9F69E945F5451A4AD7EEC299D30046E0CEE01A38BACCF95CA4A63967B8880A2B)

-   支持根据阅读排版设置[ReaderSetting](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-read-core#readersetting)对书籍内容进行按页进行排版、渲染。
    
-   支持适配不同的设备屏幕尺寸（Phone、PC/2in1、Tablet，包括横竖屏适配），并在此基础上支持通过点击、滑动的方式进行阅读交互，支持仿真、横滑翻页方式（包括翻页过程动效）。
    
-   支持排版结果通知能力，打开书籍或者触发翻页后按页提供当前页的排版结果信息[PageDataInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-read-core#pagedatainfo)。
    

**装饰器类型：** @Component

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**参数：**

| 参数名 | 类型 | 装饰器类型 | 说明 |
| :-- | :-- | :-- | :-- |
| controller | [ReaderComponentController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-read-core#readercomponentcontroller) | \_ | ReadPageComponent控制器。 |
| readerCallback | AsyncCallback<readerCore.[ReaderComponentController](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/reader-read-core#readercomponentcontroller)\> | \_ | 回调函数。 |

#### \[h2\]build

build(): void

用于创建ReadPageComponent对象的构造函数。

**元服务API：** 从版本5.0.4(16)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Reader.ReaderService.ReaderCore

**起始版本：** 5.0.4(16)

**示例：**

```typescript
import { bookParser, readerCore, ReadPageComponent } from '@kit.ReaderKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Reader {
  private readerComponentController: readerCore.ReaderComponentController = new readerCore.ReaderComponentController();

  aboutToAppear(): void {
    this.init();
  }

  private async init() {
    // 通过提前导入到应用沙箱目录中的书籍文件，初始化书籍解析器
    let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    let filePath: string = `${context.filesDir}/abc.epub`;
    let bookParserHandler: bookParser.BookParserHandler = await bookParser.getDefaultHandler(filePath);
    let spineList: bookParser.SpineItem[] = bookParserHandler.getSpineList();
    let spineIndex: number = spineList[0].index;
    let domPos: string = '';

    await this.readerComponentController.init(context);
    this.readerComponentController.registerBookParser(bookParserHandler);
    this.readerComponentController.startPlay(spineIndex || 0, domPos);
    hilog.info(0x0000, 'testTag', `startPlay succeeded`);
  }

  aboutToDisappear(): void {
    this.readerComponentController.releaseBook();
  }

  build() {
    Stack() {
      ReadPageComponent({
        controller: this.readerComponentController,
        readerCallback: (err: BusinessError, data: readerCore.ReaderComponentController) => {
          this.readerComponentController = data;
        }
      })
    }.width('100%').height('100%').onClick(() => {
      // 支持在此实现点击拉起菜单栏功能
    })
  }
}
```
