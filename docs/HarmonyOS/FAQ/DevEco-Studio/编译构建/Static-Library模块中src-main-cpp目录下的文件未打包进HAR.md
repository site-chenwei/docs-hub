---
title: "Static Library模块中src/main/cpp目录下的文件未打包进HAR"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-23"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "Static Library模块中src/main/cpp目录下的文件未打包进HAR"
captured_at: "2026-04-17T02:03:21.327Z"
---

# Static Library模块中src/main/cpp目录下的文件未打包进HAR

**问题现象**

点击**Build > Make Module ${libraryName}**编译构建生成HAR后，发现构建产物中未出现cpp目录下的文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/k-hjAAnPSjSrs2V9aIMmlA/zh-cn_image_0000002229758217.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=36E6A8B5809AC643E5D930DDC68F2CC3CBAC9E3867FE6BEBEA4F8D9AAA1D6A6A)

**解决措施**

如果使用的Hvigor为2.5.0-s及以上版本，在编译构建HAR的过程中，仅会将dependencies内处于本模块路径下的本地依赖打包进.har文件中，devDependencies里的依赖不会打包进.har文件中。

请将相应的本地依赖移至dependencies中，然后重新编译。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/NHteUZwnR52nviVLcqXR1g/zh-cn_image_0000002229603749.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=3BC50BE3A04ECD48559C983746EF6640377D6432046458329A65B3A1BBD4A02B)
