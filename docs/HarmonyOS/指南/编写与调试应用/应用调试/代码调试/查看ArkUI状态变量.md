---
title: "查看ArkUI状态变量"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-state"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "应用调试"
  - "代码调试"
  - "查看ArkUI状态变量"
captured_at: "2026-04-17T01:36:49.564Z"
---

# 查看ArkUI状态变量

从DevEco Studio 6.0.2 Beta1版本开始，支持在调试时查看ArkUI状态变量的实时变化情况。

在调试窗口中，点击**Layout Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/TnmyB3PtSWWalEenw_4hNg/zh-cn_image_0000002561832669.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=CF15A0D9F6D4DB63BC574972C0D8016D4DF43CFA136CE954820D678125F571D7)，勾选**ArkUI State**，打开ArkUI状态变量面板。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/5fZmHOxRQtGqyfP5ma09Dw/zh-cn_image_0000002561752693.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=54B0834081E1F590C0A546DD282452163D5B66E36F32226A28C8F29A209E046B)

状态变量面板分为总览（Summary）和当前值（Current Value）两个子面板：

-   总览面板显示了当前应用运行时，状态变量更新的总体情况，包含了状态变量的名称、更新次数、装饰器类型、所属组件、所属类、当前值。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/KEr5Q9gaQxeHGOrgRFpg8g/zh-cn_image_0000002530912750.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=0CB4ECB50029277181C0C18E7596241351F8D92E4563091A115A421B9CC7C624)
    
-   当前值面板记录了状态变量实时变化的数据，包含了状态变量的更新时间、名称、所属组件、所属类、装饰器类型、当前值、影响的组件数量。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/oxmbX2f9TxyJWv3RuApPeg/zh-cn_image_0000002530752746.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=AED409486329A15B7DE528BFC37972C2512B2BE831312ED87CF18118375EEBC0)当点击右侧的箭头时，新弹出的面板将显示当前选中状态变量影响的组件列表，包含影响组件的组件名、组件ID、是否为自定义组件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/krT1gHxlRkSGcjKmx74RXQ/zh-cn_image_0000002561752689.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=C17790C51FD94618DD23AD656A13AE625BFA1C838E3D46E55FEE6EB0F56C6276)
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/wk8PrZbeRwSqCVuPL8K71A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013650Z&HW-CC-Expire=86400&HW-CC-Sign=9F43E8362752BD05B34410C120922AFF63E589B86163B53CF92F16F70C98ABE0)

-   打开状态变量面板后才会开始监听状态变量的更新，因此，无法查看面板打开前状态变量的更新情况。
-   同一次调试过程中，关闭状态变量面板不会清空之前的数据，当前值面板最多展示1000条数据，超过限制后，仅展示最新的1000条数据。
