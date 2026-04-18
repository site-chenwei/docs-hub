---
title: "并行编译多个大型Hap/Hsp模块可能会导致DevEco Studio闪退"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-193"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "并行编译多个大型Hap/Hsp模块可能会导致DevEco Studio闪退"
captured_at: "2026-04-17T02:03:23.479Z"
---

# 并行编译多个大型Hap/Hsp模块可能会导致DevEco Studio闪退

**问题现象**

当应用包含了多个Hap/Hsp，每个模块的代码量都是100万行级别，直接点击DevEco Studio的构建（点击Build然后点击Build Hap(s)/APP(s)）之后DevEco Studio工具出现闪退。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/bK6wwoS0TQGrmOIgqK80rw/zh-cn_image_0000002515675178.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=703C43A44EB6947CD392DCCFC640021BE99FF58B780FD47A723956F9605E1D07)

**可能原因**

单个模块代码量大于100万行时单模块编译消耗内存大于5G，4个以上的模块并行编译内存会达到20G导致系统内存不足。

**解决措施**

将并行编译改为串行编译执行。在DevEco Studio上依次选中每个模块再点击编译(左侧选中模块，然后点击Build,再点击第一个按钮Make Module 'xxx')。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/IXC399miQGml-IOujiSPiA/zh-cn_image_0000002515835104.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=02E963F846935E77DBF74ECAC3FF454452F03FFB8C74D03E07FC54C18C4C291E)
