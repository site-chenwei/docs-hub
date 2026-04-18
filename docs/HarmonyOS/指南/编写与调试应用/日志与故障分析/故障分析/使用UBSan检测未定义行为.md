---
title: "使用UBSan检测未定义行为"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ubsan"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "日志与故障分析"
  - "故障分析"
  - "使用UBSan检测未定义行为"
captured_at: "2026-04-17T01:36:49.973Z"
---

# 使用UBSan检测未定义行为

代码中出现未定义行为，最初可能不会产生任何问题，但是随着代码的复杂度提高，未定义行为可能造成程序崩溃或发生错误，检测出根源会变得更加困难。UBSan（Undefined Behavior Sanitizer）可以检测代码中出现的未定义行为，帮助用户清除未定义行为引起的运行时错误。

常见的未定义行为有：

-   除数为零。
-   使用未对齐的指针，或未对齐的引用。
-   浮点数转换导致的溢出。
-   访问空指针。

该功能从DevEco Studio 5.1.0 Release版本开始支持。

#### 使用约束

ASan、TSan、UBSan、HWASan不能同时开启，只能开启其中一个。

#### 开启UBSan

可通过以下两种方式开启UBSan。

#### \[h2\]方式一

点击****Run > Edit Configurations >** Diagnostics**，勾选**Undefined Behavior Sanitizer**开启检测。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/x32Sup0ERG6pjGPLWh-few/zh-cn_image_0000002530753114.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=193DC0E4DB242743E2415ECCEF8E1532F4FA9A296ADABB7CCCFF759242EF3F2C)

#### \[h2\]方式二

在需要开启UBSan的模块中，通过添加构建参数开启UBSan检测插桩，在对应模块的模块级build-profile.json5中添加命令参数：

"arguments": "-DOHOS\_ENABLE\_UBSAN=ON"

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/IckDVvQAQu-l4gPOwJjS5Q/zh-cn_image_0000002530753110.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=BE385EC67747B53059752074A17C37F8CF618ED3FA5865224925FF48BF09A144)

#### 使用UBSan

1.  运行或调试当前应用。
2.  当检测出未定义行为时，弹出UBSan log信息，点击信息中的链接即可跳转到未定义行为的代码处。日志中的异常检测类型请参考[UBSan异常检测类型](https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-ubsan-detection#section124211321406)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/NPP3YLnTTZuvXsk_DCnFCg/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=E0CDB860C44D9DF2DBBFD821A434C065AB02FAEF3067EAD74EC7D706F2F6F133)
    
    无论[编译模式](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-guide#section192461528194916)是debug或release，均有链接可直接跳转至源码。
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/s1dD2PUrT7SRQIRBaY3UCQ/zh-cn_image_0000002561833031.png?HW-CC-KV=V1&HW-CC-Date=20260417T013651Z&HW-CC-Expire=86400&HW-CC-Sign=7111AABEE716047851B20B511D2938EA9C6FD85813DADBDCAA0F70F1F0FB27C9)
