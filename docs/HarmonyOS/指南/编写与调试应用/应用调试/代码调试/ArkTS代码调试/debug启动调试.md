---
title: "debug启动调试"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debug"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "应用调试"
  - "代码调试"
  - "ArkTS代码调试"
  - "debug启动调试"
captured_at: "2026-04-17T01:36:49.289Z"
---

# debug启动调试

可以按照如下方式启动调试会话。

1.  如果需要设置断点调试，找到需要暂停的代码片段，点击该代码行的左侧边线，或将光标置于该行上并按Ctrl + F8（macOS为Command+F8）。如果无法添加断点，请查看FAQ[调试过程中无法添加断点](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-1)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/N8G-3-qgS4aOxaSdkew6OA/zh-cn_image_0000002530912932.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=2186C94EA5BF011547F68BDFBC7A4481F0871A633FEA1CF7D3A2FB0BD65B4627)
    
    设置断点后，调试能够在正确的断点处中断，并高亮显示该行。
    
2.  在设备选择框中，选择调试的设备。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/dK-by3pPSFOYuHL70jRalQ/zh-cn_image_0000002530752928.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=A0F02D0DC71B21F6B36A72BFC720CAF772856DB8F546BCC7380A35C9B1938B73)
    
3.  选择启动调试的配置，在模块选择框中选择需要调试的模块。也可以通过Edit Configurations[配置调试参数](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-run-debug-configurations)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/XjebEE7kSV2P9GmCvEY4KA/zh-cn_image_0000002530752940.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=D85340279165C32C0F1009F4D1C1D0ABC4F17A90DDDB8B0B0ED5E43AA461D678)
    
4.  在工具栏中，单击Debug![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/6gaRuxHtTNSloazPqPJ9mA/zh-cn_image_0000002530912928.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=9969E6EBD2E1CC1D6D9A90C2E79AD2473E82F93FA1BFB7EE062C12E4B6360750 "点击放大")。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/iktpzoiNQh-fvyQhGb5wjw/zh-cn_image_0000002561832861.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=938970D2A493A042A142BFE13425E861F170FB11BA2CC918405D83998A4066B6)
    
    或者在工具栏中Run中选择Debug。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/t2FeGt6TSG2WS8kXKgl-Ag/zh-cn_image_0000002561832855.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=00FF43AD6222EECC60C764D157854331669469B93305FDF11FA6B71CF1585C38)
    
5.  启动调试后，开发者可以通过[调试器](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-debugger)进行代码调试。
    
    如有断点会在断点处高亮，并展示当前断点处的Frames和Variables。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/7PSdJ-QvSRWlfdu51AFc-A/zh-cn_image_0000002530912926.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=F688F1AF94565450068F1FF6D74F08117774F28A74E2B2E20616A2CBEF3F31EF)
