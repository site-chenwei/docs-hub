---
title: "StartAbilityParameter"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-ability-startabilityparameter"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "FA模型能力的接口"
  - "ability"
  - "StartAbilityParameter"
captured_at: "2026-04-17T01:47:46.848Z"
---

# StartAbilityParameter

定义启动Ability参数，可以作为入参，调用[startAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-ability-featureability#featureabilitystartability)启动指定的Ability。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/oz3uCutGRuCr7YJQZCvdTA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014748Z&HW-CC-Expire=86400&HW-CC-Sign=4A6AA340E07274FA1B05D2FE063F3ED1C798D4F38A254CF24EC8C782E5B053CF)

本接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

此接口仅可在FA模型下使用。

#### 导入模块

```ts
import ability from '@ohos.ability.ability';
```

#### 属性

**系统能力**：SystemCapability.Ability.AbilityRuntime.FAModel

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| want | [Want](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-want) | 否 | 否 | 启动Ability的want信息。 |
| abilityStartSetting | { \[key: string\]: any } | 否 | 是 | 启动Ability的特殊属性，当开发者启动Ability时，该属性可以作为调用中的输入参数传递。 |
| abilityStartSettings11+ | Record<string, Object> | 否 | 是 | 启动Ability的特殊属性，当开发者启动Ability时，该属性可以作为调用中的输入参数传递。推荐使用该属性替代abilityStartSetting，设置该属性后，abilityStartSetting不再生效。 |

**示例：**

```ts
import ability from '@ohos.ability.ability';
import featureAbility from '@ohos.ability.featureAbility';
import Want from '@ohos.app.ability.Want';

let want: Want = {
    bundleName: 'com.example.abilityStartSettingApp2',
    abilityName: 'com.example.abilityStartSettingApp.EntryAbility',
};

let startAbilityParameter: ability.StartAbilityParameter = {
    want : want,
    abilityStartSettings : {
        abilityBounds : [100,200,300,400],
        windowMode :
        featureAbility.AbilityWindowConfiguration.WINDOW_MODE_UNDEFINED,
        displayId : 1,
    }
};

try {
    featureAbility.startAbility(startAbilityParameter, (error, data) => {
        if (error && error.code !== 0) {
            console.error(`startAbility fail, error: ${JSON.stringify(error)}`);
        } else {
            console.info(`startAbility success, data: ${JSON.stringify(data)}`);
        }
    });
} catch(error) {
    console.error(`startAbility error: ${JSON.stringify(error)}`);
}
```
