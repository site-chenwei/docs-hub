---
title: "attach启动调试"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-debug-arkts-attach"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "应用调试"
  - "代码调试"
  - "ArkTS代码调试"
  - "attach启动调试"
captured_at: "2026-04-17T01:36:49.239Z"
---

# attach启动调试

开发者也可以通过将调试程序attach到已运行的应用进行调试。

Attach Debugger和Debug的区别在于，Attach Debugger to Process可以先运行应用/元服务，然后再启动调试，或者直接启动设备上已安装的应用/元服务进行调试；而Debug是直接运行应用/元服务后立即启动调试。

#### 前提条件

当前设备上被attach的应用代码和本地代码一致，且已提前进行构建生成必要的sourceMap文件。

#### 使用约束

attach不支持的场景：

-   本地无源码。
-   bundleName不匹配，将出现提示“The selected process does not match the bundlename of the current project!”，但不阻塞调试过程。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/E7Qiz6_oTy24J6-vsE1dRA/zh-cn_image_0000002561753631.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=0DC99FE2F3882D07814DE09160B29A284911A9F7C56C36B5D3E67B38FDBCAFCA)
    

#### 操作步骤

1.  在工具栏中，选择调试的设备，并单击**Attach Debugger to Process**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/vvEqD94LQE-SWrlmUGPaow/zh-cn_image_0000002561833599.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=1B1D3ED69808E5B4C8CCC19F3D6DE4433BE0F0D22D1871B98679AA0C2EAA9A62)启动调试。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/usRyPOk4SeaKxbtY4FvA9w/zh-cn_image_0000002561833609.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=4BCB5E8FC284558827FC96AF8436F4A04D8455CC372ED90644B812F90BC72FC1)
    
2.  选择要调试的应用进程，若应用bundleName与当前工程不一致，则需勾选Show all process。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/PSMSW_TCQ2OPUScwIt3nDQ/zh-cn_image_0000002561753623.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=960DB2AB19EE7110EC80A3A7EDDA134D4AEE804D229FE9CF718449CD873FB7F9)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/hvvp1guzSset_EWex5iLXA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=DA6CCE68CA16F0D7FDEBF96DF13EBC21FF5C69F99954571D61BBC7125E547F4F)
    
    正常情况下，attach调试仅支持debug签名的应用，从DevEco Studio 6.0.2 Beta1版本开始，PC/2in1上的应用，如果使用了release签名并且配置了ohos.permission.kernel.ALLOW\_DEBUG权限，也支持被attach调试。
    
3.  选择需要使用的调试配置，或者使用默认配置。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/W4HmmkrUQWmaRZ66Wz9aUw/zh-cn_image_0000002530913674.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=2C86CB7DEB6EA73FA7BF483535690392936951AE25BA96DE3C4707A11EDFC6FA)
    
4.  选择需要调试的Debug type，若选择已创建的Run/Debug configuration进行attach调试，此时Debug type不可改变，只可在Run/Debug configuration界面修改。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/0z3QAn_UTaarloie3ZJ1Pw/zh-cn_image_0000002530753682.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=94E80D29F1888339E39BC24BB5C32560D67A9B81093C400B4393749FF0BF060C)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/tK7YV4NUTHSrjRYZfjM6XA/zh-cn_image_0000002530753688.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=A349B3E86099461D1C307EDC760803C0AFE1529DAE0A5401A7EF162F34C7E1AD)
    
5.  点击**OK**开始attach调试。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/e3wVbNLpTzWtdoMKJk2Tpg/zh-cn_image_0000002561753627.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=17FF5FCB6011FECD148A923DB78DDCE5B9FD831B337B7364FF3F4F2E98C9B6BB)
