---
title: "编译报错“Error: open 'xxx\\libimage_transcoder_shared.dll' failed”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-181"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Error: open 'xxx\\libimage_transcoder_shared.dll' failed”"
captured_at: "2026-04-17T02:03:23.308Z"
---

# 编译报错“Error: open 'xxx\\libimage\_transcoder\_shared.dll' failed”

**问题现象**

Windows下编译工程出现错误，提示“Error: open 'xxx\\deveco-studio\\sdk\\default\\hms\\toolchains\\lib\\libimage\_transcoder\_shared.dll' failed”，加载dll失败。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/QmoxJqh6TAaQwxNu6dTdNQ/zh-cn_image_0000002194158948.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=A6EA688C46A1275749C46E19088CD2EDE000CCB97B0B013CCE2F49CE46C528ED)

**可能原因**

1、系统在环境变量中找不到libimage\_transcoder\_shared.dll及其依赖的第三方库路径。

2、用户环境变量或系统环境变量中的某些路径包含权限受限或损坏的文件，这些文件无法被正常访问。如果这些路径在环境变量中的顺序排在libimage\_transcoder\_shared.dll之前，系统在加载 DLL 时会按顺序搜索环境变量，并首先访问这些出错的文件。

例如，用户环境变量中包含%USERPROFILE%\\AppData\\Local\\Microsoft\\WindowsApps。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/ZDU_ajR4SWWvr1Wq2MaEaw/zh-cn_image_0000002229758829.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=2BC28F6DDF37CDDC7640214938323751FC94A4231E59D2195724110B2A25653D)

该路径的文件无法访问。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/k4aQn8msSqeOND_5xy0zbw/zh-cn_image_0000002194158944.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=D38767EFD8AB456A7C562C0899EE084B1700A9CB7CFABFD013E475854AB579DB)

**解决措施**

1、将报错的路径xxx\\deveco-studio\\sdk\\default\\hms\\toolchains\\lib和xxx\\deveco-studio\\sdk\\default\\openharmony\\previewer\\common\\bin手动添加到系统环境变量的最前面。

2、检查用户环境变量和系统环境变量中的所有路径，确保这些路径下的文件均可访问。可以通过尝试修改文件（如覆盖、压缩等）来观察是否有报错。将无法访问的路径从环境变量中删除。
