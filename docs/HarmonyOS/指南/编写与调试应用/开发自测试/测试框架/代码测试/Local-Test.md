---
title: "Local Test"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-local-test"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "开发自测试"
  - "测试框架"
  - "代码测试"
  - "Local Test"
captured_at: "2026-04-17T01:36:50.025Z"
---

# Local Test

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/JiJhf3wWQI6GlisB9z967w/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=CBCB06333A406EEE3A1EDD57963887A0E79309FE3CA97C6BB520863878B3390E)

当前不支持测试C/C++方法及系统API。

#### 创建Local Test测试用例

1.  在工程目录下打开待测试模块（支持HAP、HAR、HSP模块）下的ets文件，将光标置于代码中任意位置，单击**右键 > Show Context Actions** **> Create Local Test**或快捷键**Alt+Enter****（macOS为Option+Enter） > Create Local Test**创建测试类。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/4PKTbTjiT6GPP1rhXSP5GA/zh-cn_image_0000002561833569.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=B45CE175922A9B852FCCC0111031D3EE168C6F5719A4642B740B6E709AC9512C)
    
2.  在弹出的Create Local Test窗口，输入或选择如下参数。
    
    -   **Testing library**：测试类型，默认为DECC-ArkTSUnit。
    -   **ArkTS name**：创建的测试文件名称，测试文件中包含了测试用例。测试文件名称要求在工程目录范围内具有唯一性，仅支持字母、数字、下划线（\_）和点（.）。
    -   **Destination package**：测试文件存放的位置，建议存放在待测试模块的test目录下。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/fkimPOc1QvC2qt8_fXp_Ag/zh-cn_image_0000002561753591.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=BA8E2B59EB472F7BED61C1FD7A88AE66827DB74411CB9B1AA6A3C40B5C9ADCF7)
    
3.  DevEco Studio在test目录下自动生成对应的测试类。在测试类中，DevEco Studio会生成对应方法的用例模板，具体测试代码需要开发者根据业务逻辑进行开发，具体请参考[单元测试框架](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/unittest-guidelines)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/EqB7BVPZRNOVYiVoNPsf6g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=429C1EB07C3571164578B113933A09D7F10E84FA92FB9B90A1465DA4E5422F53)
    
    您也可以手动在test文件夹下创建测试用例，手动创建后，需要在List.test.ets文件中添加创建的用例类。
    

#### 运行Local Test测试用例

#### \[h2\]运行模式

可以采用运行工程目录（test）、测试文件（如Index.test.ets）、测试套件（describe）、测试方法（it）的方式来执行Local Test，各级别测试执行入口如下。

<table id="table8849024115311" style="border-style: none;"><tbody><tr id="ZH-CN_TOPIC_0000002530912610__row1084920245537"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002530912610__p2084932419536"><span><img originheight="445" originwidth="501" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/bvQpf6Q1S42TnDwLinSEzg/zh-cn_image_0000002530753674.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T013651Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB73C5E26A1B0D7941BEDE457F875E072A546596E36E741E65DACEF906E56E0B"></span></p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002530912610__p48491324125312"><span><img originheight="436" originwidth="468" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/LeTtGIzIREGXz2jSiOsX2w/zh-cn_image_0000002561753585.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T013651Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FCFAAA419AAA436056651CE1DB3C60E5F8850895A977C361DAFDBC810C18259"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002530912610__row168495245531"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002530912610__p108491924115318">目录级</p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002530912610__p14849142411534">文件级</p></td></tr><tr id="ZH-CN_TOPIC_0000002530912610__row88495249531"><td align="center" class="nocellnorowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002530912610__p13849132419537"><span><img originheight="174" originwidth="506" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/c2q_ZiP_Qr2p5au_l_StAw/zh-cn_image_0000002530753664.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T013651Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BA84D041D7132EB93F3AC0517FB8B923A2047372A1F0B88FDD7402AF9430A13"></span></p></td><td align="center" class="cell-norowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002530912610__p1985018244535"><span><img originheight="174" originwidth="469" src="https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/_fNGk9xvS8Ca44ZmWQO4-w/zh-cn_image_0000002561833577.png?HW-CC-KV=V1&amp;HW-CC-Date=20260417T013651Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7205F85ABC3B0E17BA06F41F463F84E7D45ABF8C3E3C577B0D00369B5B598FE"></span></p></td></tr><tr id="ZH-CN_TOPIC_0000002530912610__row1885072411535"><td align="center" class="row-nocellborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002530912610__p1485092465312">套件级</p></td><td align="center" class="cellrowborder" style="border: none;" valign="top" width="50%"><p id="ZH-CN_TOPIC_0000002530912610__p1085015248538">方法级</p></td></tr></tbody></table>

以文件级别为例，在工程目录中，选中文件，单击**右键 > Run'测试文件名称'**，执行测试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/48AbvC1KS7iFgBN2vHw0bw/zh-cn_image_0000002530753656.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=6BC807FE96FD3449DE36EC00A9AB7FF5E1D6249F75F94FBA92548FC6EBEB40DE)

也可以通过如下方式，执行Local Test：

-   在工具栏主菜单单击**Run > Run'测试名称'**。
-   在DevEco Studio的右上角，选择一项测试任务的配置，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/HbyjmNhzSOWy5SZ4dSBDtg/zh-cn_image_0000002530913656.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=5F6C5B3ADD2F538FCDA45C199446F04DFFF869CDAF169DD8FDC99047C0603E3D)按钮，执行Local Test。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/2RvxY_47ScCG_CAIhomfYA/zh-cn_image_0000002561753609.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=17F91601A032665930162ED79CEDE3476FF1753C3A5044B243FC22C03E6C7A49)
    

执行完测试任务后，查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/4eLtlfbTRS-mVpJmv4B49A/zh-cn_image_0000002530753644.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=BA44EB9935BA89B8D9B7679199AA8591F3EEE903E362EA7B59FD972C76B83769)

#### \[h2\]调试模式

调试模式相比运行模式增加了断点管理功能。在断点命中时，可以选择单步执行、步入步出、进入下个断点等方式进行调试，另外可以使用线程堆栈可视化、变量和表达式可视化功能，快速定位问题。

以文件级别为例，在添加断点之后，在工程目录中，选中文件，单击**右键 > Debug'测试文件名称'**，以调试模式执行测试任务。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/SgTTB8KiQ3a2zH9niFqtWw/zh-cn_image_0000002530753642.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=69A107F0D5454EBEBF697BAB4DD1E7BF37E388854DB09C29CE567063600F016E)

在断点命中时，下方将出现Debug窗口。开发者可在该窗口中进行断点管理与基础调试能力的可视化操作，在断点命中时可查看当前线程的变量和堆栈信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/H1bRoDo_RcWqcA8PX8BVQg/zh-cn_image_0000002530753666.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=8F1A2CC3DB784C5A011FA3DE048359E9B8B24EC2E45060A6529EAFFC7DC33A4F)

断点命中时，在代码编辑器窗口单击右键，在弹出的菜单中将出现调试模式特有功能，如计算表达式、添加变量监视等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/XgYHNS8ATCW6VpjxvolWXA/zh-cn_image_0000002561833587.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=3432F810FB8D0BF9E8A79C1355FBD193FB46F2A84889F20E260C0D95ACBE8654)

在跳出所有断点后，测试结束，与运行模式相同，在测试窗口查看测试结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/rqXOcIgoSXqtr9o3mYUaNA/zh-cn_image_0000002561753599.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=13441A2F4A58A7AFABDF701CA93A87078DD5986DB5CB9FA02A459289F8768953)

#### \[h2\]覆盖率统计模式

在LocalTest运行的基础上支持代码覆盖率统计，当前仅支持ArkTS工程。

开发者可以自定义需要参与覆盖率测试的文件，具体配置方法请参考[配置覆盖率过滤文件](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section13756446154)。

如前所述，覆盖率统计模式也有多级别入口，以文件级别为例，有两种方式启动测试：

-   方式一：在工程目录中，选中文件，单击**右键 > Run '测试文件名称' with Coverage**，以覆盖率统计模式执行测试任务。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/37PM_13USZyLfhbYpYvsVg/zh-cn_image_0000002530913648.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=DCAB6B21CA664BC18A8C7A990CC3B48F4507D71B128195684B64A9A17F8D31BA)
    

-   方式二：在DevEco Studio的右上角，选择测试任务，然后单击右侧的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/3dp3tICTTV6A0vPTX8XyjQ/zh-cn_image_0000002561753581.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=8FD50BE3720188189DBDC8EA5E019804626932D25E4B6A6EEC7B652B1ED67319)按钮，执行测试。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/_0QiKQGyS3OueB1ESzn9aQ/zh-cn_image_0000002530913666.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=3771CCACDC8FB05F1B4D58434BEC1B76DF61F84BC996B35B153746025750D227)
    

启动测试后，进行编译构建，底部将出现Cover窗口，构建结束后自动拉起Cover窗口，测试任务结束后，窗口中会打印测试报告的路径。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/oL1WljhgSNi4h6Fnu9LK1A/zh-cn_image_0000002530913638.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=4C3A7A0179AD4529A1BBA86767ED819ADFF4A88352A7A9D7DDCE4AFE5B2AC2A4)

点击链接可打开报告，查看代码覆盖率详情，关于覆盖率的计算方式请参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/QiS2S9buTBmFr7FTI-vvRw/zh-cn_image_0000002561833561.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=D51CF7EC7576644527AB704B073402D43CC0F47F1069DF7B7B2C8037DC4F8E69)

在Cover窗口中，单击rerun按钮可以按照之前的设置，重新执行覆盖率用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/lNHbpPHtQuWGmvgDzbxrCg/zh-cn_image_0000002530753648.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=E2D1B82D31804AEFC61A41CE96FE3D16C2E21F0F577CCBA9359B8115F77D87C8)

#### （可选）自定义测试用例运行任务

默认情况下，测试用例可直接运行。如果需要自定义测试用例运行任务，可通过如下方法进行设置。

1.  在工具栏主菜单单击**Run**\>**Edit Configurations**，进入Run/Debug Configurations界面。
2.  在**Run/Debug Configurations**界面，单击**+**按钮，在弹出的下拉菜单中，单击**Local Test**。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/7p3Q6XiXT9-mZ0T3yI7bew/zh-cn_image_0000002530913632.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=3EE896488CA8BA03BF6A3808196060F9AE20129C3E464D696512A5D248E3EA1E)
    
3.  根据实际情况，配置Local Test的运行参数。 然后单击**OK**，完成配置。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/4tttNhACRRCknUApZdtY4g/zh-cn_image_0000002561753575.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=7B5DB3A09A1D607D2FF2915E6BA2D3329D2348872A6855AEB172D0D4A9B53026)
    

#### 使用命令行执行Local Test

通过命令行方式执行Local Test，在工程根目录下执行命令：

hvigorw test -p module={moduleName} -p coverage={true | false} -p scope={suiteName}#{methodName}

-   module：执行测试的模块。缺省默认是执行所有模块的用例。
-   coverage：是否生成覆盖率报告，缺省默认是true，在<module-path>/.test/default/outputs/test/reports路径下生成两份报告，一份是html格式（index.html），一份是json格式（coverageReport.json），具体参考[查看覆盖率报告](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ui-test#section10394362109)。
-   scope：格式为{suiteName}#{methodName}或{suiteName}，分别表示测试用例级别或测试套件级别的测试，缺省默认是执行当前模块的所有用例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/sWiJqsGSTzGP-F605iXw4Q/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=7471C8F821AF3C13620B0640DE53A31D3A84886DFEB9D640FF7FE79067D62313)

-   多个module和scope之间用英文逗号隔开。
-   暂不支持在Linux上执行该命令。

测试结果文件：<module-path>/.test/default/intermediates/test/coverage\_data/test\_result.txt
