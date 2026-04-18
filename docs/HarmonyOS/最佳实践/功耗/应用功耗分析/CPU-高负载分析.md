---
title: "CPU 高负载分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-high-cpu-load-analysis"
menu_path:
  - "最佳实践"
  - "功耗"
  - "应用功耗分析"
  - "CPU 高负载分析"
captured_at: "2026-04-17T01:54:18.502Z"
---

# CPU 高负载分析

#### 日志获取

对于CPU高负载问题的分析，需要在Profiler工具中启动Energy模板分析任务，并重现问题场景。

IDE工具中集成了CPU高负载故障的异常检测功能，操作步骤如下：

1.  点击Profiler工具，选择要分析的应用进程，创建一个Energy Session，按照复现路径操作应用，捕获大约15秒的信息。
2.  观察Energy Anomaly泳道，若标注为红色的异常则表示已识别到CPU高负载异常。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/exW-ZB9PT_-fPDJzZuy2GQ/zh-cn_image_0000002370405460.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=CEFC613B2723D7E197610B3A8B68287FDA5B9C0E48836D65A56EEA0AB0DD2FF7 "点击放大")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/uh2e4YkuRQCA07Gww0s5pA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=0EC481EB537FA44BD5A612F56B7723AD30BCFAD52339E02EB59C706F2B598D6D)
    
    CPU负载是3秒内的平均负载值。如果线程连续在大核最高频率下运行3秒，负载值将达到100%。当线程在不同的核心、不同的频率下运行，且运行时间不同时，将根据芯片的计算能力和运行时间进行相应的比例折算。
    
3.  点击More中的箭头，可直接查看当前函数执行的总时间比较长的函数，可接着分析函数执行时间长的原因。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/LSKYF1uXQ1eQeXZHz3M-Rg/zh-cn_image_0000002404045185.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=9053D381A838200E746FB206BCBDA3C4714BADFEA33EF9CB5799B188698C104F "点击放大")
    

#### 分析思路

CPU高负载问题通常涉及以下三种情况：

1.  GC线程负载高。需要通过Allocation和Snapshot模板来分析内存使用情况。
2.  UI线程负载高。应通过Trace泳道分析是否存在冗余绘制及组件未复用等问题，主要结合应用主进程、render\_service、RSUniRenderThre以及RSHardwareThread这些管线中的帧率、帧长和未送显情况进行详细分析。
3.  应用侧其他线程负载高。需要借助Callstack泳道分析函数栈，排查应用的业务逻辑是否存在异常，是否频繁执行了长耗时任务，或因异常业务逻辑导致了无限循环。

针对上述情况进行详细分析和定位，确认根本原因后进行修复，随后观察功耗和发热情况是否满足性能要求。如不满足，则需重复上述分析和定位过程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/y0Oa7Z6nRu2LeI-_xJ67BQ/zh-cn_image_0000002416845134.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=7D45860100D253FFDC9AECD4E3F60555B73756942076DC55F039E3CB100DA183)

#### 分析步骤

#### \[h2\]案例一：应用侧某线程负载过高

某应用使用过程中，边刷视频边查看评论或推荐时，手机发烫严重，关闭应用后逐渐恢复正常。

1.  在Profiler工具中开启Energy模板分析任务并复现问题场景。
2.  观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu)。
    
    选择CPU Core泳道，通过下方详情区可以看出应用进程占比时长较高。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/g-Gf5xAzTpmUYSop7Dmunw/zh-cn_image_0000002404125017.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=D5C2465BF49E9BE4838BF3B6D453190141BC9FA46B26C73FFAB8980C256314DF "点击放大")
    
    查看CPU频点情况，通过查看Frequency泳道发现CPU核的频点都很高，CPU调度非常频繁。
    
    Frequency子泳道：表示CPU频率，鼠标悬浮在Frequency泳道上，可以看到CPU的运行频率。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/pNamSyJsRuqiwMaL2TQYWg/zh-cn_image_0000002370405468.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=97FECBAD591C22E1EDB3A82FA567FCF3CA58D03707D3939C08FC5472D6CAD967 "点击放大")
    
    当所有CPU核频点都较高时，选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用侧的子线程（线程号55523）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/2Vt7GzNUQ1uWMbIIbHgzLQ/zh-cn_image_0000002404045189.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=3CA1BAD7B6335140E3C282117CE5FF444746B7706F2BE99FFFDE8BCD67FA98CE "点击放大")
    
3.  根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用侧的子线程（线程号55523）。需要借助[点击完成时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-complete-delay-analysis)该线程执行的任务，结合函数栈排查业务逻辑是否存在异常。大多情况下都是由于该线程频繁执行长耗时任务或者无限循环逻辑导致的。

#### \[h2\]案例二：GC线程负载过高

某应用使用期间，屏幕发烫严重，壳温高达40摄氏度；结束应用后，温度自行恢复正常。

1.  在Profiler工具中开启Energy模板分析任务并复现问题场景。
2.  观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu)。
    
    选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。不同应用的应用进程名称不同，一般与应用包名一致。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/KGClUwgiQmmgw1psesKjbw/zh-cn_image_0000002370565356.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=76821173A9FD0E57D45F214D0624880E9489ADA7E570AB77DE168281D7461C4D "点击放大")
    
    查看CPU频点情况，通过查看Frequency泳道的CPU频率可以看出CPU部分核上频点很高，基本保持在最高频状态运行。即下图中的CPU10、CPU11，其对应的Frequency子泳道基本被填满。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/3Cl_TmUoTpWyq9E4Rw6zJQ/zh-cn_image_0000002404125021.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=03397EB406BDE956C72A8B75CA8EE9EA9F5C6FFF02A7641C3C814C909B3476CF "点击放大")
    
    当部分核频点较高时，选择CPU频点比较高的核对应的Slice子泳道，查看CPU负载来源。即CPU10与CPU11对应的Slice子泳道，通过详情区可以看到CPU负载主要来源于应用进程的OS\_GC\_Thread线程。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/vY3dLvMLSPKzQf06BRD6xA/zh-cn_image_0000002370405472.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=2933D74464F632E82C0E4A94CB451828481FE67BBCFADD913704C3624BDDD913 "点击放大")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/QhU5D5PhSQGShmfiWjL8yQ/zh-cn_image_0000002404045193.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=05A444B813AA8FD61BAEEAEAB40B225416D43857DB1A9B3540A3238ACE4930FC "点击放大")
    
3.  根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用进程的OS\_GC\_Thread线程。针对GC线程负载高的情况，需要借助Allocation和Snapshot模板具体分析内存使用情况。详细分析方法参考：[Allocation分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-allocations)和[Snapshot分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-snapshot)。

#### \[h2\]案例三：UI主线程负载过高

在某应用上进入直播页面进行观看，功耗超100mA，手机温度持续升高。

1.  在Profiler工具中开启Energy模板分析任务并复现问题场景。
2.  观察CPU Core泳道找到运行时长占比比较高的线程，详细分析方法可参考：[CPU活动分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu)。
    
    选择CPU Core泳道，通过下方详情区可以看出，应用进程占比时长较高。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/fry0Z5wcS66nMUJ7j5d_Ag/zh-cn_image_0000002370565360.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=F0D0979BE3A9EABF5C5785E0AE4D42CB1F6FA448417107F900AAA1CF24F6D223 "点击放大")
    
    查看CPU频点情况，通过查看Frequency泳道发现CPU部分核（CPU10、CPU11）的频点很高，且每个CPU核调度都非常频繁。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/sAjYBSzVSLKBABNyGUY57w/zh-cn_image_0000002404125025.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=98F2B1DE09717ECA6B5291C8D69EA881C6D0C0AFCE1CF481FE8043EAFB514FF1 "点击放大")
    
    选择CPU Core泳道，查看CPU负载来源。通过详情区，可以看到CPU负载主要来源于应用UI主线程（线程号43436，与应用进程号一致为主线程）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/e8X8eRrHQuGn-wd7QCWBsA/zh-cn_image_0000002370405476.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=D003708D64C49ED50ABA7E2AD9A8D126805F8F7A9D3E9657A1F986AA801F33F2 "点击放大")
    
3.  根据CPU高负载线程类型进行详细排查。本案例中，CPU负载主要来源于应用UI主线程。需要分析UI主线程的Trace泳道判断是否存在冗余绘制及组件未复用等情况。
    
    找到UI主线程对应的Trace泳道（可以根据应用包名或上一步中的线程号查找）。选择对应的线程泳道，可以看到详情区包含了线程运行状态，选择Thread States，可以看出Running状态占比非常高。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/AXRjgUT5TW-SwJf9lXowSA/zh-cn_image_0000002404045197.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=6939C9B823314CDB65E1C9C78187F8606E0D5068DCE94222296C74A852A4B4C6 "点击放大")
    
    查看Slice List，检查是否存在冗余绘制及组件未复用等情况。选择Slice List，发现id为-1的Image一直在执行绘制任务，Occurrences达到了4万多次。然后借助ArkUI Inspector工具进行排查确认组件是否存在冗余绘制情况。关于ArkUI Inspector的使用可参考：[布局分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/yzGFy8cySxOk8Gb3l-_NkQ/zh-cn_image_0000002370565364.png?HW-CC-KV=V1&HW-CC-Date=20260417T015420Z&HW-CC-Expire=86400&HW-CC-Sign=231D106FAFF1B039EAEB7BD78D228FFC7E15F2ED010B4FACBE3054F278093B93 "点击放大")
