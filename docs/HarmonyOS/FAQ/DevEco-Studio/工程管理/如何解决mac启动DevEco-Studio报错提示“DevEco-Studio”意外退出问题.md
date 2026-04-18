---
title: "如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-13"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "工程管理"
  - "如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题"
captured_at: "2026-04-17T02:03:20.497Z"
---

# 如何解决mac启动DevEco Studio报错提示“DevEco Studio”意外退出问题

**问题描述**

Mac启动DevEco Studio时，“DevEco Studio”意外退出。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/pONQ_k4hTkq94veyYIBdrQ/zh-cn_image_0000002229758581.png?HW-CC-KV=V1&HW-CC-Date=20260417T020320Z&HW-CC-Expire=86400&HW-CC-Sign=7DA5158CB24FC660F37FB58511F0C5E3501B453427F34380704BDBAC4773207E)

**解决方案**

问题根因：异常修改了JetBrains启动脚本中的环境变量，导致Java虚拟机无法启动，DevEco Studio无法打开，弹窗显示错误。

规避措施：删除启动脚本 /Users/{USER\_NAME}/Library/LaunchAgents/jetbrains.vmoptions.plist，然后重启 Mac。
