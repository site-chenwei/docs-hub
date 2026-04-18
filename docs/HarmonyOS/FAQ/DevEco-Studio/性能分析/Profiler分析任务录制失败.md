---
title: "Profiler分析任务录制失败"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-profiler-1"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "性能分析"
  - "Profiler分析任务录制失败"
captured_at: "2026-04-17T02:03:24.938Z"
---

# Profiler分析任务录制失败

**问题现象**

单击Profiler深度分析任务的启动录制按钮后，录制失败。

-   DevEco Studio提示任务启动或录制失败。

-   Session列表中任务显示异常图标。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/V7AlokUcSX6MYxW-gUygWQ/zh-cn_image_0000002194318540.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=92EE7266F2616FA3347DC14156A9AF13FBFCF64B19B1C87DC07204C3F067705D)
    

**解决措施**

启动深度分析任务录制后，将经历初始化、录制和停止录制后分析及组装数据三个阶段。每个阶段都可能遇到任务录制失败的问题，具体原因包括连接断开、插件错误和设备状态异常。

请参考以下步骤进行操作。

1.  确保设备亮屏运行。

2.  尝试重新推送包到设备，或者重启应用和服务。
3.  重启设备。
4.  重启DevEco Studio。
