---
title: "编译报错“This project is in the FA model and does not allow for external dependencies.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-153"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“This project is in the FA model and does not allow for external dependencies.”"
captured_at: "2026-04-17T02:03:23.013Z"
---

# 编译报错“This project is in the FA model and does not allow for external dependencies.”

**错误描述**

FA模型项目不得依赖外部项目模块。

**可能原因**

在FA模型项目中，build-profile.json5文件的srcPath字段引用了外部项目模块。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/QwDWX51iTxS7TRu6JhpMRw/zh-cn_image_0000002194318412.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=8CAD14159D4D50221FE5C334A03B014B8423FBCA2FF5D77DF265989241C41258)

**解决措施**

在项目根目录的build-profile.json5文件中，移除srcPath字段依赖的外部项目模块。
