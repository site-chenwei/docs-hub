---
title: "通过命令行或终端可以正常发布，在Git Bash上发布时提示错误：私钥路径中的私钥内容错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-command-line-tool-1"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "命令行工具"
  - "通过命令行或终端可以正常发布，在Git Bash上发布时提示错误：私钥路径中的私钥内容错误"
captured_at: "2026-04-17T02:03:25.509Z"
---

# 通过命令行或终端可以正常发布，在Git Bash上发布时提示错误：私钥路径中的私钥内容错误

**问题现象**

通过命令行或终端可以正常发布，但在Git Bash上发布时出现错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/eHAZEYvtQ-qnTA5lhsfnrw/zh-cn_image_0000002194158912.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=7C787C2B852D797B5478F1C07665B4805AAFFC867E1F995B04032F56E3957E1B "点击放大")

**解决措施**

方法一：从Git官网下载并安装最新版本的Git，使用该版本自带的Git Bash终端进行操作。

方法二：在当前Git安装目录下的etc目录中新增git-bash.config文件，文件中添加一行MSYS=enable\_pcon配置。重新打开Git Bash终端，运行ohpm publish命令即可。
