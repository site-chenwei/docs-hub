---
title: "编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-38"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”"
captured_at: "2026-04-17T02:03:21.552Z"
---

# 编译报错“The reason and usedScene attributes are mandatory for user\_grant permissions”

**问题现象**

DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user\_grant permissions”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/V6xsFQSUS0SULT0DxOUnVw/zh-cn_image_0000002194158568.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=4E93D4A21C6B55212B5834DDCB17893750237005BE9BD6E0B110F098DBFDB804 "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview 2版本开始，新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定（可以为空，若非空则name必填；user\_grant权限则必填reason和usedScene字段）。

**解决措施**

进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：

"requestPermissions": \[
  {
    "name": "ohos.permission.READ\_IMAGEVIDEO",
    "reason": "$string:module\_desc",
    "usedScene": {
      "abilities": \[
        "EntryAbility"
      \],
      "when": "inuse"
    }
  }
\],
