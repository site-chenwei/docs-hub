---
title: "DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-61"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "DevEco Studio安装HAP时报错“FileTransfer Failed: [Fail]Error opening file: operation not permitted”"
captured_at: "2026-04-17T02:03:24.783Z"
---

# DevEco Studio安装HAP时报错“FileTransfer Failed: \[Fail\]Error opening file: operation not permitted”

**问题现象**

DevEco Studio安装HAP时报错“FileTransfer Failed: \[Fail\]Error opening file: operation not permitted”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/ijctClTSQ5yWEWwj1fxB-w/zh-cn_image_0000002557334391.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=61C3EBA522414BEE2FDC0F116238CFDFB1DD5660CCBF1C1264099BA4B9B38639)

**解决措施**

出现该问题的原因是安装包HAP所在路径没有权限。

1、Windows系统建议将工程移出C盘，然后重新运行。

2、MAC系统为DevEco Studio获取完全磁盘访问权，请进入**“系统设置”>“隐私与安全性”>“完全磁盘访问权限”**，在列表中勾选DevEco Studio软件并重启。
