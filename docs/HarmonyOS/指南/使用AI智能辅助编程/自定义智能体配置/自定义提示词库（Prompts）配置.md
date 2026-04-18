---
title: "自定义提示词库（Prompts）配置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-prompts"
menu_path:
  - "指南"
  - "使用AI智能辅助编程"
  - "自定义智能体配置"
  - "自定义提示词库（Prompts）配置"
captured_at: "2026-04-17T01:36:44.624Z"
---

# 自定义提示词库（Prompts）配置

从DevEco Studio 6.1.0 Beta2开始，CodeGenie支持添加和管理提示词库。如果经常针对不同的文件或代码使用某个提示词向AI提问，可以将提示词添加到常用提示词库中，在需要时通过菜单栏快速触发，从而提高开发效率。

1.  点击页面右侧菜单栏CodeGenie图标完成登录后，可以通过如下两种方式打开Prompts配置界面：
    
    -   点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/GsNJ1IYRQgOZWYiNtEix2w/zh-cn_image_0000002561753075.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=42051053C89BB99BE083FA8D18E1255449B2CED0CE45F400B6B4A3C97F4C8FD0)按钮，选择**Prompts**。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/2gjjXXMKRMWsMMGaPgNiTw/zh-cn_image_0000002530913134.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=C95D678D5DA7CEE46A87940D0F55F33524BD1955F885D63A2F75C2F2ED5CFD1F)
        
    -   在代码编辑区右键唤醒菜单栏，点击**CodeGenie > Add New Prompts**。
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/7WBJuUHCQtWDJ7g8DtB_UQ/zh-cn_image_0000002530753148.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=5444D4001D220572898DC3F4215435C049F5051E805287CD3047BFA2C27F43ED)
        
    
2.  点击**Add Now**进入Prompts配置页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/gzTlt9MYSQ-R9_CkMDO0hQ/zh-cn_image_0000002530753156.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=DBA4D11818F95A7156D074BDB24F0B123E1CCA83B774994464E6067135701F36)
    
3.  填写提示词名称、提示词内容等，点击**Save**进行保存。
    
    -   **Title**：提示词名称，长度不超过20个字符。
    -   **Prompt**：提示词的具体内容，长度不超过5000个字符。
    -   **Auto-reference selected code for context**：是否自动引用所选代码作为上下文，勾选该选项后，会将选中代码和提示词一并发送给CodeGenie。
    -   **Auto send prompts to AI**：是否自动发送给CodeGenie，不勾选该选项时需手动点击![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/UC-kQQZ3QZaotb9BtWjhBg/zh-cn_image_0000002561833061.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=17C68AD39611CD19C2AB10675F7EB9F3F8480E7BF93A965877A5A1B8C6CB86DC)发送。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/IcCmQTB-Qzm72OAQkwfwsw/zh-cn_image_0000002561753079.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=03F9E652C5B03F9BD898A91E8FB76280E941A1D5E59CF8769BC835DD3E2C88A4)
    
    将鼠标悬浮在自定义Prompts上，可出现编辑和删除按钮，方便开发者编辑或删除。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/l73ccvCwTqeINf8TE1w30w/zh-cn_image_0000002561753089.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=03ACF0D8F43615442A27AAABD7624CF3C008DA9EDBFE62844BEA436D368A1D18)
    
4.  选中代码片或在编辑区空白位置右键，点击CodeGenie下的提示词（如安全检查），发送提示词后等待AI解析回复。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/iL2EJ6zTR7qpqIYjE5CaQg/zh-cn_image_0000002530753146.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=F77DD57E3A4FB4335AA17F8D613962A0249FC9D8C36521EFC5916320079AFCF7)
