---
title: "GPU帧捕获工具：Graphics Profiler抓帧入口"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-graphics-profiler"
menu_path:
  - "指南"
  - "优化应用性能"
  - "附录"
  - "GPU帧捕获工具：Graphics Profiler抓帧入口"
captured_at: "2026-04-17T01:36:52.043Z"
---

# GPU帧捕获工具：Graphics Profiler抓帧入口

Graphics Profiler（图形性能调优）是专为GPU分析和优化提供的一种调试分析解决方案，可帮助OpenGL ES游戏或Vulkan游戏提升性能，分析绘制和计算问题。从DevEco Studio 6.0.0 Beta1版本开始，提供Graphics Profiler工具的抓帧入口，该工具用于对HarmonyOS手机设备进行调试，需使用调试证书。

#### 操作步骤

1.  将需要分析的使用OpenGL ES或Vulkan API接口开发的应用推送到设备，并确认应用完成安装。
2.  在DevEco Studio顶部菜单栏中点击View > Tool Windows > Graphics Profiler进入帧捕获页面。
3.  在帧捕获页面，可配置Ref All Resources和Verify Buffer Access两个参数，配置完成后点击Launch APP拉起应用。
    
    -   Ref All Resources：默认关闭，在打开此选项后，抓帧时捕获所有活动资源，无论抓取的这一帧是否使用活动资源，都保存在Trace中。
    -   Verify Buffer Access：默认关闭，设置校验Buffer是否可以访问。
    
    此处为可选配置，不配置也可直接点击Launch APP拉起应用。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/eKziqhhSTTWH_VWh8MI5Bw/zh-cn_image_0000002561753539.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=6821D07E6040FB06607E3CE4AEC9EEE6D74AC1008EA55AF23A91C49D46F31529)
    
4.  在帧捕获界面拉起应用，成功建立连接后，Capture按钮点亮。设置抓帧数量，点击Capture按钮，等待帧捕获完成。
    
    -   Scope：不可修改，默认为Frame。
    -   Count：抓帧数量设置，范围为1-10帧。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/duUvJ2gMTduH5AxrcEoLUA/zh-cn_image_0000002530913596.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=47317DE16E85E540B5D00CDDBAAF931CC65D77175200617F9EB68D00FCADD6C4)
    
5.  当抓帧完成，在下方显示界面中选择一条捕获帧，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/3HJgdfj0RCaJm2BxBnGbhw/zh-cn_image_0000002530753608.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=0D2DC4E44446D67955B2D5ADBE7265AF4FA1E3BA6BECBF688DA196E382B49D2A)按钮，可自动打开Graphics Profiler工具解析捕获帧信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/Ky7_1u3RTS-khPf0X9X-SQ/zh-cn_image_0000002530913598.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=EC890030DF00FD6890B0965A1A3EE66616460F92143D1A21E156D5AA27A2DA6E "点击放大")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/Zk52F1shST2EygXFocCiPw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=A164AFB170B2B22BCCF0A5B633EE649612AE134509AA7E93C130389B6EA9CA24)
    
    -   抓帧文件名格式为：\[应用包名\] \_ \[抓帧时间\] \_frame \[帧号\].rdc。
    -   Graphics Profiler工具一次只能解析一个rdc文件。
    
6.  若首次使用，需根据界面提示下载Graphics Profiler执行工具，并在菜单栏**File > Settings**（macOS为**DevEco Studio > Preferences/Settings**） **> Tools > Graphics Profiler**中配置工具路径。默认路径为：工具安装路径/frame\_profiler/FrameProfiler.exe（macOS中为工具安装路径/Contents/macOS/FrameProfiler）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/EbmdDjrgQCix3VEOUNcZAg/zh-cn_image_0000002561753537.png?HW-CC-KV=V1&HW-CC-Date=20260417T013653Z&HW-CC-Expire=86400&HW-CC-Sign=2E3A261482A543832028284D21D446C5C2E7AD470FFAF3DC2B39E162384D781F)
