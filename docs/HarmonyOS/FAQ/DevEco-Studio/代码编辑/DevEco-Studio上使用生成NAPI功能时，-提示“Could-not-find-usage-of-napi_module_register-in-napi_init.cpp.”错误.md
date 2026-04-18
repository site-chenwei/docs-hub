---
title: "DevEco Studio上使用生成NAPI功能时， 提示“Could not find usage of napi_module_register in napi_init.cpp.”错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-coding-15"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "代码编辑"
  - "DevEco Studio上使用生成NAPI功能时， 提示“Could not find usage of napi_module_register in napi_init.cpp.”错误"
captured_at: "2026-04-17T02:03:20.809Z"
---

# DevEco Studio上使用生成NAPI功能时， 提示“Could not find usage of napi\_module\_register in napi\_init.cpp.”错误

**问题现象**

右键单击函数， 在弹出的菜单中依次选择 Generate... > NAPI， 生成胶水代码报错。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/j9zp99j-SpeVHFWbXFAKmg/zh-cn_image_0000002229758437.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=22F95ED81956F99ED7393F15647FED2E922D76611856F2BCED3628761B12BBD3)

**解决措施**

检查napi\_init.cpp文件的RegisterEntryModule函数中是否调用了napi\_module\_register函数。napi\_module\_register的参数类型为napi\_module\*, napi\_module初始化示例代码如下图所示。然后重新生成NAPI。

字段含义：

nm\_version: N-API模块版本

nm\_flags: 模块的属性标志

nm\_filename: N-API模块的文件名

nm\_register\_func: 注册函数

nm\_modname: 模块名称

nm\_priv: 私有数据指针

reserved: 保留字段

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/UicaMyxxRCmDOut8GwH7aA/zh-cn_image_0000002519864254.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=D5C7F3662F02F52F2C62A8ABFE13E3775425EC8FF28D23BB8E3340B6557E11DA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/FqBsHXBBS3y50eG0IlI83Q/zh-cn_image_0000002229603969.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=6EB289824E6250994CB43B4121B01686DC3492FC6AFE2EF699A051D412A6CE76)
