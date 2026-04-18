---
title: "无法调试，DevEco Studio提示“ The target can not be empty. Check the build"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-43"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "无法调试，DevEco Studio提示“ The target can not be empty. Check the build-profile.json5 file of the project root directory and make sure the targets of the modules in configuration is set to specified product: default in applyToProducts.”"
captured_at: "2026-04-17T02:03:21.608Z"
---

# 无法调试，DevEco Studio提示“ The target can not be empty. Check the build-profile.json5 file of the project root directory and make sure the targets of the modules in configuration is set to specified product: default in applyToProducts.”

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/pay2K_NfRR-dMSnW1lsrhw/zh-cn_image_0000002229604385.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=873341058106757EC0FA5108F7A634E9ACA95241BD5747C153FCCDE2B53A069C "点击放大")

**问题分析**

报该错误，可能是build-profile.json5文件中未添加“targets”配置，Module Target下为空，工程同步失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/AVN52TBzQ5yk0EQVgTa8CQ/zh-cn_image_0000002272490329.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=F3EC9F97D08FA9AEA6ACE7F1C09709E37C24695D621D2CFE1AAC39770BA8A175)

**解决措施**

需要在模块级build-profile.json5文件中添加“targets”配置，点击“Sync Now”，待完成同步后，即可解决该问题（确保工程同步成功）。具体配置如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/_z_0xlWhTXOekDUhuKFEYw/zh-cn_image_0000002229758873.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=16547544E4374A36645602A2D934350AFF2754D8737DD74AD9D7219D163FD23C "点击放大")
