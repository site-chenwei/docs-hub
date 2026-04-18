---
title: "应用UI生成"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-generator"
menu_path:
  - "指南"
  - "使用AI智能辅助编程"
  - "应用UI生成"
captured_at: "2026-04-17T01:36:44.508Z"
---

# 应用UI生成

UI Generator用于快速生成可编译、可运行的HarmonyOS UI工程，支持基于已有UI布局文件（XML），快速生成对应的HarmonyOS UI代码，其中包含HarmonyOS基础工程、页面布局、组件及属性和资源文件等。

#### 使用约束

建议使用DevEco Studio 5.0.3.700及以上版本。

#### 启用插件

1.  在DevEco Studio菜单栏，点击**File > Setting****s...**（macOS为**DevEco Studio > Preferences****/Settings**）**\> Plugins**，在Installed列表中找到UI Generator插件，点击**Enable**启用。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/mFUonuBNTgimp6Bcjj2LSw/zh-cn_image_0000002530913614.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=5200D099AA3E52B5D91FFE6243FC8D8D18D54DEB78CBFFAD83D98432CE786D96)
    
2.  单击OK并关闭设置窗口，插件启用成功。

#### 开始使用

1.  在DevEco Studio菜单栏点击**Tools > Generate Project From...**打开UI Generator工具，首次使用需要阅读并确认用户协议，确认后可继续使用。
2.  输入待配置项路径，点击**Next**进入下一步。
    
    | 
    待配置项
    
     | 
    
    说明
    
     |
    | :-- | :-- |
    | 
    
    Installation package path
    
     | 
    
    待转换的APK应用包的路径，请提供未混淆的Debug版本应用包。
    
     |
    | 
    
    SDK path
    
     | 
    
    等于或高于编译应用包所使用版本的SDK路径。
    
     |
    | 
    
    Git Bash path
    
     | 
    
    Git Bash工具存放路径。若本地已下载安装Git Bash，插件将自动获取其路径。
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/2U940vDuTcCq1IG5Ekypgg/zh-cn_image_0000002561833533.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=84AFDAA8A3D262705566584491E10ECBE9BF0B6E6966DD52D4A6AA1BE86E3FFF)
    
3.  选择将要生成的XML页面（可在搜索框进行搜索），勾选后点击向右箭头将选中的XML导入至右侧。点击**Next**开始生成。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/UTNy3dxVQlihQvjjHn3LkQ/zh-cn_image_0000002530753612.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=6379CB4ECBE6B36EF8141AD42A6F813AFAFA2DD5079FB0D648FFBE5FA110530D)
    
4.  配置输出工程待配置项，点击**Finish**进行生成。
    
    | 
    待配置项
    
     | 
    
    说明
    
     |
    | :-- | :-- |
    | 
    
    Destination Path
    
     | 
    
    生成新工程的保存路径（默认生成到用户目录下UIGenerationProjects，用户可根据需要自行更改）
    
     |
    | 
    
    Compatible SDK
    
     | 
    
    生成的新工程所使用的SDK版本
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/JzxY6nZTSaqTJDSluIR1iA/zh-cn_image_0000002561833541.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=97A0628D3316168E3EDBB68E766B8C8275D9CA1AEB661D5EDB24CC2EBAD671AE)
    
5.  （可选）如果所选XML无有效根节点，需要选择根节点信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/XcFcfWLIQVeF4GUNWz1S8w/zh-cn_image_0000002561833535.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=AFDABF08594C1DA7E86C7810BD4A46E709C624C6AB2B1EDB55A0056F77AC36D9)
    
6.  点击**Finish**，在弹窗中点击确认，打开新工程。
    
    生成的页面位于entry > src > main > ets > pages目录下，可以点击Previewer查看页面预览效果。不支持生成的组件、属性会以注释的形式给出，方便后续定位修改。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/KoVnKHTESkeIIyoVRWq8gA/zh-cn_image_0000002561833543.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=CA626FCA77F9722A1AAADDB7C7FFF54788362460737E2EB90C123BA55F42E281)
    
7.  生成的新工程内的entry > src > main > resources目录包含文本、图像、颜色资源。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/7pCUJIyQSd-mFvWH1B9aLw/zh-cn_image_0000002561753559.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=395564A6CAFAD58F5133AD1F5EFD9C03B98C6105C45C0D4ABBB9396AD5DB865F "点击放大")
    
    更多操作指导，请参考视频课程：[毕方HarmonyOS UI代码生成工具](https://developer.huawei.com/consumer/cn/training/course/live/C101731322888995220)。
