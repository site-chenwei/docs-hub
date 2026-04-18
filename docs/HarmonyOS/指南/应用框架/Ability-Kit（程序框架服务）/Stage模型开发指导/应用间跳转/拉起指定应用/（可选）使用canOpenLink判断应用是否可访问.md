---
title: "（可选）使用canOpenLink判断应用是否可访问"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/canopenlink"
menu_path:
  - "指南"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "Stage模型开发指导"
  - "应用间跳转"
  - "拉起指定应用"
  - "（可选）使用canOpenLink判断应用是否可访问"
captured_at: "2026-04-17T01:35:31.964Z"
---

# （可选）使用canOpenLink判断应用是否可访问

#### 使用场景

在应用A想要拉起应用B的场景中，应用A可先调用canOpenLink接口判断应用B是否可访问，如果可访问，再拉起应用B。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/nZJH-2qMRWuypl5mK6tbYQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013532Z&HW-CC-Expire=86400&HW-CC-Sign=0A1DECD21CB3B692BF5D8995D484B48401C0A56B2940C6FC899B72C35E8B8FAC)

canOpenLink接口不支持判断以App Linking方式跳转的目标应用是否可访问。

#### 约束限制

在entry模块的module.json5文件中的[querySchemes](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)字段中，从API version 21开始，最多允许配置200个URL scheme。API version 20及之前的版本，最多允许配置50个URL scheme。

#### 接口说明

canOpenLink是[bundleManager](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-bundlemanager#bundlemanagercanopenlink12)提供的支持判断目标应用是否可访问的接口。

匹配规则请参考[显式Want与隐式Want匹配规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/explicit-implicit-want-mappings)。

#### 操作步骤

#### \[h2\]调用方操作步骤

1.  在entry模块的module.json5文件中配置[querySchemes](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)属性，声明想要查询的URL scheme。
    
    ```json5
    {
      "module": {
        //...
        "querySchemes": [
          "app1Scheme"
        ]
      }
    }
    ```
    
2.  导入ohos.bundle.bundleManager模块。
    
3.  调用canOpenLink接口。
    
    ```ts
    import { bundleManager } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    try {
      let link = 'app1Scheme://test.example.com/home';
      let canOpen = bundleManager.canOpenLink(link);
      hilog.info(0x0000, 'testTag', 'canOpenLink successfully: %{public}s', JSON.stringify(canOpen));
    } catch (err) {
      let message = (err as BusinessError).message;
      hilog.error(0x0000, 'testTag', 'canOpenLink failed: %{public}s', message);
    }
    ```
    

#### \[h2\]目标方操作步骤

在module.json5文件中配置[uris](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file#skills标签)属性。

```json5
{
  "module": {
    //...
    "abilities": [
      {
        //...
        "skills": [
          {
            // actions不能为空，actions为空会造成目标方匹配失败
            "actions": [
              "ohos.want.action.home"
            ],
            "uris": [
              {
                "scheme": "app1Scheme",
                "host": "test.example.com",
                "pathStartWith": "home"
              }
            ]
          }
        ]
      }
    ]
  }
}
```

#### FAQ

1.  为什么限制querySchemes中配置的URL scheme个数？
    
    canOpenLink()接口提供了判断应用是否可以访问的能力。通过该能力，应用可以间接获取到指定应用是否安装等信息。
    
    为了保护系统安全和用户隐私，避免恶意应用扫描应用安装列表等行为，要求开发者在使用canOpenLink()接口时必须配置querySchemes属性，从API version 21开始，最多允许配置200个URL scheme。API version 20及之前的版本，最多允许配置50个URL scheme。
