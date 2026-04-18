---
title: "模型上下文协议（MCP）配置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-mcp"
menu_path:
  - "指南"
  - "使用AI智能辅助编程"
  - "自定义智能体配置"
  - "模型上下文协议（MCP）配置"
captured_at: "2026-04-17T01:36:44.591Z"
---

# 模型上下文协议（MCP）配置

#### 功能介绍

模型上下文协议（Model Context Protocol，简称MCP）是一种开放协议，允许大型语言模型（LLMs）访问自定义的工具和服务，可以通过部署MCP Server并将其集成到自定义智能体中来使用。关于 MCP 的更多信息，请参考 [MCP 官方文档](https://modelcontextprotocol.io/introduction)。

从DevEco Studio 6.0.1 Beta1开始，CodeGenie支持配置MCP。

从DevEco Studio 6.1.0 Beta2开始，支持在MCP配置界面添加Node (npx) Path和Python (uvx) Path，支持从MCP市场添加MCP工具。

#### 环境约束

为保证MCP Server正常启动，需要安装npx和uvx，可在配置MCP工具时在Node (npx) Path和Python (uvx) Path中添加。

-   npx：依赖于Node.js，建议使用Node.js的LTS版本。
-   uvx：基于Python的快速执行工具，建议安装Python 3.9 以上的版本。

#### 操作步骤

1.  点击界面右上方![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/Z2hd7xVXQ9yATeK_1pDCPw/zh-cn_image_0000002561752883.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=8BABB6EEC06FF2812F78FCEFCF14C7ED445AC11A4AE4A2D38508C7CC18E22C5A "点击放大")按钮，或者点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/jYGWTeN8TTWlcYN_4eqVkA/zh-cn_image_0000002530912934.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=4DE95D3EBAE0DBAE85A27027A95E471D336805ED346FE11F2494A1D740DA2F85)按钮，选择**MCP**，进入配置页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/ZwpdmZmmTN2rEqNXNOMRLw/zh-cn_image_0000002561832867.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=63E62B235DBD7F43DBC6D4AA157794A3231467495D7D5524E28D84D8255ECD84 "点击放大")
    
2.  添加MCP工具。点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ssSA4A08TxuZ70eYscmHgw/zh-cn_image_0000002561832863.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=A97AF439E096E8CE07A5C5EC1EB58F90E79230285D5DCB9E85BD19BB10610303 "点击放大")按钮或**Add Manually**手动添加，点击**MCP Market**或**Add from MCP Market**从MCP市场添加。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/m63Sa6X8RF-R0XZTdXpptg/zh-cn_image_0000002561832873.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=B61EF1770972B0A923F2C1E10C69741773DE420357AD011491CCA8E175509F2C "点击放大")
    
    -   **手动添加**：在编辑框中填写MCP工具的配置信息，填写完成后点击**Add**。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/daEdlKFqST2eaF9kHVS1hQ/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=086C7D40837B277F7557A27F57A79E555CD916EE0197474908E669ACD67D13CD)
        
        MCP Server支持三种通信方式：Stdio 、Server-Sent Events (SSE) 和Streamable HTTP。
        
        Stdio方式支持配置cmd、args和env字段，SSE和Streamable HTTP方式支持配置url字段。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/IACpC22SSFiiuRsL-ftM3w/zh-cn_image_0000002530752950.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=8A51566BCB87FFFF62B03E47B3A09B5DBFC3610FAD8A45EDFABF53E08E84E7F8 "点击放大")
        
    -   **从MCP市场添加**：在搜索框中搜索目标MCP工具，点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/05IUO8rHTqKORXpV4kfT5Q/zh-cn_image_0000002530912938.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=D6E64C547EC5E4FF6D9E48D45F4D4518EDAAF39AE57B4A7ED22F67050CF2588C "点击放大")按钮添加。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/IFANX4xpQy6e5gsrM3LNIg/zh-cn_image_0000002530912944.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=B1188FEDE5DB84DD6CE961E45F40B9E46E403FCCA4561163A27E307BF5040873 "点击放大")
        
    
3.  在**MCP Tools**列表中，展示所有MCP工具信息，包括名称、连接状态、启用状态。同时，将鼠标悬浮在工具上会显示三个操作按钮：刷新、编辑和删除，方便开发者管理工具。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/mf8XW6EzQneRcDDTj4caXw/zh-cn_image_0000002561832875.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=54BFCB6BA8EB159EECA16E4880B44DBD3C4FC84852A6358B50AD0AFBF985F1B3 "点击放大")
    
    -   名称：MCP工具名称，如everything、time。
    -   连接状态：工具连接状态，包括“成功”、“失败”和“连接中”三种状态。
    -   启用状态：工具是否已启用。
