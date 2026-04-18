---
title: "安装VPN软件astrill后hdc访问不了设备"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-analysis-kit-68"
menu_path:
  - "FAQ"
  - "应用质量"
  - "技术质量"
  - "运维"
  - "安装VPN软件astrill后hdc访问不了设备"
captured_at: "2026-04-17T02:02:57.704Z"
---

# 安装VPN软件astrill后hdc访问不了设备

**问题现象**

hdc访问不了设备。hdc list targets -v出现unknown状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/5BjHRMi0TNas6rHnGfL3Ww/zh-cn_image_0000002474863621.png?HW-CC-KV=V1&HW-CC-Date=20260417T020259Z&HW-CC-Expire=86400&HW-CC-Sign=D87323CE8C30BCCAA70D48CA83BD9286C9E4B4EE8C04DAE2DBDFB48AC623ECA6)

查看hdc.log日志

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/Sfc9pFGTT7apbtmjYPwyzw/zh-cn_image_0000002474943789.png?HW-CC-KV=V1&HW-CC-Date=20260417T020259Z&HW-CC-Expire=86400&HW-CC-Sign=7CF367C23E7A31E93D702B972976FEC8DECEF84DDCC8BA7626883D0971A337E6)

**可能原因**

系统兼容问题。在win10上安装vpn工具astrill后，会导致出现这样问题。

**解决措施**

-   当前版本hdc建议卸载掉vpn软件，注意不是停掉vpn，而是卸载vpn。
-   参考[hdc版本配套表](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hdc#hdc版本配套表)升级最新版本后重试。
