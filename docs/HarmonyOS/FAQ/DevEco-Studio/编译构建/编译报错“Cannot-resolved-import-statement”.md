---
title: "编译报错“Cannot resolved import statement”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-140"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Cannot resolved import statement”"
captured_at: "2026-04-17T02:03:22.849Z"
---

# 编译报错“Cannot resolved import statement”

**错误描述**

在编译过程中，提示“Cannot resolved import statement”错误信息。

**可能原因**

导入文件时，大小写不一致会导致问题（导入到单个文件夹时，默认寻址小写 “index.ets”文件，但该文件夹下仅存在大写“index.ets”文件）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/CpytTd7TS8iEsEmaRBP8lg/zh-cn_image_0000002194318384.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=50F55B4AE34B1CF446D2C73B4F0F8D858BC41BF28162443DE61AE9077B3FC3A0)

**解决措施**

检查import文件的大小写。
