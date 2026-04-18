---
title: "RawFileDescriptor"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-rawfiledescriptor"
menu_path:
  - "参考"
  - "应用框架"
  - "Localization Kit（本地化开发服务）"
  - "ArkTS API"
  - "global"
  - "RawFileDescriptor"
captured_at: "2026-04-17T01:48:16.328Z"
---

# RawFileDescriptor

本模块提供rawfile文件所在hap的descriptor信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/CS3qSWt2TPG6CtIvMQ1S-g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014816Z&HW-CC-Expire=86400&HW-CC-Sign=F7D8AAFD86922A2B800BFF38B2260D5B4667A2E4ED0D6121BBF9EFFA8BF537CD)

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import { resourceManager } from '@kit.LocalizationKit'
```

#### RawFileDescriptor

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Global.ResourceManager

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | 否 | 否 | 文件描述符。 |
| offset | number | 否 | 否 | 起始偏移量。 |
| length | number | 否 | 否 | 文件长度。 |
