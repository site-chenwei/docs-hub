---
title: "编译报错“Invalid form name 'xxx'.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-146"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Invalid form name 'xxx'.”"
captured_at: "2026-04-17T02:03:22.937Z"
---

# 编译报错“Invalid form name 'xxx'.”

**错误描述**

卡片名称无效。

**可能原因**

在insight\_intent.json中配置意图框架时，formName必须是form\_config.json中已配置的forms之一。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/gWlskKVvR9uhiOrP-ZBGaw/zh-cn_image_0000002194158436.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=61B4273CF4D51986D3E0283A7807AA85048C2D8C6AEC838A670718E4B9712E38 "点击放大")

**解决措施**

修改insight\_intent.json中的 form 配置，确保formName已在form\_config.json文件的 forms 中配置。
