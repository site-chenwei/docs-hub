---
title: "ArkTS卡片界面开发概述"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-widget-page-overview"
menu_path:
  - "指南"
  - "应用框架"
  - "Form Kit（卡片开发服务）"
  - "ArkTS卡片开发（推荐）"
  - "ArkTS卡片提供方开发指导"
  - "ArkTS卡片UI界面开发"
  - "ArkTS卡片界面开发概述"
captured_at: "2026-04-17T01:35:44.156Z"
---

# ArkTS卡片界面开发概述

ArkTS卡片开发采用通用[ArkTS语言](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/learning-arkts)，开发者可以使用[ArkTS声明式开发范式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-development-overview)开发ArkTS卡片页面。

如下卡片页面由DevEco Studio模板自动生成，开发者可以根据自身的业务场景进行调整。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/bykImaPJQHGwFTdgoVI5Og/zh-cn_image_0000002569018929.png?HW-CC-KV=V1&HW-CC-Date=20260417T013545Z&HW-CC-Expire=86400&HW-CC-Sign=E16A2E2CFAAA7C9B957EE60EFBFCCC4BDF74D7E3BE5EABC6368F350347921823)

#### ArkTS卡片支持的页面能力

ArkTS卡片具备JS卡片的全量能力，并且新增了动效能力和自定义绘制的能力，支持[ArkTS声明式开发范式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-ui-development-overview)的部分组件、事件、动效、数据管理、状态管理能力。

对于支持在ArkTS卡片UI界面中使用的接口，会添加“卡片能力”的标记，如：从API version 12开始，该接口支持在ArkTS卡片中使用。同时请留意卡片场景下的能力差异说明。

例如：以下说明表示CircleShape可在ArkTS卡片中使用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/6Y1YI4uwS2eEz5-XA5jbWQ/zh-cn_image_0000002568898919.png?HW-CC-KV=V1&HW-CC-Date=20260417T013545Z&HW-CC-Expire=86400&HW-CC-Sign=08577DF69EE41EAD7F4A3E50ADF947190CD8E9026841B21900993B6682C1CC4D)
