---
title: "编译时DevEco Studio提示Signing material error"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-44"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译时DevEco Studio提示Signing material error"
captured_at: "2026-04-17T02:03:21.609Z"
---

# 编译时DevEco Studio提示Signing material error

**问题现象**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/tSL7lMCcRgOyMNdq8ZOjrg/zh-cn_image_0000002229604197.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=D2DFC74B27D3D7AAC421B910C41655ABBFC41A937D1246991A6F8E9D09D47220 "点击放大")

**解决措施**

删除C盘用户路径下 .hvigor 文件夹中的 meta 文件，然后重新签名并编译。
