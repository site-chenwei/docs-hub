---
title: "编译报错 “Unknown resource name”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-36"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错 “Unknown resource name”"
captured_at: "2026-04-17T02:03:21.463Z"
---

# 编译报错 “Unknown resource name”

**场景一：**

**问题现象**

工程中模块A引用了模块B，编译模块A时出现错误，提示 "Unknown resource name 'xxxx'"，找不到模块B的资源。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/5sSkLQJlSTWnkVajxA5Zeg/zh-cn_image_0000002229603765.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=52BA3705DC3F7EC1B5360C020E4DA5A27E1A3C04D09AA1318AFE47F5BF96DFB5)

**解决措施**

需要满足以下条件：

1.  资源需放置在模块B目录resource/base路径下，参考链接：[应用资源](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-device-resource#应用资源)。
2.  模块B已安装。
3.  模块A中不能使用相对路径引用模块B的资源，应直接通过定义的模块名称来引用。

**场景二：**

**问题现象**

引用模块的方式不正确，如果引用的是其他模块的代码，也会导致资源未找到的错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/emIZO9HxRfqjnNP8jpigew/zh-cn_image_0000002194158372.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=7B58D4DE8AD0AABD6358F95A515A3A483568C230BF324CA709F7D585A20247D4)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/RjP1BJkZQU-ia9weA8Bd_g/zh-cn_image_0000002229603773.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=FEE5C5568E9A5B075ED43ABB75FA37971BA0E02C6E33993FD01638896975A58C)

**解决措施**

在oh-package.json5中引入该模块。通过定义的模块名称来引用。

如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/Eci2JfEET9iJFEqn_tBthQ/zh-cn_image_0000002194317992.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=8FF690EBD0310387356A519390B92835DAD31CB78D066259D8AE2EB3C0A1B214)

**场景三：**

**问题现象**

HSP A 申请了某个权限并引用了资源。在构建所有依赖 A 的组件时，报错提示找不到 A 引用的资源。

**解决措施**

在引用方的配置文件中手动添加对应资源可以解决此问题。
