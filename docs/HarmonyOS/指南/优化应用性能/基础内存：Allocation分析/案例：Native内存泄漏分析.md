---
title: "案例：Native内存泄漏分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-native-allocation-case"
menu_path:
  - "指南"
  - "优化应用性能"
  - "基础内存：Allocation分析"
  - "案例：Native内存泄漏分析"
captured_at: "2026-04-17T01:36:51.929Z"
---

# 案例：Native内存泄漏分析

本案例介绍如何判断应用存在Native内存泄漏。

DevEco Studio 6.1.0 Beta1以下版本，通过Native Allocation泳道找出Native内存泄漏的原因。

DevEco Studio 6.1.0 Beta1及以上版本，通过All Heap泳道找出Native内存泄漏的原因。

#### 初步识别内存问题

1.  使用[实时监控功能](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/realtime-monitor)对应用的内存资源进行监控。正常操作应用，观察运行过程中的应用内存变化情况。
    
    监控Memory用到变化。当在一段时间内应用内存没有明显增加或者在内存上涨后又逐渐回落至正常水平，则基本可以排除应用存在内存问题；反之，在一段时间内不断上涨且无回落或者内存占用明显增长超出预期，那么则可初步判断应用可能存在内存问题。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/hst_HGReRYu253OM5dzq7Q/zh-cn_image_0000002530752708.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=E10BC10E19AD84C644F2C2227C645D62315BA91E7D3DF0DD3615A3DB3C33B3AC "点击放大")
    
2.  当从实时监控页面初步判断应用可能存在内存问题后，通过[深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)抓取应用内存在问题场景下的详细数据，初步定界问题出现的位置。Memory泳道存在Allocation或Snapshot模板中，使用Allocation或Snapshot模板录制均可。
3.  以Allocation模板为例，创建模板后，将模板中的其余泳道去除勾选，仅录制Memory泳道的数据。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7/v3/DyuiPDhuRmiX4mo-Wt21Gg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=EC0A8C45F7C51E6B4F1BE518CD5ED932112C93EE96392751336656EC7C428D1E)
    
    其余泳道会抓取内存分配、内存对象等数据，为避免额外开销和影响分析，建议先排除录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/n9qgvlJJSjidgTqworK4-w/zh-cn_image_0000002530912718.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=6859CA02A02F2A37D6F1876BC7A1C4CD2C7014F2FFB8DDD411BB5D9D782D7669)
    
4.  点击三角按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/zl2g_dC0S0C6_sf-RrPbEQ/zh-cn_image_0000002561752653.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=30DB42F238A0F5B0B959D014FE36D082EFBBD0479E3DA8FC6C645A207A8DB0E1 "点击放大")即开始录制。
5.  录制过程中，不断在问题场景操作应用功能，放大问题便于快速定界问题点。
6.  点击下图中方块按钮或者左侧停止按钮结束录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/jkSBRhF_Ty24oeP9cfAF_g/zh-cn_image_0000002530752718.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=61C6FEC16C07D1B47FF6560B1C5C6090FD6BCA8020F23C9A385AD2A9731ECB30 "点击放大")
    
7.  录制完成后，展开Memory泳道，其中Native Heap表示Native内存，主要是应用使用到的一些涉及Native API所申请的内存以及开发者自己的Native代码所申请使用的堆内存（通常是C/C++），这部分内存需要开发者自行管理申请和释放。
    
    当Native Heap有明显的上涨，说明Native内存上可能存在内存泄漏，可以使用[Allocation模板](#section776643810160)进行下一步分析。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Ugzx6H4MQXSySG1_mwArrA/zh-cn_image_0000002530912732.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=87268B8825C88EF2F3806AD14CFF137D3E461CD5EEA79C377A953669BFD13EAA "点击放大")
    

#### 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1及以上版本）

#### \[h2\]录制模板数据

1.  连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2.  创建模板后，点击三角按钮即开始录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/avuQNLM8QIKzKUdD2pCSPg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=385DD893C2D79C51D08869324FF510322929485925082BEB13428F69165E0BE2)
    
    如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/zqwuarzhTmiIbJfMVnHfmA/zh-cn_image_0000002530912730.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=B61F7E4E8EED501196B0CA8973B7637AE4300C70CCCAF148EE5328BB35BB74EB "点击放大")按钮。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/lZMCMfBJQ5KiQRl5uwaSYQ/zh-cn_image_0000002530912720.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=B57D70167D3329495792B57C4ECF246E486CC8F0B2D68CA178A1DB4B75D59754 "点击放大")
    
3.  操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/TLv9aUucSt-iMAxQs51-vQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=36357DC01F95978331A84E986AB09BA40EAA1CE3514BB9C695041125A2DCE175)
    
    默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/hp9TLSHKR3O7-kn2APPeNA/zh-cn_image_0000002530912726.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=FEACEB4417451923CCF74E0B07CB372EFBD0FAD1D0D4B648EC26B6EF77D95CBD "点击放大")
    

#### \[h2\]分析Native数据

1.  框选All Heap中的Native Heap子泳道。

2.  在下方详情区的“Statistics”页签中选择Created & Existing。
    
    -   All Allocations：框选的时间段的所有分配内存信息。
    -   Created & Existing：默认选中，在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
    -   Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/KG010iiRQAC7It23CrBVeA/zh-cn_image_0000002530912724.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=C6DE191993DC3953791402130EABD3D1278D055A78FB7745BC9D551B681C9D68 "点击放大")
    
3.  切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/yAqBIDDASwaniEbydDe6eg/zh-cn_image_0000002561752663.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=62A1DD38A4A1878D928320E464CC2B26358497A779DE9F8A9CA7C4F73DF75F5F "点击放大")
    
4.  优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/C4IAANW5TBaEfRwppHIBEA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=A0A8C16DBB4AE96C8F4A7C043543287DC2FB8981A307B5F20B4926FCE04062E3)
    
    -   Category中亮色代表开发者调用栈，灰色代表系统调用栈。
    -   栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-data#section11376118192614)）。
    

#### 使用Allocation模板分析Native内存问题（DevEco Studio 6.1.0 Beta1以下版本）

#### \[h2\]录制Allocation模板数据

1.  连接设备后，点击应用选择框选择需要录制的应用，选择**Allocation**模板，点击Create Session或双击Allocation图标即可创建一个Allocation的录制模板。
2.  创建模板后，点击三角按钮即开始录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/6IZBStuhTSq2cQYZUzH9ow/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=D3A80B1438F4C76ADD58F3DDFAA48CE5A83AC3B8D052B08D1F12B2ECF5C423D0)
    
    如果要分析启动内存，单击Allocation任务后的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Keprm5oJRq-g5EIsGqyg_w/zh-cn_image_0000002561832631.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=F6F41C85B806D55A3CB73F4D287A94F66ACB6929CE3AF3C7D3C464F9A30451BB "点击放大")按钮。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/XxmQqD5dTQycePXHcc6I9w/zh-cn_image_0000002561832633.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=FD5FF67E97754B5620CD96CAE23AB8AC182E575351FCEA5EE3B2106B259615F6 "点击放大")
    
3.  操作应用复现问题场景，并在问题复现完成后，点击下图中方块按钮或者左侧停止按钮结束录制。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/48q-AJncT7atLD7OzCxGNA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=67079D236DD6A02696122B0C5DDB5BD676EB5D45434232D14F1978774E3B29AE)
    
    默认使用统计模式采集数据。该模式下工具的采集性能更好、负载更低。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/yKFk4ql2QAyrEQXLGS98ZA/zh-cn_image_0000002530752722.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=09C6E6507ED0C98B0C74D2DB0CC3E529845DD1D5D86625532420585D63924FF8 "点击放大")
    

#### \[h2\]分析Native数据

1.  框选Native Allocation泳道或子泳道。两个子泳道All Heap和All Anonymous VM分别代表使用malloc和mmap函数分配的内存情况。

2.  在下方详情区的“Statistics”页签中选择Created & Existing。
    
    -   All Allocations：框选的时间段的所有分配内存信息。
    -   Created & Existing：在框选范围的起点之后分配的，且在框选范围的终点之前没有释放的内存数据。
    -   Created & Released：在框选范围的起点之后分配的，且在框选范围的终点之前已经释放的内存数据。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/dxR1ChyUTKOGdRIzInyEOw/zh-cn_image_0000002530912712.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=9B1BCCD0D8E1AB837A6E163E838F3B7A8138798559763EA61ECF9BB80F676AF9 "点击放大")
    
3.  切换到“Call Trees”页签，该部分数据展示了详细的内存分配栈信息，同样需要选择Created & Existing。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/vsSbnUjHTsWPhX2Ci_1S1g/zh-cn_image_0000002561832641.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=B9BB03F63E92B54B8D22F5D6A4CA9333DDD668A1467A10E4F611EEFD4881BA04 "点击放大")
    
4.  优先在内存分配栈信息中寻找与业务代码强相关的Symbol Name，即Category中为亮色。从上图中看，主要泄漏点在业务代码侧，需要结合业务代码进行分析。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/ABIARK2KRQq8ZL1bxVdxnw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=4752FC1D623A11BC9F93269E48D43D3BAD0FFBB4E013DF3C28FACDE312CFFFF7)
    
    -   Category中亮色代表开发者调用栈，灰色代表系统调用栈。
    -   栈帧中主要为 Native 栈，除了应用本身编译的一些so及带有部分接口信息的so信息外，其他系统库部分仅展示so库与函数偏移信息，若需要查看这部分信息，需要导入相应版本的带符号的 so 库（具体参考[离线符号解析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-data#section11376118192614)）。
