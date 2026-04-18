---
title: "DevEco如何配置不响应raise捕获到的assert信号"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-57"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "DevEco如何配置不响应raise捕获到的assert信号"
captured_at: "2026-04-17T02:03:24.821Z"
---

# DevEco如何配置不响应raise捕获到的assert信号

在DevEco Studio RUN/Debug Configurations中的Edit Configurations > Debugger > LLDB Post Attach Commands，添加配置：process handle -p false -s false -n false signal。其中，signal为assert发送的信号。详细步骤如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/T0EVxfW4Tzu3Ua5h580w9Q/zh-cn_image_0000002194158524.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=5F306AD0F042241462A40EC4474DEC7465C26FA89D251AE0AB6198628DE79340)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Y65ndVp3SDKP0U9j828DQA/zh-cn_image_0000002229603925.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=97A5ADA07F6DA8A9629C8E816FCFA33640C5B9E69CEC43548C488CBABB963397 "点击放大")
