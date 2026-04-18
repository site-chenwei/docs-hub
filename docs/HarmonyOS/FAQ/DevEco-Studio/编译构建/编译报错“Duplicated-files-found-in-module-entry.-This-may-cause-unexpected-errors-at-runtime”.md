---
title: "编译报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-107"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”"
captured_at: "2026-04-17T02:03:22.368Z"
---

# 编译报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”

**问题现象**

编译构建时，报错“Duplicated files found in module entry. This may cause unexpected errors at runtime”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/MV8Nix16QzaTrpG_YgnQuw/zh-cn_image_0000002229603833.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=CE0AA342315BE0AD0D13A836CB3C5E72D35DE9A1D5AC0CA00429F7308E25CA15 "点击放大")

**解决措施**

该报错是从不同的包中收集到了相同名称的so包，导致so包冲突，可在模块级build-profile.json5文件中添加enableOverride字段并设置true。更多内容可参考[模块级build-profile.json5文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile)。

"buildOption": {
  "nativeLib": {
    "filter": {
      "enableOverride": true
    }
  }
},
