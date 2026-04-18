---
title: "MCP协议上架指导"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-kit-listing-mcp-protocol"
menu_path:
  - "指南"
  - "AI"
  - "Intents Kit（意图框架服务）"
  - "意图框架上架配置指导"
  - "MCP协议上架指导"
captured_at: "2026-04-17T01:36:39.617Z"
---

# MCP协议上架指导

#### **意图注册配置操作步骤**

1.  账号登录：
    
    1.  通过“[https://developer.huawei.com/consumer/cn/](https://developer.huawei.com/consumer/cn/) > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架”，进入意图注册入口。
        
        如发布渠道为“智能体/小艺对话”只能使用与应用上架相同的账号登录。反之发布渠道为“插件市场”无特殊账号要求。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/7oungLRUSlKiEZZCs9fcXg/zh-cn_image_0000002538020284.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=A9867663E003D9CE0EAF1BD4AC09C08D214433C5D0F43F02AFF0B75DE68A7359)
        
    2.  点击“立即体验”即可进入意图注册入口。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/--CzEXz8ScWJUEWoXR5Suw/zh-cn_image_0000002538180210.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=4381D05380B3E0D1FFF4C2CE2D778622F002253E15F0A3D5D93BB3EF6AAAF69D)
        
2.  注册意图集
    
    1.  如图，点击“注册意图”。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/vBBLYWdOQvuUWzG-Q70TNQ/zh-cn_image_0000002569019997.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=0F9C12280DF35D3FD06D9FA58D9D4B3B5065CCEE09D28985D727DD6B02949C19)
        
    2.  选择“MCP协议”并填写基本信息创建意图集。
        
        1.  意图集（插件）名称：需唯一标识。
        2.  意图集（插件）描述：开发者自定义插件描述信息。
        3.  分类：按业务场景选择。
        4.  MCP服务配置：填写MCP URL（服务器地址信息，不含鉴权信息）。
        5.  认证信息配置：对应鉴权信息（注意放在Header/Query）。
        6.  协议类型：根据情况选择，提供SSE/Streamable两种。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/Ea8V821pQc6qtqW8xuAilA/zh-cn_image_0000002568899991.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=349402D448538DF4399688C92797410D8DCE736CFD306B0C08F5B51092AC0025)
        
3.  编辑：创建后自动进入”插件编辑“页面。
    
    1.  编辑基本信息：
        
        1.  开发者品牌：该信息是对外露出的品牌传播名（注意和企业账号，公司名称区别开）。
        2.  图标：192\*192。
        3.  使用描述：需使用Markdown格式。（需对server的功能概述、apikey申请方式表达准确清晰）。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/Ch7jgTBiR8moqSkGMepCKA/zh-cn_image_0000002538020286.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=25831D8150EC14EEF1FC13F445A3A6C369C6B18C54A564E14F81E7B6FF28FB83)
        
4.  工具检查：保存后切换至"工具"页签。若基本信息配置无误，工具列表中会根据基本信息内容自动生成1条/多条信息。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/AIDpsGvxSf2Jk2TVh6Zt1w/zh-cn_image_0000002538180212.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=FC0BABAD77A2AB176D5B6948A38F5D159058A43601C83EE0C7B1EB2CBB1BD1C9)
    
    1.  出现工具列表：请检查工具入参，参数是否重复或者缺失，参数类型是否正确。若一切无误，则配置成功。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/umJPDRYRTLWiKmFOg-ATJg/zh-cn_image_0000002569019999.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=9D52D6B77F5FCA4BDED112BE97CCB6DF144627C3F388E984D62FA5F582928924)
        
    2.  未出现工具列表：请等候几分钟重新进入，后台加载存在延时；如若重新进入后，仍未加载出工具信息，可能是插件的链接和鉴权信息配置错误。多次尝试后仍未解决，请通过邮箱联系华为意图框架同学（hagservice@huawei.com） 。
        
5.  审核：切换至“发布”页签，点击“提交审核”。
    
    1.  选择发布渠道，点击确定，提交审核。
        1.  智能体：开发者上架MCP Server，仅供开发者自己开发的智能体来调用。
        2.  小艺对话：开发者上架MCP Server，可供开发者自己开发的智能体调用，也可供小艺APP主对话调用（当前暂不支持开发者独立在小艺主对话上线该能力，需联系华为意图框架同学）。
        3.  插件市场：开发者上架MCP server，可供开发者自己开发的智能体调用，也可供平台上其他开发者开发智能体时调用（回到开发者源头平台去开服）。
            
            ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Ul29YyfxR-CmAlkdrq2DZQ/zh-cn_image_0000002568899993.png?HW-CC-KV=V1&HW-CC-Date=20260417T013639Z&HW-CC-Expire=86400&HW-CC-Sign=BA130E3EC0BCC56CFB24B645A6406C210C47FD4034EEA6F82C97542E66F5A90D)
            
    2.  提交审核后，请耐心等待平台相关审核流程完成；完成后即可在“[https://developer.huawei.com/consumer/cn/](https://developer.huawei.com/consumer/cn/) > 管理中心 > 生态服务 > 智慧服务 > 小艺开放平台（原HarmonyOS服务开放平台） > 意图框架 > 小艺插件市场”中找到您的工具。
