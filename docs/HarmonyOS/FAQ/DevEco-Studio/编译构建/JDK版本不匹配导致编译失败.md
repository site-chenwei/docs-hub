---
title: "JDK版本不匹配导致编译失败"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-14"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "JDK版本不匹配导致编译失败"
captured_at: "2026-04-17T02:03:21.181Z"
---

# JDK版本不匹配导致编译失败

**问题现象**

通过命令行方式构建HarmonyOS应用或元服务过程中出现构建失败，现象如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/0TLwd5ytRiqXmwUoEAjm6w/zh-cn_image_0000002229604033.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=CF0D44F521C8454CBF4EE5CE8841EA2B7CC0F319EE397A38A01D1606D97C6065)

**解决措施**

该问题需使用配套的JDK 17版本解决，请根据如下方法进行修正：

1.  下载并安装JDK 17版本。
2.  修改JAVA\_HOME环境变量，取值为JDK 17。如果是Linux系统，可参考命令行方式构建服务或应用的[配置JDK](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app#section195447475220)。
