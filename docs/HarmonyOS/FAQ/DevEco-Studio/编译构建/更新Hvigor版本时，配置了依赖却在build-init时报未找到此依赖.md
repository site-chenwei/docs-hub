---
title: "更新Hvigor版本时，配置了依赖却在build init时报未找到此依赖"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-35"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "更新Hvigor版本时，配置了依赖却在build init时报未找到此依赖"
captured_at: "2026-04-17T02:03:21.452Z"
---

# 更新Hvigor版本时，配置了依赖却在build init时报未找到此依赖

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/lTfVfWmzQHmr5QrnIRbZNg/zh-cn_image_0000002194158852.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=B12098740103D67712BD9163508954C6CA9C75194E1183BA5793E29287FC923F)

**解决措施**

出现该问题的原因是工程中使用了3.3.0及后续版本的Hvigor，但Hvigor-wrapper.js版本较旧，两者不兼容。不兼容的场景包括：

-   场景一：使用4.0 Canary2之前的DevEco Studio时，同步只会下载Hvigor，不会下载dependencies下的内容（即hvigor-ohos-plugin）。如果需要更新Hvigor版本且不更新DevEco Studio，只能下载Hvigor，无法下载hvigor-ohos-plugin。建议更新至DevEco Studio NEXT Developer Preview1及以上版本
-   场景二：对于4.0 Beta1之前的DevEco Studio创建的工程，需要更新Hvigor版本。使用DevEco Studio NEXT Developer Preview1及以上版本的DevEco Studio打开历史工程，修改hvigor-config.json5中的Hvigor和plugin版本号，然后Sync。同步时会提示更新，点击按钮后将自动完成Hvigor和plugin的下载。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/cAgfxCOsQO69EQf91OX-uA/zh-cn_image_0000002229758729.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=6E812FAE0E50A8ADD15DD75AABB7AD0A99ED76885500343D4B578A8C5179F08C)
