---
title: "编译报错“Failed to generate test project build system”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-21"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Failed to generate test project build system”"
captured_at: "2026-04-17T02:03:21.272Z"
---

# 编译报错“Failed to generate test project build system”

**问题现象**

执行多模块Native模块构建时，出现“Failed to generate test project build system.”错误信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/H4Jx5ngzR9eZHhpAolqmgA/zh-cn_image_0000002194158584.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=913C5EE7F51081CFEF545A97ACE4094E2DDA97CF7D6BDF5250DC466A6B9EDDC9)

**解决措施**

请删除报错模块下的.cxx文件夹，然后选中需要构建的模块，执行Make Module {moduleName}完成单独构建。注意：此方案需避免多模块并行构建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/e_gocmvxRj6DtgqCKwhmqg/zh-cn_image_0000002229758457.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=398BB05D2EAEFC750F436476EF237C5E19C33667E62E87CF50684FBBAADD2034)
