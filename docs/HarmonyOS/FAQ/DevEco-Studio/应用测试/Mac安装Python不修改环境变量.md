---
title: "Mac安装Python不修改环境变量"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-11"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用测试"
  - "Mac安装Python不修改环境变量"
captured_at: "2026-04-17T02:03:25.353Z"
---

# Mac安装Python不修改环境变量

1\. 下载官方Python Mac系统安装包，推荐使用 [3.11.7](https://mirrors.huaweicloud.com/python/3.11.7/python-3.11.7-macos11.pkg)。

2\. Mac版本自定义安装可以不修改环境变量，请查看文档：[在 macOS 上使用 Python](https://docs.python.org/zh-cn/3/using/mac.html)不勾选UNIX command-line tools和shell profile updater。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/YTYzxD_mTuGP0bfJVZZufg/zh-cn_image_0000002498271829.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=3789FFE3DE04DD650C759E90C7E031E90BB19EEB5051FAC8E8A3DF9977E1B518)

3\. 关闭DevEco Studio修改other.xml配置 。

```powershell
cd ~/Library/Application\ Support/Huawei/DevEcoStudio6.0/options
```

```powershell
vi other.xml
```

输入： /python，定位到location.python.path这一行, 修改后面的python路径为/Library/Frameworks/Python.framework/Versions/3.11/bin

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/KQSOqGUQTpKy9uegWjEp3g/zh-cn_image_0000002465312430.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=04D7C09D79D6D74350B08027393FC8EC71B72A9B875A6E219D8D61D87384278A)
