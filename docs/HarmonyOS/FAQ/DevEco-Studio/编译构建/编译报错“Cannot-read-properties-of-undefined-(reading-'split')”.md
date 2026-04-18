---
title: "编译报错“Cannot read properties of undefined (reading 'split')”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-184"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Cannot read properties of undefined (reading 'split')”"
captured_at: "2026-04-17T02:03:23.351Z"
---

# 编译报错“Cannot read properties of undefined (reading 'split')”

-   场景一：
    
    **问题现象**
    
    当前使用的DevEco Studio版本与SDK版本不配套，导致DevEco Studio抛出异常：“TypeError: Cannot read properties of undefined (reading 'split')”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/fmsSOYaQRnOiUvFGalIcyA/zh-cn_image_0000002264138776.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=00EBD8298573D4714F78C88EAE24E3C065176D97D15EC572BC5E250DD44C0663)
    
    **解决措施**
    
    1.  访问华为[开发者官网](https://developer.huawei.com/consumer/cn/download/deveco-studio)下载最新版DevEco Studio。
    2.  使用新版本DevEco Studio打开待迁移项目。
    3.  根据DevEco Studio自动弹出的迁移提示进行操作。
        
        -   点击“Migrate Assistant”功能。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Qo9uGrftQceco6Xa_GaSEw/zh-cn_image_0000002264083104.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=B2E227A80059AF0E84F32EF97BEFC4F435F97BB3DCC1858669CB971578376BD8)
        
        -   从版本列表中选择目标迁移版本。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/3fvjeIE_Ss2fBRboxgYTUg/zh-cn_image_0000002264081160.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=8295A3079490D45DAB8CA46D69F98F0415620DE0D81859A9A76221586453DD96)
        
        -   按照向导完成项目迁移流程。
        
-   场景二：
    
    **问题现象**
    
    当工程级 build-profile.json5 文件未配置工程外模块依赖，而模块级 oh-package.json5 声明了工程外模块依赖并在代码中实际引用时，编译阶段会抛出异常：”Error: Cannot read properties of undefined (reading 'split')”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/Im2nU9dBTZCM2ersZV8vCA/zh-cn_image_0000002264140556.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=DA554C988F61B14FACE324107D5D005379BFB73ADDA14643A47A2B5A1AFA0A3F)
    
    **解决措施**
    
    1.  检查下报错子模块中所引用的依赖，确保目标模块已在工程级 build-profile.json5 文件的 modules 字段中正确声明。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/1BjY7ZCFTy6hKGuH1xRU9Q/zh-cn_image_0000002264140648.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=EE80EA7BB3A9F5E41AF8F26A904549576E7F70B879CCB934F96566D58DFFC344)
        
    2.  确认当前子模块的 oh-package.json5 中，该模块已添加到 dependencies 依赖列表。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/zjhR-g4gQHWJAtQiX_m4ng/zh-cn_image_0000002298773813.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=4663D6F3134CE8DEA97455F7F4F58AA7C1B00917374CA26E0A3E0695DB1B50D8)
        
    3.  若发现配置缺失，请手动补充完整。删除项目中的 oh\_modules 缓存目录，然后重新执行编译。
        
-   场景三：
    
    **问题现象**
    
    在HAP依赖字节码HAR进行编译的场景下，当import语句中的模块别名与dependencies中声明的别名大小写不一致时，编译系统将无法正确识别该依赖为字节码HAR，进而导致编译错误。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/mvUqq3dZQZ-xTwQTgp-YZg/zh-cn_image_0000002264083960.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=20F62B0B0501AC70E387849B3E49E80B18743ED26308AE19741C3A74866B8D1B)
    
    **解决措施**
    
    请检查并确保所有import语句的模块别名与其在dependencies中的声明保持完全一致的大小写格式。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/WhkGdmqMT6aqkmV04OkgXw/zh-cn_image_0000002298661041.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=2DE80FF48B96D417BF55B9A4246327BEDA28E7A25C8CA38E712D5BE44F59933C)
    
-   场景四：
    
    **问题现象**
    
    在编译字节码HAR时，若将依赖配置于devDependencies下，hvigor构建系统在编译阶段不会收集devDependencies中的依赖项，导致依赖解析失败并引发编译错误。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/QRvtyAnsRqWSV9Y51wYJcQ/zh-cn_image_0000002264141304.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=06C80B86C6104BE6792F973B2363BEF386074B43372DBABA1EAD29BC8AFF911B)
    
    **解决措施**
    
    请将依赖项从devDependencies移至dependencies。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/mXraUmx4R1q2Vl6ztSpUyA/zh-cn_image_0000002264084432.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=0359ACC40D960A8CC56D7DC414F3D8B26B0CFF6663AAB4B5CF04AAF14CFAF5C0)
