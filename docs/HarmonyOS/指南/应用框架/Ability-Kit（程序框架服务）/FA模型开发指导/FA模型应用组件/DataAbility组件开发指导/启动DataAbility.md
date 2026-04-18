---
title: "启动DataAbility"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-dataability"
menu_path:
  - "指南"
  - "应用框架"
  - "Ability Kit（程序框架服务）"
  - "FA模型开发指导"
  - "FA模型应用组件"
  - "DataAbility组件开发指导"
  - "启动DataAbility"
captured_at: "2026-04-17T01:35:32.760Z"
---

# 启动DataAbility

启动DataAbility会获取一个工具接口类对象（DataAbilityHelper）。启动DataAbility的示例代码如下：

```ts
import featureAbility from '@ohos.ability.featureAbility';
import ability from '@ohos.ability.ability';

let uri: string = 'dataability:///com.samples.famodelabilitydevelop.DataAbility';
let DAHelper: ability.DataAbilityHelper = featureAbility.acquireDataAbilityHelper(uri);
```
