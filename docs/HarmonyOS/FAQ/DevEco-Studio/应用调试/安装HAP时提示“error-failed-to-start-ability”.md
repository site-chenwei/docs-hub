---
title: "安装HAP时提示“error: failed to start ability”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-23"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "安装HAP时提示“error: failed to start ability”"
captured_at: "2026-04-17T02:03:24.536Z"
---

# 安装HAP时提示“error: failed to start ability”

**问题现象**

启动调试或运行应用/服务时，如果安装HAP出错，提示“error: failed to start ability. error: ability visible false deny request”，请检查应用的可见性设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/DIyGapRTScm0H9UjjGQQwA/zh-cn_image_0000002229758621.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=767F436B049EDCBE9B684EF5593E0B2FE8710EF3DD9CB3CB10EC2075F7CFFF88)

**解决措施**

-   在Stage模型工程的module.json5文件中，将abilities字段内的exported设置为true。
-   FA模型工程：在config.json文件的abilities字段中，将visible设置为true。
