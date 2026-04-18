---
title: "编译报错“Invalid tag 'xxx' at 'xxx/xxx.json5'.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-148"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Invalid tag 'xxx' at 'xxx/xxx.json5'.”"
captured_at: "2026-04-17T02:03:22.936Z"
---

# 编译报错“Invalid tag 'xxx' at 'xxx/xxx.json5'.”

**错误描述**

在xxx/xxx.json5文件中存在无效的tag标签“xxx”。

**可能原因**

在项目根目录的oh-package.json5文件中定义parameterFile参数配置文件的配置版本号时，使用的tag标签包含不符合要求的字符。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/hWSHgh_LSaaba6OG0y5j8w/zh-cn_image_0000002229758505.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=53390AFC41A12DD1A9BA8784FC45ADDBA8464017B625B7467FD0F4F9DFB04D2D)

**解决措施**

确保parameterFile中定义的tag标签仅由字母、数字、“.”、“-”或“\_”组成，必须以字母或数字开头，长度不超过 60 个字符，且不能配置为latest。
