---
title: "ArkUI分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-analysis"
menu_path:
  - "指南"
  - "优化应用性能"
  - "卡顿丢帧分析"
  - "ArkUI分析"
captured_at: "2026-04-17T01:36:51.749Z"
---

# ArkUI分析

ArkUI分析用于定位由于组件耗时、页面布局、状态变量更新导致的卡顿问题。常见场景包含：

场景1：布局嵌套过多引起的性能问题；

场景2：数据结构设计不合理，应用使用一个较大的Object，在更新时，只更新某些属性，导致其他没变化的属性也会更新，产生冗余刷新；

场景3：父组件中的子组件重复绑定同一个状态变量进行更新；

场景4：未正确使用装饰器，如错误使用@Prop传递一个大的对象进行深度拷贝。

#### ArkUI Component 泳道：查看组件绘制耗时

开发者通过ArkUI Component泳道可以直观感知组件绘制频率、耗时等统计情况。

1.  在时间轴上拖拽鼠标选定要查看的时间段。
2.  详情区Summary列表给出录制时段内定制组件以及系统组件的绘制统计情况，包括绘制次数、总耗时、最小耗时、平均耗时、最大耗时、耗时标准差。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/qbDkoGtGTHq8FtnqOfO2JA/zh-cn_image_0000002530912850.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=D099B8887EE9F70883C2D7A8AA8F08221B3BC7F6DC474655BB044C0C2E51FFF5 "点击放大")
    
3.  详情区Details列表可以查看按照时间线排序的组件详情，同时more区域展示以该组件为根节点的组件树信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/goSZsubkQiqCVJQiV-Og8A/zh-cn_image_0000002530752844.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=33CC444F96C95990A9BD31DA79C2001964547B78E2624CF9F053B7CF62861944 "点击放大")
    
4.  点选ArkUI Component泳道中的条块，展示Slice Detail数据，Slice Detail中的Name支持跳转至对应Process子泳道并选中trace信息，同时more区域展示以该组件为根节点的组件树信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/iZy4cxOrRqiyJLRdwLF-Cg/zh-cn_image_0000002530912840.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=E139B09D9A5D6B55246CAE5370D38F156132002F29D59798948271A0CB24C3A2 "点击放大")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/kAHjNv6sQlCthGd296v_tw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=236FDE78810CA42D3A9A4EF9E81D4089EF438F74E4EDE9D1FCBC52FA74D4C93A)
    
    由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI Component泳道。
    

#### ArkUI State 泳道分析

1.  点击ArkUI模板创建session并启动录制，录制过程中触发组件刷新。
2.  录制结束等待处理数据完成。点击ArkUI State泳道，可在下方数据区查看录制过程中发生的状态变量变化。Summary区域可查看状态变量名称，变化次数，状态变量类型、所属组件和所属类。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/TklgDsq5TVqn5UDv5HmXIg/zh-cn_image_0000002530912844.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=88B12FFA3FE8BC5F397C0D1E19248F2BF2D669AB269DC7498F4B904925B3A9DF "点击放大")
    
    Current Value以时间顺序展示状态变量变化，Current Values列展示变化后的值。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/OAPOArJ-TMy5tGfvSZj3ng/zh-cn_image_0000002561752783.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=F211D9B4ECEB01E7E72DDE77116EA8F6146103E8B9BBAA03A7E3B517D55EAF51 "点击放大")
    
3.  选择Current Value中某一个数据，泳道区域将以虚线展示其时间位置。同时，右侧More区域展示该状态变量影响的组件关联关系。打开页面下方的**Delivery Chain**开关，该状态变量影响的组件关联关系将以图形展示。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/wOI76i17TDK5_OcDQnJRhw/zh-cn_image_0000002530912846.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=0389A709482E15AF035247B691D672346D1C8C6BEA51E92882B602C2CC36A5BE "点击放大")
    
4.  定位到可能造成卡顿的状态变量变化时间点，框选对应时间段，选择ArkUI Component泳道查看对应组件刷新时间。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/Cro8cHBlSrusCpr4pMHlCA/zh-cn_image_0000002561832767.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=916A006C6F1FDC1706A275E87CBF8163FB661524D01978F9137D3B37E05B7CFD "点击放大")
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/Bq0UQIueTcqKlRjLLmSUoA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=00A53DA92398762DF2D450D8008062D5A001F89AD630F8878F2D1CFF889C0FCB)

-   如需查看其他泳道信息，请参考[Frame分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame)。
-   由于隐私安全政策，已上架应用市场的应用不支持录制ArkUI State泳道。
