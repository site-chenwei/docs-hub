---
title: "@system.package (应用管理)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-system-package"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@system.package (应用管理)"
captured_at: "2026-04-17T01:47:48.216Z"
---

# @system.package (应用管理)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/TzufCqJlR0WkgIkqTxuMOQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=7CFFD7ADA92F2C26425189EBB821BB723AEC5EECECDB4949A04B1E2C68C71106)

-   从API version 9开始不再维护，推荐使用该模块[@ohos.bundle.bundleManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager)。
    
-   本模块首批接口从API version 3开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    

#### 导入模块

```ts
import Package from '@system.package';
```

#### package.hasInstalled(deprecated)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/swi7TtLRRYS-rm9mo0GsjQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=A083CB81EB2AE3EBCAD2B34177565BA8D2FDA1D43BA0D16CF3A50768E8A25568)

从API version 3开始支持，从API version 9开始废弃，建议使用[getBundleInfo](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagergetbundleinfo14)替代。

hasInstalled(options: CheckPackageHasInstalledOptions): void

查询指定应用是否存在，或者原生应用是否安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| options | [CheckPackageHasInstalledOptions](#checkpackagehasinstalledoptions) | 是 | 选项参数。 |

**示例：**

```ts
import Package from '@system.package';

@Entry
@Component
struct MainPage {
  hasInstalled() {
    Package.hasInstalled({
      bundleName: 'com.example.bundlename',
      success: (data) => {
        console.log('package has installed: ' + data);
      },
      fail: (msg:string, code) => {
        console.log('query package fail, code: ' + code + ', data: ' + msg);
      },
    });
  }
  build() {
  }
}
```

#### CheckPackageHasInstalledResponse

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/7E_wubXrSq-_MT1pVthhuA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=E2B8436DCF129DCABF5A1DCFF709BDA14FB1377BE33B89E67DF6022703C91759)

从API version 3开始支持，从API version 9开始废弃。

指示应用包是否已安装。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| result | boolean | 是 | 指示应用是否已安装。 |

#### CheckPackageHasInstalledOptions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/gAI6HQFhR0mQbOXB2KiwyA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=F60EF3E13004BE6130D67486A320F9939E853AA5C7E7F834053296DFA16E148D)

从API version 3开始支持，从API version 9开始废弃。

查询包是否已安装时的选项。

**系统能力：** SystemCapability.BundleManager.BundleFramework

| 名称 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| bundleName | string | 是 | 应用Bundle名称。 |
| success | Function | 否 | 接口调用成功的回调函数。 |
| fail | Function | 否 | 接口调用失败的回调函数。 |
| complete | Function | 否 | 接口调用结束的回调函数。 |
