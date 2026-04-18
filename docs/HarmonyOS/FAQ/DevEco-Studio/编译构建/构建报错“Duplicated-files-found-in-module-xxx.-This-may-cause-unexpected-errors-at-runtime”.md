---
title: "构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-109"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”"
captured_at: "2026-04-17T02:03:22.372Z"
---

# 构建报错“Duplicated files found in module xxx. This may cause unexpected errors at runtime”

**问题现象**

编译构建时，出现错误信息“Duplicated files found in module xxx. This may cause unexpected errors at runtime”。

构建时存在不同版本的同名SO文件会导致问题。例如，将har模块产物中的SO文件拷贝到entry模块的libs目录下，此时har模块和entry模块中都有一个名为libhar.so的文件。如果再配置entry依赖har，构建entry时就会出现错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/5r6tzURlQkO1oF92nvKJ_Q/zh-cn_image_0000002194318620.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=9BB6815DFCA57CD1F6B8EA382D356D6B29E9C339A1FA6D271DB6E13DF17BB8C6)

**解决措施**

使用select、pickFirsts、pickLasts等配置项选择要使用的.so文件。select提供对 native 产物的精准选择，优先级高于excludes、pickFirsts等配置项。pickFirsts和pickLasts按照.so文件的优先级顺序打包，优先级顺序基于依赖收集的顺序，越晚被收集的优先级越高。

具体可参考：[模块级build-profile.json5文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-profile)。

在entry/build-profile.json5中，配置select选中har模块中的so文件，package选中包名为har的模块，include选中libhar.so文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/BzSVHB3-T62Uoz3A0b6msg/zh-cn_image_0000002194159000.png?HW-CC-KV=V1&HW-CC-Date=20260417T020322Z&HW-CC-Expire=86400&HW-CC-Sign=C66205BADA6A5B1E3FD74989CFAF276E8472D824B90843FB4CCD7C5565AA9D31)
