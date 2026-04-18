---
title: "DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-35"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”"
captured_at: "2026-04-17T02:03:24.741Z"
---

# DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: Error while Deploy Hap”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/fYKMuGMRTZaJCo-3IqC_dA/zh-cn_image_0000002215508376.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=F49E42A5DD103A3453F7C40B00A27CFD3F44CF80EB985ADD7C66EDA893264E07)

**解决措施**

使用真机场景：请更换数据线或PC侧USB接口后尝试。

使用模拟器场景：

-   在Local Emulator的设备列表窗口，点击“Wipe User Data”清除数据，启动模拟器并重新运行工程。
-   打开命令行工具，并进入DevEco Studio安装目录下的sdk\\default\\openharmony\\toolchains路径，执行 hdc kill -r 命令，启动模拟器，重新运行工程。
