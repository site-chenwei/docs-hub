---
title: "点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-codegenie-2"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "AI辅助编程"
  - "点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应"
captured_at: "2026-04-17T02:03:25.494Z"
---

# 点击CodeGenie顶部栏的新建会话、历史记录等快捷按钮后无反应

**问题现象**

CodeGenie使用过程中，点击顶部栏新建会话、历史记录、Agent配置等快捷按钮后无反应。

**问题原因**

代码异常，导致前端渲染问题。

**解决措施**

1.  保存工程并关闭DevEco Studio。
2.  打开当前DevEco Studio的安装目录，按如下安装路径找到**codegenie-plugin**文件夹，手动删除此文件夹或将此文件夹移动到其他位置缓存备份。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/h5eEfkpyRIm1AENeMkQu4A/zh-cn_image_0000002566394897.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=A37507B913A4259E8912B4B8D387D60B491607F15C3016428D1C472AAC01848C)
    
3.  在[官网链接](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)下载最新发布的**DevEco CodeGenie 6.0.2 Release**版本，按照[插件安装指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie#section18337533718)安装和使用新版本插件。
