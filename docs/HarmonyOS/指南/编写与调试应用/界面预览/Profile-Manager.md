---
title: "Profile Manager"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-profile-manager"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "界面预览"
  - "Profile Manager"
captured_at: "2026-04-17T01:36:48.720Z"
---

# Profile Manager

由于真机设备型号众多，不同设备型号的屏幕分辨率可能各不相同。因此，在HarmonyOS应用/元服务开发过程中，为了适配多种设备型号，可能需要查看不同设备上的界面显示效果。对此，DevEco Studio的预览器提供了Profile Manager功能，支持开发者自定义预览设备Profile（包含分辨率和语言），从而可以通过定义不同的预览设备Profile，查看HarmonyOS应用/元服务在不同设备上的预览显示效果。当前支持自定义设备分辨率及系统语言。

定义设备后，可以在Previewer右上角，单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/TtbYx7XTTpiRq4PQeRHtuA/zh-cn_image_0000002561832605.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=2A686F825D5D8207B218536E56536D704C7DD9589A8D5452C50871F331C36916 "点击放大")按钮，打开Profile管理器，切换预览设备。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/-yzk-Ug1TheAaobmGpbpDw/zh-cn_image_0000002530912682.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=06F4EB163925C6E41879A4764ADEFFFE0DAE321D1C3ACCCE612683E2A9FD9D46)

同时，Profile Manager还支持多设备预览功能，具体请参考[查看多端设备预览效果](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-multi-profile)。

下面以自定义一款Phone设备为例，介绍设备Profile Manager的使用方法。

1.  在预览器界面，打开Profile Manager界面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/uwyjtiAUSlyEm-gnAFHmnw/zh-cn_image_0000002530912680.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=95FB9DA486592C19A9D703B961D4E49E4389114F7E41327CEBF416C981F7C18F)
    
2.  在Profile Manager界面，单击**\+ New Profile**按钮，添加设备。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/hXWJkMbzTKCSM-DcuDWwTw/zh-cn_image_0000002561832603.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=EBC368511E022E0EE6B2B93578B256C3A2F6C12EA533688818CED9F9D16C54BC)
    
3.  在**Create Profile**界面，填写新增设备的信息，如**Profile ID**（设备型号）、**Device type**（设备类型）、**Resolution**（分辨率）和**Language and region**（语言和区域）等。其中Device type只能选择module.json5中deviceTypes字段已定义的设备。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/gP4uDcgMQpewmqXCkOLMaA/zh-cn_image_0000002561752621.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=6CCA4F811BCAEC69833B9E1DE8B5A7295491762D06E11D0BD6ED25FA913B0B97)
    
4.  设备信息填写完成后，单击**OK**完成创建。
