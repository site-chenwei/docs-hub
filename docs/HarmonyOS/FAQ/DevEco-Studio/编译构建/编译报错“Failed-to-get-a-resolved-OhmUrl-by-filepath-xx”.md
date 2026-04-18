---
title: "编译报错“Failed to get a resolved OhmUrl by filepath xx”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-10"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Failed to get a resolved OhmUrl by filepath xx”"
captured_at: "2026-04-17T02:03:21.099Z"
---

# 编译报错“Failed to get a resolved OhmUrl by filepath xx”

-   **场景一：**
    
    **问题现象**
    
    如果工程在本地可编译成功，压缩后拷贝到其他环境中再打开该工程编译构建失败，提示 “ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xx”。
    
    **解决措施**
    
    该问题源于工程中存在oh\_modules目录。由于oh\_modules中包含软链接，压缩后软链接失效，导致在其他环境中编译时无法找到对应的文件。
    
    删除工程中的oh\_modules，执行File > Sync and Refresh Project。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/NPQmVOhBQ12Cu_AJhf1NHg/zh-cn_image_0000002194158588.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=47DE59D7E5712AF75642DED3D9C6A67090AB7616FE07759FB1E9FE0E21DC3600)
    
-   **场景二：**
    
    **问题现象**
    
    当配置第三方包依赖时，如果将依赖配置到devDependencies，而源码中又引用了这些依赖中的 API，会导致编译失败。例如，第三方包@hms-security/ucs-appauth将依赖@network/gr配置在devDependencies中，源码中使用了@network/gr的 API 时，编译会失败，提示错误信息：“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/TqfrYKRbSBSQWJY4gXGOkA/zh-cn_image_0000002229603977.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=DDFC2BC2F2EE9F9579D3EE4E5E0DBED2A2342BB13C9C6EAD0E2891985FFE9312)
    
    **问题确认**
    
    1.  进入上面标黄色的源码文件中，可以看到依赖有红色告警信息。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/hR3sEWBiQnCEmAmePVQGgA/zh-cn_image_0000002194318188.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=2F0FEBCDE785BD7FBDCE97199F6E476D0BBB369553EE0C7003D1BF30CD469EB4 "点击放大")
        
    2.  进入包下的oh-package.json5文件，查看依赖配置为devDependencies。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/u_o_LogMQlGpMgtpmxEA1g/zh-cn_image_0000002229603989.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=1A87827C78A95B0F8DF5702DFB3D7DE0BF9EF27C538301A025D50F7D11CE5614)
        
    
    **解决措施**
    
    -   向开发团队建议：运行时的依赖不应配置在devDependencies中。
    -   在依赖上层引入对应的devDependencies中的第三方包规避此问题。

-   **场景三：**
    
    **问题现象**
    
    DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。
    
    **问题确认**
    
    检查工程目录下的build-profile.json5文件中modules字段配置的srcPath路径是否与实际路径不同，以及是否存在大小写不一致的问题。
    
    **解决措施**
    
    将build-profile.json5文件中modules字段的srcPath路径与真实路径保持一致。
    
-   **场景四：**
    
    **问题现象**
    
    工程A以相对路径引用了工程B的模块，这种引用会导致报错。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/ihVdhaBrQm2BSmUD7p-xCA/zh-cn_image_0000002194318200.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=00499CB20DB3EA71EBF94E3A3B17D0268CE7B2236771DA20D7C36FCE46239132)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/XMOUztP6R2ebBu_Bv9O76w/zh-cn_image_0000002194158572.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=0978CA472D382CE2D0A80C969D6D6CE7566A52E19291EE65CE87766161EC55BD)![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Labjn9p4QWWf8wpvyo6pDg/zh-cn_image_0000002229758449.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=4AAFAA2D4ADFB3F7A3ECB5A2E9A23FBBFA0CA3D7A9F6DB9BA123BCAA8E985501)**处理措施**
    
    -   将工程B的har转换为工程A的一个模块引用。
    -   把工程B的har提前打包，在A中 以.har的方式引用。
    -   上传到仓库，以版本号的方式引用。
-   **场景五：**
    
    **问题现象**
    
    DevEco Studio编译失败，提示“Error Message: Failed to get a resolved OhmUrl for 'hvigor\\\_ignore\\\_xxxxx' imported by xxx”。
    
    **处理措施**
    
    如果hvigor\_ignore\_xxxxx所在的模块是一个har模块，需要排查oh-package.json5中是否存在“"packageType": "InterfaceHar"”，如果存在，请删除“"packageType": "InterfaceHar"”。
    
    如果hvigor\_ignore\_xxxxx所在的模块是一个hsp模块，需要排查${模块路径}\\build\\default\\cache\\default\\default@CompileArkTS\\esmodule\\${debug/release}\\filesInfo.txt文件中是否存在hvigor\_ignore\_xxxxx路径，如果存在，可将hvigor\_ignore\_xxxxx路径所在的模块或包添加到当前编译模块oh-package.json5的dependencies中临时规避。
    
-   **场景六：**
    
    **问题现象**
    
    DevEco Studio编译失败，提示“Failed to get a resolved OhmUrl for‘xxx’imported by‘yyy’”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/xTQzN8dxQRaEOztGVOV48Q/zh-cn_image_0000002194318204.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=4C37B737A2A441E07A3D64330432A3EA86CF9E4458C95F6F4F7E124B9D475B55 "点击放大")
    
    **问题确认**
    
    1.  检查yyy所在模块是否为[字节码HAR](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-build-har#section16598338112415)，并查看工程级build-profile.json5的useNormalizedOHMUrl是否为true（缺省默认值为false）。如果为true，则默认构建字节码har。
    2.  如果yyy模块是字节码har，请检查xxx依赖是否已配置在工程级oh-package.json5的dependencies中，但未配置在yyy模块级oh-package.json5的dependencies中。
    
    **处理措施**
    
    -   将xxx依赖配置到yyy模块oh-package.json5的dependencies中。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/HejtF_XVSdq5kkVnvEafXQ/zh-cn_image_0000002229603981.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=85B82AE34C7D08E4C6BE1F462C82C201B478D247B931146E914A211A75EE4F45 "点击放大")
        
    -   将yyy模块改为非字节码har，在模块级build-profile.json5文件中添加byteCodeHar字段并设置为false。

-   **场景七：**
    
    请确认当前使用的DevEco Studio和SDK版本是配套的，点击菜单栏**Help > About DevEco Studio**，**Help > About HarmonyOS SDK**分别查看DevEco Studio和SDK版本，版本配套关系请参考[版本概览](https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-502-release)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/wSEtNEXYTxawsYf8IrisSA/zh-cn_image_0000002229603985.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=22874966FF85FCFB5836E21EF03F378D3DAC428865BE1BE6EA96DE4CB28D2EFC)
    
-   **场景八：**
    
    **问题现象：**
    
    DevEco Studio编译失败，提示“ERROR: ArkTS:ERROR failed to execute es2abc ERROR: ArkTS:ERROR Failed to get a resolved OhmUrl by filepath xxx”。
    
    **处理措施**
    
    该问题由工程中引用了非标准模块目录（目录内无module.json5）引起，如下图所示。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/TiM017rHT7qJT6DSPcax9A/zh-cn_image_0000002194318192.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=9F7F2E81FB4EAD8BAC97DE9D0D66CDE78F6F3ABE19D5AC0C08A777F9913E06B7)
    
    请新建Static Library模块，并将utils/common里面的代码迁移至Static Library模块内，并使用HAP引用HAR方式进行模块间引用。
