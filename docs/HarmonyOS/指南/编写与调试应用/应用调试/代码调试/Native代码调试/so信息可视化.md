---
title: "so信息可视化"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-native-so"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "应用调试"
  - "代码调试"
  - "Native代码调试"
  - "so信息可视化"
captured_at: "2026-04-17T01:36:49.462Z"
---

# so信息可视化

在native调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/MRBcHid4QZC81A5gH9u8Sg/zh-cn_image_0000002530753332.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=823C0F9D17FDD7E2829C70DF27AF95C0BA931F15535C2362427C4412DEC6FF8B)，勾选**Modules**，打开模块视图。

在native调试期间，**Modules**窗口会列出并显示有关应用使用的so信息。点击各属性可按升序/降序来排序，支持字符串匹配搜索。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/iy2YEN0jThiGpbp-YSEW2A/zh-cn_image_0000002561753269.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=4BDDA3DE0FD69A092F7BA5AC16A2052C413216F7EF89C3F3DD5D96698EEEC0B5)

-   加载符号表文件
    
    如果符号未加载，可右键点击模块，选择**Load Modules**，加载本地携带符号信息的so文件。加载成功后，Symbol Status列会显示"Symbols Loaded"。
    
    如需将符号恢复为初始状态，可右键点击模块，选择**Reset** **Modules**。
    
-   添加源码地址映射
    
    加载的符号表文件路径默认是编译时的路径，若与本地的源码文件路径不一致时，需要关联源码文件。右键点击模块，选择**Set Source Mapping**，选择本地源码文件路径，映射成功后，Source Root Path列会显示映射后的路径。
    
    如需恢复为默认路径，可右键点击模块，选择**Reset** **Source Mapping****s**。
