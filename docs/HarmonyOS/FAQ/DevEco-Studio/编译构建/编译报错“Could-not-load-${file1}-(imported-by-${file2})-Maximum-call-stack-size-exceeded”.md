---
title: "编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-8"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”"
captured_at: "2026-04-17T02:03:21.101Z"
---

# 编译报错“Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”

**问题现象**

Stage模板工程编译构建失败，提示 “ERROR: Could not load ${file1} (imported by ${file2}): Maximum call stack size exceeded”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/gMnCu-_rTfq7E7eZM7Mn7w/zh-cn_image_0000002229758241.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=515FE11A1B21F4E62914F8C46843E33AEF31461196B2728988BFCA2DEDD7C352)

**解决措施**

问题源于file1位于当前工程外，步骤如下：

1.  在工程中右键选择New > Module...。
2.  选择Static Library模板。
3.  配置build-profile.json中的dependencies添加HAR引用。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/r0aLqeaQRH27h9mFwJSJ9A/zh-cn_image_0000002194158380.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=8A024F6927A470C799CDD913E9908D9A5590BCD97CACC61A86EC64ACF0FCA97B)
