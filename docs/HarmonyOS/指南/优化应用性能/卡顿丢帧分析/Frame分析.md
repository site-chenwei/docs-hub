---
title: "Frame分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-frame"
menu_path:
  - "指南"
  - "优化应用性能"
  - "卡顿丢帧分析"
  - "Frame分析"
captured_at: "2026-04-17T01:36:51.748Z"
---

# Frame分析

开发应用或元服务过程中，如果发现有表单滑动不顺畅、页面交互延迟、动效不流畅等卡顿现象时，可以使用DevEco Profiler提供的Frame场景分析能力，录制卡顿过程中的关键数据进行分析，从而识别出导致卡顿丢帧的原因。此外，Frame任务窗口还集成了Time、CPU、Network场景分析任务的功能，方便开发者在分析丢帧数据时同步对比同一时段的其他资源占用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/6djxLRziRDCMW8SB_MWEOg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=4CC82391A1E7D4B8912A6C12267D89310AA8DB48BF1A32BE6E3F9E63B71D097D)

-   在任务分析窗口中，可通过[快捷键](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-shortcut-key)缩放时间轴、移动时间轴、添加时间标签等。
-   Frame分析支持离线符号解析能力，请参见[离线符号解析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-time#section186881175012)。
-   Frame分析支持Energy泳道，请参见[定位能耗问题](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-profiler-energy#section889733410010)。

#### 查看GPU使用情况

1.  创建Frame分析任务并录制相关数据，操作方法可参考[性能问题定位：深度录制](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/deep-recording)，或在会话区选择**Open File**，导入历史数据。
2.  “Frame”泳道显示当前设备的GPU的使用率，将其展开，子泳道显示Render Service侧帧数据和App侧帧数据。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/gA9PLWgfSEK1hptVi3PGwg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=400F7179037A1C231652F0515BB4535715CD66CC4B4546ACD96C54560F7E0903)
    
    -   一帧的绘制，一般需要由App侧提交渲染到Render Service侧，然后Render Service侧再提交给硬件进行合成渲染，因此App侧的帧和Render Service侧的帧存在关联的情况。并且可能多个APP侧的帧/同一APP侧的多个帧提交到同一个Render Service侧帧上，出现帧之间的一对多的关联情况。
    -   一帧绘制的期望耗时，与fps的大小有关，一般情况下fps为60，对应的Vsync周期为16.6ms，即App侧/Render Service侧的帧耗时，一般需要在16.6ms以内。App侧帧/Render Service侧帧判断卡顿的标准为帧的实际结束时间晚于帧的期望结束时间。
    -   在“RS Frame”和“App Frame”标签的泳道中，正常完成渲染的帧显示为绿色，出现卡顿的帧显示为红色。
    -   除“RS Frame”和“App Frame”泳道外的“ArkTS Callstack”、“Callstack”、“CPU Core”等泳道信息，请参考[基础耗时：Time分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-time)、[CPU活动分析](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-insight-session-cpu)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/TdDTwWSASF6KRIT8RYE3DQ/zh-cn_image_0000002530752902.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=DDF4E3790C6BE1C4AE1C3CB6FC760E6905E58E88829C84B3EE21FD24FAF030D2 "点击放大")
    

#### 查看指定时间段内所有进程的Frame数据统计信息

1.  在时间轴上拖拽鼠标选定要查看的时间段。
2.  框选Frame主泳道。
    
    窗口下方的“Statistics”区域中会以进程维度对选定时间段内的Frame信息进行统计，包括卡顿率、卡顿次数、最大连续卡顿次数、最大卡顿耗时、平均卡顿耗时以及平均正常耗时等。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/0qYfgMqbQ7KN8SxbxsyLJg/zh-cn_image_0000002561832811.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=73068AA78213E08790B523E386EA10829B9439042719F8AA77BA5523C1838EED "点击放大")
    
3.  点击“Statistics”列表中任一进程的跳转按钮，在“Frame List”区域将展现该进程对应的Frame列表。体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/BWyVjxScTXCR5BM55yj-Pg/zh-cn_image_0000002561752841.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=B1F3BB2CA681489FB3F37DD4199CB8567B124B4EC8FBD98D6C41DE4EE34E49A9 "点击放大")
    
4.  单击“Frame List”列表中任意一帧，右侧的“More”区域会中显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/RSfd4pStRku8wDA54XJMAg/zh-cn_image_0000002530912912.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=24164547355250E8A1602A4A09F5D83B3ACD5B32E234C9CBFF8AC2708B22D09E "点击放大")跳转至关联的切片。

#### 查看指定Frame页面布局信息

从DevEco Studio 5.1.0 Release版本开始，支持查看最新录制的Session中指定的Frame页面布局信息。

从DevEco Studio 6.1.0 Beta1版本开始，![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/V6Q_m4iYQoqHgYklKSlKtQ/zh-cn_image_0000002530912910.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=D016CD18CF411B0F3007FF95E081681E288F7706997D8A2C6E1815A7C0E2E331 "点击放大")按钮中新增Frame Layout开关，开发者可自行设置开关状态。开关关闭时，不支持查看最新录制的Session中指定的Frame页面布局信息，默认关闭。

暂不支持在Wearable设备上查看指定Frame页面布局信息。

1.  单击RS Frame泳道或APP Frame泳道中任意一帧，“Details”区域中会展示该帧具体信息。点击**Open Layout**按钮，将在ArkUI Inspector中直接打开相应arkli文件；点击**Download Layout**将arkli文件下载到指定目录，之后可手动导入[ArkUI Inspector](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector)查看页面布局信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/2kyZ4fRiRd29PskAv5AZvg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=50509301B95F8C21BECAEAB356364CD3FCB6D549C5A36A978C695FFB423C209C)
    
    单击“Download Layout”或 “Open Layout”前，需应用进程置于前台，才能正确回放全量渲染数据，获取arkli文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/X1ej7LjwSn-gWk7L8G8XDQ/zh-cn_image_0000002530912882.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=F3F4FFDD75AF85E2E407872853DC1A1E8B8CB7B837F03438F9E627EB38204974 "点击放大")
    
2.  在ArkUI Inspector中可查看组件树和组件属性信息，当前支持BackgroundFilter、nodeGroup、nodeGroupReuseCache组件。
    
    -   BackgroundFilter：背景滤波器。
    -   nodeGroup：节点组类型，0表示非节点组节点，1表示被动画标记的节点组，2表示被UI标记的节点组，4表示被用户标记的节点组，8表示被前景滤波器标记的节点组。
    -   nodeGroupReuseCache： 0表示在生成缓存或无需缓存，1表示在重用缓存。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/904sHH0kQ6CA_svSFVzXDA/zh-cn_image_0000002530752900.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=63A94A54BB8D3ACA00937A3B73F8E122B05B4BEEBFD4F6EDED010296F6FE79B9 "点击放大")
    

#### 查看指定时间段内指定进程的Frame数据统计信息

1.  在时间轴上拖拽鼠标选定要查看的时间段。
2.  选择要观察的子泳道（例如带“RS Frame”标签的泳道）。
    
    窗口下方的“Details”区域中会显示选定时间段内的RS帧统计信息列表，体现各帧的起始时间、总耗时、GPU耗时以及卡顿丢帧类型。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/audOYa32Re6iggpmSVVZtg/zh-cn_image_0000002561832831.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=01347A2416885EBC1116A8D707E08EB23ABA47D737E7FE7DBEC5444B7EC7C3FC "点击放大")
    
3.  单击列表中任意一帧，右侧的“More”区域会中显示该帧更多关键信息。在获取该帧的预期起始时间、预期持续时间之外，您可以单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/8g-GelLmTa-seJcVIq5UPw/zh-cn_image_0000002561752835.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=8FEBCBA9AB1EFA654AEB28C927F8D55AE8767E1440FEE000477E390CF7CC0AC1 "点击放大")跳转至关联的切片。

#### 查看指定Frame信息

在子泳道（例如带“APP Frame”标签的泳道）中选中要查看的Frame，该泳道上方是耗时最长的非UI函数，下方是UI主线程泳道。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/ZFPiYF96ROmelrHTEcja0g/zh-cn_image_0000002561752857.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=DB9EE2D3B5D4FF579E644B821DECB333D30BEFC843C45D46E6C7FFAF3A32419D "点击放大")

窗口下方的“Frame”区域中会显示选定帧的关键信息，如VSync编号、开始时间、App应用侧持续时间、App应用侧业务逻辑耗时、Render Service侧持续时间、GPU持续时间、总持续时间、卡顿丢帧类型以及可能出现卡顿的原因等。“Non UI”区域中会显示非UI耗时最大的函数，如开始时间、结束时间、持续时间，函数名等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/pTDo3fc1SkmsNW2rt_VxEQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=D2D99F6EB4A739BEB1A29EBD21BB5F34E07E89712BB49D0A7E0B0EA3E93D9951)

-   在选定观察对象后，DevEco Profiler会自动关联与其相关的切片，用箭头连接。
-   如果该帧是由于超出期望结束时间引起的，则显示两条线，对应期望开始时间（Expected Start）和期望结束时间（Expected End），用于关联分析同一时刻Trace或者函数采样信息。
-   将鼠标悬浮在任意帧上，会冒泡显示该帧的Jank信息。
-   卡顿丢帧类型（Jank Type）：No Jank（不卡顿）、AppDeadlineMissed（App侧的卡顿）、RenderDeadlineMissed（Render Service侧的卡顿）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Cxud8HUNQiyqxLpnGhiU5A/zh-cn_image_0000002561752829.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=96D7E7BB67D3FCE0AE671477A1D21D1F318FB9B7B21E82F73A9D4676010F6620 "点击放大")

#### 查看屏幕帧率动态变化场景下丢帧和卡顿信息

Frame泳道下新增Lost Frames和Hitch Time两类子泳道，用于识别和优化卡顿和丢帧现象。

-   Hitch Time：展示当前时间段内卡顿时长。计算方式为渲染前后两帧的间隔减去单帧耗时，若计算结果大于单帧耗时\*70%，则视为出现卡顿现象。
-   Lost Frames：展示当前时间段内丢帧数。Lost Frames计算出的结果，六舍七入统计取整。

1.  创建Frame模板并录制会话，如存在卡顿和丢帧现象，会在Lost Frames和Hitch Time泳道对应时间显示矩形图。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/IiRoK3BpTwu5iTabMAEWsQ/zh-cn_image_0000002561752821.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=17295B1DC7578A14154CC90639DFDFA8E76351181E2D9237CF7C83826C812659 "点击放大")
    
2.  鼠标点选某一时间点，提示信息会显示该点所属时间段内的丢帧数以及卡顿时间。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/rQV2yvX0TuiyfnNKHiFFDA/zh-cn_image_0000002561832845.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=7744C0D74954C3B1C683D5673F70E0C87B4CF2938BAC49BD0255DA71AF445CBF "点击放大")
    

#### 支持动效场景调优

开发者在开发应用时，会使用到动效，动效的卡顿影响到用户的使用体验。DevEco Profiler提供动效场景的调优，能帮助开发者优化动效场景。

鼠标放置在某个动效上，显示该动效的详细信息，包括响应时延、动效持续时间、完成时延、期望帧率、FPS。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/PG-UNKQ1TFu8-9Si9pZRaA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=0FD48DF100035E1C04F934C36248684B72B896F2A7D8557DA36602E74EC6D5A9)

-   响应时延：<=85ms 绿色，85ms~150ms 浅绿色，150ms ~250ms 浅红色，>250ms深红色。
-   期望帧率：当前系统运行满帧帧率，如60HZ、90HZ、120HZ。智能刷新率模式下，不展示期望帧率。
-   动效持续时间：根据帧率展示颜色，FPS大于达标帧率即为绿色，小于则为深红色。智能刷新率模式下，帧率可变，颜色为灰色。达标帧率与期望帧率的大小有关，一般情况下期望帧率为60HZ，则达标帧率= 60HZ \* 91.7%。
-   完成时延：响应时延和动效持续时间只要有一个为深红色，完成时延为深红色。
-   Launch模板中Frame泳道点击detail区启动动效详情信息，more区域展示动效帧Animation Data List信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/PNlB1VN8SUePvvfqdNmXfQ/zh-cn_image_0000002530912924.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=6740EA4E9E425AB41394F193995B79AAF84A9D2B9B15774AEF0C9041DEE1FB8D "点击放大")

#### 查看组件动画信息

从DevEco Studio 6.0.0.828版本开始，Frame泳道下新增Component Animation子泳道，用于从组件的角度展示应用中包含的各种动画类型，包括属性动画 (animation)、显式动画 (animateTo)、关键帧动画 (keyframeAnimateTo)以及页面间转场 (pageTransition)。

在Details页签中，可以查看每个动画的详细信息，包括起止时间、帧率、动画曲线类型以及影响的组件属性等。

单击列表中任意一动画，右侧的“More”区域会中显示该动画所影响的组件属性的具体变化过程。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/4OyR1WjCQlOEkmplreSWSQ/zh-cn_image_0000002561832843.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=4F88D7090A2F220F21DBE1CBF466234EE1B5684D65E6B0BA8AC966FC926DF9B2 "点击放大")

#### 查看组件帧率信息

Frame泳道下新增两类子泳道，分别为Display Vsync与DisplaySync\_cb(tid)，用于对可变帧率的检测调优。

-   Display Vsync：该泳道显示对应时间段的屏幕刷新率，支持对框选的时间段内的vsync进行分布统计。区分“<=30HZ”、“30~60HZ”、“60~90HZ”、“>90HZ”。统计值包括框选时间段内各区间的分布比率、最小/最大/平均时长以及平均HZ。如果某场景满足了帧率改变的要求，当底层系统根据机制进行变帧，相应的情况会展现在对应的泳道，帮助开发者了解vsync的变化情况是否符合预期。该泳道仅支持在配备硬件屏幕的设备上进行数据采集。
-   DisplaySync\_cb(tid)：该泳道显示对应组件的帧率，如DisplaySync、XComponent两类接口组件动画对应的帧率。调测时，不同场景下由于帧率可变，系统实际表现是否符合预期，需要有实际的检测手段。尤其是由于DisplaySync的渲染均在UI主线程执行，当存在多个需要渲染的组件需要同时执行时，只能在UI主线程排队，此时任何一个组件的延迟都会对其他组件的渲染产生影响，导致UI卡顿。
    
    如下图所示，vsync2和vsync4中，vsync周期内的组件由于渲染耗时长，导致以下两个vsync周期挤掉下一个vsync周期的渲染时间，导致掉帧的情况产生。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/stwMIhJqSkGE9hUGrI9mHg/zh-cn_image_0000002561832795.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=60B895744E875FC35CE0F9C1DECD775FFFFB62D423CEFB623752B5206800843D "点击放大")
    

1.  选择Display Vsync泳道，在时间轴上拖拽鼠标选定要查看的时间段。
2.  详情区显示当前时间段的屏幕刷新率，当前帧最大持续时间、最小持续时间、平均持续时间以及该时间段内平均帧数。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/DPcf-_LMRimvAngq9bZ2LQ/zh-cn_image_0000002561752849.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=DA32C1AE6B457343BA891AAA8E78F745B8033E10310B213409ABE4170505B4E2 "点击放大")
    
3.  点选Display Vsync泳道，可以查看当前帧的耗时和帧率。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/wR8JWwMaQjq-JT0kuY2X0Q/zh-cn_image_0000002561832803.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=362FEEDDDD9C93BD05C702C633D60AC172479CE6D15C10B310ED3F37D1168FAE "点击放大")
    
4.  框选DisplaySync\_cb泳道，可以查看应用侧对应组件的帧率，渲染时间等信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/I6HjzTCkRh-6HJJQ7UMnLA/zh-cn_image_0000002530912902.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=37A64EC9C6DE9BA81CEEFEA17C89DACC91668DD10AAA4C4FF42C92002E12F0DA "点击放大")
    
5.  同时如果组件有可能的掉帧情况，DisplaySync\_cb泳道显示对应的掉帧情况并标红展示。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/fRqCn0V3QTK6hxfw6rzZuw/zh-cn_image_0000002561752871.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=2FB9E9904A5CB1C844F94ECB24226E2CAEF215F55F6CC259729D88D8724B3E60 "点击放大")
    

#### 查看帧率统计信息

Frame泳道中的App Frame泳道和RS Frame泳道在框选时新增fps标记。RS泳道新增过滤按钮，用于过滤ArkWeb数据。

1.  展开Frame泳道，框选一段数据。
2.  泳道出现fps标记，展示当前框选范围内的帧率统计信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/-7fsH1z0STyjOnpZabMUBw/zh-cn_image_0000002530752908.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=9CFB7BC3244F23B55A69E9FB095B15ABDF1F7167BF7E34981C13D9ADD696F6F0 "点击放大")
    
3.  打开Only ArkWeb data开关，筛选过滤出包含ArkWeb帧的数据。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/y6git49aSXyhiNcnieZguw/zh-cn_image_0000002530752888.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=F7553079E3D763D9471D251B218DAE2B17EC211C652B2E580DC294F95144E204 "点击放大")
    

#### Anomaly泳道：查看解码过度耗时和超过阈值的序列化、反序列化操作

如果工程中存在图片资源，并感知到解码绘制/渲染过程存在卡顿，可以通过Anomaly泳道查看主线程解码过程中是否存在解码过度耗时告警，并确认发生告警的时段。

如果应用中使用了worker, Taskpool工作线程等场景，通常会触发跨线程对象传递，并触发序列化和反序列化的操作。对于耗时超过阈值的序列化、反序列化操作，Anomaly也会给出对应的耗时告警，并给出发送这个操作的开始时间和耗时时间。

1.  在时间轴上拖拽鼠标选定出现告警的时间段。当耗时超过VSync周期的50%时，将在Anomaly泳道中出现红色告警，提示“Image decoding has exceeded 50% of the VSync time”。
2.  详情区给出录制时段内解码过度耗时的统计情况，包括类型，图片名，计数，总耗时，最小耗时、平均耗时、最大耗时，耗时标准差、 图源尺寸大小，目标尺寸大小等。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/9Hkb-d4DTbKTTpD60SVMJA/zh-cn_image_0000002561832799.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=F69C9975778DD1062127F240D3C54785481D508B1120A992F9E19B8BD624684B "点击放大")
    
3.  对于耗时超过阈值的序列化、反序列化操作，Anomaly也会给出对应的耗时告警。其中可以通过泳道启动配置按钮配置检测阈值，默认配置阈值为8ms。
4.  详情区给出录制时段内序列化、反序列化耗时情况统计信息，包括类型、计数、总耗时、最小耗时、平均耗时、最大耗时、耗时标准差等。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/NSTObBG8QU-3HHd-I1YgxA/zh-cn_image_0000002530912896.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=8A8D3FBD126BF4710B3A4BC9322C699443C70D48A960D86440887A2ABEAF6650 "点击放大")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/jzEChGUoSC-hAQor6QbwIQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=21D13E79CAE227B3D3E0823A4874C78792976719C6583C812B3247284531CC1A)
    
    已上架应用市场的应用不支持录制Anomaly泳道。
    

#### User Events泳道：查看用户事件耗时

开发者在卡顿丢帧场景可通过User Event用户事件，查看用户事件开始时间、应用开始处理时间以及应用处理耗时等情况。

1.  选择User Event泳道，在时间轴上拖拽鼠标选定要查看的时间段。
2.  详情区列表给出录制时间段内用户事件详情，包括用户事件ID、事件开始时间Input Time、应用开始处理时间Processing Start、应用处理耗时Duration和事件类型User Event Type。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/Oy4wi6fgRIqqngkGO8pZtA/zh-cn_image_0000002561752833.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=B9C0ACCAA831B3FF0F9CD104227A8AA2DB2D4B697F8D743D0FBF847B892B3776 "点击放大")
    
3.  点选User Event泳道中的条块，Slice详情区展示该事件的详情信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/rDgpv-RDRNawYlY8fjDPJg/zh-cn_image_0000002561832853.png?HW-CC-KV=V1&HW-CC-Date=20260417T013652Z&HW-CC-Expire=86400&HW-CC-Sign=B7120B1742BC207B453FAEDD8CAF52366B9339CBF6AD4AFE312959D3725CC6F9 "点击放大")
    

更多性能调优最佳实践，请参考[点击响应时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-click-response-optimization)、[点击完成时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-click-to-complete-delay-analysis)、[帧率问题分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-zhenlv)、[Web点击响应时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-click-response-delay-analysis)、[Web加载完成时延分析](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-completion-delay-analysis)。
