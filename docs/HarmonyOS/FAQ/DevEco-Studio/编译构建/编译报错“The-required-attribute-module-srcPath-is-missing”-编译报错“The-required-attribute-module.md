---
title: "编译报错“The required attribute module"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-137"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The required attribute module-srcPath is missing”"
captured_at: "2026-04-17T02:03:22.761Z"
---

# 编译报错“The required attribute module-srcPath is missing”

**错误描述**

缺少必需属性：module-srcPath。

**可能原因**

build-profile.json5文件中缺少模块的相对路径，具体表现为module-srcPath字段缺失。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/YnRmyMMgS8Og6af2qGNxfg/zh-cn_image_0000002229758669.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=6D3A93400244E5087867723C5257F3973A9D0B9D5F68D96EF53A10FEE7E20FE7)

**解决措施**

进入项目根目录下的build-profile.json5文件，确保module下srcPath字段存在且非空。
