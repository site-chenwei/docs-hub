---
title: "编译报错“The type of target device does not match the device type configured by module：xxx”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-141"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The type of target device does not match the device type configured by module：xxx”"
captured_at: "2026-04-17T02:03:22.856Z"
---

# 编译报错“The type of target device does not match the device type configured by module：xxx”

**错误描述**

指定target设备的类型与模块配置的设备类型不匹配。

**可能原因**

指定target设备的类型与模块配置的设备类型不匹配。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/KAkXbDzjQZSbibh4HfzRJQ/zh-cn_image_0000002194158392.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=64690A3CD0CDA32AAAA1FBEDADBA79EA1B57D50756F5EA0864ACF0D4A7F4940D)

**解决措施**

1.  确保module目录的build-profile.json5文件中targets下指定的设备类型包含所需的设备类型。
2.  确保module目录下src/main/module.json5中配置的deviceTypes字段包含所需的类型。
3.  检查hvigorfile.ts或[Hvigor脚本文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-life-cycle#section810245135914)是否包含任何可能更改模块deviceTypes设置的代码。
