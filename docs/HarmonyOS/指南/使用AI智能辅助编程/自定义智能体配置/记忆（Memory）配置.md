---
title: "记忆（Memory）配置"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-memory"
menu_path:
  - "指南"
  - "使用AI智能辅助编程"
  - "自定义智能体配置"
  - "记忆（Memory）配置"
captured_at: "2026-04-17T01:36:44.625Z"
---

# 记忆（Memory）配置

#### 功能介绍

CodeGenie搭载长期记忆功能，在应用开发过程中，会学习和提取个人偏好、项目细节等有价值的信息，进行主动记忆或自动记忆。伴随开发者的持续使用，逐步形成覆盖开发者信息、项目场景、问题沉淀的全域记忆体系。在长期交互中，记忆也会随时间更新。

依托这一核心能力，CodeGenie能够精准理解和生成符合开发者需求的代码、回答等，与开发者实现更高效的协作。

#### \[h2\]基本概念

-   主动记忆：开发者要求CodeGenie记住输入的内容，CodeGenie会保存这些信息。
-   自动记忆：自动提取对话中有价值的信息，记录任务执行进度，随时间推移学习开发者的编码风格和项目细节等。

#### \[h2\]使用约束

-   当前仅自定义Agent支持长期记忆检索和生成。
-   当CodeGenie记忆与[规则（Rules）](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-agent-rules)发生冲突时，以规则为准。

#### 操作步骤

1.  点击界面右上方**Settings**![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/UOkL1gPpT8yDBFgpNG5vjg/zh-cn_image_0000002530913008.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=5A2F5827B2D080F861CBC1AADBA675CDC010DE842FBC601F3B785E25A6D41C00)按钮，选择**Memory**，进入配置页面。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Mq_vbgoyQZG_w8CzOez6KA/zh-cn_image_0000002561752955.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=60A1CA9BF1B0E8ADA82291CA91F4811D622ED10B14B4707512140048941FCFB4)
    
2.  点击Memory后开关，开启和关闭记忆。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/JMtewEVgSs6X9AWFV9cN8Q/zh-cn_image_0000002561832931.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=6930527D43C68097553FBFECE685A3C21B29DCCF4F4229B344F9DE11B3A1F07D)
    
3.  在**Memory List**（记忆列表）下展示所有记忆，包括**Global**（记录用户相关信息）、**Project**（记录项目相关信息）。将鼠标悬浮在记忆上会显示具体信息，以及出现编辑、删除按钮，方便开发者管理记忆。
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/IINiMwMQRJ-RjLOKfBBdcw/zh-cn_image_0000002530753018.png?HW-CC-KV=V1&HW-CC-Date=20260417T013645Z&HW-CC-Expire=86400&HW-CC-Sign=508E215E7240A92CE637470FF2A3BA46155A4BCA8750A3A233B064AB343DA8B7)
