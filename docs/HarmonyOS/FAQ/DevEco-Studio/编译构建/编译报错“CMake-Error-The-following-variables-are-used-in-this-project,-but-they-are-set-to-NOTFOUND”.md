---
title: "编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-33"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”"
captured_at: "2026-04-17T02:03:21.394Z"
---

# 编译报错“CMake Error: The following variables are used in this project, but they are set to NOTFOUND”

**问题现象**

Native工程使用find\_path时出现报错。因find\_path未在CMAKE\_SYSROOT限定路径中找到目标文件而触发该报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/kKcsemsTTxSM3P1Zw8Q4Ww/zh-cn_image_0000002229603961.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=CCC9AD2A4282E373D420F3E1C58F996543677BA137DC02936F54249650844884 "点击放大")

**解决措施**

OpenHarmony SDK的ohos.toolchain.cmake文件限制搜索路径为CMAKE\_SYSROOT。

如果开发者需要添加搜索路径，可在CMakeList.txt中使用list接口添加自定义路径，如将“D:/demo”添加至搜索路径：

list(APPEND CMAKE\_FIND\_ROOT\_PATH\_MODE\_INCLUDE "D:demo")

添加后，即可使用find\_path查找“D:/demo”目录下的文件。
