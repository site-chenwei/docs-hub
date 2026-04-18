---
title: "是否支持#include <memory_resource>和std::pmr::vector"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-149"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "ArkTS语言"
  - "ArkTS线程模型和并发"
  - "是否支持#include <memory_resource>和std::pmr::vector"
captured_at: "2026-04-17T02:03:01.532Z"
---

# 是否支持#include <memory\_resource>和std::pmr::vector

暂时不支持。

C++从C++17标准开始正式支持 <memory\_resource> 和std::pmr::vector等“多态内存资源”容器，开发者可以直接在sdk下查询到当前llvm版本是15.0.4，暂时不支持部分C++17高级特性。

Windows：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/4tsW11hoShGtFU9fn8H0zA/zh-cn_image_0000002335841501.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=18C80A5CE57B4BBC56F3C9A5A6739E7EF90A917B342F26149954832109C77198)

Mac：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/kyAtJ-hxRFyjV0eP-tllJQ/zh-cn_image_0000002301915320.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=55C1362E67A2E59ACB85D4139C725F0AA4F541C391D08B2B12C5B6122441E79F "点击放大")
