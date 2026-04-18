---
title: "Native侧如何使用hilog打印出日志信息"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-35"
menu_path:
  - "FAQ"
  - "应用框架开发"
  - "NDK开发"
  - "Native侧如何使用hilog打印出日志信息"
captured_at: "2026-04-17T02:03:01.977Z"
---

# Native侧如何使用hilog打印出日志信息

1.在CMakeLists.txt中新增libhilog\_ndk.z.so链接：

target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)

2.在源文件中包含hilog头文件, 并定义domain、tag宏：

#include "hilog/log.h"
#undef LOG\_DOMAIN
#undef LOG\_TAG
#define LOG\_DOMAIN 0x3200 // Global domain macro, identifying the business domain
#define LOG\_TAG "MY\_TAG"  // Global tag macro, identifying module log tags

3.打印日志，以打印ERROR级别的日志为例：

注意，需要加上{public}才会显示打印内容，不添加默认是{private}

int a = 5, b = 10;
OH\_LOG\_ERROR(LOG\_APP, "Pure a:%{public}d b:%{private}d.", a, b);

结果展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/a7d_LggfTPmmvl1lu3k4AQ/zh-cn_image_0000002194318320.png?HW-CC-KV=V1&HW-CC-Date=20260417T020304Z&HW-CC-Expire=86400&HW-CC-Sign=C023CBA635AB4365D307206F1F1D8B9F83E59C3B699C0C02BE3AE5FCA786FF59 "点击放大")

**参考链接：**

[使用HiLog打印日志(C/C++)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hilog-guidelines-ndk)
