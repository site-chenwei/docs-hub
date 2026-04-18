---
title: "编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-41"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime"
captured_at: "2026-04-17T02:03:21.578Z"
---

# 编译时DevEco Studio报错App Launch: To run and debug the Harmony device, configure the HarmonyOS runtime

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/dQ4Wj4n5Qy-55eHNIu6tvw/zh-cn_image_0000002229604181.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=10F88C0CE7AC48EFF9FD0698EAB1E2CFB58FDD2D790F2FA2B658FE8C37240F58)

**解决措施**

修改build-profile.json5文件，登录个人华为账号，然后重新签名。

1.  将根目录下的build-profile.json5文件里的 "runtimeOS": "OpenHarmony" 改成 "runtimeOS": "HarmonyOS"；
2.  点击 File > Project Structure > Signing Configs 进行签名配置；
3.  勾选“Support HarmonyOS（支持HarmonyOS）”和“Automatically generate signature（自动签名）”；
4.  点击“Sign In”按钮；
5.  登录华为账号，按提示在弹出的登录页面输入手机号并使用验证码登录。
