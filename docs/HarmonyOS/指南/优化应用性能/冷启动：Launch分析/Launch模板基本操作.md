---
title: "Launch模板基本操作"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-launch"
menu_path:
  - "指南"
  - "优化应用性能"
  - "冷启动：Launch分析"
  - "Launch模板基本操作"
captured_at: "2026-04-17T01:36:51.798Z"
---

# Launch模板基本操作

开发应用或元服务过程中，启动速度是很重要的一个指标。如果开发者需要分析启动过程的耗时瓶颈，优化应用或元服务的冷启动速度，可使用DevEco Profiler提供的Launch场景分析能力，录制启动过程中的关键数据进行分析，从而识别出导致启动缓慢的原因所在。此外，Launch任务窗口还集成了Time、CPU、Frame、Network场景分析任务的功能，方便开发者在分析启动耗时的过程中同步对比同一时段的其他资源占用情况。

此处仅介绍“Launch”泳道相关内容，集成的Time、CPU、Frame、Network场景分析任务的功能请参考对应任务的章节。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/xnjlMz3wTpuRL_NU7lOahw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=D126415A1CB7FF8290275C5F464E7535A605386B19888654BEEC5A83EF2F4A31)

-   不支持命令拉起的Release应用不能进行Launch分析。
-   锁屏状态下可进行Launch录制。

#### 启动模式

启动模式分为![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/BknwkVUzR6iIe4SFODANIw/zh-cn_image_0000002530912822.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=56AEF90D8AA6AD5219F77585680CB0AD0B3466C3766A90912343B7659C2B7CDA "点击放大")自动启动和![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/pDnRJAkHTp2MdCgxDXNlXw/zh-cn_image_0000002561832753.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=16C38120163B8A555EF784F045676D8951145449AC35EA51B69568B81A251C33 "点击放大")手动启动，可点击图标切换两种不同模式：

-   若选择自动启动模式，当用户使用Launch模板并开始录制时，将主动重启所选应用；
-   手动启动模式在开始录制时，只会主动终止所选应用，等待界面出现弹窗提示启动应用后，开发者需要手动启动应用。

#### 查看启动过程中各阶段的耗时情况

1.  创建Launch场景调优分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)，或在会话区选择**Open File**，导入历史数据。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/9Z7nyCyCQ6WDaJzlQF1PSQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=64BC5B5A3A24C585070D41A0BF9E716A8D91EE6212999E7EDE1BEACEAB0B2CF3)
    
    -   在任务分析窗口中，可通过[快捷键](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-shortcut-key)缩放时间轴、移动时间轴、添加时间标签等。
    
    -   Launch分析支持离线符号解析能力，请参见[离线符号解析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-time#section186881175012)。
    -   Launch分析支持动效场景调优，请参见[支持动效场景调优](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame#section258014238619)。
    
    Launch分析任务支持在录制前单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/78RZaZs-RPqdCElExioe3A/zh-cn_image_0000002561832759.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=6E73E08093E6652D825DCD65E6B3CBEDEF0AE32D4F507EE056796A1386C1FDCB "点击放大")指定要录制的泳道。“Launch”泳道显示启动生命周期各阶段的耗时分布情况。
    
2.  单击“Launch”泳道上的单个阶段，或框选多个阶段，在下方的“Details”页签中，可查看到所选阶段的耗时统计情况。
    
    展开各阶段的统计信息折叠表，可以看到各个任务的具体耗时信息。单击跳转按钮，可直接跳转至相关线程打点任务中。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/e_svfqtjROuAN3pXUi6cig/zh-cn_image_0000002530912832.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=4DE37367B16FA29F0A80AEFE57140B44FB965D13EE1DBA25612206F9A6742D56 "点击放大")
    
3.  切换到“Load ETS Files”页签，从DevEco Studio 6.0.0 Beta1版本开始，支持查看冷启动过程中ETS文件的加载情况。各字段含义如下：
    
    -   Category：该ETS文件在应用启动过程中是否被使用。
    -   Weight**：**该ETS文件加载子节点文件（不包括自身）的总耗时。
    -   Self：该ETS文件自身加载的耗时。
    -   Import Count：该ETS文件被其他文件导入的次数。
    -   File Name：该ETS文件的名称。
    -   Path：该ETS文件构建产物的路径。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/l0EGTl3-TzK8e6V9zqMGlQ/zh-cn_image_0000002530912836.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=D04213E90816675CDD0A1851803E109518231D87EC0ABD1182CA5DC38A6FC804 "点击放大")
    
4.  切换到“TOP Redundant”页签，可查看冷启动过程中TOP 100冗余ETS加载文件信息。若File Name字段显示为蓝色，双击可快速跳转至对应工程源文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/7OZF10iHQKSNFFllVAfg0g/zh-cn_image_0000002561832751.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=1BA7BCD1C0BC2C66E9A507AD6C60FF34D86C37A42129C941E510ACED61870A4B "点击放大")
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/I3wTr9nlQumaSKPaHep8LQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=9D1F62F002DDEBDF47F6127C74ED3B61263A5A85EC7CB0185F13D70D40DFA261)

已上架应用市场的应用，不支持使用Load ETS Files或TOP Redundant页签查看冷启动过程中ETS文件的加载情况。

#### 分析静态资源库加载耗时

1.  展开“Launch”泳道，其中的“Static Initialization”子泳道展示启动过程中各静态资源库的加载耗时。
2.  单击单个静态资源库色块，或框选多个静态资源库，下方的“Details”区域展示所选对象的耗时统计信息。
    
    针对耗时超过预期的加载任务，可单击跳转按钮，跳转至相关线程打点任务中进行深度分析。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/MLB170UWS3Gggx_mTvpn8w/zh-cn_image_0000002530752842.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=F0B4009FFE2D7461F74C54D822E48853BD3F412CF5B3399419D429D35B183CF3 "点击放大")
    

#### 查看核心线程在CPU Core的运行情况

1.  展开“Launch”泳道，其中的“Running CPU Cores”子泳道展示启动过程中的关键线程具体运行在哪个CPU核心。
2.  单击单个进程色块，或框选多个进程，下方的“Details”区域展示所选对象的运行情况统计信息。
    
    单击对应CPU的跳转按钮，可进一步跳转到CPU Core泳道查看详细的调度信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/vW8A83B5TbuOhxgpQKzcZA/zh-cn_image_0000002530752828.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=5119B181C1C215FD188239EFB1C19413E9F50D5168591717EED314D697EFC4B0 "点击放大")
    

#### 查看启动过程相关的线程Trace数据

1.  展开“Launch”泳道，除“Static Initialization”、“Running CPU Cores”外，还包含启动过程的关键线程的状态和Trace数据。
2.  单击单个切片色块，或框选多个切片，可查看所选对象的详情。
    
    -   “Details”区域对所选对象进行树状统计，显示任务的名称、起始时间以及耗时信息。
    -   “Thread States”区域展示线程的状态统计信息。
    -   “Thread Usage”区域展示线程的使用情况。
    -   “Slice List”区域展示所选对象的切片统计信息。
    -   “Load Statistics”区域展示所选对象的中载重载信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/CsrwQV9gSMeS3saUiaWxxA/zh-cn_image_0000002561832755.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=43E834693DBD4DC9BA5A1CBEDF49156A7A0BF5EFBE5AFC8EF2809D66459A90F8 "点击放大")
