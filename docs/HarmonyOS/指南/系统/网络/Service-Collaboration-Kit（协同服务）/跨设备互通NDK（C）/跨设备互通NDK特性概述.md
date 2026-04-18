---
title: "跨设备互通NDK特性概述"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/servicecollaboration-servicendk-description"
menu_path:
  - "指南"
  - "系统"
  - "网络"
  - "Service Collaboration Kit（协同服务）"
  - "跨设备互通NDK（C）"
  - "跨设备互通NDK特性概述"
captured_at: "2026-04-17T01:35:54.553Z"
---

# 跨设备互通NDK特性概述

跨设备互通提供相机、扫描以及图库（图片和视频）的跨设备调用能力，TV、平板或2in1设备可以调用手机的相机、扫描、图库等功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/qnxjgt2LSXS0B5RRtq2Nyw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=BEB307B6330007EA2ECC32A27BC9B24635E2A657F15D0FE067653FB7DE7D4A1D)

本章节以拍照为例展开介绍，扫描、图库功能的使用与拍照类似。

用户在TV、平板或2in1设备上使用富文本类编辑应用（如：备忘录、邮件、笔记等）时，想要拍摄一些照片作为素材，但是当前设备拍摄不太方便。通过跨设备互通-拍照，用户可以在当前设备的应用中指定平板或手机设备，并打开平板或手机的相机来拍摄所需的素材。通过手机或者平板设备拍摄，移动更便利、取景更灵巧、相机能力也更强大。拍摄的照片将实现快速回传到TV、平板或2in1设备的应用中，帮助用户高效完成图文并茂的文档设计。

如果同一组网下有多台手机或平板设备，用户可以选择不同的设备进行拍摄。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/vYfL3mglS6W55ocS-OVdWQ/zh-cn_image_0000002568899077.gif?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=B30927066840D36455B29EF923EF393B830CA7264002C9231F452706DA059D6E)

#### 运作机制

基于分布式协同框架面向跨设备拍照的业务场景，为您提供了 [HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_getcollaborationdeviceinfos)（设备列表接口）、[HMS\_ServiceCollaboration\_StartCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_startcollaboration)（跨端拍照、扫描、拉起图库选择图片）或[HMS\_ServiceCollaboration\_StartCollaborationV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_startcollaborationv2)（跨端拍照、扫描、拉起图库选择图片和视频）和 [HMS\_ServiceCollaboration\_StopCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_stopcollaboration)（终止跨设备互通）四个接口。只需要调用这四个接口，即可完成跨设备互通，无需关注分布式场景下数据传输、指令控制等具体细节。

1.  **系统分布式协同框架跨设备自动建链**
    
    a. 通过系统的分布式协同框架，同账号下的本端设备（2in1设备/平板）与远端设备（手机/平板）自动建立连接。系统将自动完成设备的发现、连接、认证等流程，通过[HMS\_ServiceCollaboration\_GetCollaborationDeviceInfos](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_getcollaborationdeviceinfos)接口提供可用的具有相机、扫描和图库能力的远端设备信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/3sA87CfkQaC1gjtYp-LAhQ/zh-cn_image_0000002538019378.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=CFE928EE18CD7F9A76F1C6E1A579BA49A06FEF1419C007271E3C6CAE29490DC4)
    
    b. 通过[HMS\_ServiceCollaboration\_StartCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_startcollaboration)或者[HMS\_ServiceCollaboration\_StartCollaborationV2](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_startcollaborationv2)拉起对应跨设备互通能力，通过[HMS\_ServiceCollaboration\_StopCollaboration](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#hms_servicecollaboration_stopcollaboration)终止跨设备互通能力。分布式协同框架会将远端拍摄状态信息实时回传到应用侧，应用侧会根据错误码做相关提示。
    
    拍摄状态可能为：对端设备拍摄中、图片导入中、协同失败、本端WLAN未开启、双端WLAN或者蓝牙未开启。具体拍摄状态提示可由应用选择绘制，对应提示信息参考[ServiceCollaborationEventCode](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/servicecollaboration-capi-module#servicecollaborationeventcode-1)。
    
    | 对端设备拍摄中 | 图片导入中 | 协同失败 | 本端WLAN未开启 | 双端WLAN或者蓝牙未开启 |
    | :-- | :-- | :-- | :-- | :-- |
    | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/HYhbHHRXRt-47sOa3G0zLQ/zh-cn_image_0000002538179308.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=FB0E22646CC5BCD0CA6A28AC04CF7E60CD17E823C2EC0D9F7A1C773FE40B4C5B) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/e4v4kDbxRMSb93QLpBh2-Q/zh-cn_image_0000002569019095.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=F03737FDA6D8BC03F7BC789496D0192C13E6A32750E5017FBF65C535F5680420) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/J-j5NqQ7SpKJL4fcdN7DXw/zh-cn_image_0000002568899087.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=64054CEE576D122CCF8B127C6A359D0BA9FD54842AE14B48CF6686B80A992A43) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/IuOmcN0yR2ukrzBs0Pvl1g/zh-cn_image_0000002538019382.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=A304624A4700C613FEAE13B83543FDDA7FD4C1C95A943DA6D65534AADF2D93F4) | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/bTTGdXlqRuma_E7WIDXkGw/zh-cn_image_0000002538179312.png?HW-CC-KV=V1&HW-CC-Date=20260417T013556Z&HW-CC-Expire=86400&HW-CC-Sign=3D8DE087DA19119E69896BAEDC47F3D2C9C6A27BB81E9A83C99AEA2B750AD5F9) |
    
2.  **用户使用远端设备拍照**
    
    1.  用户使用远端设备完成拍照并确认，照片将回传到本端设备的应用，完成整个流程。
    2.  远端设备将自动退出相机界面，回到初始状态。
