---
title: "commentManager（应用评论服务）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/appgallery-commentmanager"
menu_path:
  - "参考"
  - "应用服务"
  - "AppGallery Kit（应用市场服务）"
  - "ArkTS API"
  - "commentManager（应用评论服务）"
captured_at: "2026-04-17T01:48:56.645Z"
---

# commentManager（应用评论服务）

提供应用内评论能力，用户无需进入应用市场应用详情页进行评论。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/lqf8E_49TpqR3w-xgNWzTg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014856Z&HW-CC-Expire=86400&HW-CC-Sign=FBC020FFE5839B114A4D012D94487967067AB6B1C242D12B18D8D96BF4ED0152)

调用接口需捕获异常。

**起始版本：** 6.0.0(20)

#### 导入模块

```typescript
import { commentManager } from '@kit.AppGalleryKit';
```

#### commentManager.showCommentDialog

showCommentDialog(context: common.UIExtensionContext | common.UIAbilityContext): Promise<void>

拉起应用评分弹窗。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.AppGalleryService.Distribution.Comment

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| context | [common.UIExtensionContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext) | [common.UIAbilityContext](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext) | 是 | 应用上下文。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/store-error-code)。

| 错误码ID | 错误信息 |
| :-- | :-- |
| 1021500001 | Internal system error. |
| 1021500002 | Service request failed. |
| 1021500003 | Failed to connect to AppGallery. |
| 1021500004 | Failed to write parameters. |
| 1021500005 | The app context is invalid. |
| 1021500006 | The user has not signed in to their HUAWEI ID. |
| 1021500007 | The user has already commented on the current version. |
| 1021500008 | The number of comments has reached the maximum limit. |
| 1021500009 | The user has already left a comment, and less than a year has elapsed since then. |

**示例：**

```typescript
import { commentManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import type { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  @State message: string = 'showCommentDialog'

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            try {
              const uiContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
              // 拉起应用评分弹窗
              commentManager.showCommentDialog(uiContext).then(()=>{
                hilog.info(0, 'TAG', "succeeded in showing commentDialog.");
              }).catch((error: BusinessError<Object>) => {
                hilog.error(0, 'TAG', `showCommentDialog failed, Code: ${error.code}, message: ${error.message}`);
              });
            } catch (error) {
              hilog.error(0, 'TAG', `showCommentDialog failed, Code: ${error.code}, message: ${error.message}`);
            }
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
```
