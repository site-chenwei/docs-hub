---
title: "Instrument Test"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-instrument-test"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "开发自测试"
  - "测试框架"
  - "代码测试"
  - "Instrument Test"
captured_at: "2026-04-17T01:36:50.063Z"
---

# Instrument Test

#### 创建ArkTS测试用例

#### \[h2\]创建默认测试用例

1.  在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Instrument Test**或快捷键**Alt+Enter** **（macOS为Option+Enter）> Create Instrument Test**创建测试类。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/s6h6pcQtStmowCOYGw7cJw/zh-cn_image_0000002561753237.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=8E0111E1CAD8F7AE954E44CD10CFF7A143AE004FAAC57915E7A20F8D95B584B7)
    
2.  在弹出的Create Instrument Test窗口，输入或选择如下参数。
    
    -   **Testing library**：测试类型，默认为DECC-ArkTSUnit，JS语言默认为DECC-JSUnit。
    -   **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
    -   **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/nBApt4_kQb2De-WxwKta7g/zh-cn_image_0000002561833197.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=D4BE841EE500D2B3839DE245B7F00A27056B25C01EF83B2792B21C8D7ED1BDD7)
    
3.  DevEco Studio在ohosTest/ets/test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[自动化测试框架使用指导](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkxtest-guidelines)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/giRkWx1ATH6ph04sO6fOlw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=DEF19C0A39370D4353CB24BC484135025895F57E26786071DE4034C81EFA6643)
    
    -   您也可以手动在ohosTest > ets > test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。手动创建的工程或历史工程，ohosTest > ets > test文件夹下所有文件的文件名必须以.test.ets结尾，否则将在运行时弹窗提示“Error: Test files must end with '.test.ets'.”请点击**Fix**按钮，DevEco Studio将自动对ohosTest > ets > test目录下的文件名进行修改。
    -   首次在HarmonyOS设备上运行UI测试框架需要使用命令“hdc -n shell param set persist.ace.testmode.enabled 1”使能UiTest测试能力。
    

#### \[h2\]自定义Ability和Resources

从5.0.3.403版本开始，新创建的工程/模块的ohosTest目录下默认不创建testability、testrunner和resources目录，历史工程仍保留这些目录，如果新工程需要使用ability或resources能力，需要开发者自行创建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/Bnblg0LyS-Gcn9T6bHcFxg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=318403078712B1A207B81E2A8F8E3BB6DB07EB008AF9FF0C4B5BB07873F5DB19)

如果需要使用ability能力，需要同时创建testrunner目录及OpenHarmonyTestRunner.ets文件。

<table id="table988904811377" style="border-style: none;"><caption><b>表1 </b><strong>新旧版本ohosTest目录对比</strong></caption><tbody><tr id="ZH-CN_TOPIC_0000002561752517__row988912488371"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002561752517__p1788911489371"><strong>新版本</strong></p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002561752517__p178891248123711"><strong>历史版本</strong></p></td></tr><tr id="ZH-CN_TOPIC_0000002561752517__row118891748203717"><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002561752517__p28898483379"><span><img originheight="182" originwidth="208" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/i1RiY2zOSzaSBewunxlHoA/zh-cn_image_0000002561833233.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T013651Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6ED0E5DB1B6571C7648BDA777D40D30724F3E46E34A4D20D87AB785EA027312"></span></p></td><td align="center" class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002561752517__p1788919487371"><span><img originheight="324" originwidth="288" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/IqgBlicEQIubQZVs1_amfA/zh-cn_image_0000002530913310.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T013651Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2E560A02429165645E6D142C2B7AEFF60CADD8184905F5FB087831F0987134F2"></span></p></td></tr></tbody></table>

1.  创建以下目录或文件，文件内容示例可在[运行Instrument Test测试用例](#section1574003717165)后，在对应模块的.test/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1及以上版本）或build/{productName}/intermediates/src/ohosTest（DevEco Studio 6.1.0 Beta1以下版本）下查看，其中productName是当前生效的product，可以通过点击DevEco Studio右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/x9NwZKrpT-27WDZoA23WrQ/zh-cn_image_0000002561753229.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=7B7F5A85A38B78EDD26AD1099B296A3DAAAC6F837AB77276728ADB554EFE9B0E)图标进行查看。
    
    -   testability目录 > TestAbility.ets文件
    -   testability目录 > pages目录 > Index.ets文件
    -   testrunner目录 > OpenHarmonyTestRunner.ets文件
    -   resources目录 > base目录 > element目录 > color.json文件
    -   resources目录 > base目录 > element目录 > string.json文件
    -   resources目录 > base目录 > profile目录 > test\_pages.json文件
    
2.  在module.json5文件中补充ability配置字段mainElement、pages、abilities，关于字段的具体说明请参考[module.json5配置文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/module-configuration-file)。
    
    {
      "module": {
        "name": "entry\_test",
        "type": "feature",
        "description": "$string:module\_test\_desc",
        "mainElement": "TestAbility",                                   // 对应下方abilities中的ability name。
        "deviceTypes": \[
          "phone",
          "tablet",
          "2in1"
        \],
        "deliveryWithInstall": true,
        "installationFree": false,
        "pages": "$profile:test\_pages",                                 // 对应resources目录 > base目录 > profile目录 > test\_pages.json文件。
        "abilities": \[                                                  // 添加的ability的配置信息。
          {
            "name": "TestAbility",
            "srcEntry": "./ets/testability/TestAbility.ets",
            "description": "$string:TestAbility\_desc",
            "icon": "$media:icon",    // 确保引用的资源都存在
            "label": "$string:TestAbility\_label",
            "exported": true,
            "startWindowIcon": "$media:icon",
            "startWindowBackground": "$color:start\_window\_background"
          }
        \]
      }
    }
    

#### 运行测试用例

#### \[h2\]运行模式

使用DevEco Studio运行测试用例前，需要将设备与电脑进行连接，将工程编译成带签名信息的HAP，再安装到真机设备或模拟器上运行，具体请参考[使用本地真机运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-device)或[使用模拟器运行应用](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-emulator)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来运行测试用例：

-   在工程目录中，单击**右键 > Run'测试文件名称'**，执行测试。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/vV8RS9mQSAuQOjkDjscumg/zh-cn_image_0000002561753243.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=991A72759FE864E1FEEA991BD15D5BBEBE7BA4BC4C3FF74E6DB1DF1289EF78C7)
    
-   打开测试文件，单击测试套件左侧按钮。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/IofXzMUFTmCGYXnLAhyiCg/zh-cn_image_0000002561833189.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=4AEC07903AFF453698776D98C1D46097B12A23D40764C0ABF03539F62773C184)
    
-   如果要根据自定义的配置执行Instrument Test，在[创建测试用例运行任务](#section65264166107)后，通过如下方式的其中之一，执行Instrument Test：
    -   在工具栏主菜单单击**Run > Run'测试名称'**。
    -   在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/wVpQZSPdQYiwIOQuySZPSw/zh-cn_image_0000002561833183.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=660FE5E7A5E345ABCEA1CED53ABE95F95800AAEFD7160F5ABE0B609D6B78062B)按钮，执行Instrument Test。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/8AYFXl1gTdy2AveweNbzJg/zh-cn_image_0000002530913302.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=3128B18891C2FC73584C8599DD606C03B3B5575F3D41344A212907CC8CA9A57A)
        

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/KyntoGPcS06YLK7mpsCg0Q/zh-cn_image_0000002530913296.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=ECCF0E1E815A6A1D6A1068647DB13F732AD043114963E95501A7E07E1FD84885)

#### \[h2\]调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/67WpESlkTvKhL2pfBnk9GA/zh-cn_image_0000002530753298.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=2FFA186F94BD5CF6BD9764AAF971F691A440C4CA553CA88461DFD87C8D2CDF2B)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/Zwv0x_kfS8SB4MxLASl6Jw/zh-cn_image_0000002561833191.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=E5D4A442BB88A936C97CC31841F51440CBFDFD70B77BDB36956E76FD3399DA58)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/HpK0TXAPRSGr60d_7jQ85Q/zh-cn_image_0000002530753322.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=B17E5044BCC2BD9B33AA53856FC412811C9A661EB6DB80987D40CA799CB457E1)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/Ka4IcQ7XQHKGsFRoNQJx5Q/zh-cn_image_0000002561833251.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=134EA7201FA849FE0FA458049EE7FE77D4ADD69B9CD9BB40F2C8E3BEC251FB6A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/M86LtY5FS2alhl4uI-3ZOw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=99DE44606A8F1783655A71B5BD79D8271F87A64682D3604151A313C547D2696E)

DevEco Studio支持设置调试代码类型，具体请参考[设置调试代码类型](#section0164586312)。

#### \[h2\]覆盖率统计模式

在Instrument Test运行的基础上支持代码覆盖率统计。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section13756446154)。

可以采用运行工程目录（test）、测试文件（如Ability.test.ets）、测试套件（describe）、测试方法（it）的方式来启动代码覆盖率的统计。

以文件级别为例，有两种方式启动测试：

-   方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，执行测试。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/d4WeOK8wRNi9zuWeYs-Vew/zh-cn_image_0000002561833187.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=6E6210B583A425A7C945A6C8647EEF1E4C44CC111686D98937572A7568DBFB18)
    
-   方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ZVHdQGnYRpG6fsw8eC1nfQ/zh-cn_image_0000002561753249.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=0269B253EE5C80CF05E72D6D23BEC87434BC78FADF2C416AB396261826099DFB)按钮，执行测试。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/Q4YHLywqStq-z73tt5RYIA/zh-cn_image_0000002530753328.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=4F2628ECFA8D7F48E63FACF124B09EBD5D84566B86C02FC018EB3D5F91B26DB9)
    

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/qegdSg_OSHCzxZ8uQUFkgA/zh-cn_image_0000002530913262.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=3D91F7303206F6605BEF2F0008C8482DB9356133E1C9A6D2AC0BAB5242567D6A)

点击链接可打开报告，查看ArkTS代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/-Nxk96IsQ7yG03D97n70QQ/zh-cn_image_0000002561833207.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=DC27A37D2127EF26185B26EBE078A6DFE0E9F928A3985E6765C81866481BE571)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/74Oklf8xQUah6cHzO_Bs_g/zh-cn_image_0000002530913260.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=ED6A6FBB4A96B958E7D6DFAB6D97428C75A938A2D8366C9D847A569EEFB0B3B6)

#### （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行，如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1.  在工具栏主菜单单击**Run** > **Edit Configurations**进入Run/Debug Configurations界面。
2.  在**Run/Debug Configurations**界面，单击+按钮，在弹出的下拉菜单中，单击Instrument Test。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/8CtKwlTGTiK7QP9jTdBETw/zh-cn_image_0000002561833203.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=8358F6B98A620A3704AC0947C5876ECDA6FC714A97DDA2083FD055DC23DD15E4)
    
3.  根据实际情况，配置Instrument Test的运行参数。然后单击**OK**，完成配置。
    
    -   如果模块依赖共享包，请提前设置HAP安装方式，勾选“**Keep Application Data**”，则表示采用覆盖安装方式，保留应用/元服务缓存数据。
    -   如果工程中HAP/HSP模块直接依赖其他HSP模块（如entry模块依赖HSP模块）或间接依赖其他模块（如entry模块依赖HAR模块，HAR又依赖HSP模块）时，在测试阶段需要同时安装模块包及其所有依赖模块的包到设备中。此时，可以勾选“**Auto Dependencies**”，测试时会自动将所有依赖的模块都安装到设备上。该选项默认勾选。
    -   如果不涉及UI测试，勾选“**Only OhosTest Package**”，则只会推送OhosTest测试包到设备上，不会推送HAP/HSP包，可以缩短推包时间。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/GWmTNxciR2WNPB5MjucEqw/zh-cn_image_0000002561753275.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=71D0AB736B025C6FB442151CE5FA7B284E564D6A09A39A5B9D5E8B83EC0DF226)
    

#### \[h2\]使用过滤条件筛选待运行的测试用例

1.  在用例编写时，通过配置it的第二个入参，为每个用例添加过滤参数。此参数用于为测试用例添加标注，不添加则参数默认为0表示未被标注。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/ldE2K9upToS-JiZyqN4l0g/zh-cn_image_0000002561833199.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=83B4F553C3A3E0D39AAE908D228614D6989C899DE075B375FC6F17AAEA11EDA3)
    
2.  打开**Run/Debug Configurations**窗口，点击Test Args![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/FShCLKYoSE-oJlgFrtjmMA/zh-cn_image_0000002530753318.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=1F08186F8A20694794940660DB4A7572200A2FFE87AC4856C20D05A300AD3362)，打开**Test Args**界面，添加命令行参数。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/DsYSgxu8T5iXBPUqiVbl_A/zh-cn_image_0000002530753288.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=FBD37BAE3B8F04E994BB1058D3F0B5576A1890E2E4902E8FB018B2B3E2779A73)
    
    例如将测试参数配置为level=1, size=medium
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/w1FaEp-yQUm4ApucRHiacQ/zh-cn_image_0000002530913276.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=E49164722C29DDFF340EAC66DECCCBCC1CAAEC345C6223CB0229529E96D45C75)
    
    **表2** 参数规则参考
    | 
    Key
    
     | 
    
    含义说明
    
     | 
    
    Value取值范围
    
     |
    | :-- | :-- | :-- |
    | 
    
    level
    
     | 
    
    用例级别
    
     | 
    
    "0","1","2","3","4", 例如：-s level 1
    
     |
    | 
    
    size
    
     | 
    
    用例粒度
    
     | 
    
    "small","medium","large", 例如：-s size small
    
     |
    | 
    
    testType
    
     | 
    
    用例测试类型
    
     | 
    
    "function","performance","power","reliability","security","global","compatibility","user","standard","safety","resilience", 例如：-s testType function
    
     |
    
3.  完成以上配置后，在运行此项配置对应的测试任务时，只运行过滤后的测试用例。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b1/v3/2f73GUyNTJmj-Z7ENYQfqA/zh-cn_image_0000002530753314.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=E645F9885774274DE50E8DE7F91AE81F01C39F6541073002364B206D4A010E2B)
    

#### \[h2\]设置调试代码类型

点击**Run > Edit Configurations**，打开**Run/Debug Configurations**窗口，选择Instrument Test，点击**Debugger**页签，设置Debug type。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Id7TBs45Q3eadsawNMeWcg/zh-cn_image_0000002530913318.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=0AA7D981493C0FC181BF99E25FBF8704B7FFE3829292E29DC305BC15EC0507D5)

调试类型Debug type默认为Detect Automatically，关于各调试类型的说明如下表所示：

| 
调试类型

 | 

调试代码

 |
| :-- | :-- |
| 

Detect Automatically

 | 

自动检测。根据工程模块及其依赖的模块涉及的编程语言，自动启动对应的调试器。

如果检测到是Native模块，出现两个调试窗口（PandaDebugger、Native）；如果不是Native模块，只出现PandaDebugger调试窗口。

 |
| 

ArkTS/JS

 | 

只调试ArkTS/JS，只出现PandaDebugger调试窗口。

 |
| 

Native

 | 

单独调试C++，只出现Native调试窗口。

 |
| 

Dual(ArkTS/JS + Native)

 | 

支持ArkTS/JS和C++混合调试，出现两个调试窗口（PandaDebugger、Native）。

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/P5UUW8X9SIq1wzywd_jN1w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=A136F0B12F305CBD63AF3D66259FB688FADF18F0E67BCDFF95949BAF0CEFE40B)

调试C++代码时，当前模块及所有依赖的HSP模块的[Address Sanitizer配置](#section8352185341915)要保持一致，若不一致，可能无法进入C++代码的断点处。

#### \[h2\]ASan检测

Instrument Test针对C/C++方法提供ASan检测能力，关于ASan的介绍请参考[ASan检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan)，当前不支持JS语言。

1.  在运行/调试配置窗口，选择对应的Instrument Test，点击**Diagnostics**页签，勾选**Address Sanitizer**选项，勾选后，测试包和源码包均开启ASan能力。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/2UELKxf0QcCIuGFtaPXdEg/zh-cn_image_0000002561753267.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=7B8814556825F8E77E287F3283BF8AAEC1B67E977D526B890AF3966AFEB16E0C)
    
2.  如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_ASAN=ON”，表示以ASan模式编译so文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/9cdZMRPJQb-FX9WFXnldPA/zh-cn_image_0000002530913320.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=66BB4A4423187D05CEEE95E304EA3175A589B28DD4086E9567F042694FC2C74F)
    
3.  运行测试用例。
4.  当程序出现内存错误时，弹出ASan log信息，点击信息中的链接即可跳转至引起内存错误的代码处。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/OWIXMaWtSCenoIQAasVGwQ/zh-cn_image_0000002561753273.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=77FCF4972DC133B81B5595DC1213B00B72B1459AB4D8DCAAFB0C64D53B6EA3F7)
    

#### 测试C++代码

从DevEco Studio 6.0.0 Beta5版本开始，支持对C++代码进行测试，包括运行/调试C++测试代码、对C++代码进行覆盖率统计。

由于C++的测试so无法直接在设备上运行，需要通过Node-API的方式拉起，即通过ArkTS/JS语言拉起C/C++测试用例。

#### \[h2\]运行C++测试代码

1.  创建cpp测试目录，鼠标右键单击ohosTest目录，选择**New > C/C++ File(Napi)**，在ohosTest下生成cpp测试目录，以entry模块为例，目录结构如下。
    
    -   **src > ohosTest > cpp > types**：用于存放C++的API接口描述文件。
    -   **src > ohosTest > cpp > types** **\> libentry\_test > index.d.ts**：描述C++ API接口行为，如接口名、入参、返回参数等。
    -   **src > ohosTest > cpp > types** **\> libentry\_test > oh-package.json5**：配置.so三方包声明文件的入口及包名。
    -   **src > ohosTest > cpp > CMakeLists.txt**：CMake配置文件，提供CMake构建脚本。
    -   **src > ohosTest > cpp > napi\_init.cpp：**定义C++ API接口的文件**。**
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/Si7UnCMtSiKgSYJ_pKBw9w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=0D398C113A8862D2DC12968993081F0ABD2EFBEDE0465FFABCB839356ACCE46F)
    
    DevEco Studio生成的cpp测试目录中不包含C++测试框架，需要开发者自行选择开源测试框架使用。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/F7EruV22TMuU_EJGkCHmdw/zh-cn_image_0000002561753213.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=26A220D568E387A53B29A1FB490C23A80700A14803A0F01E1DC5B03B97994D7A)
    
2.  通过ArkTS测试用例拉起C++测试，示例如下。
    
    // ArkTS测试文件Ability.test.ets
    import entryTest from 'libentry\_test.so';
    export default function abilityTest() {
      describe('ActsAbilityTest', () => {
        ...
        it('testNative', 0, () => {
          hilog.info(0x0000, 'testTag', '%{public}s', 'testNative it begin');
          let result = entryTest.runNativeTest();
          hilog.info(0x0000, 'testTag', '%{public}s', result)
          expect(result).assertContain("ended");
        })
      })
    }
    
3.  运行testNative测试用例，查看测试结果。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/ekjASrmVRjy0HQ_i6V4FbA/zh-cn_image_0000002530753304.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=735D2FB38659B93B5DD1865EFB7802700EAD82888D79D5DAA5947496266934D0)
    

#### \[h2\]收集代码覆盖率

DevEco Studio默认不收集C++代码覆盖率，需要通过以下方式开启。

1.  在测试目录下的CMakeLists.txt中添加以下代码，开启覆盖率编译插桩能力。
    
    // DevEco Studio 6.0.2 Beta1之前版本
    set(CMAKE\_CXX\_FLAGS "${CMAKE\_CXX\_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
    set(CMAKE\_C\_FLAGS "${CMAKE\_C\_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
    
    // DevEco Studio 6.0.2 Beta1及以上版本，OHOS\_TEST\_COVERAGE在覆盖率模式下为true，在调试/运行模式下为false
    if(OHOS\_TEST\_COVERAGE)
      set(CMAKE\_CXX\_FLAGS "${CMAKE\_CXX\_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
      set(CMAKE\_C\_FLAGS "${CMAKE\_C\_FLAGS} -fprofile-instr-generate -fcoverage-mapping")
    endif()
    
2.  在napi\_init.cpp文件的RunNativeTest方法中，调用\_\_llvm\_profile\_write\_file方法，将覆盖率数据保存到设备的/data/storage/el2/base路径下的c++\_coverage.profraw文件中，该路径和文件名不可修改，示例代码如下。
    
    extern "C" {
        void \_\_llvm\_profile\_set\_filename(char \*);
        int \_\_llvm\_profile\_write\_file(void);
    }
    
    static napi\_value RunNativeTest(napi\_env env, napi\_callback\_info info)
    {
        char filename\[256\];
        snprintf(filename, sizeof(filename), "/data/storage/el2/base/c++\_coverage.profraw"); // 覆盖率报告文件路径和文件名，不可修改
        \_\_llvm\_profile\_set\_filename(filename);
        // 开启测试
        ...
        // 结束测试，保存数据
         \_\_llvm\_profile\_write\_file();
        ...
    }
    
3.  运行覆盖率测试，选中ArkTS测试文件，单击**右键 >** **Run '测试文件名称' with Coverage**，执行测试。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/0DjjYnO2RtSTwWRSDcwklg/zh-cn_image_0000002530753310.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=97786341677867696151ED3E50A9D604BA05A90C62F8AC3073D0F9F9FF94F0A1)
    
    启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/wAUen1YCRIWUM2wak1Wnzw/zh-cn_image_0000002530753290.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=AC1361CF3DA3051C31E4F0A9EE0E6AD49066A43516C8641785BDDA3C66D07DBA)
    
    点击链接可打开报告，查看C++代码覆盖率详情。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/wzDoPBsOTCS3yc97QZynkA/zh-cn_image_0000002561833213.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=D7F64E12F497B49A372031123185A0BC7E8ED24CC530F15243384E1A7A83F7A8)
    

#### 使用命令行执行测试Instrument Test

通过命令行方式执行Instrument Test，在工程根目录下执行命令：

hvigorw onDeviceTest -p module={moduleName} -p coverage={true|false} -p scope={suiteName}#{methodName} -p ohos-debug-asan={true|false}

-   module：执行测试的模块，缺省默认是执行所有模块的用例。
-   coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/ohosTest/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。
    
    如果开启了C++代码覆盖率测试，会生成C++代码的覆盖率报告，路径：<module-path>/.test/default/outputs/ohosTest/cpp\_reports/index.html
    
-   scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。
-   ohos-debug-asan：是否启用ASan检测，缺省默认是false。从DevEco Studio 5.1.1 Beta1版本开始支持。
    
    ASan日志路径：<module-path>/.test/default/intermediates/ohosTest/coverage\_data
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/kyfW9n1CQJy84DlcYl4PaQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=5E5835F1A3195C850F9CBDC58A991D3AAA5EBDC9250B77C5AD96DED25A88B522)

-   通过命令行执行测试时，不支持配置product，默认为default。
-   多个module和scope之间用逗号隔开。

测试结果文件：<module-path>/.test/default/intermediates/ohosTest/coverage\_data/test\_result.txt
