---
title: "构建报错“debug is different”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-111"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "构建报错“debug is different”"
captured_at: "2026-04-17T02:03:22.396Z"
---

# 构建报错“debug is different”

**问题现象**

打包应用时，提示“debug is different”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/TOXecp1aSyG-0LzHWwZvBA/zh-cn_image_0000002229758605.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=78209568B695F0AD18D9C2875E3396E8BA79A7A62589F7778DC6202E14321FF6)

**解决措施**

根据报错日志的Warning信息提示的模块名称，检查模块间的debug字段是否一致，重点关注本地模块与外部引用模块。

1.该debug字段由编译构建工具自动生成，保存在HAP/HSP包的module.json文件中，如下图所示，首先确认各模块间该字段是否一致。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/0jWCDGIoR4CzCZ7Q_LDeuw/zh-cn_image_0000002229604117.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=7E7470F758531FF76C41C1136F400ED17A5FFBD62BFAE763943C1EE05D5CCD8B)

2.编译工具根据设置的Build Mode选项生成debug标识，如图所示，可以通过此处进行设置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/vrVutxnsQju0DGsRR6WTyA/zh-cn_image_0000002194318344.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=A44088B47FE289E6D5DB9A001DB3CC54B0A07A68C19C766D068A908EDE81ADE0)
