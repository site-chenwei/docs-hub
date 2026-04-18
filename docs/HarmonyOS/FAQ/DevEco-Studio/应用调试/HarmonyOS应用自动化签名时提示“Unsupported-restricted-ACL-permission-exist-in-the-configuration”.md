---
title: "HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-5"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”"
captured_at: "2026-04-17T02:03:24.450Z"
---

# HarmonyOS应用自动化签名时提示“Unsupported restricted ACL permission exist in the configuration”

**问题现象**

在对HarmonyOS应用工程中，勾选“Automatically generate signature”时，提示“Unsupported restricted ACL permission exist in the configuration”报错信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/TgK5V8HWTc6kUFtncnSwjg/zh-cn_image_0000002250504069.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=017764839ABE50263FA09C57722B700FAB12B232EA3F5671E280FF622636C68E)

**解决措施**

出现该问题的原因是当前DevEco Studio自动签名只支持部分的ACL权限，当前工程中使用了不在支持范围之内的ACL权限，建议尝试手动签名。

**参考链接**

[自动签名支持的ACL权限](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section5301916183411)

[手动签名](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-signing#section297715173233)
