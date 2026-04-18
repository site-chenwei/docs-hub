---
title: "DevEco Studio编译报“Operation not permitted”无权限错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-78"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "DevEco Studio编译报“Operation not permitted”无权限错误"
captured_at: "2026-04-17T02:03:21.998Z"
---

# DevEco Studio编译报“Operation not permitted”无权限错误

**问题描述**

DevEco Studio安装完成后一直报Operation not permitted无权限，具体报错如下所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/EubMSrSuQwe9GDlZvbD5Qw/zh-cn_image_0000002194158416.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=093B88800B3BF6BE9D23F2D1AB3AF1C09D96D999AB9D044AA81B812AD7486A7F)

**解决方案**

通过以下命令查看是否有com.example.myapplication标识

xattr -l /path/to/es2abc

用以下命令删除该标识

xattr -d com.example.myapplication/path/to/es2abc

根因：mac系统对文件访问有限制
