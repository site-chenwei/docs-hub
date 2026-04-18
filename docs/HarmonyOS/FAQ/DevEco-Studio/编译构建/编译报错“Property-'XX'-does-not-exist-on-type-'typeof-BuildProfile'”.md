---
title: "编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-42"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”"
captured_at: "2026-04-17T02:03:21.555Z"
---

# 编译报错“Property 'XX' does not exist on type 'typeof BuildProfile'”

**问题现象**

本地HSP模块对外提供的接口中使用了未在HAP中定义的自定义参数BuildProfileFields。HAP引用了HSP中的该接口，导致编译失败，提示“Property 'XX' does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/QOPfAvFaQs2gAbB8sCEnYg/zh-cn_image_0000002194158808.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=94209BD576FC9E69B450A92C96F41BF504E86F9BC9CA798CA286593287F76781)

**解决措施**

采用以下两种方式解决该问题：

-   在HAP中配置与HSP相同的自定义参数BuildProfileFields。
-   将与HSP相同的自定义参数BuildProfileFields配置到工程级build-profile.json5中。这种方法会使HSP中的自定义参数在全局生效。
