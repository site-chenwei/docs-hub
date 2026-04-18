---
title: "Snapshot模板基本操作"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-snapshot-basic-operations"
menu_path:
  - "指南"
  - "优化应用性能"
  - "内存泄露：Snapshot分析"
  - "Snapshot模板基本操作"
captured_at: "2026-04-17T01:36:51.807Z"
---

# Snapshot模板基本操作

针对方舟虚拟机，DevEco Profiler提供了内存快照分析能力，结合Memory实时占用情况，分析不同时刻的方舟虚拟机内存对象占用情况及差异。

在DevEco Studio 6.0.2及之前版本，Memory泳道统计时支持选择PSS/RSS/USS中的一个或多个，可以从多维度度量当前进程的物理内存使用情况。

从DevEco Studio 6.1.0 Beta1开始，Memory泳道统计时固定为PSS、GL、Graph总和，在会话区不支持选择PSS/GL/Graph。

从DevEco Studio 6.1.0 Beta2开始，Snapshot支持导入混淆及调试文件，还原文件名称和文件路径；Shortest Paths页签支持实时切换和展示用户选择的对象。

#### 查看快照详情

1.  创建Snapshot场景调优分析任务，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)。
2.  设置Snapshot泳道。
    
    单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/1l8y7pLeSZC7ouhNqUetPQ/zh-cn_image_0000002561753311.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=242C7BAD198199A0119BEE94921DAC44037A139DF33AEF58D5709A3DF5407411 "点击放大")进行泳道的筛选，再次单击此按钮可关闭设置并生效。
    
3.  单击ArkTS Snapshot泳道的“options”下拉列表，可以设置是否需要抓取基础类型number的数据。默认不抓取。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/gBr419T2R6SRsyjSv1Moiw/zh-cn_image_0000002561833297.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=EE8A1650C71117992365EFEBC0F7AF7D37C763119DB312D753335C0005438ED8)
    
4.  开始录制后可观察Memory泳道的内存使用情况，在需要定位的时刻单击任务左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/pz5VpVnhQY-NK_WjR2-oyw/zh-cn_image_0000002530913368.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=5C275DC1461A11DD13D0DA85EDF390A2A7C4D419E3DED5A2F4AD006C5633EADC "点击放大")启动一次快照。
    
    “ArkTS Snapshot”泳道的紫色区块表示一次快照完成。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/AuKgOxT4S-2FNIQecWIuxg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=C34404B995C8DD54CC572E87D64D5053C84859B7C45DA5AAEEB02F977B500D46)
    
    -   在任务录制过程中，单击分析窗口左上角的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/bb_a5JibTtyHlFFlR2oTcA/zh-cn_image_0000002530753366.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=4B45D07824251B9C4C36C95E36D6A99326FCBD13202747CC273BC2FBE87A95E9 "点击放大")可启动内存回收机制。
    -   当方舟虚拟机的调优对象的某个程序/进程占用的部分内存空间在后续的操作中不再被该对象访问时，内存回收机制会自动将这部分空间归还给系统，降低程序错误概率，减少不必要的内存损耗。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/9d5L8DHySbiV8iu49vDQFQ/zh-cn_image_0000002561753281.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=E315B5F0D2735DB1A91079F60A6C92787CAEA6E2AB81973093EA401F35939B04 "点击放大")
    
    在“Statistics”页签中显示当前快照的详细信息：
    
    -   Constructor：构造器。
    -   Count：该对象的数量。
    -   Distance：从GC Root到这个对象的距离。
    -   Shallow Size：该对象的实际大小。
    -   Retained Size：当前对象释放时，总共可以释放的内存大小。
    -   Native Size：该对象所引用的Native内存大小。
    -   Retained Native Size：当前对象释放时，总共可以释放的Native内存大小。
    -   带![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/iig8a0tITa6_Ef5Toj685Q/zh-cn_image_0000002561753279.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=0D10A6C02884FC2B598C5D575DED2CF684BE42D273E8E4F3DD998068EA79E8FF "点击放大")标识的对象，表示其为全局对象，可以通过全局window对象直接访问。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/lY91MFaZRBSwaQZTFLJ35Q/zh-cn_image_0000002530753358.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=AE61C674C71D51318C6A75A93B551246F7DBE6D1DAA1B26B7958638100D44796 "点击放大")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/IhXOfdFfQJGahhH2QRwlAg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=C7437DE6DD3CD3D8A6B9B2F2C39A342200A95B3B701C8CD1D7CC1372667855C2)
    
    -   在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴；或使用快捷键W/S缩放时间轴，使用A键/D键可以左右移动时间轴。
    -   将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
    -   鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
    -   在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
    -   在任务分析窗口，可以通过“Ctrl+\[ ”向前选中时间段的时间标签，通过“Ctrl+\]”向后选中时间段的时间标签。
    

#### 应用对象名称解析

方舟系统目前有方舟应用对象、系统内部框架对象、其他JS对象三类对象，从DevEco Studio 6.0.0 Beta1版本开始，支持对应用对象类的名称进行解析，帮助开发者快速定位问题所在的源码位置，从而提升问题定位效率。

1.  系统内部框架对象：用于描述HarmonyOS操作系统底层框架的核心对象，提供基础系统能力。为方便开发者查看，当前在Statistics中此类对象均归类到（framework）构造器节点下。此类对象均以\_GLOBAL开头。
2.  方舟应用对象：用于表示HarmonyOS应用中的具体组件、模块或资源。方舟应用对象需按照以下格式命名展示：
    
    com.example.app/MainModule@1.0.0/src/main/ets/MainPage.ets#MainPage(line: 10)\[MainModule\] //格式为BundleName/SelfModule@Version/FilePath/File#Class(line: xx)\[RefModule\]
    
3.  其他JS对象：用于描述方舟运行时中与JavaScript引擎相关的对象，提供JS语言层面的基础能力。例如：JSArray、JSSharedObject等。

在 Snapshot分析模板中，支持在Attributes页签点击方舟应用对象名称查看当前所选方舟应用对象的解析结果，便于确认问题出现的位置。各参数含义如下：

-   Module：模块信息。
-   Class：属性名称。
-   Path：编译后的源码路径。支持通过点击属性名称旁边的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/CJYfdAscRuOMJaeNsIjjvg/zh-cn_image_0000002530753336.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=067A6E9B834AF9D7F71BFD3487703C1B5E68979595767FBB0242315E20DC1CCA)图标直接跳转至工程中的代码位置，方便开发者快速调试。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/T6Rqj01iQXitme16Zm7ahQ/zh-cn_image_0000002561753257.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=46E8560DA5822BC50FA491E3869486AED485BDA3C77BC83483772448BD3F36C2 "点击放大")

若应用编译模式是release，且启用了源码混淆，方舟应用对象将展示混淆后的数据。支持在Attributes页签查看当前所选应用对象的源码信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/2zXPFyZ-QCSXJQQyrEJgdg/zh-cn_image_0000002530913346.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=00938A9A33B61BBF36227E35D6A4BA512CCEC36A71E4EF8155D43F0FB256A6E8 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/WeVOYrjsSb6r8DhuTN8zYw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=04119007521B070BE0D8600159706FE32D8102F544556EE0C8FAF2A852EB881B)

-   确保工程代码路径与解析信息匹配，否则跳转可能失败。
-   系统内部框架对象（framework）仅提供基本信息，不支持跳转。
-   对象名称后的line=0时表示无效行号，不支持跳转。

#### 节点属性与引用链

在“Snapshot”的“Statistics”页签和“Comparison”页签中，所有实例对象节点展开后会显示"<fields>"以及"<references>"，这两项节点分别代表该实例对象的属性以及该实例对象的引用链信息。

在“Snapshot”的More区域则展示“Fields”和“References”两个页签，分别代表Detail区域所选择对象的属性以及引用链信息，方便快捷查看所选中对象的属性等详细信息，而不需要跳转至对应对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/ivzIsohETaGvcRShxt8-uQ/zh-cn_image_0000002561833277.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=449A8C946235ED1E7C0E03BD62701D57D5C33E913410C6C75F5C3D40CEA429B7 "点击放大")

#### 节点跳转

在“Snapshot”的“Comparison”页签中，查看内存对象、对象属性及其引用链时，若要查看某一对象的详细信息，可以单击该对象所在行行尾的跳转图标跳转至该对象所在的“Statistics”页签并定位至该对象所在的位置，以查看该对象的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/MFqfFiJbQ5SGjcilJBMhuQ/zh-cn_image_0000002530913334.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=90A244C854CE40778333701D4AEBB529A6BDEEF09F2E513120C2660871DE2814 "点击放大")

#### 历史节点前进/后退

当在“Comparison”和“Statistics”之间进行节点跳转后，单击详情区域左下角的左右箭头可以前进或者后退至下一个或上一个历史节点，以便快速在多个历史节点之间跳转查看。当箭头为激活状态时，表示前进/后退功能可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/HjHbJS6yQwOiommHznisyQ/zh-cn_image_0000002561833241.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=F1A200F3B03BD57846192FC7447761AB8093D334A1E00363E21BF0F60474045D "点击放大")

#### 比较快照差异

在“Snapshot”的“Comparison”页签中，以当前选择的快照为base，下拉框选择的快照为Target，即可得到两次快照信息的比较结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/Rkdjy7K6S0Gu3_-Easo8OQ/zh-cn_image_0000002530913354.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=39631E3EB0219B87E99DC33081A6477C25AFB18B5062DAEED82E2B2AE2E6C501 "点击放大")

在“Snapshot”的“Comparison”页签中，可进行两次快照的差异比较，比较内容包括新增数、删除数、个数增量、分配大小、释放大小、大小增量等等。通过不断对比，可快速分析和定位内存问题的具体位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/bbtSIP0eQ4CxzSVIKfZ7fg/zh-cn_image_0000002561833269.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=3846718671AB29AEC90A28210B26BD81563418DB27D4D5137D953FE25C17CEB7 "点击放大")

#### 引用链向最小引用距离展开

Snapshot分析支持一键向引用链最小的引用距离方向展开。系统会计算从GC Roots垃圾收集器根到选定实例对象的最短路径（最短路径是指Distance逐渐-1的路径，最终抵达Distance = 1的节点），通过最短路径，能够清晰地看到该对象的句柄被哪些对象持有，快速定位问题产生的根源。

#### \[h2\]DevEco Studio 6.1.0 Beta2及之后版本

选择一个实例节点，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签实时切换和展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/YwsFflGqS6ir_9qbXP7tQw/zh-cn_image_0000002530753348.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=002AF7E432E9079A22BD2E2F8DE07841C72D7EE69E14C76792F3B63894D6CDE0 "点击放大")

#### \[h2\]DevEco Studio 6.1.0 Beta2之前版本

选择一个实例节点，底部搜索栏的Path to GC Root按钮呈可点击状态。点击该按钮选择搜索模式并确认，系统会计算从GC Roots到选定对象的最短路径，并在右侧Shortest Paths页签展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/C5IwvEhmR8ehBPHzZdXyxQ/zh-cn_image_0000002561753293.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=6057C2A2D2BD948D519855F7DDA3B98835C0CDCB26684DE3B3C14AD4105858A7 "点击放大")

目前支持单根路径搜索、指定数量的根路径搜索和展示所有根路径三种搜索模式，默认为单根搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/o5f0y73tRc65Hxw6zz07dQ/zh-cn_image_0000002530913328.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=7D0ED8C26779D74F8FCE310C82B66E4B97C3CB432991CDEC66CC00D957ED64E5 "点击放大")

设置完搜索模式后点击OK，右侧more区域会自动跳转至Shortest Paths页面展示搜索结果。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/_0eHXz5-R2amLKGaLAUuWg/zh-cn_image_0000002530753354.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=92C3FD98DC669F01A1370E16E4964FC8F76CAB0C65C92BD97B0C3BA0AD5321AF "点击放大")

#### 引用链可视化

从DevEco Studio 6.0.0 Beta1版本开始，Snapshot模板支持将所有引用链以图表形式展示。系统会计算该节点周边的引用节点，并以关系图的形式清晰展示该对象的引用关系，便于定位问题产生的根源。

选择一个实例结点或reference引用关系节点后，底部搜索栏的**Visualization**按钮呈可点击状态。点击该按钮，配置搜索模式后，系统会计算该节点周边的引用节点，并跳转到Graph页签进行展示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/T9oY67L-TpiwNPMkL8-6ng/zh-cn_image_0000002530753370.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=5436FAF78CE2AF6E4D5DCC095886833F879AE74AB9412CC83E331C8DFE42FB5A "点击放大")

目前支持最多展示30个周边节点，默认展示20个。当前支持以下两种优先级的引用链展开方式：

-   Retained Size：按照Retained Size从大到小展示周边节点。
-   Distance：按照Distance从小到大展示周边节点。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/6FsymJSNQDuF80vNwPpaAA/zh-cn_image_0000002530753362.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=4B71941C6B646D8B7E1B4046A11FBEFB2910E0389F51BE7A7A638E35B12E94D7 "点击放大")

设置完搜索模式后点击OK，底部页签会自动跳转至Graph页面展示搜索结果，红色标示的是中心节点，线段展示连接的两个节点之间的引用关系。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/zO1aR_lyT72Y4aiYJ9PWdg/zh-cn_image_0000002561753263.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=B59FC748595D6A8FB63D9934AB792D7AB5BE01CD2730A26017F3ECFA0190A453 "点击放大")

支持选中节点，右侧的More区域将展示该节点的详细信息，包括Fields、References和Shortest Paths三个页签。当鼠标悬浮在图形上的节点或线段时，悬浮框将展示对应的详细信息。图形区域支持拖动查看，使用Ctrl+鼠标滚轮可对图形进行缩放。

当在节点点击右键，展示的菜单列表包括以下选项：

-   **Show More References**：展示当前节点更多的引用链。配置搜索模式后，重新生成以该节点为中心的引用链图形。
-   **Show Path to GC Root**：展示当前节点到GC Root的路径。选择搜索模式后，重新生成以该节点为中心到GC Root的引用链图形。
-   **Redraw with this node**：以该节点为中心重绘。
-   **Reveal in Statistics**：在Statistics页面中显示该节点。
-   **Clear Diagram**：清空当前图表中的所有内容。且清空底部栏的激活状态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/iR1X1yCzQJS5ia-apr9QFQ/zh-cn_image_0000002561753265.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=0BE22D30E633CE201B31D30048E3A739C328E26A309F2FEA0ED2D1B03DCB0482 "点击放大")

点击**Show More References**、**Show Path to GC Root**和**Redraw with this node**选项后，单击详情区域左下角的左右箭头，可以前进或者后退至下一个或上一个历史图形，以便在多个（最多三个）可视化图形之间跳转查看。当箭头为激活状态时，表示可用，当箭头为灰色状态时则代表无法使用该功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/6JYUkmWeTsGChbTAmV1HXw/zh-cn_image_0000002530753346.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=7A6113D39002EB43CD409095896DEB76F4C1A07BD55B17B8C5CB79214DCC7F48 "点击放大")

#### 离线导入内存快照

DevEco Profiler支持离线导入内存快照功能，可导入一个或多个.heapsnapshot及.rawheap文件。

您可以在DevEco Profiler主界面的“Create Session”区域中，单击“Open File”，导入.heapsnapshot或.rawheap文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/5Drr2P7HRemcaE9IT_l8CA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=A7BF8FB3A11D407287D261314DC54606DCDAF5F6B50DAE0DC3F9A77763FCAC96)

-   导入的单个文件大小不超过1.5G。
-   批量导入的文件数量不超过10个。
-   .rawheap文件是应用发生Out of Memory现象时产生的原始内存文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/hEV415LRSkiwyqEJ9Aygiw/zh-cn_image_0000002530913322.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=8D3703CCDEB97FEC032B848151543085123394C7625235F7F855CA9DDCFC8139 "点击放大")

离线导入内存快照成功后，可以导入与.heapsnapshot或.rawheap文件匹配的.jsleaklist文件，展示jsleakwatcher监控采集到的内存泄漏对象。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/4mTahxrDR-2XO59ORIxqYg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=F7D22E190BC45C589CE0F2947FBDA6A186B94F5E7469EE063C0936311DC0DD5A)

-   导入的单个jsleaklist文件大小不超过30M。
-   导入的jsleaklist文件通过文件中的hash值与已导入的heapsnapshot文件匹配。
-   可多次导入不同的jsleaklist文件，也可同时导入多个不同的jsleaklist文件，重复导入不会覆盖已导入的匹配上的jsleaklist文件。总的导入匹配成功的文件数量不超过导入的heapsnapshot文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/laTrvj2wT62h8MmSFI_Xmw/zh-cn_image_0000002530753340.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=C57EB79462DA1A8B3807F71BBB18FDA1C5160172DBA1D3469B81F5D4418A0E5A "点击放大")

#### 解析内存对象

DevEco Profiler支持导入[代码混淆产物nameCache](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section19215122372720)文件和[ArkTS调试产物sourceMap](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-exception-stack-parsing-principle#section666114451518)文件，还原文件名称和文件路径。

以nameCache文件为例，文件导入前，Class为d8，

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/b3ZKKN06RmiH4LprmoeI6A/zh-cn_image_0000002561753285.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=553CF9E94230FFF168A79F16F41437ECBD275D45B4CBC40B177384D15A9A4A90 "点击放大")

点击工具栏![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Ddo3r4BHT82E_Fzk3pA5hg/zh-cn_image_0000002530913326.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=697240045121DE1FD42323E1677CBEFEFF398EA28C9CD13FFFAC73F8E3D06213)按钮，导入nameCache文件，Class显示为文件名称MyAbilityStage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9yoxOOqfTlCMFBn1pGMSDQ/zh-cn_image_0000002530753368.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=10463BB7691D2C8E9051AB32DCE5DFEACA6299122283781A13165FAAFD1D61E5 "点击放大")
