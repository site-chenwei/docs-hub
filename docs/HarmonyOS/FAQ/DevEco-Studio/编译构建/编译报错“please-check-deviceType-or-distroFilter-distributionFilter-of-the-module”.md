---
title: "编译报错“please check deviceType or distroFilter/distributionFilter of the module”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-20"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“please check deviceType or distroFilter/distributionFilter of the module”"
captured_at: "2026-04-17T02:03:21.270Z"
---

# 编译报错“please check deviceType or distroFilter/distributionFilter of the module”

**问题现象**

HarmonyOS DevEco Studio编译时出现错误，提示如下之一：

-   Module: (xxx) and Module: (xxx) are entry, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/-Q0Ct-X8ScKutGTrjQLZsQ/zh-cn_image_0000002229604261.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=1FDB9573816138343CE2CE522BF7A31E18C6B6C774B2CA74DDC4C178C39F061A)
    
-   Module: (xxx) and Module: (xxx) have the same moduleName, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/DQ6VyWC7TuWFUj9WFbiRww/zh-cn_image_0000002194158880.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=BF3020A5C42C66C4849A4570995B4EF347B4D698B687693F17692D55BF712A4F)
    
-   Module: (xxx) and Module: (xxx) have the same packageName, please check deviceType or distroFilter of the module.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/trOnaL0rSmaksK1vn7TM2Q/zh-cn_image_0000002194318488.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=5025E09E18B28F1525E792E16C69B1169A669FA2300B1673FA591B9DF3DB432A)
    
-   Module: (xxx) and Module: (xxx) have the same ability name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/h6HmFw7PRX-_It-rdvwj7A/zh-cn_image_0000002194318492.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=0B7F43C1B9CF6A9DCCD002FC1A5C3F3D0D011511336186F242300D95678A9EF4)
    

**解决措施**

-   可能是打包时工程未满足HAP唯一性校验逻辑，请参考[HAP唯一性校验逻辑](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-verification-rule)修改工程配置，满足校验逻辑即可正常打包。
-   如果工程中仅有一种设备类型，请确保工程级build-profile.json5文件中，同一模块的不同目标target的applyToProducts字段对应的product不相同。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/SxzLZL9DSZuSKidQ9pBoig/zh-cn_image_0000002194158884.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=2F6D4F9A8E62020A8A5C2137B6D270CDC830525C3D85C6DF446C38ED97A7EDB7)
