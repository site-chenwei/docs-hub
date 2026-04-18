---
title: "CPU活动分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu"
menu_path:
  - "指南"
  - "优化应用性能"
  - "CPU活动分析"
captured_at: "2026-04-17T01:36:52.028Z"
---

# CPU活动分析

开发者可使用DevEco Profiler的CPU场景调优分析，在应用或元服务运行时，实时显示CPU使用率和线程的运行状态，了解指定时间段内的CPU资源消耗情况，查看系统的关键打点（例如图形系统打点、应用服务框架打点等），进行更具针对性的优化。

#### 查看各CPU使用情况

1.  创建CPU分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)，或在会话区选择**Open File**，导入历史数据。
    
    CPU分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/uBvqsgtATy-0PMiNQ2YC_Q/zh-cn_image_0000002530753316.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=27F5AC529091179F62DC684EBD1C632FB2034C3CD4A7D39A1AEE1494A6E41A52 "点击放大")指定要录制的泳道。
    
2.  “CPU Core”泳道显示当前选择调优应用或元服务的CPU的使用率。
    
    可在“CPU Core”右侧的下拉列表中选择显示内容：
    
    -   Slice and Frequency：每个子泳道包含时间片和频率两部分，时间片显示占用该CPU核心的进程、线程。
    -   Usage and Frequency：每个子泳道包含CPU核心使用率和频率两部分。
    
    框选主泳道，可对所选时间段内的CPU使用情况进行汇总统计，可查询多时间片的进程维度统计信息、线程维度状态统计信息、线程状态统计信息，以及所有时间片的数据统计信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/F-xPvGhySValGmqCEejLAw/zh-cn_image_0000002530913304.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=3E80D96AF68E4BF020F7AE16757019E3EA0B6D94ABD90771DA157EC4E4D5CDAA "点击放大")
    
3.  将其展开，子泳道显示各CPU核心调度信息、各CPU核心频率信息以及各CPU核心使用率信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/FUI0vib7SImjpDN2e7Nugg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=F4D78E15633248004A6530585E453A3F7662C1F253D7D9F5B215821583A89EDE)
    
    将鼠标悬浮在某时间片上时，能够置灰非同进程时间片，通过此方法可以确定时间片的关联性。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/PQTEfwgvTse9bpV4Wqp67g/zh-cn_image_0000002530753302.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=A024AC804CC811D10BFF8B94B7E4721F4DFE096DE9FD25C2169CB1D0FB804530 "点击放大")
    
4.  指定时间片，查看统计信息。
    
    -   单击某个运行状态的时间片，可查询这个时间片的基本运行信息及调度时延信息。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/cqaDS2i_SXiOqxX-qKsCjA/zh-cn_image_0000002561833239.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=9DA9C96D99407EFF7ADE088467627E4F3779B02D3204D0146F7CC6B7733BACA8 "点击放大")
        
    -   框选多个时间片，则可查询多时间片的进程维度统计信息以及所有时间片的数据统计信息。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/q0eyEhI-QUuXL-2zKTTzVA/zh-cn_image_0000002530913306.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=6CA4EDDF96AC45714B70BDFB7AC7B45517FB39087004FC43AF994FB2B4173BB2 "点击放大")
        
    -   开启"View Integrated Scheduling Chain"后，点击CPU时间片泳道的节点可以查看某一个CPU运行线程的完整唤醒调度链。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/4Vi9DYMaT-O2BK2Zxc53Yg/zh-cn_image_0000002561833231.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=2037CFEC207A1C003FAACFDEF09D2A46E233733600DC55A7673422DEDF36E1F5 "点击放大")
        
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/53si_wMwS0uDiYnOYJjJ2g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=62F2DFC0053C4CE9E35F75FCD2526F369516414E98EB8F49F8123ED7BD0857FF)

-   在任务分析窗口，可以通过“Ctrl+鼠标滚轮”缩放时间轴，通过“Shift+鼠标滚轮”左右移动时间轴。或使用快捷键W/S放大或缩小时间轴，使用A键/D键可以左右移动时间轴。
-   将鼠标悬停在泳道任意位置，可以通过M键添加单点的时间标签。
-   鼠标框选要关注的时间段，可以通过“Shift+M”添加时间段的时间标签。
-   在任务分析窗口，可以通过“Ctrl+, ”向前选中单点的时间标签，通过“Ctrl+. ”向后选中单点的时间标签。
-   在任务分析窗口，可以通过“Ctrl+\[ ”向前选中时间段的时间标签，通过“Ctrl+\]”向后选中时间段的时间标签。
-   CPU分析支持能耗分析，请参见[能耗诊断：Energy分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-energy)。

#### 查询进程详情

单击工具控制栏中的![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/FBsAzpYUQfKFGTNTCkTPew/zh-cn_image_0000002561833243.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=A6005AFFC64B51AEBCA2DD56A229BD2943F7AD4F940F7B961D8D959EF7C16719 "点击放大")按钮，可以设置是否为精简模式。精简模式下，trace数据量将大幅减少，主要采集当前进程、大桌面进程和render\_service进程的trace数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/WUWe9NluQ3Ww_AYgR55kZg/zh-cn_image_0000002561753251.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=FD7D05963B999FD723427BEDFB69BACD3F694B4D0693409638E326C89D530D07 "点击放大")

进程泳道显示进程对各CPU核心的占用情况。展开进程泳道，显示进程下的线程列表以及线程的运行状态。

-   单击运行状态的时间片，显示线程在该片段的运行详情，包括起始时间、持续时长、运行状态、频率、线程优先级、所属进程、所属线程、上一运行状态、下一运行状态、唤醒线程，支持跳转到上个或者下个线程运行状态，支持跳转到唤醒线程状态等。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/Pa5dK-VzSU-Bm0v6zDqdSw/zh-cn_image_0000002561753245.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=68868481555EBDC6FCC13A1B3DF3D2D166B3B94DA4D234E316969159019EFB98 "点击放大")
    
-   框选Thread泳道中多个运行状态的时间片，可查看此时间段内的不同运行状态的线程的统计信息，包括总耗时时长、最大耗时、最小耗时、平均耗时、处于当前状态的线程数量以及线程中的中载和重载数据统计。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/Otlli2HzRDmQylwzthJEfQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=5359B1E8B8F99E786C3BDBFD1A9D562E3B07DEB65FDAA7FB0A195C797AD9BFB5)
    
    中载、重载数据每100ms做一次统计，24ms < Running时长 ≤ 48ms 记为中载，Running时长大于48ms记为重载。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/mtOq7bm5QlWEhFFp-m9Fug/zh-cn_image_0000002561753259.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=C13D261D63B8B0A79E2FCA09D2FCA448C3D2D25E6F6F9FF64FAB284D1B8B15DE "点击放大")
    
-   框选应用进程Process主泳道，可查看此时间段内该进程下的线程并行度统计信息。并行度数据每100ms做一次统计，可以查看100ms内运行的总线程数量、各线程并行的总时间和并行度。点选某一行，可以查看对应线程编号和运行时间段。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/hT7ddsc9Tl2i0zV8FqUgHg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=265831413E88B513C9F62A87519AD618F676FA974B3E7FCED6793CB7BF28BD8F)
    
    并行度（Parallelism）取值范围是\[1,CPU核数\]，数值越小代表并行度越低。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/vWj3-k_fSQaP1A15eV5IWA/zh-cn_image_0000002561833237.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=03F6DD8FF67357622CD8D5C3DD49BB5831C12662C8864137DCDED75A6AF3E085 "点击放大")
    

#### 查看Trace详情

当存在Trace任务时，可在对应的线程泳道查看到当前线程已触发的Trace任务层叠图。选择待查询的Trace。

-   点选泳道中的Trace片段，可查看单个Trace详情，包括名称、所属进程、所属线程、起始时间、持续时长、深度等。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/KHLCxVIpTOWhIWBo5DauyQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=647F1992A032805D311881B4730D0F829F6A469CB5B8DD12821AE8F15BA7296F)
    
    -   如果用户对线程进行了自定义打点，在此处亦可查看到对应的User Trace打点信息。
    -   从所在线程名称可分辨当前Trace的类型，系统Trace对应的线程名称为“线程名+线程号”，User Trace对应的线程名称为“打点任务名”。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/yThoYc11REK1vLxet6mAJA/zh-cn_image_0000002561833225.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=8BC7022AF0B13A2FDADA8BE2094EBF54B7EC4BE8970F651F9D422E861446DB2C "点击放大")
    
-   框选多个Trace片段，可查看到Trace统计信息列表，包括Trace名称、此类Trace的总耗时、单个Trace的平均耗时、以及该时间段内该类Trace的触发次数等。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/abMzNzotTRiMpFMza2YD_w/zh-cn_image_0000002561833221.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=4EF1D62F25A9F1B9E29E8A1EDD41A0D5F1303A249660DB3CB4C9BB12EA9EEFE2 "点击放大")
