---
title: "Hot Reload执行失败原因说明"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-21"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "Hot Reload执行失败原因说明"
captured_at: "2026-04-17T02:03:24.619Z"
---

# Hot Reload执行失败原因说明

**问题现象**

热重载执行结果失败，控制台打印蓝色重启链接：“Reloaded 1 files failed. Please reinstall and restart.”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/0c9rkRg4TEaFu24U4i08Fg/zh-cn_image_0000002194318548.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=57D125EDECE7484268B9A75D2A23CF6254D0794A292CEA37A78750EB1189075C "点击放大")

**解决措施**

热重载的最后一步是将补丁包安装到设备并执行quickfix命令。如果quickfix命令执行失败，热重载也会失败。

导致补丁包安装失败的原因可检查以下几个方面：

-   检查工程签名是否正确，热重载需要使用debug签名（不支持release签名），否则热重载将无法执行。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/bVHsBwXKR9u7CTuoUi92uw/zh-cn_image_0000002229604317.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=F36D3F35FECBD24F634C4AB671F62283946B3596548D8B2231DE86F21C31D0B4 "点击放大")
    
-   检查工程的Build Mode，热重载不支持release模式，支持debug和<None>。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/KHq1wcUgQUCE0K3ysIkWAg/zh-cn_image_0000002487886068.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=7E0BD414AABE300A8E64D3712ADA8BC78D19BBB7D546036336EB031BEE2E2D0D)
