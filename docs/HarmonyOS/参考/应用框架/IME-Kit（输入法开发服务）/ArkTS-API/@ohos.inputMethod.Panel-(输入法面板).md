---
title: "@ohos.inputMethod.Panel (输入法面板)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod-panel"
menu_path:
  - "参考"
  - "应用框架"
  - "IME Kit（输入法开发服务）"
  - "ArkTS API"
  - "@ohos.inputMethod.Panel (输入法面板)"
captured_at: "2026-04-17T01:48:15.187Z"
---

# @ohos.inputMethod.Panel (输入法面板)

本模块提供对输入法面板的属性管理。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/rrcSqsFxS2mZgddIpMAnyg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=5F17BADB71C665707619F0B5DA4808FA62BC381DD2DF993774D078207B61F22C)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```ts
import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';
```

#### PanelInfo

输入法面板属性信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| type | [PanelType](#paneltype) | 否 | 否 | 输入法面板类型。 |
| flag | [PanelFlag](#panelflag) | 否 | 是 | 
输入法面板状态类型。

\- 默认值为固定态。

\- 当前仅用于描述软键盘类型的面板的状态。

 |

#### PanelType

输入法面板类型枚举。

**系统能力**：SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| SOFT\_KEYBOARD | 0 | 软键盘类型。 |
| STATUS\_BAR | 1 | 状态栏类型。 |

#### PanelFlag

输入法面板状态类型枚举。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/sS9thTn7S2m59-JGG_U4-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014815Z&HW-CC-Expire=86400&HW-CC-Sign=63A92AC12289D91AFD43993E0F6677606419F9AE5F97511219E235649ECB1E41)

目前仅用于SOFT\_KEYBOARD类型的面板。

**系统能力**：SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| FLAG\_FIXED | 0 | 固定态面板类型。 |
| FLAG\_FLOATING | 1 | 悬浮态面板类型。 |
| FLAG\_CANDIDATE | 2 | 
候选词态面板类型。

\- 当输入面板为候选词态时，面板为显示用户输入候选词的窗口。

\- 输入法服务不会主动控制候选词态面板的显示和隐藏，需要开发者根据情况自行控制。

 |
