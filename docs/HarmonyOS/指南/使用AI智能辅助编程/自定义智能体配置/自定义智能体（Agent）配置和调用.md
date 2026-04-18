---
title: "自定义智能体（Agent）配置和调用"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-use"
menu_path:
  - "指南"
  - "使用AI智能辅助编程"
  - "自定义智能体配置"
  - "自定义智能体（Agent）配置和调用"
captured_at: "2026-04-17T01:36:44.621Z"
---

# 自定义智能体（Agent）配置和调用

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持用户添加模型和自定义Agent，增强AI问答能力，提升AI辅助编程和分析能力。

从DevEco Studio 6.0.2 Beta1开始，自定义Agent配置时支持添加DevEco Studio内置的工具Built-in Tools、Auto Run和Blocklist。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始，DevEco Studio内置工具新增To Do工具；支持Agent智能体切换模型和配置三方模型。

从DevEco Studio 6.0.2 Beta1开始，DevEco Studio内置工具新增Web Rag工具；Blocklist变更为AllowList，在调用命令行工具执行命令时，白名单中的命令会自动执行；不支持在对话区域输入"/"调出命令，选择自定义的Agent功能。

#### Agent配置

1.  点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/NqZoKyJsTmuydkLnFCVWcA/zh-cn_image_0000002530913180.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=DB33689655EFD65EAEC02F624AE4F05CF227F2C03A22F4FBFAAFA61FD4640413 "点击放大")按钮；或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/NyqkiC24SRCcgI3yT7CzYQ/zh-cn_image_0000002561833109.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=43CBB4E66F944667283F1B8E61111773FA59E3594092749ECC0E09251823C8BE)按钮，选择**Agent**；或者在输入框左下角下拉框选择**Create Agent**，进入配置页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/GdMQH5jeT4msMinoIPl39g/zh-cn_image_0000002530753198.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=1761CAADC8F10188138FEA439709D0C59908F59780B6493D32D63B0FE516D233)
    
2.  点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/nPzJsxw1T4ioZ1fIvvlp_w/zh-cn_image_0000002561753133.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=120B46428BEEF6584BBC97B872E97C0F023FDAAB2F08E467896B9232F5E174B8 "点击放大")按钮，填写自定义Agent的相关信息。点击**Add**，将创建自定义Agent。
    
    -   **Name**：必填，自定义Agent的名称。
    -   **Prompt Description**：可选，自定义Agent的提示词。
    -   **MCP Tools**：可选，添加MCP工具，具体请参考[MCP配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp)。
    -   **Built-in Tools**：可选，开启或关闭File Manager、Terminal、Compile and Build、Web Rag、To Do，默认开启。。
        -   File Manager开启后，支持读写本地的代码文件；
        -   Terminal开启后，在CodeGenie对话框执行命令时可自动拉起Terminal终端；
        -   Compile and Build开启后，支持编译与构建项目；
        -   Web Rag开启后，支持在问答过程中检索鸿蒙相关的资料，提升答复准确性；
        -   To Do开启后，支持把一个复杂任务拆解成多步执行，帮助CodeGenie聚焦任务，避免遗忘任务，提升答复准确性。
    -   **Select Model**：必填，选择需要使用的模型，具体请参考[模型（Model）配置](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model)。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/O31fVOx-RK-iZzDqQvgyVg/zh-cn_image_0000002530753184.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=6AD9D2FD444F0FEF05B4503E59AC36C7027539EA41982169A061C465152673E0 "点击放大")
    
3.  在**All Agents**下展示所有智能体。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/V34KxUzHSXqqnZh7h-C1rw/zh-cn_image_0000002530913184.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=14B43AB88A572357CB8CB67943FB10A9344469E4E28C087332320A2B3676FA80 "点击放大")
    
4.  设置自动执行开关和白名单列表。
    
    -   **Auto Run**：内置工具（命令行工具除外）和MCP工具被调用过程中，自动执行的开启开关。开启时，工具被调用可自动执行和输出内容；关闭时，工具被调用需开发者授权。默认关闭。
    -   **AllowList**：白名单列表，开启Auto Run后，白名单中的命令同样会自动执行。点击**Enter Command**中输入命令，点击**Add**可将命令添加至白名单列表；点击命令后×，可将命令从白名单列表中删除。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/e9AO52aASQCI8Ubsgu67RA/zh-cn_image_0000002530913186.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=A2A455E22FFCDDECA8EBCC05B0728899D82AA4AD0B1E5CA600141C2C670C4F64 "点击放大")
    
5.  选择自定义智能体后，开发者可以切换模型，包括内置模型/默认模型（deepseek-v3.2、glm-5）和三方模型（如deepseek）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/RRLWAC9VTAqet-rBnVuvpw/zh-cn_image_0000002561833113.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=6FF72C09DAABD47DF64B3D3A821E62168A0B84EBC057BB408712F5BEE304DED2)
    
6.  点击置灰的三方模型会跳转到Service Provider配置界面（如**deepseek-chat**），填写**API Key**字段即可添加模型。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/mqC0vZ0tQKGfOlVjIExggQ/zh-cn_image_0000002561833105.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=959361F962D6F8E77D7DBDDE8F92412A0DDBA5375C18D0D2A022EC432417E809 "点击放大")
    

#### Agent调用

1.  Agent配置完成后，可以通过如下两种方式开启调用：
    
    -   在对话区域输入"/"调出命令，选择自定义的Agent（如**figma2code**）。
    -   在输入框左下角HarmonyOS Ask处下拉框中选择自定义的Agent（如**figma2code**）。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/P6nbnGx_RTKWaEOc9CZ23A/zh-cn_image_0000002561753131.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=ED9F792EDCE9F869BCC905FD7BA3B279FE5B09F81EDDD178CB1D213EF5887CFD)
    
2.  选择自定义Agent后，在右侧可以切换模型，默认使用配置Agent时添加的模型。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/InJnI_QoSnK-uEcQd0jLBw/zh-cn_image_0000002530913190.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=D194331FA8C90935CB332AD5B707EBCC22774DEBB64DBF712986A4014D2B7F09 "点击放大")
    
3.  根据业务需要，进行智能问答、代码生成、代码智能解读等，CodeGenie将会调用自定义Agent和选择的模型生成内容。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/KCYHNZDvQ5qZvPS55F22WA/zh-cn_image_0000002561833103.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=9BC11A0092E1A6416E24A2B51BA73B15115CEFF3CDBCF2B3B21D516E3D049E5C "点击放大")
