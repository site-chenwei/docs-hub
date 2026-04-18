---
title: "修改代码后使用Hot Reload不支持情况说明"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-20"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "应用调试"
  - "修改代码后使用Hot Reload不支持情况说明"
captured_at: "2026-04-17T02:03:24.626Z"
---

# 修改代码后使用Hot Reload不支持情况说明

**问题现象**

执行热重载过程中，如果当前修改不支持热重载，控制台会打印蓝色重启链接，提示重新安装并重启。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/x95dN7xaSfKmx9gicUjXGA/zh-cn_image_0000002194318220.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=3F44041C68CABC9AB48914FF5CB131A1F71928BB40B04B2BB168DBDE83B887A1 "点击放大")

**解决措施**

DevEco Studio的热重载功能支持特定的代码场景。如果修改的代码超出支持范围，系统将提示“当前修改不支持”，并要求重启。具体支持的代码范围，请参阅[Hot Reload使用约束](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hot-reload#section995453874915)。

**常见不支持代码场景**

-   不支持@Entry装饰器的struct Index内成员变量和成员函数的新增或修改。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/R1bL3Wq4RbGvQd7ZUEzLnA/zh-cn_image_0000002229604013.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=64443FA92EFC485D200C33D20B027E2FE30CC944B0CF27CFCF9656F4451F31F5 "点击放大")
    
-   不支持@Entry入口文件内class成员函数的新增。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/5-fOXddfSVmmw8jecK8qdA/zh-cn_image_0000002194158608.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=E7F86D3DA2DEE63ED911ECB734E389EF57CDDAABBF05925D9A4B8D69A0148033 "点击放大")
    
-   不支持@Entry入口文件内枚举的修改。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/ngRjK9fwQyur5YdTcnoLHA/zh-cn_image_0000002194158604.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=FF8C6C8AF70336A023E8181FF34F16F180D90517AD43EDA8B1B6DA5B61528D12 "点击放大")
    
-   不支持import未加载的模块的新增、修改。
    
    若一个代码文件在热重载启动时未被当前文件导入，则不支持在热重载过程中新增对该代码文件的导入。如下图所示，TestC.ets在热重载启动时未在Index.ets中导入，则在热重载过程中不支持在Index.ets中新增导入TestC.ets的语句。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/boetjiOIQv-JquNYDA2jPw/zh-cn_image_0000002229604005.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=D64E46AA9120A7C37320F9AEB8A9B503659447756CEDA7F5D4D2217A7E86A7A0 "点击放大")
    
    如果热重载启动之前import语句处于置灰状态，此文件在编译过程中将不会被编译，属于未加载的模块。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Lj7ilbXsSzSfVLNd4OCHoA/zh-cn_image_0000002194318228.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=2AB29A71B65FE409CE0F9344FD7BC298DE359922C118BCABE0F4CDA2B9689396 "点击放大")
    
-   不支持顶层闭包变量的修改（但支持顶层闭包的新增、删除）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/H2PJ3LuSQQus-WEPoxMc4w/zh-cn_image_0000002229758481.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=BF4C1B7BCFFB5B01A85040794015561FF11380BDD0BC67BCC95495716EF41CB5 "点击放大")
    
-   支持class类继承，但class继承类和被继承类都不可以放在@Entry入口文件中，建议将class写在非@Entry入口文件中。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/iuar2DnKSgOmQ8-H7HwnuQ/zh-cn_image_0000002229604009.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=B86553767744CD4AD5DC9278615A215B7927003231AB402B0D47FA7894747863 "点击放大")
    
-   不支持@Entry入口文件内大部分装饰器的修改。
    
    当前Hot Reload不支持大部分装饰器的修改。@Entry入口文件内支持@Styles装饰器的新增和修改，支持@Builder装饰器的修改，但不支持新增，不支持@State装饰器的新增和修改。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/nvmPTy3URfC-X6-rvaAhtw/zh-cn_image_0000002229758473.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=B554E9F44D77508A70ED708B7F9507945CBA9BDA63E1E156321927A681F1E412 "点击放大")
    
-   不支持在@Entry文件内新增、修改其他struct自定义组件。建议以import方式引入。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/GWU1vHB3RgewgFYY6rOxiw/zh-cn_image_0000002194318224.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=B4EDFC49E9244FF349F17EF59750D8AAD57A92D078A5B3FEA99E3D29229C54F7 "点击放大")
    
-   不支持在@Entry文件内新增、修改与@State变量重名的class或函数。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/HpSlF9ZNTnilpoGn1czY5g/zh-cn_image_0000002194318216.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=3A219AAB6A123670066B13E365CB0F92C75D67A7D513598D1F27346F2CF5DD6F "点击放大")
    
-   不支持修改非ets/ts代码文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/_sfYzT9XRqev_WjIdaZAvg/zh-cn_image_0000002229758489.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=5AC6AC466EE6D27D568D557169B1377DE9E62CD31E5FB308CB9191270F27E8C1 "点击放大")
    
-   不支持修改worker线程文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/woaGTfbOTsiqAW2y8ipS8g/zh-cn_image_0000002194158612.png?HW-CC-KV=V1&HW-CC-Date=20260417T020325Z&HW-CC-Expire=86400&HW-CC-Sign=7F04F944E9F4E780DE210D154A411F5CA8D1529BFC92D7766AF332416CE6FEF8 "点击放大")
