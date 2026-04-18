---
title: "如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-123"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "如何解决编译报错“Error: cJSON_Parse failed, please check the JSON file.”的问题"
captured_at: "2026-04-17T02:03:22.615Z"
---

# 如何解决编译报错“Error: cJSON\_Parse failed, please check the JSON file.”的问题

**问题现象**

编译错误：“Error: cJSON\\\_Parse failed”。请检查JSON文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/w6imAje3S0mKvRxLpX7iZg/zh-cn_image_0000002194158800.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=B9953EB2AA3B02F30A36A7269BF36339B8273D9939E13E448B29D0B7CF9977BE "点击放大")

**报错原因**

module.json 文件格式不正确。

**常见场景**

1\. JSON文件末尾有多余的逗号。

2\. 根标签不是大括号{}。

**解决方案**

检查报错指向的 JSON 文件格式，例如末尾是否有多余的逗号，根标签是否为大括号 {}。
