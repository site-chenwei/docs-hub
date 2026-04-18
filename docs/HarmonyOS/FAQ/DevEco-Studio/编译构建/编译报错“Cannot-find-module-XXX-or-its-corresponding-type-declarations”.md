---
title: "编译报错“Cannot find module XXX or its corresponding type declarations”"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-4"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "编译报错“Cannot find module XXX or its corresponding type declarations”"
captured_at: "2026-04-17T02:03:21.095Z"
---

# 编译报错“Cannot find module XXX or its corresponding type declarations”

-   **场景一：**
    
    **问题现象**
    
    Stage模板工程编译引用native文件(.so) 提示“Cannot find module XXX or its corresponding type declarations.”。
    
    **解决措施**
    
    当前Stage工程在编译构建阶段新增对native文件（.so）导出符号的语法校验。如果现有工程引用了没有对应声明文件（.d.ts）的native文件（.so），语法校验工具会报错，提示找不到对应的声明文件。
    
    如果出现类似问题，尝试以下解决方法：
    
    1.  在对应cpp目录下新建types/libxxx目录，并在该目录下新增index.d.ts用于声明native文件的类型符号；新增oh-package.json5配置文件用于校验工具的模块查询。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/dysGdbDIRr2C1uceXJpD6A/zh-cn_image_0000002229604373.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=1535CE87F34DCD5327092C4611767F7E74FE9965192C0282CE0E93E4A7F94351)
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/KSjfrI9jSTmw5Lz7dlf6-Q/zh-cn_image_0000002194158980.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=3C72471CF9C9069508F5B9A518BC95BE3981FE8FED786D32382D9A46E1010A9A)
        
    2.  在native文件引用的模块内的oh-package.json5中添加native文件的本地依赖，并根据DevEco Studio提示点击\*\*Sync Now\*\*同步工程，下图以entry模块引用native文件为例。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/kPpltCluRj6XvYROwpzZrQ/zh-cn_image_0000002194318572.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=15EBD43B335B8BB3E3E5B8A47D81F7B0E6FE6643928106A9A5F01FF9D1E04148)
        

-   **场景二：**
    
    **问题现象**
    
    API 11 Stage模板工程编译失败，提示“Cannot find module '@kit.xxx' or its corresponding type declarations”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/trFtq7UlT66kZ1lv2F_hig/zh-cn_image_0000002229758849.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=6370FD62BDC21D6A189F63D63D3964448C5B62C98F56E9129DB778A9E2277A1E)
    
    **问题原因**
    
    出现该问题的原因是使用DevEco Studio NEXT Developer Preview1及之后版本。新创建的API 11 Stage模型的模板文件中，import方式改为import xxx from '@kit.xxx'。若SDK使用的是HarmonyOS NEXT Developer Preview1之前的版本，将会出现编译报错，因为旧的SDK不支持此类方式导入。
    
    **解决措施**
    
    如果出现类似问题，需要对SDK进行更新或更新DevEco Studio。
    
    -   如果使用的是DevEco Studio NEXT Developer Preview1至HarmonyOS NEXT Developer Beta1（5.0.3.300）之间的版本，在菜单栏点击**Tool > SDK Manager**，将SDK更新至HarmonyOS NEXT Developer Preview1及以上版本后，重新进行编译。
    -   如果使用的是HarmonyOS NEXT Developer Beta1（5.0.3.300）及以上的版本，SDK随DevEco Studio软件包安装，无需单独下载，请在[下载中心](https://developer.huawei.com/consumer/cn/download/)下载并使用新版本DevEco Studio。
-   **场景三：**
    
    **问题现象**
    
    引用第三方包，构建失败，提示“Cannot find module 'xxx' or its corresponding type declarations”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/u_FyeIH4QmWYWrNuQAwbiQ/zh-cn_image_0000002229758853.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=1E7F4E816E77D126AB08331BB60E57E584451126BB54AD031D0CBDF3812514FA)
    
    **解决措施**
    
    进入模块级或工程级的oh-package.json5文件，检查第三方包是否已安装。若未安装，执行ohpm install安装。若已安装，检查“main”字段是否配置正确。若未配置或配置错误，需配置为正确的入口文件。
    
-   **场景四：**
    
    **问题现象**
    
    包路径被混淆，代码中又是在引用包路径后面拼接了路径，导致模块引用不到而报错。
    
    例如：
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/6z9iH43KTqu0Ka8FWW86fg/zh-cn_image_0000002194158984.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=09C70D51CF32072379C053C12E7726E08ED2C34F605908B8466C8526A5063826)
    
    代码中这样引用
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/EiHx_a8kQ2qmM3Dx-yX-ig/zh-cn_image_0000002229758861.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=C535F01D80FFC3648285B0158B94574B3CDB5D65364DF6D9F19D33BB7F9ECC97)这样引用会找不到模块，导致报错。
    
    **解决措施**
    
    修改引用方式，采用推荐的方式。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/zAd6LYx9TJCcrvpwIFtTRA/zh-cn_image_0000002194158972.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=5BA661541C84715E90EB195576CBF4EE3E59B76142D44112CFCD9E8AB04C7F14)
    
-   **场景五：**
    
    **问题现象**
    
    被引用模块oh-package.json5配置有误，执行了ohpm install 并且成功地安装了依赖，但是还报错模块找不到。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/FSUP_gKjSYKUrRGlIqVdHQ/zh-cn_image_0000002194158976.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=6D7B4D3D8E7049192242B7D17E206E761EEA507A5EC4FF20FBA1CEF835B132E7)
    
    被引用模块的 oh-package.json5 中配置了错误的types字段。
    
    该字段优先于main字段。 如果 types 字段配置的不存在，就会报错模块找不到。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/l1Hv4wW6Q1SI62SB7QH8ag/zh-cn_image_0000002229604353.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=A9377C3D1D09726DCD01B6A5808FFAEC7AACC59DFFECFE08C7D6E1EB75C7DA58)
    
    **解决措施**
    
    如果该包中没有d.ets声明，可以删除这个字段。配置错误或不存在会导致报错。
    
-   **场景六：**
    
    **问题现象**
    
    oh-package.json5中dependencies中引入模块的名称和实际使用时import的不一致。
    
    在代码中“import”时，应使用大写的“HAR”而不是“dependencies”里配置的“har”。务必保持完全一致，否则在Linux系统中会报错，提示模块找不到。
    
    **解决措施**
    
    引入和使用改成一致。
    
-   **场景七：**
    
    **问题现象**
    
    引用模块的oh-package.json5中main字段值和实际的文件名称大小写不一致。
    
    **解决措施**
    
    将main字段和实际文件名称大小写改为一致。
    
-   **场景八**：
    
    **问题现象**
    
    Stage模板工程编译构建失败，提示“Cannot find module '@bundle:rollup\_plugin\_ignore\_empty\_module\_placeholder' or its corresponding type declarations”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/6PqEIvBkQm6MX_ggJ1Jcrw/zh-cn_image_0000002229758841.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=52F4A6079B382BC499BA3826AF8A4082930F0F3FAD69EDCDAA67A1F1917DD3BC)
    
    **解决措施**
    
    该问题源于工程引用了无对应实现文件的.d.ts声明文件。
    
    1.  在build目录搜索\`rollup\_plugin\_ignore\_empty\_module\_placeholder\`定位问题模块。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/AA0O_hkARDaYAnhaodBUXQ/zh-cn_image_0000002194158956.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=8FCDB28C06DFDA9319308B1B7F005752D1B4E3C92DF9A6679C209232FA70D219)
        
        在输入栏中输入“rollup\_plugin\_ignore\_empty\_module\_placeholder”，找到问题模块的中间文件。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/vijCKIupSn2yv-P-xpYy5g/zh-cn_image_0000002194158964.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=0FE31583DE8EAA5A08272CCEABD8CA0D3DBE8F36FD597756FA28679FC6B95E63)
        
    
    2.  在引用类型文件中通过添加type显式声明符号类型。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/-RK5l6DCREeX9-ocrMI5kw/zh-cn_image_0000002229758865.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=F93953E1E2CAE384081E5107512B73E8990BE454E4EE8EC1AAD5CC5928790DC4)
        
    
    3.  同时排查是否从d.ts/d.ets中引用值类型符号。禁止在声明文件中声明值变量。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ZXWrg196R3ybko5vZNfpog/zh-cn_image_0000002194158968.png?HW-CC-KV=V1&HW-CC-Date=20260417T020321Z&HW-CC-Expire=86400&HW-CC-Sign=C70CC281F4310D8937C604F47C4430E0DB136C187B08F001F9628FB57BF0B7F8)
