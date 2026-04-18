---
title: "ohpm"
source_url: "https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-start"
menu_path:
  - "指南"
  - "开发环境搭建"
  - "工程创建"
  - "模块管理"
  - "ohpm-repo私仓搭建工具"
  - "相关命令"
  - "ohpm-repo start"
captured_at: "2026-04-17T01:36:42.401Z"
---

# ohpm-repo start

启动ohpm-repo服务。

#### 前提条件

已成功执行[install命令](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-install)，并按要求刷新环境变量。

#### 命令格式

ohpm-repo start 

#### 功能描述

用于启动ohpm-repo服务，创建一个ohpm-repo实例。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/7br1GdJhSc6XaQOyXsIE3A/note_3.0-zh-cn.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=00675F473FF0EDFBA62EDEB7C3249162080CCE704885A7133F133AC9697308E9)

启动时将ohpm-repo服务的pid存放到<deploy\_root>/runtime/.pid文件中，其中<deploy\_root>为[ohpm-repo私仓部署目录](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-ohpm-repo-configuration#zh-cn_topic_0000001745376470_关于-deploy_root)。

#### 示例

执行以下命令：

ohpm-repo start

结果示例：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/ZBPZGC07TjqWgsg33gSRkA/zh-cn_image_0000002530911298.png?HW-CC-KV=V1&HW-CC-Date=20260417T013642Z&HW-CC-Expire=86400&HW-CC-Sign=D1CC1F294E71B431D54C8DA3E629F989580C26B07A3B0621C29E35B5D39DD4D3 "点击放大")
