---
title: "调用云存储业务接口失败，app日志提示“\"state\":65”，upload进程日志提示“404 Not Found”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-6"
menu_path:
  - "指南"
  - "应用服务"
  - "Cloud Foundation Kit（云开发服务）"
  - "Cloud Foundation Kit常见问题"
  - "云存储"
  - "调用云存储业务接口失败，app日志提示“\"state\":65”，upload进程日志提示“404 Not Found”"
captured_at: "2026-04-17T01:36:13.884Z"
---

# 调用云存储业务接口失败，app日志提示“"state":65”，upload进程日志提示“404 Not Found”

**问题现象**

通过“使用指定的实例”方式初始化云存储实例时，调用业务接口（如调用uploadFile接口上传文件）失败，出现如下错误提示：

-   app日志提示“"state":65”
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/jJ4UEeWGTQahjaPhh1lkfQ/zh-cn_image_0000002538019822.png?HW-CC-KV=V1&HW-CC-Date=20260417T013614Z&HW-CC-Expire=86400&HW-CC-Sign=964145CFF23124E562BA6E429B9BDA6AC8105577D0E067D84056A95B6407AC10)
    
-   upload进程的日志提示“404 Not Found”（通过设置“No filters”模式、过滤“C01C50”关键字查找）
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/-Wk0veUHQT6IsrqbArYFSw/zh-cn_image_0000002538179750.png?HW-CC-KV=V1&HW-CC-Date=20260417T013614Z&HW-CC-Expire=86400&HW-CC-Sign=5490D4A5211C1AE49512E3DAD2E6F88B136210C4735931571868A2983B798CD5)
    

**解决措施**

出现此问题，原因是当前云侧不存在该存储实例，或传入的存储实例名称错误。

请检查您传入的存储实例名称，确保云侧存在该存储实例，且传入的存储实例名称与云侧存储实例名称完全一致。
