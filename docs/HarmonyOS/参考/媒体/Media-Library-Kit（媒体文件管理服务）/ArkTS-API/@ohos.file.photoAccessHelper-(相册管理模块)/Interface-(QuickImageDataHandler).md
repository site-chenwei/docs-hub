---
title: "Interface (QuickImageDataHandler)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-photoaccesshelper-quickimagedatahandler"
menu_path:
  - "参考"
  - "媒体"
  - "Media Library Kit（媒体文件管理服务）"
  - "ArkTS API"
  - "@ohos.file.photoAccessHelper (相册管理模块)"
  - "Interface (QuickImageDataHandler)"
captured_at: "2026-04-17T01:48:45.323Z"
---

# Interface (QuickImageDataHandler)

媒体资源处理器，应用在onDataPrepared方法中可自定义媒体资源处理逻辑。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/Aev1Ha3fSKuWNWxityRUMA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014847Z&HW-CC-Expire=86400&HW-CC-Sign=7140237FBCCCD26DA43C258C0753C8B20BCDA39BF06BA3538091E1699A85AE0B)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 13开始支持。

#### 导入模块

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### onDataPrepared13+

onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void

当请求的图片资源准备就绪时，系统会回调媒体资源就绪通知方法。如果资源准备出错，回调的data将为undefined。

map支持返回的信息：

| map键名 | 值说明 |
| :-- | :-- |
| 'quality' | 图片质量。高质量为'high'，低质量为'low'。 |

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| data | T | 是 | 已就绪的图片资源数据。泛型，支持[Picture](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-picture)数据类型。 |
| imageSource | image.ImageSource | 是 | 已就绪的图片资源数据。 |
| map13+ | Map<string, string> | 是 | 用于获取图片资源的额外信息，如图片质量。仅支持'quality'。 |

**示例：**

```ts
import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
  onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
    console.info('on image data prepared');
  }
}
```
