---
title: "Interface (MediaAssetProgressHandler)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/s-apis-photoaccesshelper-mediaassetprogresshandler"
menu_path:
  - "参考"
  - "媒体"
  - "Media Library Kit（媒体文件管理服务）"
  - "ArkTS API"
  - "@ohos.file.photoAccessHelper (相册管理模块)"
  - "Interface (MediaAssetProgressHandler)"
captured_at: "2026-04-17T01:48:45.211Z"
---

# Interface (MediaAssetProgressHandler)

媒体资产进度处理器，应用于onProgress方法中获取媒体资产进度。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/DSa-s-00T1qj8M5ks0DjEg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014847Z&HW-CC-Expire=86400&HW-CC-Sign=CC6E865214574F634B5140B43E896D27F87FD0EEBD8F3E1A15204AFDAB0390B9)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
-   本Interface首批接口从API version 15开始支持。

#### 导入模块

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';
```

#### onProgress15+

onProgress(progress: number): void

当所请求的视频资源返回进度时系统会回调此方法。

**系统能力**：SystemCapability.FileManagement.PhotoAccessHelper.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| progress | number | 是 | 返回的进度百分比，范围为\[0, 100\]。 |
