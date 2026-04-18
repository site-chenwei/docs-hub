---
title: "多Module应用通过startAbility()启动时报错"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-20"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "程序框架"
  - "程序框架（Ability）"
  - "多Module应用通过startAbility()启动时报错"
captured_at: "2026-04-17T02:02:58.782Z"
---

# 多Module应用通过startAbility()启动时报错

**原因**

在同一个工程和设备中存在多个模块，并且这些模块之间存在调用关系，但并非所有HAP包都已安装到设备中。

**解决措施**

单击Run > Edit Configurations，设置指定模块的HAP安装方式，勾选“Keep Application Data”，表示采用覆盖安装方式，保留应用和服务的缓存数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/-BphBeEpR1aqx3UD1O04zg/zh-cn_image_0000002194318612.png?HW-CC-KV=V1&HW-CC-Date=20260417T020300Z&HW-CC-Expire=86400&HW-CC-Sign=7095C5EDF3D95D85F2D25223D6EC5AFE74586A6F6DCC115F777692E40A6800D4 "点击放大")

**参考链接**

[设置HAP安装方式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations#section531811771410)

[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)
