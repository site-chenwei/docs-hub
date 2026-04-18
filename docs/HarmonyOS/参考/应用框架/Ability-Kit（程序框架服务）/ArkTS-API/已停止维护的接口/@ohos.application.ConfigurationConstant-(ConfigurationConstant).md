---
title: "@ohos.application.ConfigurationConstant (ConfigurationConstant)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-configurationconstant"
menu_path:
  - "参考"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "ArkTS API"
  - "已停止维护的接口"
  - "@ohos.application.ConfigurationConstant (ConfigurationConstant)"
captured_at: "2026-04-17T01:47:48.185Z"
---

# @ohos.application.ConfigurationConstant (ConfigurationConstant)

ConfigurationConstant模块提供配置信息枚举值定义的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/EKeIBcfZT7CA1ZVnhZ5c6Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014749Z&HW-CC-Expire=86400&HW-CC-Sign=53432E57FE6FFCB62C12F876A8B3F9D36244A40559FC0758B187C556736EF0F9)

本模块首批接口从API version 8开始支持，从API version 9废弃，替换模块为[@ohos.app.ability.ConfigurationConstant (ConfigurationConstant)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-configurationconstant)。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import ConfigurationConstant from '@ohos.application.ConfigurationConstant';
```

#### ColorMode

表示颜色模式的枚举。

**系统能力**：SystemCapability.Ability.AbilityBase

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| COLOR\_MODE\_NOT\_SET | \-1 | 未设置颜色模式。 |
| COLOR\_MODE\_DARK | 0 | 深色模式。 |
| COLOR\_MODE\_LIGHT | 1 | 浅色模式。 |
