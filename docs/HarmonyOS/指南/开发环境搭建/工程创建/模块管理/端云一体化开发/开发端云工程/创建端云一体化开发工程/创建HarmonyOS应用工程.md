---
title: "创建HarmonyOS应用工程"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-create-appproject"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "端云一体化开发"
  - "开发端云工程"
  - "创建端云一体化开发工程"
  - "创建HarmonyOS应用工程"
captured_at: "2026-04-17T01:36:43.329Z"
---

# 创建HarmonyOS应用工程

#### 新建工程

#### \[h2\]前提条件

-   您已完成[开发准备工作](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-prerequisite)。
-   您已使用[已实名认证](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-account)、且注册地为中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）的华为开发者账号登录DevEco Studio。
-   请确保您的华为开发者账号无欠款，账户欠费将导致云存储服务开通失败。

#### \[h2\]选择模板

1.  选择以下任一种方式，打开工程创建向导界面。
    -   如果当前未打开任何工程，可以在DevEco Studio的欢迎页点击“Create Project”开始创建一个新工程。
    -   如果已经打开了工程，可以在菜单栏选择“File > New > Create Project”来创建一个新工程。
2.  在“Application”页签，选择合适的云开发模板，然后点击“Next”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/HDD_X9NKR4eYxHYbs_Od-A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=1801E06A9DED1DE7869EB17A70D3D24F7D56FF547FB3AFEBB10650A6EFBDD5F0)
    
    当前仅支持通用云开发模板（\[CloudDev\]Empty Ability）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/CpKfiHb3RVyJcdZfW5fEwA/zh-cn_image_0000002462973802.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=0B34AB72706FB609546DFC56B4BA96A6733E75EEAC7F8FFFA8BC36BE719E8D59)
    

#### \[h2\]配置工程信息

1.  在工程配置界面，配置工程的基本信息。
    
    其中，Device type和Enable CloudDev参数不可更改，其他参数请参考[创建一个新的工程](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-create-new-project#section11644183711342)内对应的指导进行配置。
    
    | 
    参数
    
     | 
    
    说明
    
     |
    | :-- | :-- |
    | 
    
    Device type
    
     | 
    
    该工程模板支持的设备类型，目前仅支持手机设备。
    
     |
    | 
    
    Enable CloudDev
    
     | 
    
    是否启用云开发。云开发模板默认启用且无法更改。
    
     |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/PjxAqQCJTnOUbk-5OeXoLg/zh-cn_image_0000002547465643.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=D3C0360E1C0F6D3AA18A5D084C20323AC07C64CD6E67172A02575555F22BBEE4)
    

2.  点击“Next”，开始关联云开发资源。

#### \[h2\]关联云开发资源

为工程关联云开发所需的资源，即将您账号团队在AGC创建的同包名应用关联到当前工程。具体操作如下：

1.  （可选）如您尚未登录DevEco Studio，点击“Sign In”，在弹出的账号登录页面，使用[已实名认证](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-account)的华为开发者账号完成登录。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/sr7-aw6yS76PeaqjwYk1Ig/zh-cn_image_0000002214858793.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=73AC726DEDEEB33D36ABC002AD7B8497B21BD1DC651A6E6538824F65E3B1CE58)
    
    登录成功后，界面将展示账号昵称。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/NEtSGK0qQCWRYDw_p3ox_A/zh-cn_image_0000002179338404.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=2BD2DE70BA778B29C5CC8ABCB4D6DECC295ADCF370F36D65DD73E589F26411AA)
    
2.  点击“Team”下拉框，选择开发团队。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/qUIv2bBLRY2zkuKkgQRtDg/zh-cn_image_0000002500639597.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=937D7D0768B11E2C6C5CCD7032077AD85FC1C82FEF0D04E8DFD107D73CD3F96C)
    
3.  关联应用。
    
    选中团队后，系统根据工程Bundle name在该团队中自动查询AGC上的同包名应用。
    
    -   如查询到应用，选中该应用，点击“Finish”即可。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/jBy-orMhSZ-AeFH8bgTObg/zh-cn_image_0000002214704349.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=3D3CBBFE33470FB0D9BE75FF644FA6F449323DC80CEB1CCAB8A675FD752728F4)
        
    -   如查询到的应用尚未关联任何项目（即为游离应用），则无法选中。请先[将游离应用添加到AGC项目下](#section152521927193013)。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/EtHeQgC7TBeazMqfzxr-Pg/zh-cn_image_0000002179498144.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=291E7C15ED93A18DAF7EA69339E6AAEE55076D24BAE2D57442B0478453D9351C)
        
    -   如果查询到的应用所属项目尚未启用数据处理位置，请点击界面提示内的“AppGallery Connect”[设置数据处理位置](https://developer.huawei.com/consumer/cn/doc/app/agc-help-datalocation-0000001160439813)。设置完成后返回DevEco Studio界面，点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/JCWnA2HxQBCjXyDecXl-Gw/zh-cn_image_0000002495893905.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=F8C84655F9C1A66913DFBE1B1E6390A9052481767C8691C3A5CC25792C42D182)刷新当前APP ID列表，即可看到设置的数据处理位置。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/SkY6EFogQUCeloFsEwnzAw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=AD95E3328733B7543002778DDDA2D6EF67C7197EB115F044350DF84C5B2FFE57)
        
        -   由于云开发目前仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外），请确保项目启用的数据处理位置包含“中国”。
        -   无论项目启用的默认数据处理位置为哪个站点，后续开发的云服务资源都将部署在“中国”站点。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/fNXk5dPrTNq-xfK7qfaDrg/zh-cn_image_0000002495893753.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=393129D090F1BC6D16ED36CD23979246B1D2A8D173652A924F2B6F138A3B70A0)
        
    -   如查询到应用但出现如下提示，表明查询到的应用类型为元服务，与当前工程类型不一致。请修改以确保当前工程与AGC上同包名应用均为HarmonyOS应用类型。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/awr6qu0sSFuzJCKsLocDRQ/zh-cn_image_0000002462815550.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=C5DEAC7F586928CB6F013DB4EE1534C2183D8C5374E34C846F72F0A99806AB0A)
        
    
    -   如在当前团队中未查询到同包名应用，请先确认填写的包名是否有误。
        
        -   如包名有误，点击界面提示中的“go back”返回工程信息配置界面进行修改。
        -   如包名无误，则表明当前团队尚未在AGC控制台创建与当前工程包名相同的应用。您可点击界面提示中的“AppGallery Connect”，[前往AGC控制台进行补充创建](#section397317130308)。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/99JSpN1oQuajX065sJIWpw/zh-cn_image_0000002214858765.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=14EA77EBF572A26C9B306E1628AC8D8B9F8CBFC75B0E4D558A73CF6A5D2C3F34)
        
        完成以上操作后，DevEco Studio即可获取到同包名应用信息。选中应用后，点击“Finish”。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/RXZuIQ4rRRGNp_G-EgJVMA/zh-cn_image_0000002214858801.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=E0D89C6023ADECC8573A348B878138569590B9E692926CD3A9969DCD7B938703)
        
4.  如您所属的团队尚未签署云开发相关协议，点击协议链接仔细阅读协议内容后，勾选同意协议，点击“Finish”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/cggMNUr3RMGuxJm_jgdVNA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=F3D65D0019296BD2757A638A57FC46F70599E9A1E5CE6CBD3EDABBFDDA7DCD96)
    
    只有账号持有者和法务角色才有权限签署协议。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/li_bZTqbRJm15rsvBNxwNw/zh-cn_image_0000002179498108.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=5330326C59BD3CDEC6505244250AA7157CB31F1772F8E611A8990E32E84D1751)
    
5.  进入主开发界面，DevEco Studio执行工程同步操作，端侧工程会自动执行“ohpm install”，云侧工程会自动执行“npm install”，以分别下载端侧和云侧依赖。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/cyjeUjzPTYqnUhH4D9cKDw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=4359287BCB33EF73C9B2B6D8D4138676C869FFD3DF009F67E2DB3472E7F43F14)
    
    若云侧执行“npm install”失败，请排查是否尚未[配置NPM代理](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-environment-config#section197296441787)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/ZVYO2zeJQOaRP0RpMwlefw/zh-cn_image_0000002179498148.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=F1D2A9AC8ECCF3164BE3A9379F841F163B7CF8F1EEE68943D18FAA70FCE7F75B)
    
6.  在主开发界面，可查看刚刚新建的工程。关于工程的详细目录结构介绍，请参见[端云一体化开发工程目录结构](#section20250910164411)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/kxJNc6fYR2iOAtksA71Xrw/zh-cn_image_0000002214704397.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=C3C572ACEF533437E4232F5A1FFA8D043D769B635AA76051800969A6CA31050C)
    

#### 工程初始化配置

当您成功创建工程并关联云开发资源后，DevEco Studio会为您的工程自动执行一些初始化配置。

#### \[h2\]自动开通云开发服务

DevEco Studio为工程关联的项目自动开通云函数、云数据库、云存储等云开发服务，您可在“Notifications”窗口查看服务开通状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/r5EYt3V8SGyWKDFwtzI92A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=6E051308767792DD3A1296840EA3EBD2B3B05E5B0BD54E5184795B4AFBE39E02)

-   如服务开通失败，您可通过[CloudDev云开发管理面板](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/agc-harmonyos-clouddev-console)快捷进入AGC控制台进行手动开通。
-   如云存储服务自动开通与手动开通均失败，可能是账户欠费导致。请您[检查账户是否余额不足](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-account-bill-0000001200817917#section813072912208)，[补齐欠款](https://developer.huawei.com/consumer/cn/doc/AppGallery-connect-Guides/agc-account-recharge-0000001126625360)后再前往AGC控制台进行手动开通。

#### 端云一体化开发工程目录结构

端云一体化开发工程主要包含端开发工程（Application）与云开发工程（CloudProgram）。

#### \[h2\]端开发工程（Application）

端开发工程主要用于开发应用端侧的业务代码，使用通用云开发模板创建的端开发工程目录结构如下图所示。“Application/cloud\_objects”模块用于存放云对象的端侧调用接口类，“src/main/ets/pages”目录下包含了云存储、云数据库和云函数页面，其他目录文件介绍请参见[工程目录结构](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-project-structure)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/VYOlBV7nT1efavdzAGVXdg/zh-cn_image_0000002214858825.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=65D843B178B016F99E26A92276D2CF3BBC1D244480646D7BF96B357D98A63F5E)

#### \[h2\]云开发工程（CloudProgram）

在云开发工程中，您可为您的应用开发云端代码，包括云函数和云数据库服务代码。使用通用云开发模板创建的云开发工程目录结构如下图所示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/ln2-ah7NRwy0fouse8dkeQ/zh-cn_image_0000002279845320.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=FF2DA396B5DC69850702B3D52E90294D29975A4E997D2024FDF658B20F52E754)

-   clouddb：云数据库目录，包含数据条目目录（dataentry）和对象类型目录（objecttype）。
    -   dataentry：用于存放数据条目文件。
        
        该目录下一般会根据您选择的云开发模板预置数据条目示例文件。在通用云开发模板工程中，该目录下会预置名为“d\_Post.json”的数据条目示例文件，内含两条示例数据。您可按需使用、修改或删除。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/iWReVemISk2YY5BCAMjHjQ/zh-cn_image_0000002314788585.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=F97BFEAA99CFBEE34D9AA8A8C1A23CBD17723F9EF66A2CBDD261125C54F4D822)
        
    -   objecttype：用于存放对象类型文件。
        
        该目录下一般会根据您选择的云开发模板预置对象类型示例文件。在通用云开发模板工程中，该目录下会预置名为“Post.json”的对象类型示例文件，内含对象类型“Post”的权限、索引、字段名称和字段值等。您可按需使用、修改或删除。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/Riq9yokNTTasteC_KCAZNA/zh-cn_image_0000002179498164.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=F5389771C7DC82788A79EEDC0BB4CC07E9DD01E9E80A95BC71D295C72C551EEC)
        
    -   db-config.json：模块配置文件，主要包含云数据库工程的配置信息，如默认存储区名称、默认数据处理位置。
-   cloudfunctions：云函数目录，包含各个云函数/云对象子目录。每个子目录下包含了云函数/云对象的配置文件、入口文件、依赖文件等。
    
    该目录下一般会根据您选择的云开发模板预置示例函数。通用云开发模板工程下预置了一个用于生成UUID的示例云对象“id-generator”，您可按需使用、修改或删除。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/ksUMXaYtSgqk1hFDtUlEqw/zh-cn_image_0000002179498100.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=8435780932B41C92D274E5227A657902BF208BE5B1D040BD3A63C97E065B9A87)
    
-   node\_modules：工程同步时执行“npm install”生成，包含“typescript”和“@types/node”公共依赖。
-   cloud-config.json：云开发工程配置文件，包含应用名称与ID、项目名称与ID、启用的数据处理位置、支持的设备类型等。
-   package.json：定义了“typescript”和“@types/node”公共依赖。
-   package-lock.json：工程同步时执行“npm install”生成，记录当前状态下实际安装的各个npm package的具体来源和版本号。

#### （可选）AGC应用管理

#### \[h2\]从DevEco Studio补充创建同包名应用

如创建工程时，发现尚未在AGC控制台创建与工程包名相同的应用，可进行补充创建。

1.  点击界面提示内的“AppGallery Connect”，浏览器打开AGC控制台页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/VGwFbC_aTn6sUIYHYWwWeQ/zh-cn_image_0000002214858733.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=B1DD98017F97C7689C29221E798B60F4CCD613902375D72BCCA4BD6726E866BF)
    
2.  在“应用开发基础信息”页面，填写待创建的应用信息，完成后点击“下一步”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/jApWeOkkSkmnzO6omoYXyA/zh-cn_image_0000002312627449.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=AB19DBB4C20AC5BFCEE8F4704E71A5001B2A910EF28F979227CCBF6C73899391)
    
    | 
    参数
    
     | 
    
    说明
    
     |
    | :-- | :-- |
    | 
    
    应用类型
    
     | 
    
    创建的HarmonyOS应用形态，默认与您本地工程类型保持一致，不可更改。
    
     |
    | 
    
    应用名称
    
     | 
    
    应用在华为应用市场详情页展示的名称。
    
     |
    | 
    
    应用包名
    
     | 
    
    从DevEco Studio中带入自动填充，且不可更改。
    
     |
    | 
    
    应用分类
    
     | 
    
    请选择普通应用或游戏类应用。
    
    说明：
    
    应用分类设置后不支持修改，请谨慎选择。
    
    
    
    
    
     |
    
3.  进入“所属项目信息”页面，为应用选择所属的项目后点击“下一步”。
    
    -   如需将应用添加到已有项目，点击下拉框进行选择。
    -   如需将应用添加到新项目，直接在框中填写新项目名称。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/LclG_34QR8SpK3SS_xjdrQ/zh-cn_image_0000002312628981.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=DDE26C6B1ED941C76303C3F2FBA151F566F3FBE0B0851F1EB27CDC62DACF69E1)
    
4.  进入“云开发数据处理位置”页面，设置或管理项目的数据处理位置。
    -   如项目尚未设置数据处理位置：
        1.  点击“启用”。
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/Q3wmiZDgTWuZqfOtrPepHA/zh-cn_image_0000002312516673.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=FE75FA524AA051D118B5D4A97B21BCDEA524C8B295FA6705E7E6F0A8A58E0160)
            
        2.  仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/7kPrUztfRJ2EkrF_PxEF-A/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=800C528363DE6933D3E9654491F049E0A39DF6A12883A265618680079E4CF300)
            
            启用的数据处理位置必须包含中国站点。
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/55PuamzbTJybLYIN4EKGYg/zh-cn_image_0000002214858805.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=4D4FD9C02AF7A1798BF7062A2BED0894A327E5DEB6E768B23D51686B5A134608)
            
    -   如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/czXp_yayTfep_xCAA152IA/zh-cn_image_0000002312630869.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=A817A0A8A4D416EDD50722AD0DCE5629A7BAC3857953CD21B81A011C8EB7173C)
        
5.  点击“确认”，应用创建完成。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/UDqlxtd0QamAOOFxRZjVxQ/zh-cn_image_0000002214858821.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=F7AF58A3510FC75EE3E0085BF639D435CF0FD8B122C861C8EBE52A038F0191AA)
    
6.  返回DevEco Studio，可看到界面已获取并展示了刚刚创建的应用信息。若不展示，可点击Bundle name后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/VmQcONwhSGSJJ0OJ315MoA/zh-cn_image_0000002500745449.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=BA07E5FDE6B046908278F9BA40FE2C41F45FCAB4A3030A7B6161D9786CDCDC2E)刷新。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/uMOmOjF8S7af8QOtYhXWJQ/zh-cn_image_0000002179338492.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=DA31CD643136DD5D4FB9D511CF0962DDEA60C527CA909F090422B3EB7A30EFF3)
    

#### \[h2\]将游离应用添加到AGC项目下

游离应用指未关联任何AGC项目的应用。创建工程时，如需要关联的AGC应用为游离应用，则您需要将该应用添加到您的AGC项目下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/99-JQtZNQmOujx6qIaF-vQ/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=EF5044BB0982EEAA99B631CDD44B6AC88D75590A84646F76F6AB2CE001B7A7C2)

应用与项目的关联关系一旦创建则无法再修改，请谨慎操作。

1.  点击“Not associated yet”，或点击界面下方提示内的“AppGallery Connect”，可打开AGC控制台“开发与服务”页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/7IEZ5am8SGuRN7WvTIOueQ/zh-cn_image_0000002214704437.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=E1B488F1A2EE3641E1DEC44DC98E9612D13C170724EEC531ADDDD8B2B2BD2081)
    
2.  点击选择希望为应用关联的项目，或者点击“添加项目”新建一个项目。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/987hpHcYS0y79UUxCOJoNQ/zh-cn_image_0000002496495517.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=DE794485E1E7D96898A283738633A2CDB92B6EE087157E2B8DA6BAFBC5508D89)
    
3.  如选择了新建一个项目，设置项目名称，点击“确认”。
    
    如选择了已有项目，则忽略此步骤。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/-8-jF1J6RVG9vA9Cyzk7Sg/zh-cn_image_0000002214704389.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=843E1CF3416E2B5F471453CD83FF2F92EFF0A85D6688BAE6258271D379D98850)
    
4.  设置或管理项目的数据处理位置。
    -   如项目尚未设置数据处理位置：
        1.  点击“启用”。
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/lFjT_4HLQIC3dUUiw5neDA/zh-cn_image_0000002214704417.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=78CF37613DB8E561A6A74EBAB220A859880628A65CBE078B6381F991EE72E4A0)
            
        2.  仔细阅读提示框的文字说明后，在“启用”栏为您的项目勾选一个或多个数据处理位置，并在“设为默认”栏将其中一个设置为默认数据处理位置。
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/QhX8av-xTdmlSWZeHURQtw/caution_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=1F0C9559A64504A55B1807EBC65814FA3C28391E813D1B390ACB4371DD9F4A1F)
            
            启用的数据处理位置必须包含中国站点。
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/u0pbMzdKTtmRNl4c2mF52Q/zh-cn_image_0000002179338436.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=66AF828A94DFA3DF3B021DF0E008ECCE27CDF473842DDDDF571768DC3B4B1356)
            
    -   如项目已设置过数据处理位置，可点击“管理”启用新的数据处理位置、取消已启用的数据处理位置，或修改默认数据处理位置。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/nfl0Cg4SRLCSCF7PnRjk6A/zh-cn_image_0000002179338464.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=1B9892460B136B6C078C21268EB07D4C6A96C3E0CF84CCB6A568E1FB295BA3D9)
        
5.  点击“确认”，应用成功关联项目。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/1fPFaRC3Qb-3wDWJwD566Q/zh-cn_image_0000002179498200.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=B0B5A1CA8B979109D935B10863613513C378A524739E07B2A56CF26D1409C890)
    
6.  返回DevEco Studio，可看到应用已关联上了项目。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/YI4phZQ1SaCjLGBuKQygzQ/zh-cn_image_0000002214858777.png?HW-CC-KV=V1&HW-CC-Date=20260417T013643Z&HW-CC-Expire=86400&HW-CC-Sign=53DC6CC1326AD07E47D55A93F1DF6A2A8BA41A62B3C032481F01840F8BCC817C)
