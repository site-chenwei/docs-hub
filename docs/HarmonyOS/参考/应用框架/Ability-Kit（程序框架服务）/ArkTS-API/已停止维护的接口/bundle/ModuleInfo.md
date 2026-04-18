---
title: "ModuleInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-moduleinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "bundle"
  - "ModuleInfo"
captured_at: "2026-04-17T01:47:48.385Z"
---

# ModuleInfo

应用程序的模块信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/crDIbzQmQZmCjrdWWIw0lQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=58990827465E5FAAECD6A2CCBA29B9B93F7DB3A8B5FB8AF0FF6A05A5C027E14D)

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo)替代。

#### ModuleInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/nZOWj7KzSfWK21YNiLr94w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=E6BF14EDFFBD2FDE5C45C6E207019D567E7CE122E914B1A5FF391BA916857043)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-hapmoduleinfo#hapmoduleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| moduleName | string | 是 | 否 | 模块名称。 |
| moduleSourceDir | string | 是 | 否 | 安装目录。不能拼接路径访问资源文件，请使用[资源管理接口](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-resource-manager)访问资源。 |
