---
title: "Stack布局设置Alignment.Bottom没有生效"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-160"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "UI框架"
  - "方舟UI框架（ArkUI）"
  - "Stack布局设置Alignment.Bottom没有生效"
captured_at: "2026-04-17T02:03:04.331Z"
---

# Stack布局设置Alignment.Bottom没有生效

**问题现象**

在build()中使用Stack作为容器，设置alignContent为Alignment.Bottom，同时设置align为Alignment.Center。但alignContent为Alignment.Bottom未生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/KpOT9zC3TzOisYzhZXl-eA/zh-cn_image_0000002229604149.png?HW-CC-KV=V1&HW-CC-Date=20260417T020306Z&HW-CC-Expire=86400&HW-CC-Sign=57DBFB32EA8EE91E49D58F04BF6CB82D599D104E4A05398725AD7D9A4B6D3945 "点击放大")

**解决措施**

由于Stack布局默认采用单一对齐策略，当同时设置alignContent与align属性时，后设置的值将生效。
