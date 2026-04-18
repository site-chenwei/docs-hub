---
title: "CustomizeData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-customizedata"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "bundle"
  - "CustomizeData"
captured_at: "2026-04-17T01:47:48.337Z"
---

# CustomizeData

自定义元数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/-dgjYkZsRAqYVVIe7LCpuw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=0024D054A36CF122A118AD09C3301C551B4D61891C5A46F897C5364DFD21F9CF)

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[Metadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-metadata)替代。

#### CustomizeData(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/wJW4L3OISV-Yh0X_vNNJrg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=822C8C70649FB8A6B160BAACC9880F463E6888A65CBDAAEEB9D275B59745A525)

从API version 7开始支持，从API version 9开始废弃，建议使用[Metadata](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-metadata#metadata-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 否 | 否 | 标识自定义数据项的键名称。 |
| value | string | 否 | 否 | 标识自定义数据项的值名称。 |
| extra8+ | string | 否 | 否 | 标识用户自定义数据格式，标签值为标识该数据的资源的索引值。 |
