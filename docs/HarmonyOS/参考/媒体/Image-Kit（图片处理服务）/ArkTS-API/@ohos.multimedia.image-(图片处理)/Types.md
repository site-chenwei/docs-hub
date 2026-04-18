---
title: "Types"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-t"
menu_path:
  - "参考"
  - "媒体"
  - "Image Kit（图片处理服务）"
  - "ArkTS API"
  - "@ohos.multimedia.image (图片处理)"
  - "Types"
captured_at: "2026-04-17T01:48:41.078Z"
---

# Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/5s9-YFN9RmikyWBmMN6Nxw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014843Z&HW-CC-Expire=86400&HW-CC-Sign=68E1FA6252CAB61E811BA5D58E2398C32450056819D5CD9CE18AF12911CB674D)

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### HdrMetadataValue12+

type HdrMetadataValue = HdrMetadataType | HdrStaticMetadata | ArrayBuffer | HdrGainmapMetadata

PixelMap使用的HDR元数据值类型，和[HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#hdrmetadatakey12)关键字相对应。

**系统能力：** SystemCapability.Multimedia.Image.Core

| 类型 | 说明 |
| :-- | :-- |
| [HdrMetadataType](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#hdrmetadatatype12) | [HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#hdrmetadatakey12)中HDR\_METADATA\_TYPE关键字对应的元数据值类型。 |
| [HdrStaticMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i#hdrstaticmetadata12) | [HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#hdrmetadatakey12)中HDR\_STATIC\_METADATA关键字对应的元数据值类型。 |
| ArrayBuffer | [HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#hdrmetadatakey12)中HDR\_DYNAMIC\_METADATA关键字对应的元数据值类型。 |
| [HdrGainmapMetadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-i#hdrgainmapmetadata12) | [HdrMetadataKey](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-image-e#hdrmetadatakey12)中HDR\_GAINMAP\_METADATA关键字对应的元数据值类型。 |
