---
title: "命令行方式执行Instrument Test堆栈路径打印错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-7"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用测试"
  - "命令行方式执行Instrument Test堆栈路径打印错误"
captured_at: "2026-04-17T02:03:25.281Z"
---

# 命令行方式执行Instrument Test堆栈路径打印错误

**问题现象**

在5.0.3.400版本下，通过命令行执行Instrument Test，堆栈信息中的文件路径和位置有误，出现“|”而不是“/”，升级到5.0.3.401及以上版本仍然有误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/aNnHla4JQBOzAn_waU7XzA/zh-cn_image_0000002194158620.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=5855884F4C29648B5DB83F36AEB6873A5553089E05731DDDEC504708D52D9E5B "点击放大")

**原因**

在5.0.3.400版本下生成的.test文件和build文件夹未被同时删除，需要手动删除。

**解决措施**

删除5.0.3.400版本下生成的.test文件和build文件夹，然后重新执行测试用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/IFhFkPYDR3y8JVNf15l9Xw/zh-cn_image_0000002194318232.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=4734472D1FAB7B12C2920B58E345FB2BF7F8BD118C261F013E32E881A43E2879 "点击放大")
