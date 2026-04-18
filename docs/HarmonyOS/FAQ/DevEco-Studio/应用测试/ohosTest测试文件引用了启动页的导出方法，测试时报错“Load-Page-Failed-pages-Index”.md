---
title: "ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-test-9"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用测试"
  - "ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”"
captured_at: "2026-04-17T02:03:25.308Z"
---

# ohosTest测试文件引用了启动页的导出方法，测试时报错“Load Page Failed: pages/Index”

**问题现象**

在测试文件中引用启动页的导出方法并拉起启动页面所在的Ability时，执行测试会抛出jscrash，错误信息为：“Load Page Failed: pages/Index”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/C-nSyAixTim68t5mONOHZw/zh-cn_image_0000002229604273.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=AA45D5D79B25C02D7B7270852B05A299DFC7F1D11F1339974FF7F784B27494A4)**解决措施**

拉起启动页面所在Ability时指定当前模块名称，执行测试，用例正常运行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/7LmOzybrSzubpUbeiHH1Uw/zh-cn_image_0000002194158896.png?HW-CC-KV=V1&HW-CC-Date=20260417T020326Z&HW-CC-Expire=86400&HW-CC-Sign=2870F8D02CF2C71CA06AAF7260AF236DCD38F494B0120CCF6583B738A9D594CD)
