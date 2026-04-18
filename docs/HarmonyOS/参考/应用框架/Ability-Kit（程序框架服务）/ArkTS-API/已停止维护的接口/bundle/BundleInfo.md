---
title: "BundleInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-bundleinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "bundle"
  - "BundleInfo"
captured_at: "2026-04-17T01:47:48.343Z"
---

# BundleInfo

应用包的信息，通过[bundle.getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle#bundlegetbundleinfodeprecated)获取。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/QRHuozgBQ8iltWBhzddGOQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=E827FFD87C48605181B785237A87A3D8ED6380A73BEB8A7EA6DFABC657FA5182)

本模块首批接口从API version 7 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

从API version 9开始，该模块不再维护，建议使用[bundleManager-BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo)替代。

#### BundleInfo(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/wOK9dQ6DTV-LDbZADMcGrA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=58FD39F9A93D4FD18909ADE822660073A0648AFBC5373152F3E63AB89D0F45AE)

从API version 7开始支持，从API version 9开始废弃，建议使用[bundleManager-BundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo#bundleinfo-1)替代。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 是 | 否 | 应用包的名称。 |
| type | string | 是 | 否 | 应用包类型。 |
| appId | string | 是 | 否 | 应用包里应用程序的id。 |
| uid | number | 是 | 否 | 应用包里应用程序的uid。 |
| installTime | number | 是 | 否 | HAP安装时间，单位：毫秒。 |
| updateTime | number | 是 | 否 | HAP更新时间，单位：毫秒。 |
| appInfo | [ApplicationInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-applicationinfo) | 是 | 否 | 应用程序的配置信息。 |
| abilityInfos | Array<[AbilityInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-abilityinfo)\> | 是 | 否 | 
Ability的配置信息

通过调用[bundle.getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle#bundlegetbundleinfodeprecated)接口时，传入GET\_BUNDLE\_WITH\_ABILITIES获取。

 |
| reqPermissions | Array<string> | 是 | 否 | 

应用运行时需向系统申请的权限集合

通过调用[bundle.getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle#bundlegetbundleinfodeprecated)接口时，传入GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION获取。

 |
| reqPermissionDetails | Array<[ReqPermissionDetail](#reqpermissiondetaildeprecated)\> | 是 | 否 | 

应用运行时需向系统申请的权限集合的详细信息

通过调用[bundle.getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle#bundlegetbundleinfodeprecated)接口时，传入GET\_BUNDLE\_WITH\_REQUESTED\_PERMISSION获取。

 |
| vendor | string | 是 | 否 | 应用包的供应商。 |
| versionCode | number | 是 | 否 | 应用包的版本号。 |
| versionName | string | 是 | 否 | 应用包的版本文本描述信息。 |
| compatibleVersion | number | 是 | 否 | 运行应用包所需要最低的SDK版本号。 |
| targetVersion | number | 是 | 否 | 运行应用包所需要最高SDK版本号。 |
| isCompressNativeLibs | boolean | 是 | 否 | 是否压缩应用包的本地库，取值为true表示压缩应用包的本地库，取值为false表示不压缩应用包的本地库。 |
| hapModuleInfos | Array<[HapModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundle-hapmoduleinfo)\> | 是 | 否 | 模块的配置信息。 |
| entryModuleName | string | 是 | 否 | Entry的模块名称。 |
| cpuAbi | string | 是 | 否 | 应用包的cpuAbi信息。 |
| isSilentInstallation | string | 是 | 否 | 是否通过静默安装。 |
| minCompatibleVersionCode | number | 是 | 否 | 分布式场景下的应用包兼容的最低版本。 |
| entryInstallationFree | boolean | 是 | 否 | Entry是否支持免安装，取值为true表示支持免安装，取值为false表示不支持免安装。 |
| reqPermissionStates8+ | Array<number> | 是 | 否 | 申请权限的授予状态。0表示申请成功，-1表示申请失败。 |

#### ReqPermissionDetail(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/X2GCyhAPRP22s0B8U6zX7w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=46A6D15BDE38EE5A25AE4881965DB03F74194781D0FAB072800C9ABFDF1ADCCE)

从API version 7开始支持，从API version 9开始废弃，建议使用[ReqPermissionDetail](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo#reqpermissiondetail)替代。

应用运行时需向系统申请的权限集合的详细信息。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| name | string | 否 | 否 | 需要使用的权限名称。 |
| reason | string | 否 | 否 | 描述申请权限的原因。 |
| usedScene | [UsedScene](#usedscenedeprecated) | 否 | 否 | 权限使用的场景和时机。 |

#### UsedScene(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/DM7qI3eHTcKvnwswMCIDmw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014750Z&HW-CC-Expire=86400&HW-CC-Sign=990435C3B31207BE047C9C312CEA7237C95FC9D90EB54F948DDD14F0B0F8CFE6)

从API version 7开始支持，从API version 9开始废弃，建议使用[UsedScene](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-bundleinfo#usedscene)替代。

描述权限使用的场景和时机。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| abilities | Array<string> | 否 | 否 | 使用到该权限的Ability集合。 |
| when | string | 否 | 否 | 使用该权限的时机。 |
