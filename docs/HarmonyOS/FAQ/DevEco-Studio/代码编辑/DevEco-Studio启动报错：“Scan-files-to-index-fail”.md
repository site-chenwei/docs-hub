---
title: "DevEco Studio启动报错：“Scan files to index fail”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-16"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "代码编辑"
  - "DevEco Studio启动报错：“Scan files to index fail”"
captured_at: "2026-04-17T02:03:20.797Z"
---

# DevEco Studio启动报错：“Scan files to index fail”

**问题现象**

在DevEco Studio上打开项目工程时，启动缓慢，且一会儿后报错：“Scan files to index fail”。

**解决措施**

当DevEco Studio打开项目工程时，会启动编辑器Node进程扫描工程代码以建立索引。编辑器Node进程默认内存上限为8G，超过此内存大小时，编辑器Node进程会启动失败，从而报错Scan files to index fail。为避免工程代码量过大导致编辑器启动失败，请根据工程代码量和开发环境内存大小配置合适的Node进程内存上限。内存上限值需要随工程的代码量和复杂程度增长，通常代码量300万行的工程建议配置大于12G，400万行建议配置大于15G，每增加100万行增加3G，可根据具体情况适当增减。

以配置内存上限为12G举例，打开DevEco Studio，通过菜单栏的Help > Edit Custom Properties...，打开idea.properties配置文件。在文件中新增一行 arkts.server.max.old.space.size=12288，然后重启DevEco Studio。编辑器Node进程的内存上限将设置为12288M（即12G）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/jWPhsO3WQ72OL1qVhN_qXg/zh-cn_image_0000002378621596.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=1DF1C9D7956ED22EB694122E64AC113E57203FDD5569075F180B7EABA470A1C5)
