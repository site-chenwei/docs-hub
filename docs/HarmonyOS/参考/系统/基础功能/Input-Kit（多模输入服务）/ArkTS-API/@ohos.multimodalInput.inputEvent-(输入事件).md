---
title: "@ohos.multimodalInput.inputEvent (输入事件)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputevent"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Input Kit（多模输入服务）"
  - "ArkTS API"
  - "@ohos.multimodalInput.inputEvent (输入事件)"
captured_at: "2026-04-17T01:48:30.520Z"
---

# @ohos.multimodalInput.inputEvent (输入事件)

设备上报的基本事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/qDtE0kMcTa6qlmG4AkWlIg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014832Z&HW-CC-Expire=86400&HW-CC-Sign=5E30EE30EB0CDF443EF0A22F103656CC724F21D17D092482DD6779F329CDC179)

-   本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 导入模块

```js
import { InputEvent } from '@kit.InputKit';
```

#### InputEvent

输入事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.MultimodalInput.Input.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| id | number | 否 | 否 | 事件ID。 |
| deviceId | number | 否 | 否 | 输入设备的唯一标识，同一个物理设备反复插拔或重启，设备ID可能会发生变化。 |
| actionTime | number | 否 | 否 | 上报输入事件的时间。 |
| screenId | number | 否 | 否 | 目标屏幕ID。 |
| windowId | number | 否 | 否 | 目标窗口ID。 |
