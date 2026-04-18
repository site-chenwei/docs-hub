---
title: "OverlayModuleInfo"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager-overlaymoduleinfo"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "接口依赖的元素及定义"
  - "bundleManager"
  - "OverlayModuleInfo"
captured_at: "2026-04-17T01:47:47.987Z"
---

# OverlayModuleInfo

OverlayModuleInfo信息，可以通过[overlay.getOverlayModuleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-overlay#overlaygetoverlaymoduleinfo)接口获取当前应用中具有overlay特征模块的OverlayModuleInfo信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/Ml-eC7QzQ9a4WHI9SCmwQQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=0DB757DCD22641BE0B3F55818F1AD3483B60669F8DDC32BE8CA7C4A5EAC0D03F)

本模块首批接口从API version 10 开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { overlay } from '@kit.AbilityKit';
```

#### OverlayModuleInfo

**系统能力：** SystemCapability.BundleManager.BundleFramework.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 否 | overlay特征module所属的应用的bundle名称。 |
| moduleName | string | 是 | 否 | overlay特征module的名称。 |
| targetModuleName | string | 是 | 否 | overlay特征指定的目标module的名称，表示当前overlay包的资源需要替换生效的模块名称。 |
| priority | number | 是 | 否 | overlay特征module的优先级。取值为整数，取值范围1 ~ 100，数值越大优先级越高。 |
| state | number | 是 | 否 | overlay特征module的[禁用使能状态](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-overlay#overlaysetoverlayenabled)。0代表禁用状态，1代表使能状态。 |
