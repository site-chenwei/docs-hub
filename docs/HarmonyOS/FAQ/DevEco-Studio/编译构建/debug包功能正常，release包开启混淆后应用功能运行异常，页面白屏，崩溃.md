---
title: "debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-187"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃"
captured_at: "2026-04-17T02:03:23.379Z"
---

# debug包功能正常，release包开启混淆后应用功能运行异常，页面白屏，崩溃

**解决措施**

在主模块下的obfuscation-rules.txt文件中配置-disable-obfuscation选项关闭混淆，确认问题是否由混淆引起。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/-m8QACYWR-Sl7m7SyMfdyw/zh-cn_image_0000002372892821.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=82BE0D6E6752962AADDF13AF20DE9767F8BEDD0F2E075ACEA22069A519CE08EE)

如果关闭混淆后，功能恢复正常，可以使用DevEco Studio的混淆助手来辅助配置混淆白名单。

**参考链接**

[通过混淆助手配置保留选项](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-build-obfuscation#section19439175917123)
