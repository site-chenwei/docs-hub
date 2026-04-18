---
title: "extension调试"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-extension"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "应用调试"
  - "代码调试"
  - "ArkTS代码调试"
  - "extension调试"
captured_at: "2026-04-17T01:36:49.264Z"
---

# extension调试

开发者可通过两种方式对[Extension Ability](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/extensionability-overview)生命周期函数进行调试。

-   应用安装到设备上后，通过等待调试方式进行调试。
-   修改运行调试配置项，指定当前运行或调试的Ability为Extension Ability。

#### 等待调试方式

1.  参考[等待调试](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach-to-process)对当前调试工程进行调试。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/_H26Pz4-QDSV-_sgHvmoXw/zh-cn_image_0000002530913458.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=78A62D58A1BBFD3634FD7C37047F0C133988496E9396E8A495C2E01DB8E596DB)
    
2.  在Extension Ability生命周期内设置断点。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/WUR4GZcBRCGNhNVT9QJk6A/zh-cn_image_0000002530913452.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=6EA616A76F7F2DD23CC81E87D23826B581057C4215E732E185E95E8ABD21FFAE)
    
3.  等待Extension Ability生命周期函数代码调用从而命中断点。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/iZKIwcUMQP6J-hB4k8ba0A/zh-cn_image_0000002561833381.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=7A1B1A7BF950AA8D6D4B873B6CD408A3AD9EAF490AA03252AC5DC097FF16C319)
    

#### 修改运行配置方式

1.  在运行调试窗口，运行配置项**Launch Options**选择**Specified Ability**。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/oGcAfBmqRa6bODvxG_UAag/zh-cn_image_0000002561833375.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=81B22210FD1C47DDE3C9D47171732435245C93843BF156EF8FE563DCAC26F0AF)
    
2.  选择需要进行调试的Extension Ability。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/GeR19v3pSsKu9t6GuQfi4g/zh-cn_image_0000002530913454.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=778EA0568AD8AC7382F783DC3C43DBB1CB6A565AB191722F8EDC522A71752480)
    
3.  点击**OK**保存配置后，点击调试按钮![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/kgChKH_GT9GRfqUjmnj80Q/zh-cn_image_0000002561833379.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=290E05A0FBFE038BFFA302403C048AB65FF98572061EBA5C0B6A8F530C3A9794)，启动调试即可命中 Extension Ability 中的生命周期函数断点。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/dE5h4iKIRXyqc6ESJQmUCQ/zh-cn_image_0000002530913448.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=01A7FAD5649EBC1EE7402D2D0E2C5F63FCF804CD703E084F53BD42A9E1912D79)
