---
title: "GPU活动分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-gpu"
menu_path:
  - "指南"
  - "优化应用性能"
  - "GPU活动分析"
captured_at: "2026-04-17T01:36:51.965Z"
---

# GPU活动分析

从DevEco Studio 6.0.0 Beta3版本开始，DevEco Profiler提供GPU模板展示不同GPU硬件模块利用率的详细信息，这些信息可用于识别GPU利用率低、执行图形和计算工作负载性能瓶颈的根本原因。

#### 约束与限制

-   该功能仅支持中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）。
-   仅支持Phone设备。

#### 操作步骤

1.  创建GPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)。
    
    GPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/hn36PFIlTxiyCpPGJF4N0A/zh-cn_image_0000002561753031.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=168AF6136774BE5AD17D092834B23F8C04B291FA9FA116AED829EB5539BC5200 "点击放大")指定要录制的泳道。单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/2H-bAMoBRwmIPRWzsoW7XQ/zh-cn_image_0000002530913086.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=BA595D1749F7314D7E1FB3DABBEA39DDDA20F65AC22FDDB719C240F5CB23AC75 "点击放大")按钮，可以设置采样时间间隔（Sampling Interval），可设置范围为1ms~1000ms，默认为10ms。
    
2.  “Counters”泳道显示当前设备GPU的使用率，“ArkTS Callstack”、“Callstack”、“CPU Core”等泳道信息请参考[基础耗时：Time分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-time)和[CPU活动分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/bfIVGROdRt2PeA6kvQCQgg/zh-cn_image_0000002530753088.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=CBAE3CDB2BC254737FDF9E4A893CED519CFF8488F6566569D6F26B22DC7ACD81 "点击放大")
    
3.  将“Counters”泳道展开，子泳道显示GPU各项活动信息，包括counters\_gather、GPU执行命令的频率、GPU执行命令的持续时间等。除counters\_gather外，其他子泳道信息可参考[GPU Counters](https://developer.huawei.com/consumer/cn/doc/Tools-Guides/gpu-counters-0000001886127538)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/0ahQomcnQ3KhfJBzcvI1QA/zh-cn_image_0000002530913084.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=4F71907500862019BE66FF33473501685987CD0172D7D3A66DC318CC6D15266A "点击放大")
    
4.  counters\_gather泳道显示线程对各CPU核心的占用情况。单击运行状态的时间片段，显示线程在该时间片段的起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态，并且支持跳转到上个或者下个线程运行状态。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/94q2-5YISMWhkYeqqi8p5A/zh-cn_image_0000002561833021.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=FC82ADCB53E7DD71CCB69660645DD38310F0DE93D7BCB6B4B717ADFF7394982D "点击放大")
    
5.  框选counters\_gather泳道，可查看此时间段内的统计信息，包括线程状态统计信息、CPU单线程使用情况、线程中的中载重载数据统计。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/_mFBUppFTgWVlck7yRPVPA/zh-cn_image_0000002561753035.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=DC61A6E3AC5D898E38E802D1CD6F87DB390D56C9D9F9DDD2F2CD2DC59E1E53B9 "点击放大")
