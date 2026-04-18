---
title: "如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-122"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决编译报错“ Error: 'icon' value `$media:icons` invalid value.”的问题"
captured_at: "2026-04-17T02:03:22.574Z"
---

# 如何解决编译报错“ Error: 'icon' value \`$media:icons\` invalid value.”的问题

**问题现象**

编译报错。

```text
ERROR: Failed :entry:default@CompileResource...
ERROR: Tools execution failed.
Error: ref `$media:icons` don't be defined.
Error: 'icon' value `$media:icons` invalid value.
at D:\project\process_profile\default\module.json
Detail: Please check the message from tools.
```

**报错原因**

引用的资源不存在时，编译错误指向build目录中的文件路径。

**常见场景**

1.  资源文件未添加。
2.  资源文件被意外删除。

**解决方案**

根据报错的资源ID全局搜索，使用右上角的查找按钮，确认报错的资源是否存在。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/76UpSDANS9etOglMx1jbiQ/zh-cn_image_0000002262335589.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=02167B36E320F5C30AC05ACE550BF2309BABBB261A4611928A417CC2D24B59B0 "点击放大")
