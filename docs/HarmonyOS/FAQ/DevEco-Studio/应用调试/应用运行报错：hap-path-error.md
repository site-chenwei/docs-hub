---
title: "应用运行报错：hap path error"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-55"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "应用运行报错：hap path error"
captured_at: "2026-04-17T02:03:24.820Z"
---

# 应用运行报错：hap path error

**问题现象**

启动调试或运行应用/服务时，应用运行崩溃，提示错误信息“errorMsg: hap path error”。

**解决措施**

如果依赖的应用包未安装，建议进入**Run/Debug Configurations > Deploy Multi Hap****/Hsp**页签，勾选**Deploy Multi Hap/Hsp Packages**，选择所需依赖的应用包，然后重新运行应用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/uut_d2DjQF-c6PoJk-P7Sg/zh-cn_image_0000002487797922.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=B4E085E8993842EFE165E8168B40F25C8C8016C798F2E9AFEECD12CC98726E1D)
