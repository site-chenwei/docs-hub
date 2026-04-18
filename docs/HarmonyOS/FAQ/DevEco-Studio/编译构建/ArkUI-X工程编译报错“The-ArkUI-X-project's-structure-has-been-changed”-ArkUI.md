---
title: "ArkUI"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-28"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”"
captured_at: "2026-04-17T02:03:21.351Z"
---

# ArkUI-X工程编译报错“The ArkUI-X project's structure has been changed”

**问题现象**

使用DevEco Studio 4.0.0.700及以上版本打开ArkUI-X历史工程时，工程同步或构建会提示“ERROR: The ArkUI-X project's structure has been changed. Migrate and adapt the project as instructed in FAQs.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/P83HdKrLSjaGrowMhfKeHA/zh-cn_image_0000002194158592.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=6602A972408523DBE2BBDCA96A721EFFC0FCF8138580F395C1675D54197D9404)

**解决措施**

出现该提示的原因是在旧版本的ArkUI-X工程模板中，ArkUI-X工程标识（"crossplatform": true）配置在工程目录下build-profile.json5中，在DevEco Studio 4.0.0.700及以上版本需要在工程目录下.arkui-x/arkui-x-config.json5文件中配置ArkUI-X工程模块、工程标识等信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/BusQF-D7RIq59j4r84VSCw/zh-cn_image_0000002229758465.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=FD7B9A1D57711DE6322BA3DB06EE8823EAE914ACEF64F3F293E41D878C6D33D9)

配置位置变更后，使用历史工程模板的开发者，如果使用DevEco Studio 4.0.0.700及以上版本，需手动迁移适配新的工程结构。迁移步骤如下：

1.  删除工程目录下build-profile.json5中的ArkUI-X工程标识（"crossplatform": true）。
2.  在工程下.arkui-x目录中新建arkui-x-config.json5文件，配置内容为 "crossplatform": true, "modules"中配置工程中所有ArkUI-X模块的module name。
    
    工程迁移后结构如下：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/MODfdOHkRLm3qRQNgOV1KA/zh-cn_image_0000002229758461.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=74C15ACE63690AF0C848A5CEF810BF3FEE8A878339331DE0043B1B5976E896B2)
    
3.  迁移完成后，点击菜单栏 File > Sync and Refresh Project 同步工程，然后重新编译构建。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/fgxR2IBtR5uQirWA6b5dSA/zh-cn_image_0000002229603993.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=09A47E33F87D4C071AFCECA06C7AFF41FD0E74B1CE1471020F52095F58B8F10C)
