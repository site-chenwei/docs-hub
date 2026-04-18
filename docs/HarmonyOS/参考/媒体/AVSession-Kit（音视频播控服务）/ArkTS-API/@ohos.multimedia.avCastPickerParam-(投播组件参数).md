---
title: "@ohos.multimedia.avCastPickerParam (投播组件参数)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-avcastpickerparam"
menu_path:
  - "参考"
  - "媒体"
  - "AVSession Kit（音视频播控服务）"
  - "ArkTS API"
  - "@ohos.multimedia.avCastPickerParam (投播组件参数)"
captured_at: "2026-04-17T01:48:37.962Z"
---

# @ohos.multimedia.avCastPickerParam (投播组件参数)

avCastPickerParam提供了[@ohos.multimedia.avCastPicker](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ohos-multimedia-avcastpicker)组件状态枚举值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/qhvzxDxLQwSgTGzzEsnkpQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014839Z&HW-CC-Expire=86400&HW-CC-Sign=E317BC401622B8D0920847D1D333ABED184392452BD11B3A1458930471B63318)

本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### AVCastPickerState

投播组件设备列表状态参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STATE\_APPEARING | 0 | 组件显示。 |
| STATE\_DISAPPEARING | 1 | 组件消失。 |

#### AVCastPickerStyle12+

投播组件样式参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| STYLE\_PANEL | 0 | 面板样式。 |
| STYLE\_MENU | 1 | 菜单样式。 |

#### AVCastPickerColorMode12+

投播组件显示模式参数选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVCast

| 名称 | 值 | 说明 |
| :-- | :-- | :-- |
| AUTO | 0 | 跟随系统模式。 |
| DARK | 1 | 深色模式。 |
| LIGHT | 2 | 浅色模式。 |
