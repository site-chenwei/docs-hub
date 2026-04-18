---
title: "规则（Rules）配置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules"
menu_path:
  - "指南"
  - "使用AI智能辅助编程"
  - "自定义智能体配置"
  - "规则（Rules）配置"
captured_at: "2026-04-17T01:36:44.588Z"
---

# 规则（Rules）配置

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持用户配置规则（Rules）。在自定义智能体模型下，智能问答时可生成更加符合Rules规范的代码。规则包括全局级别规则（Global Rules）和工程级别规则（Project Rules）。

从DevEco Studio 6.1.0 Beta2开始，新增规则长度限制。

**Global Rules**：支持开发者自行导入规则文件（Custom rule），或使用默认规则（Default rule），或不使用规则（No rules）；规则与用户绑定，对当前用户下所有工程生效；支持添加多个自定义规则，添加后可选择是否生效。

**Project Rules**：需开发者自行导入或创建规则；规则仅对当前工程有效；仅支持添加一个自定义规则，添加后即生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/qK2xux8vQEGv3x2_9wcwSw/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=1C94E3ADED3412FC58A36C1D9D1DDB228AD64E1EFC107235D5839B62B1E9D6D4)

-   规则文件：扩展名为.md的Markdown文件，.md文件中仅二级标题及以下的规则内容生效。
-   默认规则（Default rule）需联网使用，无网络或网络故障时用户可选择Custom rule或No rules。

#### Global Rules配置

1.  点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/_2X-CHF-TAGYd_1dV0I8tw/zh-cn_image_0000002561752687.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=1992880AF34ED30F82228D3F5CF8014A9159B939632DDDC279F7FE06D0F55615)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/MWPb0TuzQUmkZmk8wle1WA/zh-cn_image_0000002530752736.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=A787C48E0EA263B8F847BDA0D1298A78991B0974C98DD49953CD5104263D7190)按钮，选择**Rules**，进入配置页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/vV__YAlVS8iDg_XWzBahTw/zh-cn_image_0000002561832665.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=52F53D291B9E600D1322B3CA839AC76A77EC9A0E9E913A5B90299BB3F3E9A654)
    
2.  选择规则长度限制，包括**Quality first**、**Token efficiency first**。默认为Token efficiency first。
    
    -   Quality first：生成代码时遵循更多规则，帮助AI获取更准确答复。
    -   Token efficiency first：生成代码时优先考虑Token长度，节省Token数量。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/ASsmRcHNRTuE6jOz-Df_lg/zh-cn_image_0000002561832661.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=550A4DFD15A58AF9A6C98407811969C7D25FA4E7604174BACF8F68087DEE34B4)
    
3.  以有网络为例，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/1fcO4T5rRxW9HcJACIusjA/zh-cn_image_0000002530752750.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=01C59A68C11D04B17697CFA91223D4188250E365C9F0768FF0FD6E3E6612971A)图标导入规则文件。无网络时操作界面可能存在差异，以实际为准。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/cOqmsLe1SaiQrrCzdVxsaQ/zh-cn_image_0000002530912740.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=E8E37176399FF717B51B231D227CC06F0050B7F7410FE09E237A32CAA1D7B2F1)
    
4.  选择和管理规则文件。Global Rules列表全量展示了默认规则（Default rule）、自定义规则（Custom rule）和无规则（No rules），当前仅支持选择其中一个规则。若选择No rules，则全局规则不生效。
    
    -   将鼠标悬停在默认规则上，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/NFoHmOUXQJeLhjp33lSU5w/zh-cn_image_0000002530752734.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=BBDA1C7DBA6EDF2C09E58FDADA276E640E2A667B02B288C95B0F25A52C6613CA)编辑图标，开发者可查看具体规则内容。
    -   将鼠标悬停在自定义规则上，会出现编辑和删除按钮，方便开发者管理自定义规则。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/lahReaYtTKmvATPkyo8TpQ/zh-cn_image_0000002530752752.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=C9331E3A893C63A4C111DF9C6E2CF8A4445994AA505A1D7FA96CD047D28DA097)
    

#### Project Rules配置

1.  点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/-sL_UfSRR5e1RJZQLIuruw/zh-cn_image_0000002561832647.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=E2331D7864855C0BCCD0248AC41800B6D8A5B33E20B04F5F13E47D95E2A98998)按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/4-qXjCHNQ8ieuVD1bSKd0w/zh-cn_image_0000002530752738.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=52BB87F13D372ED3B6AE440CC37AE7F3D33A8C2E92C1DCCA2C6AAB3E19F492C8)按钮，选择**Rules**，进入配置页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/vZ3nZia4RwehFfhUJjVGRw/zh-cn_image_0000002530752730.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=6EEB8D13D94D256F9C07B3E5B98CE65FB29D5EA8C651BC88B55DB8C3B1FCC90E)
    
2.  创建或导入Rule文件。
    
    -   创建Rule文件方法：点击**Create Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，在project\_rule.md文件中输入规则内容。
    -   导入Rule文件方法：点击**Import Rule**，工程目录中会新增/.codegenie/project\_rule.md文件，project\_rule.md文件内容即为导入的规则文件内容。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/vWMJDdeNSBm73c1V20yt8A/zh-cn_image_0000002530752726.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=356651176959FFD8FCEDA40F9C444C52F1CB6A22FF0284C119E342E72E65FE4B)
    
3.  管理规则文件。将鼠标悬停在工程文件上，会出现编辑和删除按钮，方便开发者管理工程规则文件。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/C0E-i9GBTEKTZUBjaXx8AQ/zh-cn_image_0000002561752681.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=E7073F91507E4E8B67E4C40786AFB703C3A95740850B7D494FAF393DD0E4FFA0)
