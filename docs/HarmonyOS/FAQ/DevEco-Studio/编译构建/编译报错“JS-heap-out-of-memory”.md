---
title: "编译报错“JS heap out of memory”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-1"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“JS heap out of memory”"
captured_at: "2026-04-17T02:03:21.047Z"
---

# 编译报错“JS heap out of memory”

**问题现象**

编译构建时，出现报错“JS heap out of memory”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/oC6B1KdwS2KA5bneTtb_Xg/zh-cn_image_0000002194158628.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=0D9319253C52BDE57A6E1E52AEE259C302FAD3AA1CE06C4535722F0F699C13CC)

**解决措施**

出现该报错的原因是hvigor运行时内存不足。在使用3.1.0及以上版本的hvigor时，可通过以下方式修改hvigor运行时内存的最大值。

勾选 Enable the Daemon for tasks：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/Kge14kzuRIa5tGbUUeXk2A/zh-cn_image_0000002194318244.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=A13610872B25BC34A2EC111F8A632A8E40CAE02002F6D4A1A71BF72AA39FDA62)

在hvigor-config.json5中修改maxOldSpaceSize字段，根据工程大小适当增大，例如设置为 8192。
