---
title: "使用系统Picker"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-picker"
menu_path:
  - "指南"
  - "系统"
  - "安全"
  - "程序访问控制"
  - "使用系统Picker"
captured_at: "2026-04-17T01:35:47.006Z"
---

# 使用系统Picker

应用拉起系统Picker组件（文件选择器、照片选择器、联系人选择器等），由用户在Picker上选择对应的文件、照片、联系人等资源，应用即可获取到Picker的返回结果。

系统Picker由系统独立进程实现。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/bMvxxM56SbmAnUH6G2311w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013548Z&HW-CC-Expire=86400&HW-CC-Sign=809A8FCCAB7F6CF233A8AEB9FAF3A14FEAC1DFF3A54F9B16B42A62FC2C9A809D)

由于系统Picker已经获取了对应权限的预授权，开发者使用系统Picker时，无需再次申请权限也可临时受限访问对应的资源。例如，当应用需要读取用户图片时，可通过使用照片Picker，在用户选择所需要的图片资源后，直接返回该图片资源，而不需要授予应用读取图片文件的权限。

当前，系统Picker作为拉起系统资源的一种方式，整合至“拉起系统应用”中，开发者可从“[拉起系统应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/system-app-startup)”获取所有拉起系统资源的方式。
