---
title: "DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-188"
menu_path:
  - "FAQ"
  - "DevEco Studio"
  - "编译构建"
  - "DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI-X工程构建app报错"
captured_at: "2026-04-17T02:03:23.402Z"
---

# DevEco Studio 6.0.0 Beta1 及以上版本DevEco Studio ARKUI-X工程构建app报错

**问题现象**

构建app报错：“Could not open settings generic class cache for settings file”

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/kTwyB4n9QZGsaYkVYY0-9g/zh-cn_image_0000002381980508.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=1A313BEFA1C12605C0979738A540FF8393A1E6A571313CD2EE2548EC078D804C)

**常见错误场景**

当前工程使用的是低于DevEco Studio 6.0.0 Beta1 版本的DevEco Studio创建的。

**问题原因**

DevEco Studio 6.0.0 Beta1版本DevEco Studio内置的Java版本为21，当前Gradle的版本低于Java21配套的版本。

**解决措施**：

-   **方式一：升级gradle版本**
    
    修改Gradle-wrapper.properties中的distributionUrl，升级为8.4版本。
    
    ```screen
    distributionUrl=https\://repo.huaweicloud.com/gradle/gradle-8.4-bin.zip
    ```
    

-   **方式二：指定使用Java17**
    
    如果本地有JDK17，可以在Gradle.properties中通过org.gradle.java.home变量指定使用Java17。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/ul0O0TXrQ3KqPQ5DdoAFsQ/zh-cn_image_0000002415859685.png?HW-CC-KV=V1&HW-CC-Date=20260417T020323Z&HW-CC-Expire=86400&HW-CC-Sign=8185D69190FDE630D4A1C499F7567C621CA07DB758F18546BBDCFFADB766064F)
