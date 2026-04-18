---
title: "如何进行DevEco Studio编译构建初步性能分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-70"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何进行DevEco Studio编译构建初步性能分析"
captured_at: "2026-04-17T02:03:21.926Z"
---

# 如何进行DevEco Studio编译构建初步性能分析

Build Analyzer工具显示编译构建的重要信息，帮助开发者分析和排查性能问题。

构建完成后，通过以下方式打开Build Analyzer窗口：

-   在底部的工具栏区域，单击Build Analyzer窗口进行查看。
-   在左侧边栏单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/RNwQqRJZT9WO9yAY1hVsjw/zh-cn_image_0000002229758897.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=82E73327E3CA1F60C18B8776E4802CA0F45D76E3725C9BEAF84AE46B2C4AF59F)，打开Build Analyzer窗口。
-   完成构建后首次打开Build Analyzer时，窗口显示构建分析概览，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/CWeVxhTWRpKG3teeLhWW2Q/zh-cn_image_0000002229604409.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=8588D68F7ED41777D42CF2B4D87EC27471F1EC1E113DA58EF6021B578F07D594 "点击放大")

如需查看构建任务时间图谱，从下拉菜单中点击Tasks，默认进入时间图谱界面。该界面分块显示构建历史记录、构建任务时长图谱、构建日志及日志详情信息，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/sWFGLRn-T8yZhfaCoKIkFw/zh-cn_image_0000002194159012.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=94A16446BFCCBE66843E3EFED563E0B3DCDD3C3F47B2AD3C42A5FE22AFC65D44 "点击放大")

事件信息：

<table><tbody><tr><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>事件</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>子事件</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>业务</p></td></tr><tr><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>CompileResource</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>资源编译</p></td></tr><tr><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>PackageHap</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>打包工具</p></td></tr><tr><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>SignHap</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>签名工具</p></td></tr><tr><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>BuildNativeWithCmake</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>cpp编译工具链</p></td></tr><tr><td class="cellrowborder" rowspan="13" valign="top" width="33.333333333333336%"><p>CompileArkTS</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>watchChangedFiles</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>ArkUI</p></td></tr><tr><td class="cellrowborder" valign="top"><p>invalidCachePlugin</p></td><td class="cellrowborder" valign="top"><p>编译构建</p></td></tr><tr><td class="cellrowborder" valign="top"><p>oh-resolve</p></td><td class="cellrowborder" valign="top"><p>编译构建</p></td></tr><tr><td class="cellrowborder" valign="top"><p>moduleInfoMetaPlugin</p></td><td class="cellrowborder" valign="top"><p>编译构建</p></td></tr><tr><td class="cellrowborder" valign="top"><p>commonjs</p></td><td class="cellrowborder" valign="top"><p>编译构建</p></td></tr><tr><td class="cellrowborder" valign="top"><p>语言和类型编译器</p></td><td class="cellrowborder" valign="top"><p>ArkUI</p><p>语言和类型编译器</p></td></tr><tr><td class="cellrowborder" valign="top"><p>ArkUI</p></td><td class="cellrowborder" valign="top"><p>ArkUI</p></td></tr><tr><td class="cellrowborder" valign="top"><p>buildInstrument</p></td><td class="cellrowborder" valign="top"><p>测试框架</p></td></tr><tr><td class="cellrowborder" valign="top"><p>模块化，es2abc</p></td><td class="cellrowborder" valign="top"><p>模块化，es2abc</p><p>语言和类型编译器</p></td></tr><tr><td class="cellrowborder" valign="top"><p>编译构建</p></td><td class="cellrowborder" valign="top"><p>编译构建</p></td></tr><tr><td class="cellrowborder" valign="top"><p>编译构建</p></td><td class="cellrowborder" valign="top"><p>编译构建</p></td></tr><tr><td class="cellrowborder" valign="top"><p>ignorePlugin：编译构建工具</p></td><td class="cellrowborder" valign="top"><p>编译构建</p></td></tr><tr><td class="cellrowborder" valign="top"><p>api范式</p></td><td class="cellrowborder" valign="top"><p>api范式</p></td></tr><tr><td class="cellrowborder" valign="top" width="33.333333333333336%">&nbsp;&nbsp;</td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>commonPlugin：编译构建工具</p></td><td class="cellrowborder" valign="top" width="33.333333333333336%"><p>编译构建</p></td></tr></tbody></table>

参考链接：

[分析构建性能](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-analyzer)
