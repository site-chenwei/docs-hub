---
title: "安装HAP时提示“error: unlock screen failed in developer mode”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-39"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "安装HAP时提示“error: unlock screen failed in developer mode”"
captured_at: "2026-04-17T02:03:24.563Z"
---

# 安装HAP时提示“error: unlock screen failed in developer mode”

**问题现象**

在启动调试或运行应用/服务时，如果安装HAP失败并显示“error: failed to start ability. error: unlock screen failed in developer mode”错误信息，表示在开发者模式下未能成功解锁屏幕。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ujkFIdkVRUiVDL89RrupPw/zh-cn_image_0000002194317996.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=CDF9E2CCDA0DF53CEE56FC755F5F1880A3A80D8F137B6A810647E434DB5E3462 "点击放大")

**解决措施**

该问题的原因是在锁屏状态下，设备设置了锁屏密码，导致应用无法正常启动。

-   方法一：通过设置显示和亮度中的屏幕休眠选项，延长自动休眠时间。
-   方法二：应用开发时，可不设置锁屏密码。应用启动时，设备将自动亮屏并启动应用。
