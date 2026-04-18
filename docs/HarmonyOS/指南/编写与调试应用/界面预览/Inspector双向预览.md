---
title: "Inspector双向预览"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-inspector"
menu_path:
  - "指南"
  - "编写与调试应用"
  - "界面预览"
  - "Inspector双向预览"
captured_at: "2026-04-17T01:36:48.720Z"
---

# Inspector双向预览

DevEco Studio提供HarmonyOS应用/元服务的UI预览界面与源代码文件间的双向预览功能，支持ets文件与预览器界面的双向预览。使用双向预览功能时，需要在预览器界面单击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/xw0F-lBYS5uHkVT2z_0Yyg/zh-cn_image_0000002561832897.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=81586A5F3FA0E8833C7A1714D3E867D6AA4AC94E004A5513D51D5721B0ECE61D)图标打开双向预览功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/OG8o2LRjRTi1Q0gf1qmrhA/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=16C098587344C463A18D9A4CE97DFA2DA10492DEB20E4C659471759C2D05B049)

不支持服务卡片的双向预览功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/eCQQG3jrRViGShP5cwVS9A/zh-cn_image_0000002561752913.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=D0283D1E8828D7942B9480B57C680ACB8E2CC5C72109522E6FFC5480122045AD "点击放大")

开启双向预览功能后，支持代码编辑器、UI界面和Component Tree组件树三者之间的联动：

-   选中预览器UI界面中的组件，则组件树上对应的组件将被选中，同时代码编辑器中的布局文件中对应的代码块高亮显示。
-   选中布局文件中的代码块，则在UI界面会高亮显示，组件树上的组件节点也会呈现被选中的状态。
-   选中组件树中的组件，则对应的代码块和UI界面也会高亮显示。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/5XCqAFz1Rr6HiQa-i7nUpQ/zh-cn_image_0000002530912970.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=39C3FBA4BA13A059BC306EAFA08E6938949B185749AC3115BE5E966E08628B92 "点击放大")

在预览界面还可以通过组件的属性面板修改可修改的属性或样式，在预览界面修改后，预览器会自动同步到代码编辑器中修改源码，并实时的刷新UI界面；同样的，如果在代码编辑器中修改源码，也会实时刷新UI界面，并更新组件树信息及组件属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/mev0hFpKSemsaYNVWCsB_g/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013649Z&HW-CC-Expire=86400&HW-CC-Sign=A742D00C9A4CFBD7CAC5494E992B2C8CB42D0D980CB8531A6A8A79A242CBEC85)

-   如果组件有做数据绑定，则其属性不支持在属性面板修改。
-   如果界面有使用动画效果或者带动画效果组件，则其属性不支持在属性面板修改。
-   多设备预览时，不支持双向预览。
