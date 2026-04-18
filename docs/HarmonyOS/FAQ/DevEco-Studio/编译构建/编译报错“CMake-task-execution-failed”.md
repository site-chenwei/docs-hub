---
title: "编译报错“CMake task execution failed”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-160"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“CMake task execution failed”"
captured_at: "2026-04-17T02:03:23.095Z"
---

# 编译报错“CMake task execution failed”

**错误描述**

CMake任务执行时提示“CMake task execution failed”错误信息。

**可能原因**

需要手动删除 .cxx 目录，并在 build-profile.json5 文件的 arguments 字段中添加 “--version” 参数。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/6oivT678TMac4jSqHxkmMA/zh-cn_image_0000002229604133.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=80B7AF6EE30824732F9CA57BFEA151CA1E87256E2C573A7B7E9F5ACB7C542D68)

**解决措施**

移除arguments字段中的“--version”参数。
