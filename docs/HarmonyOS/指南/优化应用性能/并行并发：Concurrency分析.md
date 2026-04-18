---
title: "并行并发：Concurrency分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-parallel-concurrency-analysis"
menu_path:
  - "指南"
  - "优化应用性能"
  - "并行并发：Concurrency分析"
captured_at: "2026-04-17T01:36:51.945Z"
---

# 并行并发：Concurrency分析

任务池（TaskPool）（详细信息请参考[@ohos.taskpool（启动任务池）](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-taskpool)）是为应用程序提供一个多线程的运行环境，降低整体资源的消耗和提高系统的整体性能，且您无需关心线程实例的生命周期。您可以使用任务池API创建后台任务（Task），并对所创建的任务进行如任务执行、任务取消的操作。

DevEco Profiler提供的Concurrency场景分析能力，帮助开发者针对并行并发场景，录制并行并发关键数据，分析Task的生命周期、吞吐量、耗时等性能问题。Concurrency模板支持展示ArkTS异步接口、NAPI异步接口、TaskPool、FFRT并发模型相关信息，并集成ArkTS Callstack、Callstack、Process信息，支持用户从Task生命周期关联到具体调用栈信息，方便用户定位并行并发性能问题。

#### 查看Task统计信息

1.  选择展开某个泳道，可以用options下拉框筛选不同进程。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/xCxJpdKnSr2LEIQOnx44Gg/zh-cn_image_0000002561753355.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=25B85BD27CA5BBFA1B4194710AF61137B91F785588C6049EEE9D9E3270B5F301 "点击放大")
    
2.  框选子泳道中某段时间范围，详情区会出现该时段内，泳道对应执行状态下，并行并发任务的统计信息。
3.  点击Task Name的跳转按钮可跳转到对应的Task泳道。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/lBFO1w-RRnGRQ58_x34-8w/zh-cn_image_0000002561753367.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=BA46336A912E1C1A6CA315EC7A16B171C91D0F8AC0A50C2C495A01DC12DC7A97 "点击放大")
    

#### 查看某一个Task的所有状态

1.  选择展开某个泳道，可以用options下拉框筛选不同进程。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/5oRX1YLXREyZTFGS2B7JTg/zh-cn_image_0000002561833335.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=C9ED98A54922BB64DCC52DB1D06204D6AA2CD02229C0D2B8BB1255C892D5823F)
    
2.  框选子泳道中某段时间范围，可以看到该Task在框选时间范围内的任务状态。
3.  点击Task Name的跳转按钮可跳转到对应线程的泳道，可查看在该Task执行时间范围内，trace文件的打点信息，反映的是线程该时段内的函数执行情况。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/FHVvIsVaTnWkTxeAB5S5yw/zh-cn_image_0000002530753424.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=7858923FE01653152EFEA7377B9CD1A304E6FAD3105882C08C58E6EB602B1D7C "点击放大")
    
4.  展开Async ArkTS泳道，可单独查看ArkTS异步调用任务详情。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/wspZjHs9TC62TcxRM_DfOw/zh-cn_image_0000002561833343.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=0DFA7A2D43114CF3BDEA2B14E1691DE502D641BC6A6F13A0E41B00807E77B9E5 "点击放大")
    
5.  展开Async NAPI泳道，单独查看NAPI异步调用任务详情。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/yZKC1fuYTU2dUsotRc3Apg/zh-cn_image_0000002530913414.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=0562C98EB110FB377E36EB7EBE2F026EE0E59F325F45518F93002849AD9E04AE "点击放大")
    

#### 查看Task的某个状态

点击Task子泳道的某个执行节点，Details详情区里会出现task在该状态下的详细信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/LIKvg2jySz2vSke9SUlIPw/zh-cn_image_0000002561753359.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=F24BFD4EDD61C3B0B1FB25F8DBD947715E28362128A73A98032E754BBBEA38D9 "点击放大")
