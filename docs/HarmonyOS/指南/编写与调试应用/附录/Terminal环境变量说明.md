---
title: "Terminal环境变量说明"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-variable"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "附录"
  - "Terminal环境变量说明"
captured_at: "2026-04-17T01:36:50.451Z"
---

# Terminal环境变量说明

在DevEco Studio的Terminal中执行hvigor、ohpm等命令时，默认使用内置的环境变量，无需额外配置。

DevEco Studio内置环境变量的设置方式如下：

点击菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings** ） **> Tools > Terminal**，勾选以下选项表示开启内置环境变量。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/a6imRvE0TZqXGXspOx5veg/zh-cn_image_0000002533959996.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=D73C373EDBC463BBD13A665336EDB464B1436BA7706D5FA082CFD58EF28A0EF4)

除了内置的环境变量外，开发者也可以在本地系统中配置PATH环境变量。如果同时配置了内置环境变量和本地系统环境变量，两者存在优先级关系，实际生效的环境变量如下。

-   DevEco Studio 6.0.2 Release（6.0.2.650）及以上版本：内置环境变量生效。
-   DevEco Studio 6.0.2 Release（6.0.2.650）之前的版本：
    -   Windows：内置环境变量生效。
    -   macOS：本地系统环境变量生效。
