---
title: "编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-149"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”"
captured_at: "2026-04-17T02:03:22.948Z"
---

# 编译报错“The 'tag' keyword is not allowed for 'version' at 'xxx/oh-package.json5'”

**错误描述**

oh-package.json5文件中的version字段不能包含tag标签。

**可能原因**

使用parameterFile参数化配置版本号时，oh-package.json5文件中的version字段不能包含tag标签。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/IdEJW7xTSDG9tYfdHwD_tg/zh-cn_image_0000002229604173.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=434464DF3DB56029B327C07017FA44D9E62619014F283335C7D9C16C54728754)

**解决措施**

当oh-package.json5文件中的version字段引用parameterFile时，开发者不应使用tag标签。
