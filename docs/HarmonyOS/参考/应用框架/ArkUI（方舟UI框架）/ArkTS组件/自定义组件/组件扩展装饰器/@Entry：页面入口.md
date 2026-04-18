---
title: "@Entry：页面入口"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-entry"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS组件"
  - "自定义组件"
  - "组件扩展装饰器"
  - "@Entry：页面入口"
captured_at: "2026-04-17T01:47:59.294Z"
---

# @Entry：页面入口

@Entry装饰的自定义组件将作为UI页面的入口。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/yAnJQBJhRHGJUJ8nz2GXkQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014801Z&HW-CC-Expire=86400&HW-CC-Sign=E0D2023C597A3841BD3C1961F8C85D0C7C1BF091958BB77BD0090992C196A97B)

本模块首批接口从API version 7开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

#### @Entry

在单个UI页面中，仅允许存在一个由@Entry装饰的自定义组件作为页面的入口。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```ts
@Entry
@Component
struct Index {
  build() {
    Text('@Entry Test')
  }
}
```

#### EntryOptions10+

命名路由跳转选项。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| :-- | :-- | :-- | :-- | :-- |
| routeName | string | 否 | 是 | 
表示作为命名路由页面的名字。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| storage | [LocalStorage](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-localstorage) | 否 | 是 | 

页面级的UI状态存储。当未传入时，框架会创建一个新的LocalStorage实例作为默认值。

**卡片能力：** 从API version 10开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

 |
| useSharedStorage12+ | boolean | 否 | 是 | 

是否使用[loadContent](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-window-windowstage#loadcontent9)传入的LocalStorage实例对象。默认值false。true：使用共享的LocalStorage实例对象。false：不使用共享的LocalStorage实例对象。

**卡片能力：** 从API version 12开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

 |

**示例：**

```ts
@Entry({ routeName: 'myPage' })
@Component
struct Index {
  build() {
    Text('Index')
  }
}
```
