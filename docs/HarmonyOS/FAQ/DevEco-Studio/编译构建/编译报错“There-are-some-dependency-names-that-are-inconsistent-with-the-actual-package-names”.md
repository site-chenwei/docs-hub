---
title: "编译报错“There are some dependency names that are inconsistent with the actual package names”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-144"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“There are some dependency names that are inconsistent with the actual package names”"
captured_at: "2026-04-17T02:03:22.867Z"
---

# 编译报错“There are some dependency names that are inconsistent with the actual package names”

**错误描述**

依赖名称与包名称不匹配。

**可能原因**

依赖名称与依赖包中oh-package.json5文件的name字段不一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/u2PcFuEdRHGz5Ax6RX_ANQ/zh-cn_image_0000002229758445.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=E907C857EC3BB60FC62C1F231BD0C93D0E8C40553C03CB9EC84139C13B7092BA)

**解决措施**

将依赖名修改为依赖包在oh-package.json5中定义的name。
