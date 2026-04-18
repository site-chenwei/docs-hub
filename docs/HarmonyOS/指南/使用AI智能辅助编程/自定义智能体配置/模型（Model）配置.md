---
title: "模型（Model）配置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-model"
menu_path:
  - "指南"
  - "使用AI智能辅助编程"
  - "自定义智能体配置"
  - "模型（Model）配置"
captured_at: "2026-04-17T01:36:44.601Z"
---

# 模型（Model）配置

CodeGenie支持通过Anthropic-API、Gemini-API和OpenAI-API协议接入第三方模型，为自定义Agent提供多样化的模型选择。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持通过OpenAI-API协议接入第三方模型。

从DevEco Studio 6.0.2 Beta1开始，CodeGenie支持通过Anthropic-API、Gemini-API协议接入第三方模型，以及新增Built-in Models内置模型。

从DevEco Studio 6.0.2 Release（6.0.2.646）开始， 支持通过服务提供商接入三方模型，URL接入时支持使用Ollama协议的三方模型。

#### 操作步骤

1.  点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/Gsto2OZUTWWhcDn2FI5sXw/zh-cn_image_0000002530753022.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=E181CE131388F7C8A22196AEE56A240E26F8538F8D29C2D028FCDF87B8D70BA7 "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/szMqZBZ8Rhe_6p9z778E5g/zh-cn_image_0000002561832939.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=9B8D51ABA8505CAEDE6033BA7EE3AEFFE1E5ADF6915E0175A7AF1BD2B62A9608)按钮，选择**Model**，进入配置页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/BRxxNbEUT_GEvYxAl6WNAQ/zh-cn_image_0000002530753026.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=AD37F7C4D9B700E341E3C6486D055EB0166D589C12A1729744F67902BFD862CD "点击放大")
    
2.  点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/FLAN7ILGRHuMOb7zcvYHSQ/zh-cn_image_0000002561752963.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=89F0CA941EBAA22721166F20BE36CB9096CB9F7A911315C129BDCF447500320F "点击放大")按钮添加模型，当前支持通过Service Provider（服务提供商）和URL两种方式添加。
    
    -   通过服务提供商添加。填写**Name**、**Provider**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
        
        -   **Name**：模型名称。
        -   **Provider**：模型的提供商，可选项包括OpenAI、Gemini、Anthropic、DeepSeek、Alibaba Cloud、Z.ai。
        -   **API Key**：模型的访问密钥，在提供商网站申请。
        -   **Model**：模型的标识。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/68P_-CG4SZyFNJ1PZYYKoA/zh-cn_image_0000002561752961.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=4EC8525BB2043834E869476A6A75745B281DF27B7E0530A7A26C2C61B8C292C0 "点击放大")
        
    
    -   通过URL添加。填写**Name**、**Protocol**、**Url**、**API Key**、**Model**字段后，点击**Add**，校验成功后模型将被添加到列表中。
        
        -   **Name**：模型名称。
        -   **Url**：模型的访问地址。
        -   **Protocol**：模型的协议，可选项包括OpenAI、Anthropic、Gemini、Ollama。
        -   **API Key**：模型的访问密钥，在提供商网站申请。
        -   **Model**：模型的标识。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/mT619-RZR-eP4_PL3gaMkg/zh-cn_image_0000002561832941.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=6841E658E03266204F3AD064609556D4792ECD79D1C4F105940FA4ADF5AA4EF1 "点击放大")
        
    
3.  在**All Models**下展示所有添加成功的模型，Built-in Models为内置模型，Custom Models为三方模型（自定义模型）。将鼠标悬浮在三方模型上会显示两个操作按钮：编辑、删除，方便开发者管理三方模型。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/MOMngkPrRFWUacTLYBux6Q/zh-cn_image_0000002530913014.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=4B0165B052D74F73A7B103FECF6E6CD77B4EC786454F06707D9FB6DDBC97DBD3 "点击放大")
