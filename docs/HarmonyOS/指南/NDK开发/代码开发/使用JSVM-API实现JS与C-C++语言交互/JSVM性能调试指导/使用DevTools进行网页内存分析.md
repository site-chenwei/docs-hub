---
title: "使用DevTools进行网页内存分析"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-jsvm-about-analyze-memory-usage"
menu_path:
  - "指南"
  - "NDK开发"
  - "代码开发"
  - "使用JSVM-API实现JS与C/C++语言交互"
  - "JSVM性能调试指导"
  - "使用DevTools进行网页内存分析"
captured_at: "2026-04-17T01:36:41.758Z"
---

# 使用DevTools进行网页内存分析

#### 开启DevTools

DevTools为Chrome浏览器自带工具，[下载](https://www.google.com.hk/intl/en_uk/chrome/)并启动Chrome浏览器后，在需要进行内存分析的页面按下F12或者Shift+Ctrl+I启动DevTools开发者工具。

#### 获取js堆内存快照

在内存界面下选择堆快照，点击获取快照即可对当前页面进行一次内存快照。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/Hj_eYIePSCu2vAhFKeEKAg/zh-cn_image_0000002538020326.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=39E9B3CB74F1AEA416B8D14DC0718525722BE82D24C4AE0B2B111238E073593A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/Tn0DzvDuSHqKfYkXSwvuCA/zh-cn_image_0000002538180252.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=345FDEC3D912F425F740B9EEEE5E4A9B76414AF57AD4CE1713361093BD4CAFE6)

#### 堆快照分析

#### \[h2\]摘要(Summary)

摘要展示当前内存快照的概览。其中：

-   构造函数(Constructor):表示对象的构造器
-   距离(Distance):与GCroot的引用链距离。当出现同一类对象距离不同的情况，要注意代码逻辑可能出现问题。
-   对象计数(Object Count)：跟在构造器后方的灰色数字，表示当前构造器所构造的对象总数。
-   浅层大小(Shallow Size)：对象自身占用的内存大小。
-   保留大小(Retained Size)：当一个对象被释放后，系统虚拟机可以释放的总内存。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/rmq5KUwzRwm5zW9AXeG-jA/zh-cn_image_0000002569020039.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=3175E326FF2E59EC359E45FDC28F31D97D7143850A1845FECCE52A3E0055A2CE)

在摘要界面的右侧有一个选择栏，用户可以选择查看特定的对象，例如下图中选择“在快照2和快照3之间分配的对象”，这样生成的摘要可以用于定位内存问题发生的位置。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/o6HARLaKRGe3w8W7h2Rhrg/zh-cn_image_0000002568900031.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=C1DE99C0E2BA008D90F71BCFEC9E03ADE40E1F3693754B013613CF34BEC58558)

#### \[h2\]比较(Comparison)

在比较(Comparison)中可以将当前快照与另一个快照比较，跟踪对象属性和内存占用的变化。其中：

-   构造函数：对象的构造器。
-   新对象数(New)：该对象构造器下有多少新的对象被创建。
-   已销毁(Deleted)：该对象构造器下有多少新对象被销毁。
-   增量(Delta)：新对象与被删除对象的差值。
-   分配大小(Alloc Size)：两份快照间分配的内存大小。
-   已释放大小(Freed Size)：两份快照间释放的内存大小。
-   大小增量(Size Delta)：分配大小和已释放大小的差值。

可以根据比较界面不同快照间的差异分析内存问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/nUTiTNGZQeGJrCPYlBmZBA/zh-cn_image_0000002538020328.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=B2A52EE6F4E124ADC3D9F26110F71EB6E3DF53E803B4685F43D12494531C51A3)

#### \[h2\]控制(Containment)

控制(Containment)提供了一个自上而下的树形界面，该界面允许浏览和探索堆内存中的内容。我们可以用它来分析任意变量的引用情况。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/cBYl7IppRoWCeOXESXL-dw/zh-cn_image_0000002538180254.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=9AC8DC7D43EF02471259A429D3881928C005BF1CB413AE5B8E0C8DD090AA34FE)

#### \[h2\]统计信息(Statistics)

统计信息(Statistics)用一个饼图展示各个类型对象的内存占用比例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/IZsxUOToTKOFaH5bxLPavg/zh-cn_image_0000002569020041.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=9ED3AC0849AF79CAB39F1746BC856217D6568C3B00321FAC6A84B7DE43886D68)

#### 内存泄漏分析流程

1.  打开一个可能存在内存泄漏问题的页面并启用DevTools。下图展示的页面来自GitHub上的[memory-leak-simulation](https://github.com/Buchatech/JavaScript-Memory-Leak-Simulation)项目，该网页通过设置全局数组并不断向其推入'memory leak'字符串来模拟内存泄漏场景。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/PZmxcC4oRea7GCL3S3bpgQ/zh-cn_image_0000002568900035.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=6B8672E95C6A297E6D88999E5BDB9473F7F9DBDB8C4479E4AE70742A7407686F)
    
2.  在性能界面录制可能导致内存泄漏的用户操作，以识别引起内存泄漏的用户操作或组件。下图显示，网页已加载完毕，但内存仍在持续上升，表明可能存在内存泄漏问题。对于包含大量动态组件和频繁DOM操作的网页，内存曲线可能呈起伏状态。持续观察内存起伏的最低值变化，若最低值逐渐上升，怀疑网页存在内存泄漏问题。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/RlQ-QQghSNyjqQsOQbBHvg/zh-cn_image_0000002538020330.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=064DC895D1D3058417116BA362A280D3D11441A0A54A8468DDE55669BE7B3564)
    
3.  我们对这个网页进行第一次堆快照，发现Array占用了28M内存，基于该对象的内存占用显著高于正常值(通常在几MB范围内)，可以判断该对象可能存在内存泄漏问题。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/PpP2sLVqTuWR52BiyZlljA/zh-cn_image_0000002538180256.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=29123531C0359269BB074D11FA00080211CA068CB37750E0C48EFBCE08FF8F7B)
    
4.  对网页进行可能会造成内存泄漏的操作，操作完成后进行第二次堆快照，然后选择两个快照间分配的对象，观察到Array构造器新产生约16MB内存占用。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/oqqTk5bPRgS_8Pqklnw6bw/zh-cn_image_0000002569020043.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=B664335033B165E70453F52D7DDABF7D81DE640EDDFAB7B4DBC9AF7703208ADF)
    
5.  查看**比较(comparison)**，选择快照3并使用快照2作为比较对象，观察到Array构造器新产生了4030个对象，占用了16.1MB空间，但只释放了184B空间，根据此结果，确定内存泄漏发生在Array中。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/iqsU8kOcSiC4qJ1k97WP1g/zh-cn_image_0000002568900037.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=13053027A4224E0008F2D17341D575513C307BE43E6AB839B25118EF34C4A6EC)
    
6.  录制1-2分钟的堆快照来获得包含时间轴的摘要视图，这与性能界面中的视图类似。使用此视图可以分析是哪个动作造成了内存占用的变化。录制快照时选择“时间轴上的分配情况”选项，点击录制。完成想要测试的动作后，停止录制即可生成内存堆时间轴视图。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/hdXY6o8yRESA-w8vA1EXhw/zh-cn_image_0000002538020332.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=5DF8380C002CB1F0F33BEEC652CBD6BF1B06AFCBCD03A4C1439DD150E2870AF5)
    
7.  在结果的时间轴上，使用左键滑动选择想要查看的区域，即可查看选定时间段内的内存分配情况。从下图中框选部分可以看到，在选定时间内，Array构造器产生了两千个新对象。利用该功能，可以明确不同操作对内存的影响。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/UVMDaql6TiG3JkQGbnqIQA/zh-cn_image_0000002538180258.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=98A5B9E0E08D5ED7DADF4F64D839418D2007FAD46E198776A219D707C7D91FA5)
