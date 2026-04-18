---
title: "编译初始化报错“resource busy or locked, open 'xxx\\outputs\\build"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-132"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译初始化报错“resource busy or locked, open 'xxx\\outputs\\build-logs\\build.log'”"
captured_at: "2026-04-17T02:03:22.743Z"
---

# 编译初始化报错“resource busy or locked, open 'xxx\\outputs\\build-logs\\build.log'”

**问题现象**

在升级DevEco Studio至5.0.3.403版本后，打开旧工程时，可能会遇到以下错误：resource busy or locked, open 'xxx\\outputs\\build-logs\\build.log'。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/74-mrpBRRmCh3RX4_lUZ2Q/zh-cn_image_0000002194158364.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=A3E2A64D0EFC0271CD1BC53350FED2B17CCDE27C5034AD1443C8EF7A10DEFCED)

**问题原因**

初始化时，日志写入存在冲突，.hvigor目录中的build-log文件被占用，导致报错。

**解决方案**

-   方法一：点击编辑器窗口上方的Sync Now。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/tJf7-EzqR6O8gA8rS0n3VQ/zh-cn_image_0000002194317984.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=93F2316FE0C45C3D8BD205DA71A96A01CFF62973B86E3F13485349F9A310D5FF)
    
-   方法二：点击工具栏**File > Sync and Refresh Project**。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/I1zHuR1aTHW9Q8Kjd6WYGw/zh-cn_image_0000002229758229.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=28D2C23BCD783D784BCE6880FACB9C1948CBF53CF06323761F05602100A2E4F4)
    
-   方法三：如果方法一和方法二无法解决问题，可以手动删除工程目录下的 .hvigor目录，然后重启并执行 Sync。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/BgKVv0AxSpepZgFAXWkkBA/zh-cn_image_0000002229758233.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=36E3F96D41B047FE1DA6FC47054B37605DA878BDDFF4D0633095B3E06A72AF9E)
