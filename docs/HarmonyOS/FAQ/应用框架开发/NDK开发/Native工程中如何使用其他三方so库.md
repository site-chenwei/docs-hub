---
title: "Native工程中如何使用其他三方so库"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-34"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native工程中如何使用其他三方so库"
captured_at: "2026-04-17T02:03:01.962Z"
---

# Native工程中如何使用其他三方so库

1.将编译好的so库放到Native工程的entry/libs/arm64-v8a/目录下，并将so库对应的头文件放到entry/src/main/cpp目录层级下（可以在cpp目录下增加一个文件夹专门存放三方so库的头文件）。

2.在CMakeLists.txt文件中链入so库。

3.在Native侧 .cpp文件中引入头文件使用so库的相关能力。

示例如下：

在Native侧集成三方库Curl

1\. 将移植后的Curl的so库放到Native工程的entry/libs/目录下，并将移植后生成的、包含头文件的include目录放到entry/src/main/cpp目录下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/eMS8X9gJRn6zW5eqHOsv_g/zh-cn_image_0000002194158760.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=C41557DE767FE3E9D37A7EC81B0D8457ECBB40923EF10312E7A5C4B9113E7CCE "点击放大")

2\. 在CMakeLists.txt文件中链接Curl对应的so库。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/66FbG90dQtWUJ0NQpz0f4A/zh-cn_image_0000002194158764.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=E324FF38AC18F0FD252C5672D0DEAE788DA0536144CB4A910D206A973CD7D9D2 "点击放大")

3\. 在Native侧.cpp文件中通过引入头文件curl.h来使用Curl的相关能力。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/tqrS5BirQVmg9BjcUDqPWQ/zh-cn_image_0000002229758629.png?HW-CC-KV=V1&HW-CC-Date=20260417T020303Z&HW-CC-Expire=86400&HW-CC-Sign=D7E2AEBCD2CA967ABD266890AE4F5A6983467B3C4F4BE2E239509ACA29EE490A "点击放大")

**参考链接：**

[在NDK工程中使用预构建库](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/build-with-ndk-prebuilts)
