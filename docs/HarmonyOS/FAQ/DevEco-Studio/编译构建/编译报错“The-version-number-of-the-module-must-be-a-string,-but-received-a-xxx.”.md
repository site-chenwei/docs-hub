---
title: "编译报错“The version number of the module must be a string, but received a xxx.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-152"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The version number of the module must be a string, but received a xxx.”"
captured_at: "2026-04-17T02:03:22.997Z"
---

# 编译报错“The version number of the module must be a string, but received a xxx.”

**错误描述**

模块版本号必须为字符串类型。

**可能原因**

模块下的oh-package.json5文件中，version字段的配置值必须为字符串类型。

**解决措施**

在模块的oh-package.json5文件中，将version字段的值修改为字符串类型。
