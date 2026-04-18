---
title: "如何获取App版本号，版本名，屏幕分辨率等信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-71"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "如何获取App版本号，版本名，屏幕分辨率等信息"
captured_at: "2026-04-17T02:02:59.066Z"
---

# 如何获取App版本号，版本名，屏幕分辨率等信息

1.  通过@kit.AbilityKit中的bundleManager模块查询bundleInfo，其中包含App版本号和版本名。
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { bundleManager } from '@kit.AbilityKit';
    
    // ...
    bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION).then((bundleInfo) => {
      let versionName = bundleInfo.versionName; //App version name
      let versionNo = bundleInfo.versionCode; //App version code
    }).catch((error: BusinessError) => {
      console.error('get bundleInfo failed, error is ' + error);
    })
    
2.  在context.config中获取screenDensity，其中包含屏幕分辨率信息。
    
    import { common } from '@kit.AbilityKit';
    
    // ...
    // In the utility class: Save the context to AppStorage in the EntryAbility - onCreate lifecycle, then use AppStorage to retrieve it in the utility class
    let context = AppStorage.get('context') as common.UIAbilityContext;
    
    let screenDensity = context.config.screenDensity;
