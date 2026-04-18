---
title: "使用TSan检测线程错误"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-tsan"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "日志与故障分析"
  - "故障分析"
  - "使用TSan检测线程错误"
captured_at: "2026-04-17T01:36:49.940Z"
---

# 使用TSan检测线程错误

TSan（ThreadSanitizer）是一个检测数据竞争的工具。它包含一个编译器插桩模块和一个运行时库。TSan开启后，会使性能降低5到15倍，同时使内存占用率提高5到10倍。关于TSan的检测原理请参考[TSan](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-tsan-detection)。

#### 使用约束

-   ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。
-   TSan开启后会申请大量虚拟内存，其他申请大虚拟内存的功能（如gpu图形渲染）可能会受影响。
-   TSan不支持静态链接libc或libc++库。

#### 开启TSan

可通过以下两种方式开启TSan。

#### \[h2\]方式一

1.  点击**Run > Edit Configurations >** **Diagnostics**，勾选**Thread Sanitizer**。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/zP5QsS0zSCqGZ_062xl2cg/zh-cn_image_0000002530753432.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=871B2C2F4A1555FAA9CB6B41046196A77D4E7F826FBC099400177E0190296E20)
    
2.  如果有引用本地library，需在library模块的build-profile.json5文件中，配置arguments字段值为“-DOHOS\_ENABLE\_TSAN=ON”，表示以TSan模式编译so文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/dA4ozDwERTm1GXl9QVsXVw/zh-cn_image_0000002561833357.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=A7A915FE380FAC7A028C48A980FACB8ABDCB7F7819DF57AD0EC4F81A165B67B4)
    

#### \[h2\]方式二

1.  修改工程目录下AppScope/app.json5，添加TSan配置开关。
    
     "tsanEnabled": true
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/rs5RXnZ-S5m7Y6k4M846ng/zh-cn_image_0000002561753375.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=32C9C0C7FAFED0F4258E2F018EB69EA518FDAF022131BFF3799F31F200AA51F4)
    
2.  设置模块级构建TSan插桩。
    
    在需要开启TSan的模块中，通过添加构建参数开启TSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：
    
    "arguments": "-DOHOS\_ENABLE\_TSAN=ON"
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/iBWRZd4mQSmIe4mGQ9t9MQ/zh-cn_image_0000002561753371.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=AE532C74217F8088A1E75C8295115410374E67FEE82FB0F4D952B7E4FF336D9C)
    

#### 使用TSan

1.  运行或调试当前应用。
2.  当程序出现线程错误时，弹出TSan log信息，点击信息中的链接即可跳转至引起线程错误的代码处。日志中的异常检测类型请参考[TSan异常检测类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-tsan-detection#section1180812915516)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/Kh1KHY-5RQuaFfIDH1PkfQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=772B88DFD82F8B23E71450324755E324EB998D1EF9D7C62886F8E09156A45E86)
    
    当前使用call\_once接口会存在TSan误报的现象，开发者可以在调用该接口的函数前添加\_\_attribute\_\_((no\_sanitize("thread")))来屏蔽该问题。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/WZRZblfzThSskwjcLVsxEw/zh-cn_image_0000002530753434.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=E5D19E83D7277F87D06B0155D395A136F5244F1BB6360126D677A0E4EDB06402)
    
3.  如果是release应用，本地无工程代码，可以使用AnalyzeStackTrace功能，提供要解析堆栈的so，解析结果为源码地址。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/J6o3k5zwT4-QKVXlIBIbkQ/zh-cn_image_0000002530913430.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=D6DD61B6A9F60664C52A8ADE02F7CC92176D3412E52D539EDD4EFD53BB452E0B "点击放大")
