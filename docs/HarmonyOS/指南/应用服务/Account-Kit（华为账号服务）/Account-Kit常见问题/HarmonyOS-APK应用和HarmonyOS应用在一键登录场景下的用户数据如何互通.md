---
title: "HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-7"
menu_path:
  - "指南"
  - "应用服务"
  - "Account Kit（华为账号服务）"
  - "Account Kit常见问题"
  - "HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通"
captured_at: "2026-04-17T01:36:11.188Z"
---

# HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通

终端设备从HarmonyOS 3.x/4.x（简称HarmonyOS）升级到HarmonyOS NEXT/5.0.x及之后版本（简称HarmonyOS NEXT）。

1.  HarmonyOS APK应用使用OpenID关联用户数据时，将用户数据关系切换成UnionID，具体切换指导可以参考：[通过OpenID获取UnionID](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/account-api-get-unionid)。
    
2.  HarmonyOS APK应用使用UnionID关联用户数据时，在HarmonyOS NEXT/5.0.x上接入华为账号一键登录获取手机号后，应用需要同时将UnionID和手机号与用户信息进行关联，最终实现应用使用华为账号一键登录和手机号登录数据互通。详细流程可以参考：[用户场景设计](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-phone-unionid-login#用户场景设计)。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/zvgFVWIRQz2nWhLj43orXQ/zh-cn_image_0000002569019421.png?HW-CC-KV=V1&HW-CC-Date=20260417T013611Z&HW-CC-Expire=86400&HW-CC-Sign=66BF6811A8C9F3BDC956A684AEED081739480A1997EFD43CE675F46DA437DF52)
