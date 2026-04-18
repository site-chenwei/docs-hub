---
title: "StatusBarViewExtensionAbility（状态栏扩展Ability）"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/statusbar-extension-ability"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Desktop Extension Kit（桌面拓展服务）"
  - "ArkTS API"
  - "StatusBarViewExtensionAbility（状态栏扩展Ability）"
captured_at: "2026-04-17T01:48:29.818Z"
---

# StatusBarViewExtensionAbility（状态栏扩展Ability）

StatusBarViewExtensionAbility为状态栏扩展Ability，继承自[UIExtensionAbility](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-uiextensionability#uiextensionability)，用于给应用提供接入状态栏图标左键业务弹窗的能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/y1Xlg6OcTYSlco4THH0BtQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014831Z&HW-CC-Expire=86400&HW-CC-Sign=91AD9CC45FEF29355254BB1F5E83FF52674A3430A99C25776B0ACFAC1CA1142D)

本模块接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.StatusBarManager

**起始版本：** 5.0.0(12)

#### 导入模块

```typescript
import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
```

**示例：**

```typescript
import { StatusBarViewExtensionAbility } from '@kit.DeskTopExtensionKit';
import { UIExtensionContentSession, Want } from '@kit.AbilityKit';

let TAG = "MyStatusBarViewAbility";

export default class MyStatusBarViewAbility extends StatusBarViewExtensionAbility {
  onCreate() {
    console.info(TAG, `onCreate`);
  }

  onSessionCreate(want: Want, session: UIExtensionContentSession) {
    console.info(TAG, `onSessionCreate, want: ${want.abilityName}`);
    session.loadContent('pages/Index');
  }

  onForeground() {
    console.info(TAG, `onForeground`);
  }

  onBackground() {
    console.info(TAG, `onBackground`);
  }

  onSessionDestroy(session: UIExtensionContentSession) {
    console.info(TAG, `onSessionDestroy`);
  }

  onDestroy() {
    console.info(TAG, `onDestroy`);
  }
}
```
