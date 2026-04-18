---
title: "C/C++项目三方依赖库未打包到HAP"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-22"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "C/C++项目三方依赖库未打包到HAP"
captured_at: "2026-04-17T02:03:21.292Z"
---

# C/C++项目三方依赖库未打包到HAP

**问题现象**

C/C++项目依赖三方so时，在打包生成HAP后，发现三方so未打包到HAP中。

**解决措施**

当前DevEco Studio对C/C++项目中第三方so文件的寻址方式存在限制。如果第三方so文件未打包到HAP中，请尝试修改so文件的引入方式。

1.  定义一个别名，例如jsbind\_shared\_lib\_tracing，代表将要引入的三方so。
2.  使用SHARED IMPORT将三方so动态引入。
3.  使用IMPORTED\_LOCATION定义引入的so文件位置。
4.  将定义的三方so声明给目标。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/G56WIeadSImgHbxcFf9Qvg/zh-cn_image_0000002194318404.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=7694554578977E6F6954C931F4180157A3572698DB062DD9F8C28723EA423DDF)
5.  再次打包生成HAP，确认三方so已打包到HAP中。
