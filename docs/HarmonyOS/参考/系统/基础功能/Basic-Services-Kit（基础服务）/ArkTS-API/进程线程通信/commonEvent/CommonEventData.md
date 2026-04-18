---
title: "CommonEventData"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventdata"
menu_path:
  - "参考"
  - "系统"
  - "基础功能"
  - "Basic Services Kit（基础服务）"
  - "ArkTS API"
  - "进程线程通信"
  - "commonEvent"
  - "CommonEventData"
captured_at: "2026-04-17T01:48:28.133Z"
---

# CommonEventData

表示公共事件的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/rbpvgJDpSa6Y6L8rrTi5sQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014829Z&HW-CC-Expire=86400&HW-CC-Sign=4CCF5187C5E7CF2728880EB3D172B275311659325909768423D9522FCFA1A71B)

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### 属性

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Notification.CommonEvent

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| event | string | 否 | 否 | 表示当前接收的公共事件名称。 |
| bundleName | string | 否 | 是 | 表示包名称，默认为空字符串。 |
| code | number | 否 | 是 | 表示订阅者接收到的公共事件数据（number类型）。该字段取值与发布者使用[commonEventManager.publish](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagerpublish-1)发布公共事件时，通过[CommonEventPublishData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata)中的code字段传递的数据一致。默认值为0。 |
| data | string | 否 | 是 | 表示订阅者接收到的公共事件数据（string类型）。该字段取值与发布者使用[commonEventManager.publish](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagerpublish-1)发布公共事件时，通过[CommonEventPublishData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata)中的data字段传递的数据一致。 |
| parameters | {\[key: string\]: any} | 否 | 是 | 表示订阅者接收到的公共事件的附加信息。该字段取值与发布者使用[commonEventManager.publish](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-commoneventmanager#commoneventmanagerpublish-1)发布公共事件时，通过[CommonEventPublishData](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-commonevent-commoneventpublishdata)中的parameters字段传递的数据一致。 |
