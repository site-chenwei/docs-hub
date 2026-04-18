---
title: "编译报错“Failed to obtain the module type.”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-162"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Failed to obtain the module type.”"
captured_at: "2026-04-17T02:03:23.143Z"
---

# 编译报错“Failed to obtain the module type.”

**错误描述**

未找到指定的模块类型。

**可能原因**

在FA模型中，config.json文件中的module/distro/moduleType字段缺失或配置错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/cFH8xVCiRqCqZUf9dZJNnA/zh-cn_image_0000002229604177.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=D648AF5CA395B20AB79144711BEB9404A3406A9C91E2D377D9ABC7B1FB5CF516)

**解决措施**

确保在FA模型的config.json文件中，module/distro/moduleType字段存在且配置正确。
