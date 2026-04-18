---
title: "Class (MediaQuery)"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-mediaquery"
menu_path:
  - "参考"
  - "应用框架"
  - "ArkUI（方舟UI框架）"
  - "ArkTS API"
  - "UI界面"
  - "@ohos.arkui.UIContext (UIContext)"
  - "Class (MediaQuery)"
captured_at: "2026-04-17T01:47:52.839Z"
---

# Class (MediaQuery)

提供根据不同媒体类型定义不同的样式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/PdVzhCkBTbakOx2NiQM0tA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T014754Z&HW-CC-Expire=86400&HW-CC-Sign=5A24AE3228269719D4856CE67088A9C6B4F337E1CFF7AF40BFAEF1E9050FB134)

-   本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
    
-   本Class首批接口从API version 10开始支持。
    
-   以下API需先使用UIContext中的[getMediaQuery()](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uicontext#getmediaquery)方法获取到MediaQuery对象，再通过该对象调用对应方法。
    

#### matchMediaSync

matchMediaSync(condition: string): mediaQuery.MediaQueryListener

设置媒体查询的查询条件，并返回对应的监听句柄。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| :-- | :-- | :-- | :-- |
| condition | string | 是 | 媒体事件的匹配条件，具体可参考[媒体查询语法规则](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-layout-development-media-query#语法规则)。 |

**返回值：**

| 类型 | 说明 |
| :-- | :-- |
| [mediaQuery.MediaQueryListener](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery#mediaquerylistener) | 媒体事件监听句柄，用于注册和去注册监听回调。 |

**示例：**

完整示例请参考[mediaquery示例](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-mediaquery#示例)。
