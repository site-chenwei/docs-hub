---
title: "编译报错“Unrecognized archive format in parameterFile”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-157"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Unrecognized archive format in parameterFile”"
captured_at: "2026-04-17T02:03:23.096Z"
---

# 编译报错“Unrecognized archive format in parameterFile”

**错误描述**

parameterFile中包含无法识别的格式。

**可能原因**

使用parameterFile参数化配置的本地依赖既不是目录，也不是.har或.tgz文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/Np62aRQnS0S5MwwxveB1pw/zh-cn_image_0000002194318392.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=C60A829831A1E8422B767375E58215B7C62CA4DCE18213F646146C5504E6A0EC)

**解决措施**

将本地依赖修改为模块目录或模块编译后的har/tgz文件。
