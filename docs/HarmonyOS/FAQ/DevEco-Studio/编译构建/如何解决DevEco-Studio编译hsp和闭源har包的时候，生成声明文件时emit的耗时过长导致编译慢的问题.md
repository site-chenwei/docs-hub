---
title: "如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-71"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题"
captured_at: "2026-04-17T02:03:22.003Z"
---

# 如何解决DevEco Studio编译hsp和闭源har包的时候，生成声明文件时emit的耗时过长导致编译慢的问题

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/DkiWsgefTIuFOAOXy4K-Yw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=D9F8703E5F2E3F1F6CAA766DDBB2F918380ADBA363AF9996EEA8A9C41346AE14)

注：此方法为临时规避方案，后续将修复该问题，建议仅在阻塞时使用。

用于减少编译HSP和闭源HAR包时生成声明文件的耗时。

修改 ets\_checker.js 文件（文件路径：SDK路径\\default\\base\\ets\\build-tools\\ets-loader\\lib\\ets\_checker.js），编辑 processBuildHap 函数。

1.  生成 sourceFile，在遍历文件时生成声明文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/aHhMneAvSFiokEMhRfQfNQ/zh-cn_image_0000002229603953.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=902C96F871044020723A1EDB7C0404E88BFAB26FBB80002AE8F58CC594909135 "点击放大")
    
2.  修改 getEmitOutput 函数，将其改为 getFileEmitOutput 函数，以获取声明文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/C7RKZsqGTr-Fwk_Qo8iljQ/zh-cn_image_0000002194318168.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=04ADC32EB78FFA070A284CD5A20FF53110E4CA5A3C4F0A10C72F0876262C119D "点击放大")
