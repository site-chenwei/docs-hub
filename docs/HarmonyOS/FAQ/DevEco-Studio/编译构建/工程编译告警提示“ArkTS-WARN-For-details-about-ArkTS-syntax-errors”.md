---
title: "工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-30"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”"
captured_at: "2026-04-17T02:03:21.394Z"
---

# 工程编译告警提示“ArkTS:WARN: For details about ArkTS syntax errors”

**问题现象**

工程构建时，出现ArkTS语法告警提示，详情请参见FAQ。

报错信息：

1.  ERROR: ArkTS:ERROR File: C:/Users/... ,Use "let" instead of "var" (arkts-no-var)
2.  ERROR: ArkTS:ERROR File: D:/DTS/MyApplicationAPI12/... ,The "@Sendable" decorator can only be used on "class", "function" and "typeAlias" (arkts-sendable-decorator-limited)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/FMwZpjEGSmiEa9YpaWZNhw/zh-cn_image_0000002429325678.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=DAA29884130D6AA48A94695466733E7FFCBB8FA25AC3C399963BA8E0DE83F93D)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/b38m7REYQV695JRn8bwlBQ/zh-cn_image_0000002429485750.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=17EB43E83C86D2F3774A13C4E89B840A3731E703E45A08CF3C939EB249C40D6F)

**解决措施**

该告警表明工程中存在不符合ArkTS语法规范的代码，请根据ERROR报错中的报错信息进行修改，或根据提示的语法规则(如arkts-no-var、arkts-sendable-decorator-limited等)，在本网站搜索对应的说明，修改为ArkTS规范写法。ArkTS语言相关介绍请查看[ArkTS（方舟编程语言）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts)
