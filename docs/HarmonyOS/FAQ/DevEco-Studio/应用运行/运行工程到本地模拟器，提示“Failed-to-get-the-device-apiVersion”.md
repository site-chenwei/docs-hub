---
title: "运行工程到本地模拟器，提示“Failed to get the device apiVersion”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-running-5"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用运行"
  - "运行工程到本地模拟器，提示“Failed to get the device apiVersion”"
captured_at: "2026-04-17T02:03:23.827Z"
---

# 运行工程到本地模拟器，提示“Failed to get the device apiVersion”

**问题现象**

本地模拟器启动后，运行工程到模拟器，提示“Failed to get the device apiVersion”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/TY584_sJQruAi2n00gxupQ/zh-cn_image_0000002194317932.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=A454D9E360C7F541FE6FA21D01D0ADE79E0C58FDB351F8B945E84A6CDB32201E)

**解决措施**

可以通过以下方法重新运行工程：

-   在**Local Emulator**的设备列表窗口，点击“Wipe User Data”清除模拟器数据，然后重新启动模拟器并运行工程。
-   打开命令行工具，进入HarmonyOS SDK安装目录下的 \`default/base/toolchains\` 路径，执行以下命令重启 hdc server：
    
    ```powershell
    ./hdc kill -r
    ```
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/fl8YYXuAQDqyAr1AV8a_SQ/zh-cn_image_0000002229758185.png?HW-CC-KV=V1&HW-CC-Date=20260417T020324Z&HW-CC-Expire=86400&HW-CC-Sign=581024D302675543B557163C70FCDAF24D6DBA699069338829BA3F2D64A9B06F)
