---
title: "升级react"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-185"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "升级react-native-openharmony编译出错"
captured_at: "2026-04-17T02:03:23.347Z"
---

# 升级react-native-openharmony编译出错

**问题现象**

升级react-native-openharmony编译出错，类似如下报错：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/BO8mmwS7TTa041ytjc-_kQ/zh-cn_image_0000002304734606.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=5AF3892A309EA01D539F06401C7CF803D6603187931537CB12C3B3181C2701F7)

**问题原因**

旧版本的react-native-openharmony缓存还在,导致某些链接找不到。

**解决措施**

删除要编译的模块根目录下的.cxx和build目录,然后重新触发编译。
