---
title: "编译报错“Only one default card can be configured in the form_config.json file”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-39"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Only one default card can be configured in the form_config.json file”"
captured_at: "2026-04-17T02:03:21.543Z"
---

# 编译报错“Only one default card can be configured in the form\_config.json file”

**问题现象**

DevEco Studio编译失败。提示：Only one default card can be configured in the form\_config.json file。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/U3283P9wTxO-hBSoGKyVZg/zh-cn_image_0000002229758657.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=C25C0FBA5F43AC9CD511FAF1475C9070A71A258458B4DFBD51CC16F0BDCC8E39 "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview2版本开始，新增规则：卡片的配置文件中isDefault不可缺省。每个UIAbility有且只有一个默认卡片。

**解决措施**

进入对应module.json5文件，选择唯一默认卡片。将其他卡片的isDefault字段设置为false。
