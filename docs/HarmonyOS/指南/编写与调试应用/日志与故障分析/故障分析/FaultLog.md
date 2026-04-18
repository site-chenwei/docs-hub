---
title: "FaultLog"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-fault-log"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "日志与故障分析"
  - "故障分析"
  - "FaultLog"
captured_at: "2026-04-17T01:36:49.887Z"
---

# FaultLog

当应用运行发生错误导致应用进程终止时，应用将会抛出错误日志以通知应用崩溃的原因，开发者可通过查看错误日志分析应用崩溃的原因及引起崩溃的代码位置。

FaultLog由系统自动从设备进行收集，包括如下几类故障信息：

-   App Freeze
-   CPP Crash
-   JS Crash
-   System Freeze
-   [ASan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-asan)
-   [HWASan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hwasan)
-   [TSan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan)
-   [UBSan](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ubsan)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/tLS1qNKYRqaSjK3-Jit2uQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=3C5960975911378315DD619E9AF77B3F1B1AB303D795EDBD99DEF3EFF878575A)

调试模式（debug和attach）下，DevEco Studio会屏蔽当前工程的App Freeze和System Freeze等超时检测，避免调试过程出现超时检测影响开发者调试。

当前支持屏蔽的App Freeze故障类型：

-   THREAD\_BLOCK\_3S/THREAD\_BLOCK\_6S：应用主线程卡死检测，卡住3秒/6秒。
-   APP\_INPUT\_BLOCK：输入响应超时。

当前支持屏蔽的System Freeze故障类型：

-   LIFECYCLE\_TIMEOUT：app、ability生命周期切换超时。

#### 查看FaultLog日志

#### \[h2\]查看设备历史抛出的FaultLog日志

打开FaultLog窗口，将显示当前选中设备抛出的所有FaultLog日志。

FaultLog故障信息左侧按照**应用/元服务包名 > 故障类型 > 故障时间**结构组成，选中具体的故障日期，则会在右侧展示详细的故障信息，并对部分关键信息进行高亮展示，便于开发者进行故障定位。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/zowXvHypT6SxGC1ZLs1qLQ/zh-cn_image_0000002530913384.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=6F23EB1E9EA1BE63788B93BDC1965519921F6F4A98D1C586FDF197C0F60C10E4)

#### \[h2\]查看设备实时抛出的FaultLog日志

当设备抛出FaultLog日志时，DevEco Studio将会弹出消息提示框，开发者点击**Jump to Log**即可跳转至FaultLog窗口查看日志信息。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/Dik-RJ_aTu-gt_-RXPquxw/zh-cn_image_0000002561833305.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=B708DE2310C33D01D0AFDD9983BD47AF61A92825D92F675B3454944230F1F063)

#### \[h2\]跳转至引起错误的代码行

若抛出的FaultLog中的堆栈信息中的链接或偏移地址指向的是当前工程中的某行代码，该段信息将会被转换为超链接形式，点击后可跳转至对应代码行。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/86_7pAuWRk2ROfxAJVm1cw/zh-cn_image_0000002561833313.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=80DD05C37D338F8FF481D5517C6299308B0E17250228104E1A97CA0D686325DA)

#### 导出日志

开发者可将当前显示的日志信息保存到本地，以便后续的进一步分析。开发者可根据需要选择保存当前选中节点的日志或保存所有日志。

-   保存当前选中节点的日志：
    -   在当前选中节点右键点击**Export FaultLog**。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/IbCqAXu8TGm4KhsD6ikNOg/zh-cn_image_0000002561833285.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=8F3948F35EC76B21CFCF4B275A95225AF2B2369B2A8CB3E924380057BEE4CB50)
        
    -   点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/uUc6BcYAQtm_tJX2eLqwJQ/zh-cn_image_0000002561753315.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=3C90F9C99D6E257CE4AC137FC38242E36B40A4DEE954AD682430B9B02CCA2F3A)，弹出子选项后进一步点击**Export Selected FaultLog**。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/bFiCxmAxQmSRh5Npvn9lOA/zh-cn_image_0000002561753299.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=820D58BA3F9ADB5ED09E16A3132AEEA941E5A049B54B0009BEB04237ECE652D7)
        
-   保存所有日志：点击Export FaultLog按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/8Sod3B2CSuytrGMsCus2FA/zh-cn_image_0000002530753376.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=110CCA783564EA15858725856307508017FDC4EB830BC8C1925909D3CA4C842F)，弹出子选项后进一步点击**Export All FaultLog**。

#### 查看cppcrash结构化日志

从DevEco Studio 6.0.0 Beta1版本开始，支持对Cpp Crash类型的FaultLog，进行结构化展示和日志过滤。

1.  双击cppcrash日志，**Fault Info**右侧会出现**Fault Analysis**页签。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/6LT-vpiOTuiGXQbx3TXv4Q/zh-cn_image_0000002530913356.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=55A4D3A941D0C0A66DB964A43A087D6CD3B65D7F0C1FE8CC886A052D24EA0EC5)
    
2.  点击**Fault Analysis**页签，会展示结构化的日志信息。
    
    -   页面上方的字段对应了FaultLog中的字段，具体对应关系请查看[字段说明](#section1983219211210)。
    -   页面下方包含Stacks和Logs两个页签。
        -   **Stacks**：展示线程的堆栈信息，具体请参考[查看堆栈信息](#section459581010138)。
        -   **Logs**：展示FaultLog中的HiLog日志，具体请查看[查看HiLog日志](#section13361239195113)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/zqHnisPVSaCBWJ2Bhyw_sA/zh-cn_image_0000002530753372.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=2043EE18BD5C8EEAF8989E43D22527CC2034138C0FFA81F941C1E27F0131BEBF "点击放大")
    

#### \[h2\]字段说明

**Fault Analysis**页签中的字段和FaultLog的字段对应关系如下。

**表1**
| 
**Fault Analysis**的字段

 | 

说明

 |
| :-- | :-- |
| 

Occurrence time

 | 

FaultLog发生的时间，对应FaultLog中的Timestamp字段

 |
| 

Analysis time

 | 

触发日志结构化展示的时间，即双击日志文件的时间

 |
| 

Frontend

 | 

是否是前台应用，对应FaultLog中的Foreground字段

 |
| 

Bundle name

 | 

包名，对应FaultLog中的Module name字段

 |
| 

Device type

 | 

设备类型

 |
| 

App build number

 | 

应用构建号，对应FaultLog中的VersionCode字段

 |
| 

App version

 | 

应用版本，对应FaultLog中的Version字段

 |
| 

Device model

 | 

设备信息，对应FaultLog中的Device info字段

 |
| 

System version

 | 

系统镜像版本，对应FaultLog中的Build info字段

 |
| 

Abnormal signal

 | 

异常信号，对应FaultLog中的Reason字段

 |

#### \[h2\]查看堆栈信息

Stacks页面包含了FaultLog中的堆栈信息，并以线程为单元进行折叠，点击展开按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/9pa7O8aTRgqPIq1SaStZuQ/zh-cn_image_0000002530753398.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=0F0EDCB9514DF4C85E4F995BCC5AD4CF5D3324B7052DA7D343CB91B9104A0491)，可以展开对应线程。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/w_Y9egq0RcuQsoFfr8FolA/zh-cn_image_0000002561833275.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=0F970C9995E184D4850CC4C7E8EB6C6F4AE654C7AFB9C3863268B009B6262CA2 "点击放大")

图中标注1的勾选框是展开应用堆栈，标注2的勾选框是展开系统堆栈，两个勾选框一共组成了四种状态，具体如下表。

**表2**
| 
勾选框勾选状态

 | 

说明

 |
| :-- | :-- |
| 

1、2都不勾选

 | 

展示所有线程，线程处于折叠状态。

 |
| 

1、2都勾选

 | 

展示所有线程，线程处于展开状态。

 |
| 

只勾选1

 | 

只展示应用线程，线程处于展开状态。

 |
| 

只勾选2

 | 

只展示系统线程，线程处于展开状态。

 |

#### \[h2\]查看HiLog日志

Logs页面展示了FaultLog中的HiLog日志，支持日志级别的过滤和搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/W7zgDQbzQDm4RJJvqxi9tw/zh-cn_image_0000002561753301.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=324DBD0927375D4F6F3D30D37E1092F05202CA0A11037B11A26B4CDF11D7DA40 "点击放大")

#### 查看appfreeze结构化日志

从DevEco Studio 6.0.0 Beta2版本开始，支持对AppFreeze类型的FaultLog，进行结构化展示和日志过滤。

1.  双击appfreeze日志，**Fault Info**右侧会出现**Fault Analysis**页签。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/4ygMDArtQD6Vx9Lj_Gya0g/zh-cn_image_0000002561753321.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=D351C47D140E5F0D80EB2DEB6DD2415BA00CAA5FB8D88E9AABF9AAF378CE5B1A)
    
2.  点击**Fault Analysis**页签，会展示结构化的日志信息。
    
    -   页面上方的字段对应了FaultLog中的字段，具体对应关系请查看[字段说明](#section15864144624712)。
    -   页面下方包含Stacks、Logs、System、3s/6s Compare四个页签。
        -   **Stacks**：展示线程的堆栈信息，使用方式和cppcrash日志相同，具体请参考[查看堆栈信息](#section459581010138)。
        -   **Logs**：展示FaultLog中的HiLog日志，使用方式和cppcrash日志相同，具体请参考[查看HiLog日志](#section13361239195113)。
        -   **System**：从DevEco Studio 6.0.0 Beta3版本开始，新增System页签，用于在高负载场景下，展示设备CPU/内存的日志信息，具体请参考[查看高负载CPU/内存日志信息](#section179717814915)。
        -   **3s/6s Compare**：从DevEco Studio 6.0.2 Beta1版本开始，新增3s/6s Compare页签，用于对[THREAD\_BLOCK\_6S](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines#thread_block_6s-应用主线程卡死超时)类型的AppFreeze问题，展示3s和6s时间点的主线程堆栈日志，具体请参考[查看3s/6s堆栈日志](#section76467955514)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/C5hcWisISuigaR-pJCWtrw/zh-cn_image_0000002561753323.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=15FAE0F72737821CEFD7FCA83EC81FE5AD755C3E3ADF149FB209C1483ED27806)
    

#### \[h2\]字段说明

**Fault Analysis**页签中的字段和FaultLog的字段对应关系如下。

**表3**
| 
**Fault Analysis**的字段

 | 

说明

 |
| :-- | :-- |
| 

Occurrence time

 | 

FaultLog发生的时间，对应FaultLog中的Timestamp字段

 |
| 

Analysis time

 | 

触发日志结构化展示的时间，即双击日志文件的时间

 |
| 

Frontend

 | 

是否是前台应用，对应FaultLog中的Foreground字段

 |
| 

Bundle name

 | 

包名，对应FaultLog中的Module name字段

 |
| 

Device type

 | 

设备类型

 |
| 

App build number

 | 

应用构建号，对应FaultLog中的VersionCode字段

 |
| 

App version

 | 

应用版本，对应FaultLog中的Version字段

 |
| 

Device model

 | 

设备信息，对应FaultLog中的Device info字段

 |
| 

System version

 | 

系统镜像版本，对应FaultLog中的Build info字段

 |
| 

Freeze type

 | 

冻结类型，对应FaultLog中的Reason字段

 |

#### \[h2\]查看堆栈信息

Stacks页签用于查看appfreeze中的堆栈信息，使用方式和cppcrash日志相同，具体请参考[查看堆栈信息](#section459581010138)。

#### \[h2\]查看HiLog日志

Logs页签用于查看appfreeze中的HiLog，使用方式和cppcrash日志相同，具体请参考[查看HiLog日志](#section13361239195113)。

#### \[h2\]查看高负载CPU/内存日志信息

从DevEco Studio 6.0.0 Beta3版本开始，新增System页签，用于在高负载场景下，展示设备CPU/内存的日志信息，有助于分析高负载和appfreeze之间的关联关系。

如下是CPU的相关日志。

①：柱状图表示对应时间点的CPU使用情况（百分比）。

②：鼠标悬浮在柱状图上，会显示CPU总使用率、CPU使用率top5的进程号（Pid）和对应的CPU使用率。

③：选中柱状图后，显示相关的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/AE_QRCCoRcKtbmRSsfWZrA/zh-cn_image_0000002561833271.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=40FB61D3B47256AE3E3AC9B7AE1669B62D7998B7694B168E49B698FD9ECEDCE2 "点击放大")

如下是内存的相关日志。

①：柱状图表示对应时间点的内存使用情况（百分比）。

②：鼠标悬浮在柱状图上，会显示内存使用率、内存占用top5的进程和对应的内存大小。

③：选中柱状图后，显示相关的日志。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/wi_9gH2zQNuicFYCSOCtbw/zh-cn_image_0000002530913348.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=82D78ED9B6FF761F204A576E15CB1989C512EE5D1BFB982E89F2D4225A4B0B54 "点击放大")

#### \[h2\]查看3s/6s堆栈日志

从DevEco Studio 6.0.2 Beta1版本开始，新增3s/6s Compare页签，用于对[THREAD\_BLOCK\_6S](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appfreeze-guidelines#thread_block_6s-应用主线程卡死超时)类型的AppFreeze问题，展示3s和6s时间点的主线程堆栈日志，并标识栈帧中可能的故障处。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/REpmdO23TbSVlu_DFfkbEA/zh-cn_image_0000002561753295.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=5A89972E27A4A42AC22D848DA1747113FC23628E18E75F0E2F3EF169A11125F2)

如果不是THREAD\_BLOCK\_6S类型的AppFreeze问题，不会展示3s/6s Compare页签。

#### 查看应用终止日志

从DevEco Studio 6.0.2 Beta1版本开始，提供**AppKilled**窗口，用于查看设备上应用终止的相关信息，包括应用异常退出的时间、进程名、是否前台应用、异常退出原因，点击**recordId**可以查看详细的FaultLog信息。支持按设备、应用和异常原因对信息进行过滤。

AppKilled窗口中支持查看的异常退出原因请参考[reason字段说明](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hidumper#reason字段说明)，如需对问题进行排查处理，请参考[App Killed（应用终止）检测](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appkilled-guidelines)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/kyYsvp_0Ss-r5v52rFS9yw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=1869C674102B76A14CA014365E4BAB7D7E2222B6BAF659F588E1EB5D8DB12927)

2in1、Tablet设备不支持查看APP\_INPUT\_BLOCK和THREAD\_BLOCK\_6S类型的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/QFl51NSbRhmx9TZBHYyi6g/zh-cn_image_0000002561753307.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=8BF7CC7136F69BEDA8601DF83781234B91892C7EB40B80A8B740214CCB2AB80F)
