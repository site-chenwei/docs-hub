---
title: "macOS上活动监视器中显示模拟器内存偏高"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-23"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用运行"
  - "macOS上活动监视器中显示模拟器内存偏高"
captured_at: "2026-04-17T02:03:24.008Z"
---

# macOS上活动监视器中显示模拟器内存偏高

配置模拟器内存为4GB并使用一段时间后，在活动监视器中可能发现模拟器进程占用的内存超过6GB（如下图所示）。请注意，图中的6.49GB不代表模拟器进程实际使用的物理内存（即Dirty内存），而是指其占用的phys\_footprint内存。在Mac系统中，针对虚拟化平台（如模拟器），phys\_footprint内存通常远高于Dirty内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/r-KQeoIkRTSooYTlPpGs-Q/zh-cn_image_0000002229758733.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=0ACD25C088E47C0B2A998C52A90CA7AA0B2E6832E492F6C6F88D206B7AA7FCD8 "点击放大")

想要查看模拟器的Dirty内存，首先打开活动监视器，查看Emulator的进程号（PID）。然后通过 \`footprint -vmObjectDirty 进程号\` 命令可以查看Dirty内存大小。
