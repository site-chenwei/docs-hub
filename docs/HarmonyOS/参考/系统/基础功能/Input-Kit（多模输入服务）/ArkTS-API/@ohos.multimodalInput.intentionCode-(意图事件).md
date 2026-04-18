---
title: "@ohos.multimodalInput.intentionCode (意图事件)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-intentioncode"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "ArkTS API"
  - "@ohos.multimodalInput.intentionCode (意图事件)"
captured_at: "2026-04-17T01:48:30.563Z"
---

# @ohos.multimodalInput.intentionCode (意图事件)

将键盘输入设备的原始事件映射为归一化交互的意图事件，如键盘上空格键映射后的事件为INTENTION\_SELECT，意图为选中。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Ga3f3PSzQlWfqIOX5HWE9g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=30CAB393B2DDE68591C1F3C04DEE2C9CD97EA5548AD98D88F97BB759092ABFD4)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import { IntentionCode } from '@kit.InputKit';
```

#### IntentionCode

意图事件枚举值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| INTENTION\_UNKNOWN | \-1 | 未知意图 |
| INTENTION\_UP | 1 | 上 |
| INTENTION\_DOWN | 2 | 下 |
| INTENTION\_LEFT | 3 | 左 |
| INTENTION\_RIGHT | 4 | 右 |
| INTENTION\_SELECT | 5 | 选中 |
| INTENTION\_ESCAPE | 6 | 逃逸 |
| INTENTION\_BACK | 7 | 返回 |
| INTENTION\_FORWARD | 8 | 前进 |
| INTENTION\_MENU | 9 | 菜单 |
| INTENTION\_PAGE\_UP | 11 | 上一页 |
| INTENTION\_PAGE\_DOWN | 12 | 下一页 |
| INTENTION\_ZOOM\_OUT | 13 | 缩小键 |
| INTENTION\_ZOOM\_IN | 14 | 放大键 |
