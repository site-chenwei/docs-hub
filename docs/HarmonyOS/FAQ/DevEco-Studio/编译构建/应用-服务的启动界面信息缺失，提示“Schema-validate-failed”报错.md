---
title: "应用/服务的启动界面信息缺失，提示“Schema validate failed”报错"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-16"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "应用/服务的启动界面信息缺失，提示“Schema validate failed”报错"
captured_at: "2026-04-17T02:03:21.237Z"
---

# 应用/服务的启动界面信息缺失，提示“Schema validate failed”报错

**问题现象**

在工程同步或编译构建时，出现“Schema validate failed”的错误提示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/aLrjjfUzSmW4OY_K09cyPQ/zh-cn_image_0000002229604277.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=B35EAD39F4AED21B77C5EC70EADB5E93641B52870BF02AD906D6BF68D0740AB8)

**解决措施**

在开发应用/服务时，创建工程后，默认设置了启动界面信息。如果开发者误删其中某个字段，将导致报错。下面以重新设置启动界面信息为例，为提高冷启动性能，可以通过以下方式设置启动界面的图标和背景颜色。

1.  在模块的**resources > base > element**目录下，右键点击并选择**New > Element Resource File**来创建资源文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/3qhatSeYSBWwAXssECKbrA/zh-cn_image_0000002194318512.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=B1677FA1B990B2E7BAEE80401E4D9DB8C8B7B1777A8C8FA512774C61DAB2F6CA)
    
2.  在弹出的对话框中，开发者可以自定义“File name”，例如 color；“Root element”请选择 **color**。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/lNoPDp8uQzqRuNs5ebiJ8Q/zh-cn_image_0000002194158900.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=739AC706ADB6EE156959723128C4D464759A12E3431AD49D67922285060B7C24)
    
    创建完成后，color.json文件如下图所示：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/wGkbMTzFS5KNmSK3f-R3Cg/zh-cn_image_0000002194318508.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=92B16D47FC920362739B672FCBED73C8259FFA5A1C955F5F7244C7B658AB8F4D)
    
3.  将[2](#zh-cn_topic_0000001233028585_li124901748185712)创建的color.json文件拷贝至模块的**ohosTest > resources > base > element**目录下。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/10jbkURoReafrrZHtr2Oxw/zh-cn_image_0000002229604281.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=AB25B32444AEFECBA30282CB6A9D101B70EEF17E6B0DD3386A9CF4E4F74E7F88)
    
4.  在模块的**src > main > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段。若缺少任一字段，将出现ERROR: Schema validate failed报错。startWindowIcon字段索引模块下**resources > base > media**中的图标资源，startWindowBackground字段索引**resources > base > element > color.json**中的颜色。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/_n1LUW9BSA-vu6D2m_490A/zh-cn_image_0000002194318504.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=4C72F8BB6CDBCBF3635F2381AC6E360112194611D4EB073E414FD0DC66F54BFD)
    
5.  在**src > ohosTest > module.json5**文件的abilities数组中，添加startWindowIcon和startWindowBackground字段。其中，startWindowIcon字段引用模块ohosTest下 **resources > base > media**中的图标资源，startWindowBackground字段引用 **resources > base > element > color.json**中的颜色。
